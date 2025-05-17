import ssl
import socket

HOST = '0.0.0.0'
PORT = 8000
PASSWORD = "secret123"

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen(5)
    print(f"Server listening on port {PORT}")

    with context.wrap_socket(sock, server_side=True) as ssock:
        conn, addr = ssock.accept()
        with conn:
            print(f"Connection from {addr}")
            auth = conn.recv(1024).decode()
            if auth != PASSWORD:
                conn.send(b"FAIL")
                conn.close()
            else:
                conn.send(b"OK")

                while True:
                    cmd = input("Enter command to run (or 'exit'): ")
                    conn.send(cmd.encode())
                    if cmd == "exit":
                        break
                    result = conn.recv(4064).decode()
                    print(result)
