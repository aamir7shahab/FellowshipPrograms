import socket

client = socket.socket()

host = 'localhost'
port = 9999

client.connect((host, port))
msg = input('Enter your message:')
client.send(bytes(msg, 'utf-8'))
print(f"{client.recv(1024).decode()}")

