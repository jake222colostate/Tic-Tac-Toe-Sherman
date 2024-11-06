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
        print("\nGame State Updated:")
        print_board(data['game_state']['board'])
        print(f"Current Turn: {data['game_state']['current_turn']}")
    elif data['type'] == 'join':
        print(f"New player joined: {data['client_id']}")
    elif data['type'] == 'disconnect':
        print(f"Player {data['client_id']} disconnected")
    elif data['type'] == 'winner':
        print(f"Player {data['winner']} wins!")
    elif data['type'] == 'draw':
        print("The game ended in a draw.")

def send_move(client_socket, move):
    message = {'type': 'move', 'move': move}
    client_socket.sendall(json.dumps(message).encode())

def print_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    
    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()
    
    try:
        while True:
            move = input("Enter your move (0-8): ").strip()
            if not move.isdigit() or not (0 <= int(move) <= 8):
                print("Invalid input. Please enter a number between 0 and 8.")
                continue
            send_move(client_socket, int(move))
    except KeyboardInterrupt:
        print("\nExiting the game.")
        client_socket.close()

if __name__ == "__main__":
    start_client()
