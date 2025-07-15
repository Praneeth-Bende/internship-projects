# 💼 Internship Projects – Cybersecurity & Python

This repository contains 3 hands-on cybersecurity projects built using Python. Each project demonstrates a specific security concept such as password analysis, encrypted communication, and local vulnerability scanning.

---

## 📁 Project List

### 1️⃣ Password Strength Checker

A GUI-based tool that evaluates the strength of a user’s password using character analysis and gives real-time suggestions.

- **Tech:** Python, Tkinter
- **Features:**
  - Classifies passwords as Weak, Medium, or Strong
  - Detects missing character types
  - Generates secure password suggestions
- 📂 [`password-strength-checker`](./password-strength-checker)

---

### 2️⃣ Secure Chat App

An encrypted client-server chat system using AES symmetric encryption and socket programming.

- **Tech:** Python, `socket`, `threading`, `cryptography`
- **Features:**
  - End-to-end encrypted chat using Fernet (AES)
  - Supports multiple clients
  - Secure communication over LAN
- 📂 [`secure-chat-app`](./secure-chat-app)

---

### 3️⃣ Vulnerability Scanner

A localhost scanner that checks for open ports and running services using Nmap, and generates a detailed security report.

- **Tech:** Python, `nmap`, `socket`, `platform`
- **Features:**
  - Scans localhost (`127.0.0.1`) for open ports
  - Identifies running services and versions
  - Saves results in `report.txt`
- 📂 [`vulnerability-scanner`](./vulnerability-scanner)

---

## ✅ Requirements

```bash
pip install cryptography python-nmap
