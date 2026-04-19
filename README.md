# CyberForgeCamp

Hands-on cybersecurity training camp: labs, CTFs, and red team ops for skill-forging.

🇨🇳 中文 | [🇬🇧 English](README_EN.md)

---

# 🛡️ 网络安全小组培训仓库

<div align="center">
  
![Security Banner](https://img.shields.io/badge/Red%20Team-Cyber%20Security-red?style=for-the-badge&logo=kalilinux)
![CTF](https://img.shields.io/badge/CTF-Competition-blue?style=for-the-badge&logo=ctftime)
![License](https://img.shields.io/badge/License-Apache%202.0-blue?style=for-the-badge)

**从入门到实战 | 技能树全覆盖 | 红队思维养成**

[📖 课程导览](#-课程导览) • [🚀 快速开始](#-快速开始) • [🗂️ 内容结构](#️-内容结构) • [🌐 文档站](#-文档站) • [🤝 贡献指南](#-贡献指南)

</div>

---

## ✨ 关于仓库

本仓库是 **Aegis CyberKnights（青海大学网络安全小组）** 的核心培训资源库，旨在为社团成员提供系统化的网络安全技能训练，涵盖：

- 🔐 **基础技能**：Linux、网络协议、Web 前后端安全、数据库安全、密码学
- 🏆 **CTF 竞赛**：Pwn、Reverse、Crypto、Web、Misc 等主要题型训练
- 🎯 **红队渗透**：信息收集、漏洞利用、横向移动、权限维持与对抗思路
- 🧪 **实战演练**：靶机场景、CTF 真题复盘、环境搭建与训练题复现

本仓库当前已经将 **Hello-CTF** 的核心入门内容、文档组织经验与在线文档实现方式吸收到 CyberForgeCamp 中。
对外统一以 **CyberForgeCamp** 为主身份呈现，Hello-CTF 仅作为内容来源与整合致谢保留在本 README 中说明。

---

## 🧭 推荐学习路径

> **⚠️ 重要**：内容按技能分类组织，但建议按以下顺序学习，避免跳跃造成基础不牢。

| 阶段 | 学习内容 | 推荐入口 |
| :---: | :--- | :--- |
| 0️⃣ | **前言与学习方法** | 文档站 `00-Basics / 前言与入门` |
| 1️⃣ | **环境配置与工具准备** | 文档站 `00-Basics / 环境准备` |
| 2️⃣ | **MISC / Web / Crypto 入门** | 文档站 `01-CTF` |
| 3️⃣ | **Reverse / Pwn 进阶** | 文档站 `01-CTF` |
| 4️⃣ | **Red Team 与 AWD 模式** | 文档站 `02-RedTeam` |
| 5️⃣ | **靶场、容器模板与部署** | 文档站 `03-Labs` |
| 6️⃣ | **扩展专题与资源归档** | 文档站 `04-Resources` |
| 7️⃣ | **赛事日历、赛事资料与竞赛复盘** | 文档站 `05-Contest` |

> 💡 可根据自身基础跳过部分阶段，但建议至少先完成前言、环境准备与一个方向的基础入门，再进入复杂题型或红队内容。

---

## 📚 课程导览

### 按技能领域

| 领域 | 主要内容 | 适合阶段 |
| :--- | :--- | :---: |
| 🖥️ **系统与网络基础** | 环境搭建、工具链、实验准备 | 0~1 |
| 🧩 **CTF 基础** | MISC、Web、Crypto 入门知识与题型方法 | 2 |
| 🛠️ **CTF 进阶** | Reverse、Pwn、调试、保护与对抗技巧 | 3 |
| 🎯 **Red Team** | 信息收集、攻防模式、横向与对抗思路 | 4 |
| 🧪 **Labs** | 靶场、容器模板、复现实验 | 5 |
| 📦 **Resources** | AI / 区块链专题、书单、视频、Docker 资料 | 6 |
| 🏁 **Contest** | 赛事日历、平台使用、赛事资料归档 | 7 |

### 按目标人群

| 阶段 | 方向 | 主要内容 | 适合人群 |
| :---: | :---: | :--- | :---: |
| 🟢 **Level 0** | 基础筑基 | 学习方式、环境、工具、训练路线 | 全员必修 |
| 🔵 **Level 1** | CTF 入门 | Web / Misc / Crypto 基础与常用方法 | 初学者 |
| 🟡 **Level 2** | CTF 进阶 | Reverse / Pwn / 调试与利用链 | 竞赛选手 |
| 🟠 **Level 3** | Red Team 基础 | 信息收集、攻防模式、实战思路 | 渗透测试兴趣者 |
| 🔴 **Level 4** | 实战扩展 | 靶场、容器模板、专题资源与赛事资料 | 进阶学习者 |

---

## 🚀 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/TianJiHub/CyberForgeCamp.git
cd CyberForgeCamp
```

### 2. 本地运行在线文档

```bash
pip install -r requirements.txt
mkdocs serve
```

默认访问地址：`http://127.0.0.1:8000`

### 3. 推荐阅读入口

- 新手：从文档站首页进入 `00-Basics`
- 有基础：直接进入 `01-CTF`、`02-RedTeam`、`03-Labs` 等分区
- 想看赛事与归档：直接查看 `05-Contest`

---

## 🗂️ 内容结构

当前仓库采用 **CyberForgeCamp 主身份 + MkDocs 在线文档站** 的整合结构：

```text
CyberForgeCamp/
├── README.md
├── README_EN.md
├── mkdocs.yml
├── build.py
├── docs/
│   ├── home/                 # 文档站首页
│   ├── 00-Basics/            # 前言、环境、快速开始
│   ├── 01-CTF/               # Web、Misc、Crypto、Reverse、Pwn、知识标签
│   ├── 02-RedTeam/           # AWD 与红队相关内容
│   ├── 03-Labs/              # 靶场、容器扩展、命题教程、模板
│   ├── 04-Resources/         # 工具、AI、区块链、附录、归档、技能图谱
│   ├── 05-Contest/           # 赛事日历与赛事页面
│   ├── assets/               # 共享静态资源
│   ├── sidebar/              # 独立侧边栏页面
│   └── stylesheets/          # 自定义样式
├── overrides/                # MkDocs Material 覆写
└── .github/workflows/        # 文档构建与部署工作流
```

对外的在线文档导航已经统一映射为：

- `00-Basics`
- `01-CTF`
- `02-RedTeam`
- `03-Labs`
- `04-Resources`
- `05-Contest`

也就是说，Hello-CTF 的内容已经按 CyberForgeCamp 的学习路径和知识结构进行了吸收，而不是作为独立子项目继续暴露。

---

## 🌐 文档站

本仓库内置一套基于 **MkDocs Material** 的在线文档站实现，用于把训练内容、导航、赛事页与专题页统一发布出来。

### GitHub Pages 访问入口

- 在线页面首页：<https://tianjihub.github.io/CyberForgeCamp/>
- 推荐从首页进入后，按导航依次查看 `00-Basics`、`01-CTF`、`02-RedTeam`、`03-Labs`、`04-Resources`、`05-Contest`
- 想直接查看赛事 page 页面：<https://tianjihub.github.io/CyberForgeCamp/05-Contest/events/>

### 本地预览

```bash
mkdocs serve
```

### 构建静态站点

```bash
mkdocs build --strict
```

### 文档站特点

- 保留了 Hello-CTF 在「新手友好」「按主题组织」「在线阅读」方面的成熟经验
- 统一改造为 CyberForgeCamp 的导航、品牌和内容结构
- 首页、赛事页、专题页与 MkDocs 正文页可以一起发布

---

## 🤝 贡献指南

我们欢迎每一位成员贡献内容。

### 你可以：

- 📝 提交更好的题解、训练材料或实验记录
- 🛠️ 补充工具使用说明、环境配置与部署模板
- 🐛 修正文档中的错误、过时信息与失效链接
- 🌟 补充学习资源、书单、视频与专题资料

### 流程：

1. Fork 本仓库
2. 新建分支 `git checkout -b feat/add-xxx`
3. 提交修改 `git commit -m "add: xxx docs"`
4. 推送并创建 Pull Request

---

## 📜 许可证

本仓库采用 **Apache License 2.0** 开源。
如需转载或二次分发，请保留原始版权声明、免责声明，并注明你的修改内容。

---

## 🙌 致谢

- 感谢 Aegis CyberKnights 成员参与内容整理与训练实践
- 感谢 Hello-CTF 项目在 CTF 入门内容、文档组织与在线文档实现方面提供的基础经验，使 CyberForgeCamp 能够更完整地完成整合与延续

---

<div align="center">
  
**⭐ 如果这个仓库对你有帮助，请点亮右上角的 Star ⭐**

**保持好奇，保持攻击性 —— HACK THE FUTURE**

[🔝 回到顶部](#-网络安全小组培训仓库)

</div>
