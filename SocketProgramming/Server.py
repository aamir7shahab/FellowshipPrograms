import socket

socketObject = socket.socket()
print(f"Socket is Created.")

host = ''
port = 9999

# binding ip with port number
socketObject.bind((host, port))

socketObject.listen(0)
print(f"Waiting for Connection")

while True:
    client, address = socketObject.accept()
    msg = client.recv(1024).decode()
    print(f"Connected with {address}, Message:{msg}")
    client.send(bytes("Welcome..", 'utf-8'))
    client.close()