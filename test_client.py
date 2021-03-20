import socket
import sys


#pull host, port, and socket information from command prompt
host = sys.argv[1]
command = sys.argv[2]
port = int(command)
socket_size = sys.argv[3]


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