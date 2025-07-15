# 🔐 Secure Chat App

A basic encrypted chat system using Python sockets and AES (Fernet) symmetric encryption.

## 📌 Features
- End-to-end encrypted messages
- Server-client chat architecture
- Multiple clients supported
- Easy to run on localhost for demonstration

## 🚀 How to Run

### 1. Install dependencies:
Make sure Python is installed. Then install the required library:

```bash
pip install cryptography
from cryptography.fernet import Fernet
print(Fernet.generate_key().decode())

Copy the printed key and paste it into encryption.py like this:

key = b'your-generated-key-here'

Run the Server
>>> python server.py

Run th Client
>>> python client.py
