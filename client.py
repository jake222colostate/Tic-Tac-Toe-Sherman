import socket
import threading
import json

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            data = json.loads(message)
            handle_server_message(data)
        except Exception as e:
            print(f"Error: {e}")
            break

def handle_server_message(data):
    if data['type'] == 'update':
        print("Game State Updated:", data['game_state'])
    elif data['type'] == 'join':
        print(f"New player joined: {data['client_id']}")
    elif data['type'] == 'disconnect':
        print(f"Player {data['client_id']} disconnected")

def send_move(client_socket, move):
    message = {'type': 'move', 'move': move}
    client_socket.sendall(json.dumps(message).encode())

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    
    threading.Thread(target=receive_messages, args=(client_socket,)).start()
    
    try:
        while True:
            move = input("Enter move (0-8): ")
            send_move(client_socket, int(move))
    except KeyboardInterrupt:
        client_socket.close()

if __name__ == "__main__":
    start_client()
