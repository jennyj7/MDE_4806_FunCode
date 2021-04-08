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
command = 9997
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
        
        aurdinoSendData = ""
        
        x_val = recieved[0:recieved.find(' ')]
        y_val = recieved[recieved.find(' ') + 1:len(recieved)]
        
        x_val = int(x_val)
        y_val = int(y_val)
        
        stringX = str(x_val)
        stringY = str(y_val)
        
        #print("x_val:", x_val)
        #print("y_val:", y_val)
        
        #check if x is positive or negative
        if x_val > 0:
            aurdinoSendData = aurdinoSendData + "P"
        else:
            aurdinoSendData = aurdinoSendData + "N"
        
        #input x value into string
        if abs(x_val) > 999:
            aurdinoSendData = aurdinoSendData + "999"
        elif abs(x_val) < 100:
            if abs(x_val) > 10:
                aurdinoSendData = aurdinoSendData + "0"
                aurdinoSendData = aurdinoSendData + str(abs(x_val))
            else:
                aurdinoSendData = aurdinoSendData + "00"
                aurdinoSendData = aurdinoSendData + str(abs(x_val))
        else:
            aurdinoSendData = aurdinoSendData + str(abs(x_val))
            
        #check if y is positive or negative
        if y_val > 0:
            aurdinoSendData = aurdinoSendData + "P"
        else:
            aurdinoSendData = aurdinoSendData + "N"
        
        #input y value into string
        if abs(y_val) > 999:
            aurdinoSendData = aurdinoSendData + "999"
        elif abs(y_val) < 100:
            if abs(y_val) > 10:
                aurdinoSendData = aurdinoSendData + "0"
                aurdinoSendData = aurdinoSendData + str(abs(y_val))
            else:
                aurdinoSendData = aurdinoSendData + "00"
                aurdinoSendData = aurdinoSendData + str(abs(y_val))
        else:
            aurdinoSendData = aurdinoSendData + str(abs(y_val))
            
        print("Sent Data:", aurdinoSendData)
        
        #get rid of garbage data
        #ser.flush()
        
        #ser.write(send_StringX.encode())
        #time.sleep(1)
        #ser.write(send_StringY.encode())
        

#update command line
print("--------------------------------------------")
print("[Client 01] New Message from Audrino")
