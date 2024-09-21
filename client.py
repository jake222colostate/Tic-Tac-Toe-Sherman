import socket
import logging

logging.basicConfig(level=logging.INFO)

def communicate_with_server(client_socket):
    try:
        while True:
            message = input("Enter message to send to server: ")
            if message.lower() == 'exit':
                break
            client_socket.send(message.encode())
            response = client_socket.recv(1024).decode()
            logging.info(f"Server response: {response}")
    except Exception as e:
        logging.error(f"Communication error: {e}")
    finally:
        logging.info("Client disconnected")
        client_socket.close()

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(('localhost', 12345))
        logging.info("Connected to server")
        communicate_with_server(client_socket)
    except ConnectionRefusedError:
        logging.error("Connection refused by the server")
    except socket.timeout:
        logging.error("Connection timed out")
    except Exception as e:
        logging.error(f"Connection failed: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()
