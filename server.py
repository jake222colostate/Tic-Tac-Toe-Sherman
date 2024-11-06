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

def reset_game_state():
    global game_state
    game_state = {'board': [' ' for _ in range(9)], 'current_turn': None}

def check_winner():
    board = game_state['board']
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return board[condition[0]]
    if ' ' not in board:
        return 'Draw'
    return None

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
    if data['type'] == 'move':
        move = data['move']
        if game_state['current_turn'] == client_id and game_state['board'][move] == ' ':
            game_state['board'][move] = 'X' if client_id == list(clients.keys())[0] else 'O'
            winner = check_winner()
            if winner:
                if winner == 'Draw':
                    broadcast_message({'type': 'draw'})
                else:
                    broadcast_message({'type': 'winner', 'winner': client_id})
                reset_game_state()
            else:
                game_state['current_turn'] = list(clients.keys())[1] if game_state['current_turn'] == list(clients.keys())[0] else list(clients.keys())[0]
                broadcast_message({'type': 'update', 'game_state': game_state})
        else:
            client_socket.sendall(json.dumps({'type': 'error', 'message': 'Invalid move or not your turn.'}).encode())

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
                if len(clients) < 2:
                    client_id = str(uuid.uuid4())
                    clients[client_id] = client_socket
                    print(f"Client {client_id} connected from {addr}")
                    if len(clients) == 1:
                        game_state['current_turn'] = client_id
                    threading.Thread(target=handle_client, args=(client_socket, client_id)).start()
                    broadcast_message({'type': 'join', 'client_id': client_id})
                    broadcast_message({'type': 'update', 'game_state': game_state})
                else:
                    client_socket.sendall(json.dumps({'type': 'error', 'message': 'Game is full.'}).encode())
                    client_socket.close()
            except socket.error:
                break

    threading.Thread(target=accept_clients).start()

    # Stop server on user input
    input("Press Enter to stop the server...\n")
    running = False
    server_socket.close()
    print("Server stopped.")

if __name__ == "__main__":
    reset_game_state()
    start_server()
