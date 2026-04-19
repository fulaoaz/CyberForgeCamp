# 推送说明

## 步骤 1: Fork 仓库

1. 访问 https://github.com/TianJiHub/CyberForgeCamp
2. 点击右上角的 "Fork" 按钮
3. 等待 fork 完成

## 步骤 2: 添加你的 fork 作为 origin

在当前目录执行：

```bash
# 将你的 fork 添加为 origin（替换 YOUR_USERNAME 为你的 GitHub 用户名）
git remote add origin https://github.com/YOUR_USERNAME/CyberForgeCamp.git

# 或者使用 SSH（如果已配置 SSH 密钥）
git remote add origin git@github.com:YOUR_USERNAME/CyberForgeCamp.git
```

## 步骤 3: 推送到你的 fork

```bash
# 推送到你的 fork
git push origin main

# 如果需要强制推送（因为历史不同）
git push -f origin main
```

## 步骤 4: 创建 Pull Request（可选）

如果你想将更改合并回原仓库：

1. 访问你的 fork 页面
2. 点击 "Contribute" -> "Open pull request"
3. 填写 PR 说明，提交

## 当前状态

- ✅ 已合并 CyberForgeCamp 仓库内容
- ✅ 已解决所有冲突
- ✅ 已创建合并提交
- ⏳ 等待推送到你的 fork

## 当前结构摘要

- 文档源统一收敛到 `docs/`
- 目录按 `00-Basics` 到 `05-Contest` 编号结构组织
- 已移除根目录历史镜像目录与静态生成物
- README 与构建链路已对齐当前结构
