from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
CN_JSON_PATH = ROOT / "docs/Event/json/CN.json"
GLOBAL_JSON_PATH = ROOT / "docs/Event/json/Global.json"
HOME_INDEX_PATH = ROOT / "docs/home/index.md"
EVENT_INDEX_PATH = ROOT / "docs/Event/index.md"
UPCOMING_EVENTS_PATH = ROOT / "docs/Event/Upcoming_events.md"
NOW_RUNNING_PATH = ROOT / "docs/Event/Now_running.md"
PAST_EVENTS_PATH = ROOT / "docs/Event/Past_events.md"
FRIENDS_INDEX_PATH = ROOT / "docs/hc-archive/index.md"
FRIENDS_PAGE_PATH = ROOT / "docs/hc-archive/friends.md"

HOME_START_MARKER = "<!-- 主页赛事展示_开始 -->"
HOME_END_MARKER = "<!-- 主页赛事展示_结束 -->"
EVENT_START_MARKER = "<!-- 赛事内容部分_开始 -->"
EVENT_END_MARKER = "<!-- 赛事内容部分_结束 -->"
UTC_PLUS_8 = timezone(timedelta(hours=8))
REQUIRED_FILES = (
    HOME_INDEX_PATH,
    EVENT_INDEX_PATH,
    CN_JSON_PATH,
    GLOBAL_JSON_PATH,
    FRIENDS_INDEX_PATH,
    FRIENDS_PAGE_PATH,
)

DISPLAY_LIMIT = 6


def read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def write_text(path: Path, content: str) -> None:
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def replace_between_markers(path: Path, start_marker: str, end_marker: str, new_content: str) -> None:
    content = path.read_text(encoding="utf-8")
    start = content.find(start_marker)
    end = content.find(end_marker)
    if start == -1 or end == -1 or start >= end:
        raise ValueError(f"Markers not found in {path}")

    start += len(start_marker)
    updated = content[:start] + "\n" + new_content.strip("\n") + "\n    " + content[end:]
    write_text(path, updated)


def parse_cn_datetime(value: str) -> datetime:
    return datetime.strptime(value, "%Y年%m月%d日 %H:%M").replace(tzinfo=UTC_PLUS_8)


def parse_global_range(value: str) -> tuple[datetime, datetime]:
    cleaned = value.removesuffix(" UTC+8")
    start_text, end_text = cleaned.split(" - ", maxsplit=1)
    return (
        datetime.strptime(start_text, "%Y-%m-%d %H:%M:%S").replace(tzinfo=UTC_PLUS_8),
        datetime.strptime(end_text, "%Y-%m-%d %H:%M:%S").replace(tzinfo=UTC_PLUS_8),
    )


def classify_event(now: datetime, start: datetime, end: datetime) -> str:
    if now < start:
        return "upcoming"
    if start <= now <= end:
        return "running"
    return "past"


def sanitize_link(link: str) -> str:
    cleaned = (link or "").strip()
    if not cleaned or cleaned == "/isPrepare":
        return ""
    return cleaned


def render_link(label: str, link: str) -> str:
    return f"[{label}]({link})" if link else label


def load_cn_events(now: datetime) -> list[dict[str, Any]]:
    payload = read_json(CN_JSON_PATH)
    events: list[dict[str, Any]] = []

    for item in payload["data"]["result"]:
        start = parse_cn_datetime(item["comp_time_start"])
        end = parse_cn_datetime(item["comp_time_end"])
        events.append(
            {
                "name": item["name"],
                "link": sanitize_link(item["link"]),
                "start": start,
                "end": end,
                "start_text": item["comp_time_start"],
                "end_text": item["comp_time_end"],
                "detail": item.get("detail", "") or "待补充",
                "status": classify_event(now, start, end),
            }
        )

    return sorted(events, key=lambda event: event["start"])


def load_global_events(now: datetime) -> list[dict[str, Any]]:
    payload = read_json(GLOBAL_JSON_PATH)
    events: list[dict[str, Any]] = []

    for item in payload:
        start, end = parse_global_range(item["比赛时间"])
        events.append(
            {
                "name": item["比赛名称"],
                "link": sanitize_link(item.get("比赛链接", "")),
                "logo": item.get("比赛标志", ""),
                "time_text": item["比赛时间"],
                "calendar": item.get("添加日历", ""),
                "format": item.get("比赛形式", "未知"),
                "weight": item.get("比赛权重", "未知"),
                "organizer": item.get("赛事主办", "未知"),
                "start": start,
                "end": end,
                "status": classify_event(now, start, end),
            }
        )

    return sorted(events, key=lambda event: event["start"])


def render_cn_event(event: dict[str, Any]) -> str:
    name = render_link(event["name"], event["link"])
    return "\n".join(
        [
            f'??? Quote "{event["name"]}"  ',
            f'    **比赛名称** : {name}  ',
            f'    **比赛时间** : {event["start_text"]} - {event["end_text"]}  ',
            f'    **比赛详细** : {event["detail"]}  ',
            "    ",
        ]
    )


