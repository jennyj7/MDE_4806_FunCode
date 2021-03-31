import serial
import RPi.GPIO as GPIO
import time

ser=serial.Serial("/dev/ttyACM0",9600, timeout=1) #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate = 9600

while(1):
    
    print("Reading")
    
    #check for recieved signal
    read_ser=ser.readline()
    
    print("Read:", read_ser)
    
    if(read_ser.decode() == 'Measure'):
        
        time.sleep(1)
        
        #make fake data
        x_val = 123
        y_val = 567

        ser.flush() # get rid of garbage data
            
        #     #wait for message from arduino
        #     read_ser=ser.readline()
        #     print(read_ser)
            
            #send stuff back to Arduino
        #     if(read_ser=="Hello From Arduino!"):
        #     pos_val_list = [str(x_val), str(y_val)]
        #     send_string = ','.join(pos_val_list)
        #print(str(ser.isOpen()))

        send_StringX = str(x_val)
        send_StringY = str(y_val)

        ser.write(send_StringX.encode())
        time.sleep(1)
        ser.write(send_StringY.encode())
    
    
    #send string and encode
#     ser.write(send_stringX.encode('utf-8')
#     #print("i sent x fam")
#     ser.write(send_stringY.encode('utf-8')
    #print("i send y fam")
              
              
              
#     # Receive data from the Arduino
#     receive_string = ser.readline().decode('utf-8', 'replace').rstrip()
#  
#     # Print the data received from Arduino to the terminal
#     print(receive_string)

