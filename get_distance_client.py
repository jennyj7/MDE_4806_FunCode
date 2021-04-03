signal = True
picture = False
sendPic = False

#import libraries
import RPi.GPIO as GPIO
import time
import socket
import sys
import serial

#GPIO Basic initialization
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Use a variable for the Pin to use
#If you followed my pictures, it's port 7 => BCM 4
GPIO.setup(24, GPIO.IN)#button
GPIO.setup(23, GPIO.OUT)#LED

#socket initialization
host = '127.0.0.1'
command = 9998
port = int(command)
socket_size = 1024

#audrino initializatipn
#ser=serial.Serial("/dev/ttyACM0",9600, timeout=1) #change ACM number as found from ls /dev/tty/ACM*
#ser.baudrate = 9600

#update command line
print("[Client 01] Waiting for Command from Audrino")

#while True:
        
#Wait read from audrino
#read_audrino = ser.readline()

#Look for "Mesure" command
if True: #read_aurduino.decode() == 'Measure':

    #update the command line
    #print("[Client 02] Message from Audrino:", read_audrino.decode())
              
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
    
    if recieved == "Realign":
        #####
        #####
        print(recieved)
    
    elif recieved == "Aligned":
        #####
        #####
        print(recieved)
    
    else:
        x_val = recieved[0:recieved.find(' ')]
        y_val = recieved[recieved.find(' ') + 1:len(recieved)]
        
        print("x_val:", x_val)
        print("y_val:", y_val)
        
        send_StringX = str(x_val)
        send_StringY = str(y_val)

#update command line
print("--------------------------------------------")
print("[Client 01] New Message from Audrino")
