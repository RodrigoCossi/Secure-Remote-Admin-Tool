# Secure-Remote-Admin-Tool

✅ Security Features
Authentication – Only allow trusted clients.

Encryption (TLS) – Encrypt communication to avoid sniffing.

Command Validation – Avoid unrestricted shell execution.

Logging – Track access and commands for auditing.

Error handling & timeouts – For stability and abuse prevention.


 To Run This:
Generate SSL cert:
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes

Start the server:
python server.py

Start the client:
python client.py <server_ip>
