# 🛡️ Cybersecurity Training Repository

Hands-on cybersecurity training camp: labs, CTFs, and red team ops for skill-forging.

🇬🇧 English | [🇨🇳 中文](README.md)

---

<div align="center">
  
![Security Banner](https://img.shields.io/badge/Red%20Team-Cyber%20Security-red?style=for-the-badge&logo=kalilinux)
![CTF](https://img.shields.io/badge/CTF-Competition-blue?style=for-the-badge&logo=ctftime)
![License](https://img.shields.io/badge/License-Apache%202.0-blue?style=for-the-badge)

**From Zero to Hero | Full Skill Tree | Red Team Mindset**

[📖 Learning Path](#-recommended-learning-path) • [🚀 Quick Start](#-quick-start) • [📂 Directory Structure](#-directory-structure) • [🤝 Contribution Guide](#-contribution-guide)

</div>

---

## ✨ About

This repository is the core training resource for Aegis CyberKnights, the cybersecurity student club of Qinghai University, designed to provide systematic cybersecurity training for our members, including:

- 🔐 **Fundamentals**: Linux, networking, web frontend/backend security, database security, cryptography
- 🏆 **CTF Competitions**: PWN, Reverse, Crypto, Web, Misc — all categories covered
- 🎯 **Red Teaming**: Recon, exploitation, lateral movement, evasion, and full-chain penetration testing
- 🧪 **Hands-on Labs**: VulnHub, HTB, internal ranges, and real CTF challenge walkthroughs

Whether you're a complete beginner or an experienced player, you'll find a suitable learning path here.

---

## 🧭 Recommended Learning Path

> **⚠️ Important**: The repository now uses a numbered documentation structure under `docs/`. Follow the order below to build a clean foundation before jumping into specialized tracks.

| Step | Topic | Directory |
| :---: | :--- | :--- |
| 0️⃣ | **Orientation & Reading Guide** | `docs/00-Basics/` |
| 1️⃣ | **Environment Setup & Tooling** | `docs/00-Basics/environment/` |
| 2️⃣ | **Getting Started with CTF Workflow** | `docs/00-Basics/start/` |
| 3️⃣ | **CTF Core Categories (Web, Misc, Crypto, Reverse, Pwn)** | `docs/01-CTF/` |
| 4️⃣ | **Red Team / AWD Practice** | `docs/02-RedTeam/` |
| 5️⃣ | **Hands-on Labs, Docker Extensions, Challenge Authoring** | `docs/03-Labs/` |
| 6️⃣ | **Tools, AI, Appendix, Archives, Skill Maps** | `docs/04-Resources/` |
| 7️⃣ | **Contest Calendar and Event Tracking** | `docs/05-Contest/` |

> 💡 New readers should finish `docs/00-Basics/` before moving into `docs/01-CTF/` or `docs/02-RedTeam/`.

---

## 📚 Course Overview

### By Skill Area

| Area | Topics | Steps |
| :--- | :--- | :---: |
| 🖥️ **System & Networking** | Linux, TCP/IP, Wireshark | 1–2 |
| 🐍 **Secure Development** | Python, HTML/JS, PHP | 3–4 |
| 🗄️ **Database Security** | MySQL, SQL injection | 5 |
| 🔐 **Cryptography** | Classic & modern ciphers, hashing | 6 |
| 🏁 **CTF** | Web, Pwn, Reverse, Crypto, Misc | 7–8 |
| 🎯 **Red Teaming** | Recon, exploitation, lateral, evasion | 9–10 |
| 🧪 **Labs** | VulnHub, HTB, internal ranges | 11 |

### By Level

| Level | Direction | Key Topics | Target |
| :---: | :---: | :--- | :--- |
| 🟢 **Level 0** | Fundamentals | Linux, networking, Python, VM, Web basics, PHP/MySQL | Everyone |
| 🔵 **Level 1** | CTF Entry | Burp/IDA/GDB, Web basics, steganography, encoding | Beginners |
| 🟡 **Level 2** | CTF Advanced | Stack overflow, ROP, RSA variants, SQL injection bypass, traffic analysis | Competitors |
| 🟠 **Level 3** | Red Team Basics | Recon (OneForAll/nmap), scanning, MSF/Cobalt Strike | Pentesting enthusiasts |
| 🔴 **Level 4** | Red Team Advanced | Domain penetration, persistence, evasion, phishing, lateral movement | Red Team candidates |

> 💡 Follow the levels in order, but you can jump based on your current knowledge.

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/TianJiHub/CyberForgeCamp.git
cd CyberForgeCamp
```

### 2. Environment Setup

- Recommended OS: **Kali Linux** or **Parrot OS** (VM or bare metal)
- Install basic tools:
  ```bash
  sudo apt update && sudo apt install python3 python3-pip git vim curl wget nmap burpsuite
  ```

### 3. Learning Path

- **Beginners**: Start from Step 0 in the Recommended Learning Path, read documents and complete exercises.
- **Experienced**: Jump directly to the section you need under `docs/`, and use each section's `index.md` page as the entry point for prerequisites and navigation.

---

## 📂 Directory Structure

```text
CyberForgeCamp/
├── mkdocs.yml
├── build.py
├── docs/
│   ├── home/                           # Landing page and homepage modules
│   ├── 00-Basics/                      # Preface, environment, getting started
│   ├── 01-CTF/                         # Web, Misc, Crypto, Reverse, Pwn, tags
│   ├── 02-RedTeam/                     # AWD and red team topics
│   ├── 03-Labs/                        # Ranges, Docker extensions, challenge authoring, templates
│   ├── 04-Resources/                   # Toolkit, AI, blockchain, appendix, archive, skill maps
│   ├── 05-Contest/                     # Event calendar and contest pages
│   ├── assets/                         # Shared images and static resources
│   ├── sidebar/                        # Standalone sidebar pages
│   └── stylesheets/                    # Custom styles
├── overrides/                          # MkDocs Material overrides
└── .github/workflows/                  # Documentation build and deployment workflow
```

---

## 🧪 Practical Activities

- **Weekly Challenge**: A new VM or CTF problem every weekend, writeup published the following week.
- **Monthly Internal Pentesting Competition**: Simulate an enterprise network, team vs team.
- **Red Team Drill Day**: Full attack chain simulation using Cobalt Strike.
- **Joint CTF**: Online competition with partner universities (past challenges are in the repo).

> 📢 Check club announcements for schedules.

---

## 🤝 Contribution Guide

We welcome contributions from all members!

### You can:

- 📝 Submit better writeups or solution scripts
- 🛠️ Add new tool tutorials
- 🐛 Fix errors or outdated content
- 🌟 Share your own cheatsheets / mind maps

### Workflow:

1. Fork this repository
2. Create your branch `git checkout -b feat/add-xxx`
3. Commit your changes `git commit -m "add: xxx writeup"`
4. Push and open a Pull Request

> All contributors will be listed in `CONTRIBUTORS.md`.

---

## 📜 License

This repository is open-sourced under the Apache License 2.0. You are free to use the content, but you must retain the copyright notice, disclaimer, and indicate any changes made (if applicable).

---

## 🙌 Acknowledgements

- Thanks to all club members who contributed to content creation and training.

---

<div align="center">
  
**⭐ If this repository helps you, please star it! ⭐**

**Stay curious, stay offensive — HACK THE FUTURE**

[🔝 Back to top](#-cybersecurity-training-repository)

</div>
