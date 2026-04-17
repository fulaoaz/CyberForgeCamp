<<<<<<< HEAD
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

[📖 课程导览](#-课程导览) • [🚀 快速开始](#-快速开始) • [🗂️ 目录结构](#️-目录结构) • [🤝 贡献指南](#-贡献指南)

</div>

---

## ✨ 关于仓库

本仓库是 **Aegis CyberKnights（青海大学网络安全小组）** 的核心培训资源库，旨在为社团成员提供系统化的网络安全技能培训，涵盖：

- 🔐 **基础技能**：Linux、网络协议、Web前后端安全、数据库安全、密码学
- 🏆 **CTF竞赛**：PWN、Reverse、Crypto、Web、Misc 全题型训练
- 🎯 **红队渗透**：信息收集、漏洞利用、内网渗透、免杀技术
- 🧪 **实战演练**：靶机实战、CTF真题复盘、红队模拟演练

无论你是零基础小白还是已有经验的老手，这里都有适合你的学习路径。

---

## 🧭 推荐学习路径

> **⚠️ 重要**：目录按技能分类，但建议按以下顺序学习，避免跳跃造成基础不牢。

| 阶段 | 学习内容 | 对应目录                                        |
| :---: | :--- |:--------------------------------------------|
| 0️⃣ | **环境配置** | `00-Basics/00-Environment_Setup/`           |
| 1️⃣ | **网络安全介绍** | `00-Basics/01-Security_Intro/`              |
| 2️⃣ | **Linux基础命令与脚本** | `00-Basics/02-Linux/`                       |
| 3️⃣ | **计算机网络基础（TCP/IP、Wireshark）** | `00-Basics/03-Network/`                     |
| 4️⃣ | **Python安全编程** | `00-Basics/04-Python/`                      |
| 5️⃣ | **Web前端基础（HTML）** | `00-Basics/05-HTML/`                        |
| 6️⃣ | **Web前端基础（JavaScript）** | `00-Basics/06-JavaScript/`                  |
| 7️⃣ | **Web后端基础（PHP）** | `00-Basics/07-PHP/`                         |
| 8️⃣ | **数据库安全基础（MySQL）** | `00-Basics/08-MySQL/`                       |
| 9️⃣ | **密码学基础** | `00-Basics/09-Crypto/`                      |
| 🔟 | **CTF入门（Web、Misc）** | `01-CTF/01-Web/`、`01-CTF/02-Misc/`          |
| 1️⃣1️⃣ | **CTF进阶（Pwn、Reverse、Crypto）** | `01-CTF/03-Pwn/`、`04-Reverse/`、`05-Crypto/` |
| 1️⃣2️⃣ | **红队基础（信息收集、漏洞扫描）** | `02-RedTeam/01-Recon/`、`02-Exploit/`        |
| 1️⃣3️⃣ | **红队高阶（内网、免杀）** | `02-RedTeam/03-Lateral/`、`04-Evasion/`      |
| 1️⃣4️⃣ | **实战靶场 & CTF真题** | `03-Labs/`、`05-Contest/`                    |

> 💡 可根据自身基础跳过某些阶段，但建议至少完成阶段0~3后再挑战CTF或红队内容。

---

## 📚 课程导览

### 按技能领域

| 领域 | 主要内容 | 适合阶段 |
| :--- | :--- | :---: |
| 🖥️ **系统与网络基础** | Linux、计算机网络、Wireshark | 1~2 |
| 🐍 **安全开发** | Python安全脚本、Web前端（HTML/JS）、后端（PHP） | 3~4 |
| 🗄️ **数据库安全** | MySQL基础、SQL注入原理与防御 | 5 |
| 🔐 **密码学** | 古典密码、对称/非对称加密、哈希函数 | 6 |
| 🏁 **CTF竞赛** | Web、Pwn、Reverse、Crypto、Misc全题型 | 7~8 |
| 🎯 **红队渗透** | 信息收集、漏洞利用、内网横向、免杀 | 9~10 |
| 🧪 **实战演练** | VulnHub、HTB、校内靶场、真题复盘 | 11 |

### 按方向
| 阶段 | 方向 | 主要内容 |  适合人群   |
| :---: | :---: | :--- |:-------:|
| 🟢 **Level 0** | 基础筑基 | Linux命令、计算机网络、Python安全编程、虚拟机使用、Web前端基础、PHP/MySQL安全入门 |  全员必修   |
| 🔵 **Level 1** | CTF入门 | 常用工具(Burp/IDA/GDB)、Web基础、隐写术、编码分析 |  初赛选手   |
| 🟡 **Level 2** | CTF进阶 | 堆栈溢出、ROP链、RSA变种、SQL注入绕过、流量分析 |  专赛选手   |
| 🟠 **Level 3** | 红队基础 | 信息收集(OneForAll/nmap)、漏洞扫描、MSF/Cobalt Strike | 渗透测试兴趣者 |
| 🔴 **Level 4** | 红队高阶 | 域渗透、权限维持、免杀、钓鱼攻击、内网横向移动 | 红队预备队员  |

> 💡 建议按顺序学习，但可根据自身基础跳跃选择。

---

## 🚀 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/TianJiHub/CyberForgeCamp.git
cd CyberForgeCamp
```

### 2. 环境准备

- 推荐使用 **Kali Linux** 或 **Parrot OS**（虚拟机或物理机）
- 安装基础工具：
  ```bash
  sudo apt update && sudo apt install python3 python3-pip git vim curl wget nmap burpsuite
  ```

### 3. 学习路径

- 新手：从「推荐学习路径」阶段0开始，逐项阅读文档并完成练习
- 有基础：直接进入感兴趣的技能目录，参考目录内的 README.md 了解先修要求

---

## 🗂️ 目录结构

```text
CyberForgeCamp/
├── 00-Basics/                          # 基础技能（按推荐顺序编号）
│   ├── README.md                        # 基础技能总览
│   ├── 00-Environment_Setup/            # 环境配置（Kali/Docker/Burp/IDA/IDE）
│   ├── 01-Security_Intro/               # 网络安全介绍（威胁模型、攻击面、法律法规）
│   ├── 02-Linux/                        # Linux命令、权限、脚本
│   ├── 03-Network/                      # TCP/IP、Wireshark分析
│   ├── 04-Python/                       # Python安全编程（requests、scapy、pwntools）
│   ├── 05-HTML/                         # HTML安全（XSS、DOM Clobbering、CSP绕过）
│   ├── 06-JavaScript/                   # JavaScript安全（原型链污染、XSS Payload、CSRF）
│   ├── 07-PHP/                          # PHP安全（文件包含、反序列化、RCE、WebShell）
│   ├── 08-MySQL/                        # MySQL安全（SQL注入、权限提升、UDF）
│   └── 09-Crypto/                       # 古典密码、对称/非对称加密、哈希函数
├── 01-CTF/                             # CTF竞赛专题
│   ├── README.md                        # CTF总览
│   ├── 01-Web/                          # SQLi、XSS、SSRF、RCE
│   ├── 02-Misc/                         # 取证、流量、隐写
│   ├── 03-Pwn/                          # 栈溢出、堆利用、格式化字符串
│   ├── 04-Reverse/                      # IDA、Ghidra、反混淆
│   └── 05-Crypto/                       # 现代密码、侧信道
├── 02-RedTeam/                         # 红队渗透测试
│   ├── README.md                        # 红队总览
│   ├── 01-Recon/                        # 信息收集（主动/被动）
│   ├── 02-Exploit/                      # 漏洞利用与武器化（MSF/Cobalt Strike）
│   ├── 03-Lateral/                      # 横向移动与权限维持
│   └── 04-Evasion/                      # 免杀与绕过（AV/EDR）
├── 03-Labs/                            # 实战靶场
│   ├── README.md                        # 实战靶场总览
│   ├── 01-VulnHub/                      # 精选VulnHub靶机Writeup
│   ├── 02-HTB/                          # HackTheBox退役机攻略
│   └── 03-Internal/                     # 校内自建靶场
├── 04-Resources/                       # 学习资源
│   ├── README.md                        # 学习资源总览
│   ├── 01-Books/                        # 推荐PDF书籍
│   ├── 02-Tools/                        # 工具清单与配置
│   └── 03-Cheatsheets/                  # 常用命令速查表
└── 05-Contest/                         # 历年CTF真题 & 竞赛复盘
    └──  README.md                       # 竞赛真题总览
```

---

## 🧪 实战项目

- **每周一练**：每周末发布一个靶机或CTF题目，次周公布Writeup
- **月度内网渗透赛**：模拟企业内网环境，分组对抗
- **红队演练日**：使用Cobalt Strike进行全流程模拟攻击
- **联合CTF**：与兄弟高校合办线上赛（仓库内提供往期题目）

> 📢 具体活动时间请关注社团群公告。

---

## 🤝 贡献指南

我们欢迎每一位成员贡献内容！

### 你可以：

- 📝 提交更优秀的Writeup或解题脚本
- 🛠️ 增加新的工具使用教程
- 🐛 修正现有文档中的错误或过时内容
- 🌟 分享自己整理的速查表/脑图

### 流程：

1. Fork 本仓库
2. 新建你的分支 `git checkout -b feat/add-xxx`
3. 提交修改 `git commit -m "add: xxx writeup"`
4. 推送并创建 Pull Request

> 所有贡献者将出现在仓库的 `CONTRIBUTORS.md` 中。

---

## 📜 许可证

本仓库内容采用 Apache License 2.0 开源，代码和文档可自由使用，但需保留版权声明、免责声明，并注明修改内容（如有）。

---

## 🙌 致谢

- 感谢所有参与内容整理和培训的社团成员

---

<div align="center">
  
**⭐ 如果这个仓库对你有帮助，请点亮右上角的 Star ⭐**

**保持好奇，保持攻击性 —— HACK THE FUTURE**

[🔝 回到顶部](#-网络安全小组培训仓库)

</div>


=======
<div align="center">
     <h2>Hello CTF</h2>
     <div align="center">
    </div> 
    <a href="http://hello-ctf.com/"> <img src="https://badgen.net/badge/Mkdocs/%E5%9C%A8%E7%BA%BF%E9%98%85%E8%AF%BB?icon=chrome&color=black"></a>
    <a href="https://github.com/ProbiusOfficial/Hello-CTF"> <img src="https://badgen.net/github/stars/ProbiusOfficial/Hello-CTF?icon=github&color=black"></a>
    <a href="https://github.com/ProbiusOfficial/Hello-CTF"> <img src="https://badgen.net/github/forks/ProbiusOfficial/Hello-CTF?icon=github&color=black"></a>
    <a href="https://github.com/ProbiusOfficial/Hello-CTF/blob/main/LICENSE"> <img src="https://badgen.net/badge/license/GPLv3/"></a>
    <br>
     <a href="http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=wJ35e-T-qSlU7Y3Cs-PAasrAvZfRSc9k&authKey=WNEQbZUpolxgfKjUHHoUIoTBvSnvk2jZtcyWlhaDcUZ6ZYGgvywqi1ah5D7UwUrg&noverify=0&group_code=590430891"> <img src="https://img.shields.io/badge/QQ%20Group-590430891-black"></a>
     <a href="https://gitcode.com/Probius/Hello-CTF"> <img src="https://gitcode.com/Probius/Hello-CTF/star/badge.svg"></a>
    <br>
    </div>


文档依靠Mkdocs-material 基于GitHub Pages 依靠 gh-pages 部署在 [https://hello-ctf.com/](https://hello-ctf.com/)   

因接入CDN，本站链接变更为：[https://hello-ctf.com/](https://hello-ctf.com/) ，感谢渊龙Sec安全团队[@AabyssZG](https://github.com/AabyssZG) 曾哥提供的CDN支持~

您可以直接访问该页面[在线阅读](https://hello-ctf.com/)，如果您想要转载本项目，请带上项目源地址：https://github.com/ProbiusOfficial/Hello-CTF

如果文档有帮助到你，麻烦点一个 :star: 支持一下！！

## 关于

随着网络安全的发展，有越来越多的小伙伴了解到了 **CTF** ，并且想要参与到比赛中来，但仅仅寻找学习资源就耗费了大量精力；  
同时每年招新时 或者带新人入门的时候 都会面临很多相似的问题，于是本项目应运而生。  
本项目旨在创建一本开源免费、新手友好的「 **夺旗赛 | CTF(Capture The Flag)** 」入门教程。  

- 对于每个方向的基础知识点，我们都会尽力提供相应的题目(包括题目附件 题目源码 Dockerfile),所有题目均可本地部署也可在NSSCTF平台上直接开启,我们会在教程中逐步引导读者,并且鼓励读者自行复现,使学习过程更加具象;  
- 在提供基础知识外，本书也将提供CTF相关的信息聚合，以消除信息差;  
- 书籍在每篇文章下都设置有讨论区，欢迎讨论，提问，以及建议;   

## 加入我们

本书仍然处于更新阶段，我们还有很多内容需要完善，欢迎您加入我们，一起完善本书，让更多的人了解CTF，参与CTF，享受CTF的乐趣。
您随时可以通过提交 [「 PR (Pull Request) 」](https://github.com/ProbiusOfficial/Hello-CTF/pulls)来协助我们完成本项目。

- 如果您在阅读过程中发现任何 知识点错误，内容模糊，名词拼写错误等等的问题，还请您协助我们进行修改，您可以直接在评论区中提出，也可以直接提交PR。
- 如果您有好的题目，好的题解，好的知识点讲解，或者其他合作意向，也欢迎您联系探姬([By QQ](2293808331))或者开启issue。

## 致谢
本项目基于[Mkdocs-material](https://github.com/squidfunk/mkdocs-material)搭建，感谢该项目提供的优秀的文档编写平台。  

项目最初只是一个Readme文档，受到 **[Hello-algo](https://github.com/krahets/hello-algo/)** 项目的启发，这才有了这个项目现在的样子，如果你对算法感兴趣，强烈推荐这本在数据结构期末考试前帮了我大忙的书籍。  

在提出这个项目的想法的时候，因为国内的环境问题，我怀疑过很多次自己这样做是否有意义，感谢 [*Ari @deCafLatte*](https://github.com/deCafLatte) 的支持和鼓励，让我有动力做自己喜欢的事情。

本项目的完成离不开以下小伙伴的贡献，感谢他们的付出。
<p align="left">
    <a href="https://github.com/ProbiusOfficial/Hello-CTF/graphs/contributors">
        <img width="550" src="https://contrib.rocks/image?repo=ProbiusOfficial/Hello-CTF" />
    </a>
</p>

**向每一个为开源社区做出努力和贡献的人，致以崇高的敬意！！！**
>>>>>>> hello-ctf/main
