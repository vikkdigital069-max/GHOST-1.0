# 👻 GHOST v1.0
### *Find the truth, protect the innocent.*

![Version](https://img.shields.io/badge/version-1.0-brightgreen)
![Language](https://img.shields.io/badge/language-Python-blue)
![Platform](https://img.shields.io/badge/platform-Termux%20%7C%20Linux-lightgrey)
![Status](https://img.shields.io/badge/status-stable-success)
![Author](https://img.shields.io/badge/author-vikkdigital069--max-purple)

---

## 📌 Description

**GHOST** is an OSINT (Open Source Intelligence) and tracking tool built for **educational purposes**. It allows you to:

- Check email addresses against public breach databases
- Validate phone numbers and detect country codes
- Search social media platforms for public profiles
- Generate detailed OSINT reports

> ⚠️ **WARNING:** This tool is for **EDUCATIONAL purposes only**.  
> Use it for **cyberbullying investigation** or **personal security**.  
> **Stalking, harassment, or any form of misuse is ILLEGAL.**  
> The developer is **NOT responsible** for any misuse.

---

## ✨ Features

| # | Feature | Description |
|---|---------|-------------|
| 1 | 📧 **Email Check** | Check email in public breach databases (HaveIBeenPwned) |
| 2 | 📱 **Phone Validation** | Validate phone number format & detect country |
| 3 | 🔍 **Social Search** | Search public social media profiles (simulated) |
| 4 | 📊 **Full Search** | Combine email/phone + social media search |
| 5 | 📋 **OSINT Report** | Generate detailed, clean report |
| 6 | 🎨 **Professional UI** | Clean, minimal, human-friendly interface |
| 7 | 🔄 **Loading Animation** | Smooth spinner + progress bar |
| 8 | 🔒 **Private Data** | All searches stay local & private |

---

## 🚀 Installation

### 1. Install Dependencies
```bash
pkg update && pkg upgrade -y
pkg install python -y
pip install requests
