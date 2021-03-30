import socket
import sys


#pull host, port, and socket information from command prompt
host = '127.0.0.1'
port = 9990
socket_size = 1024


contents = "start"
print("started")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
print("connected")
sock.send(contents.encode())

recieved = sock.recv(1024)
print(recieved.decode)
sock.close()

print(recieved)
