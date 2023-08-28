# service_2.py
def emulate_http(client_socket):
    response = b"HTTP server emulated. Enter a URL:"
    client_socket.send(response)
    url = client_socket.recv(1024).decode('utf-8').strip()

    if "malicious" in url:
        payload = b"HTTP/1.1 200 OK\nContent-Type: text/html\n\n"
        payload += b"<html><body><h1>Malicious Content Detected!</h1></body></html>"
        client_socket.send(payload)
    else:
        response = b"HTTP/1.1 200 OK\nContent-Type: text/html\n\n"
        response += f"<html><body><h1>Welcome to {url}</h1></body></html>".encode('utf-8')
        client_socket.send(response)

    client_socket.close()