def render_global_event(event: dict[str, Any]) -> str:
    headline = render_link(event["name"], event["link"])
    lines = [f'??? Quote "{headline}"  ']
    if event["logo"] and event["link"]:
        lines.append(f'    [![]({event["logo"]}){{ width="200" align=left }}]({event["link"]})  ')
    lines.extend(
        [
            f'    **比赛名称** : {headline}  ',
            f'    **比赛形式** : {event["format"]}  ',
            f'    **比赛时间** : {event["time_text"]}  ',
            f'    **比赛权重** : {event["weight"]}  ',
            f'    **赛事主办** : {event["organizer"]}  ',
        ]
    )
    if event["calendar"]:
        lines.append(f'    **添加日历** : {event["calendar"]}  ')
    lines.append("    ")
    return "\n".join(lines)


def render_event_list(events: list[dict[str, Any]], renderer: Any) -> str:
    if not events:
        return "暂无已录入赛事。"
    return "\n\n".join(renderer(event) for event in events)


def render_home_events(cn_events: list[dict[str, Any]], global_events: list[dict[str, Any]]) -> str:
    active_cn = [event for event in cn_events if event["status"] != "past"][:DISPLAY_LIMIT]
    active_global = [event for event in global_events if event["status"] != "past"][:DISPLAY_LIMIT]

    return "\n".join(
        [
            '=== "国内比赛"',
            render_event_list(active_cn, render_cn_event),
            "",
            '=== "国外比赛"',
            render_event_list(active_global, render_global_event),
        ]
    )


def render_event_index(cn_events: list[dict[str, Any]], global_events: list[dict[str, Any]]) -> str:
    sections = [
        '=== "查看比赛:"',
        "",
        '    !!! warning "健康比赛忠告"',
        '        抵制不良比赛，拒绝盗版比赛。注意自我保护，谨防受骗上当。  ',
        '        适度CTF益脑，沉迷CTF伤身。合理安排时间，享受健康生活。',
        "",
    ]

    status_labels = (
        ("running", "*正在进行*"),
        ("upcoming", "*即将开始*"),
        ("past", "*已经结束*"),
    )
    for status, label in status_labels:
        cn_group = [event for event in cn_events if event["status"] == status]
        global_group = [event for event in global_events if event["status"] == status]
        sections.extend(
            [
                f'=== "{label}"',
                '    === "国内赛事"',
                indent_block(render_event_list(cn_group, render_cn_event), "        "),
                '    === "国际赛事"',
                indent_block(render_event_list(global_group, render_global_event), "        "),
                "",
            ]
        )

    return "\n".join(sections).rstrip()


def render_split_page(title: str, cn_events: list[dict[str, Any]], global_events: list[dict[str, Any]]) -> str:
    return "\n".join(
        [
            "---",
            "comments: true",
            "---",
            f"# {title}",
            "",
            "## 国内赛事",
            "",
            render_event_list(cn_events, render_cn_event),
            "",
            "## 国际赛事",
            "",
            render_event_list(global_events, render_global_event),
        ]
    )


def indent_block(content: str, prefix: str) -> str:
    return "\n".join(f"{prefix}{line}" if line else prefix.rstrip() for line in content.splitlines())


def ensure_required_files() -> None:
    missing_files = [str(path) for path in REQUIRED_FILES if not path.exists()]
    if missing_files:
        missing_output = "\n".join(missing_files)
        raise FileNotFoundError(f"Missing required documentation files:\n{missing_output}")


def update_files() -> None:
    ensure_required_files()
    now = datetime.now(timezone.utc).astimezone(UTC_PLUS_8)
    cn_events = load_cn_events(now)
    global_events = load_global_events(now)

    replace_between_markers(HOME_INDEX_PATH, HOME_START_MARKER, HOME_END_MARKER, render_home_events(cn_events, global_events))
    replace_between_markers(EVENT_INDEX_PATH, EVENT_START_MARKER, EVENT_END_MARKER, render_event_index(cn_events, global_events))

    write_text(
        UPCOMING_EVENTS_PATH,
        render_split_page(
            "即将开始",
            [event for event in cn_events if event["status"] == "upcoming"],
            [event for event in global_events if event["status"] == "upcoming"],
        ),
    )
    write_text(
        NOW_RUNNING_PATH,
        render_split_page(
            "正在进行",
            [event for event in cn_events if event["status"] == "running"],
            [event for event in global_events if event["status"] == "running"],
        ),
    )
    write_text(
        PAST_EVENTS_PATH,
        render_split_page(
            "已经结束",
            [event for event in cn_events if event["status"] == "past"],
            [event for event in global_events if event["status"] == "past"],
        ),
    )

    print("CyberForgeCamp rebuilt event pages from repository-local data.")


if __name__ == "__main__":
    update_files()
