import socket
import json
import threading

HOST = '127.0.0.1'
PORT = 65432

def send_message(sock):
    while True:
        message = input("Enter message: ")
        try:
            sock.sendall(json.dumps({"message": message}).encode())
        except BrokenPipeError:
            print("Failed to send message. Connection lost.")
            break

def receive_message(sock):
    while True:
        try:
            data = sock.recv(1024)
            if data:
                print(f"Received: {data.decode()}")
            else:
                break
        except socket.error:
            print("Error receiving data.")
            break

def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print(f"Connected to server at {HOST}:{PORT}")

            threading.Thread(target=receive_message, args=(s,)).start()

            send_message(s)
    except ConnectionRefusedError:
        print("Failed to connect to the server. Is it running?")

if __name__ == "__main__":
    main()