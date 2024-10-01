import socket
import threading
import json

HOST = '127.0.0.1'
PORT = 65432 

clients = []

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    clients.append(conn)
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = json.loads(data.decode())
            print(f"Received message from {addr}: {message}")
            for client in clients:
                if client != conn:
                    client.sendall(data)
    except (ConnectionResetError, json.JSONDecodeError):
        print(f"Connection lost with {addr}")
    finally:
        print(f"Disconnected from {addr}")
        clients.remove(conn)
        conn.close()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            print(f"Accepted connection from {addr}")
            threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    main()
