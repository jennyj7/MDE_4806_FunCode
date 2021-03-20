signal = True
picture = False
sendPic = False

#import libraries
import RPi.GPIO as GPIO
import time

#GPIO Basic initialization
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Use a variable for the Pin to use
#If you followed my pictures, it's port 7 => BCM 4
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.OUT)

#socket initialization
host = sys.argv[1]
command = sys.argv[2]
port = int(command)
socket_size = sys.argv[3]

# print("Output High")
# 
# GPIO.output(23, GPIO.HIGH)
# #Wait 5s
# time.sleep(5)
# GPIO.output(23,GPIO.LOW)

# print("Output Low")

GPIO.input(24)

boolCheck=True

while boolCheck:
    if GPIO.input(24) == 0:
        print("button pressed")
        
        contents = "start"
        print("started")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        print("connected")
        sock.send(contents.encode())
        boolCheck = False


import socket

#Set host and port
HOST = '10.0.0.231'
PORT = 10003

#Create Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(5)

print("Waiting for connection...")

#accept connection
connection, address = s.accept()

print("Connection accepted")

#recieve data from client
data = connection.recv(1024).decode()

#read data
command = data.encode()

print("Read data: ", command.decode())

#check what the command is
if command.decode() == "LED On":
    GPIO.output(25, True)
    time.sleep(10)
    GPIO.output(25, False)

