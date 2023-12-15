import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(message)
        except ConnectionResetError:
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5555))

    username = input("Enter your username: ")
    client.send(username.encode('utf-8'))

    welcome_message = client.recv(1024).decode('utf-8')
    print(welcome_message)

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    while True:
        message = input()
        client.send(message.encode('utf-8'))

if __name__ == "__main__":
    main()
