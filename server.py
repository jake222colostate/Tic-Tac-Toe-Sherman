import socket
import threading
import json
import uuid

HOST = '127.0.0.1'
PORT = 12345
clients = {}
game_state = {'board': [' ' for _ in range(9)], 'current_turn': None}
running = True

def broadcast_message(message):
    for client in clients.values():
        client.sendall(json.dumps(message).encode())

def handle_client(client_socket, client_id):
    global game_state
    try:
        while running:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            data = json.loads(message)
            handle_message(data, client_socket, client_id)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        clients.pop(client_id, None)
        broadcast_message({'type': 'disconnect', 'client_id': client_id})
        print(f"Client {client_id} disconnected")

def handle_message(data, client_socket, client_id):
    global game_state
    pass

def start_server():
    global running
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print("Server started on port", PORT)

    def accept_clients():
        while running:
            try:
                client_socket, addr = server_socket.accept()
                client_id = str(uuid.uuid4())
                clients[client_id] = client_socket
                print(f"Client {client_id} connected from {addr}")
                threading.Thread(target=handle_client, args=(client_socket, client_id)).start()
            except socket.error:
                break

    threading.Thread(target=accept_clients).start()

    # Stop server on user input
    input("Press Enter to stop the server...\n")
    running = False
    server_socket.close()
    print("Server stopped.")

if __name__ == "__main__":
    start_server()
