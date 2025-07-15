# from cryptography.fernet import Fernet

# key = Fernet.generate_key()
# print("Generated key:", key.decode())

from cryptography.fernet import Fernet

key = b'ciDecSZL-dxOs_G3ygxE0y3oLOwKVFsaMIO6aFr8_lc='  # paste your generated key here
cipher = Fernet(key)

def encrypt_message(msg):
    return cipher.encrypt(msg.encode())

def decrypt_message(msg):
    return cipher.decrypt(msg).decode()
