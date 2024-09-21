
import socket
import threading
import logging

logging.basicConfig(level=logging.INFO)

def handle_client(client_socket, address):
    logging.info(f"Connected to {address}")
    try:
        while True:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            logging.info(f"Received from {address}: {message}")
            client_socket.send("Message received".encode())
    except Exception as e:
        logging.error(f"Error with {address}: {e}")
    finally:
        logging.info(f"Disconnected from {address}")
        client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    logging.info("Server listening on port 12345")

    while True:
        client_socket, address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()

if __name__ == "__main__":
    start_server()
