signal = True
picture = False
sendPic = False

#import libraries
import RPi.GPIO as GPIO
import time
import socket
import sys
#GPIO Basic initialization
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Use a variable for the Pin to use
#If you followed my pictures, it's port 7 => BCM 4
GPIO.setup(24, GPIO.IN)#button
GPIO.setup(23, GPIO.OUT)#LED

#socket initialization
host = '127.0.0.1'
command = 9997
port = int(command)
socket_size = 1024

#update command line
print("[Client 01] Waiting for Button to be Pressed")

while True:

        #wait for button press
        while GPIO.input(24) == 1:
                time.sleep(0.7)

        #update the command line
        print("[Client 02] Button Pressed")
                  
        #connect to server
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        print("[Client 03] Connected to Server")
                
        #send start packet
        contents = "start"
        sock.send(contents.encode())
        print("[Client 04] Sending to Server:", contents)

        #recieve from the server
        recieved = sock.recv(1024)
        recieved = recieved.decode()
        print("[Client 05] Recieved from Server:", recieved)

        #close the connection
        sock.close()
                
        #check what the command is
        if recieved == "LED On":
                print("[Client 06] Turn On LED")
                GPIO.output(23, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(23, GPIO.LOW)
                
        #update command line
        print("--------------------------------------------")
        print("[Client 01] Waiting for Button to be Pressed")
