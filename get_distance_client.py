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
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

#Use a variable for the Pin to use
#If you followed my pictures, it's port 7 => BCM 4
#GPIO.setup(24, GPIO.IN)#button
#GPIO.setup(23, GPIO.OUT)#LED

#socket initialization
host = '128.173.94.118'
command = 9990
port = int(command)
socket_size = 1024

#audrino initializatipn
ser=serial.Serial("/dev/ttyACM0",9600, timeout=1) #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate = 9600

#update command line
print("[Client 01] Waiting for Command from Audrino")

while True:
    
    #Wait read from audrino
    read_aurdino = ser.readline()
    
    #print("Aurdino Message:", read_aurdino.decode())
    
    #Look for "Mesure" command
    if read_aurdino.decode() == 'Measure' or read_aurdino.decode() == 'MeasureMeasure':
        #update the command line
        #print("[Client 02] Message from Audrino:", read_audrino.decode())
                  
        #connect to server
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        print("[Client 03] Connected to Server")
                
        #send start and name of jpg to the server
        contents = "start"
        contents = contents + "current.jpg"
        sock.send(contents.encode())
        print("[Client 04] Sending to Server:", contents[0:5])
        
        #recieve from the server
        recieved = sock.recv(1024)
        recieved = recieved.decode()
        print("[Client 05] Recieved from Server:", recieved)

        #close the connection
        sock.close()
        
        if recieved == "Realign":
            aurdinoSendData = "000P000P"
        
        #if arm is aligned, send 000P000P to the arm
        elif recieved == "Aligned":
            aurdinoSendData = "000P000P"
            
        elif recieved == "Exited":
            aurdinoSendData = "000P000P"
        
        else:
            
            aurdinoSendData = ""
            
            x_val = recieved[0:recieved.find(' ')]
            y_val = recieved[recieved.find(' ') + 1:len(recieved)]
            
            x_val = int(int(x_val)/10) - 10
            y_val = int(int(y_val)/10) - 50
            
#           #check if tolerance is good
            if abs(x_val) < 11:
                x_val = 0
            if abs(y_val) < 11:
                y_val = 0
            
            #input x value into string
            if abs(x_val) > 999:
                aurdinoSendData = aurdinoSendData + "999"
            elif abs(x_val) < 100:
                if abs(x_val) >= 10:
                    aurdinoSendData = aurdinoSendData + "0"
                    aurdinoSendData = aurdinoSendData + str(abs(x_val))
                else:
                    aurdinoSendData = aurdinoSendData + "00"
                    aurdinoSendData = aurdinoSendData + str(abs(x_val))
            else:
                aurdinoSendData = aurdinoSendData + str(abs(x_val))
                
            #check if x is positive or negative
            if x_val > 0:
                aurdinoSendData = aurdinoSendData + "P"
            else:
                aurdinoSendData = aurdinoSendData + "N"
                
            #input y value into string
            if abs(y_val) > 999:
                aurdinoSendData = aurdinoSendData + "999"
            elif abs(y_val) < 100:
                if abs(y_val) >= 10:
                    aurdinoSendData = aurdinoSendData + "0"
                    aurdinoSendData = aurdinoSendData + str(abs(y_val))
                else:
                    aurdinoSendData = aurdinoSendData + "00"
                    aurdinoSendData = aurdinoSendData + str(abs(y_val))
            else:
                aurdinoSendData = aurdinoSendData + str(abs(y_val))
                
            #check if y is positive or negative
            if y_val > 0:
                aurdinoSendData = aurdinoSendData + "P"
            else:
                aurdinoSendData = aurdinoSendData + "N"
        
        #aurdinoSendData = "999P999P"
        print("[Client 06] Sent Data to Aurdino:", aurdinoSendData)
            
        #get rid of garbage data
        ser.flush()
        
        #write to aurdino
        ser.write(aurdinoSendData.encode())            
       
        #update command line
        print("--------------------------------------------")
        print("[Client 01] Waiting for Command from Audrino")