import yaml
import socket
import threading
from logging import log_attack

def handle_connection(client_socket, addr):
    data = client_socket.recv(1024)  # Receive initial data
    # Handle data and logging here
    log_attack(addr, data)
    client_socket.close()

def main():
    with open('config.yaml') as config_file:
        config = yaml.safe_load(config_file)

    listen_ip = config['network']['listen_ip']
    ports = config['network']['ports']

    for port in ports:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((listen_ip, port))
        server.listen(5)

        print(f"Listening on {listen_ip}:{port}")
        
        while True:
            client_socket, addr = server.accept()
            print(f"Accepted connection from {addr[0]}:{addr[1]}")
            
            # Start a new thread to handle the connection
            client_handler = threading.Thread(target=handle_connection, args=(client_socket, addr))
            client_handler.start()

if __name__ == "__main__":
    main()
