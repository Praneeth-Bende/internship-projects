import socket
import threading
from encryption import encrypt_message, decrypt_message

HOST = '127.0.0.1'
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive_messages():
    while True:
        try:
            encrypted_msg = client.recv(1024)
            message = decrypt_message(encrypted_msg)
            print(f"\n[Friend]: {message}")
        except:
            print("[ERROR] Disconnected from server.")
            break

def send_messages():
    while True:
        msg = input("")
        encrypted = encrypt_message(msg)
        client.send(encrypted)

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()
