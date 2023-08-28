# service_1.py
def emulate_ssh(client_socket):
    response = b"SSH server emulated. Please log in.\nUsername:"
    client_socket.send(response)
    username = client_socket.recv(1024).decode('utf-8').strip()
    
    response = b"Password:"
    client_socket.send(response)
    password = client_socket.recv(1024).decode('utf-8').strip()

    # Simulate authentication (for demonstration purposes)
    if username == "admin" and password == "password":
        success_msg = b"Login successful!\n"
        client_socket.send(success_msg)
    else:
        failure_msg = b"Login failed. Please try again.\n"
        client_socket.send(failure_msg)

    client_socket.close()
