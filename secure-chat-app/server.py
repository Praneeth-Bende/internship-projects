import socket
import threading
from encryption import decrypt_message, encrypt_message

HOST = '127.0.0.1'
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.send(message)

def handle_client(client):
    while True:
        try:
            encrypted_msg = client.recv(1024)
            message = decrypt_message(encrypted_msg)
            print(f"[RECV] {message}")
            broadcast(encrypted_msg, client)
        except:
            clients.remove(client)
            client.close()
            break

print(f"Server running on {HOST}:{PORT}...")
while True:
    client, addr = server.accept()
    print(f"[NEW CONNECTION] {addr}")
    clients.append(client)
    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()
