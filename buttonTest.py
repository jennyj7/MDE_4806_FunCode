import RPi.GPIO as GPIO
import time


#GPIO Basic initialization
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Use a variable for the Pin to use
#If you followed my pictures, it's port 7 => BCM 4
GPIO.setup(23, GPIO.OUT)#led
GPIO.setup(24, GPIO.IN)#button
GPIO.setup(25, GPIO.OUT)

# print("OFF")
# GPIO.output(25, False)
# time.sleep(5)
# print("ON")
# GPIO.output(25, True)
# time.sleep(5)
# print("OFF")
# GPIO.output(25, False)

# 
# if GPIO.input(24) == 0:
#     print("pressed")
#     print("ON")
#     GPIO.output(25, True)
#     time.sleep(5)
#     GPIO.output(25, False)
GPIO.output(25, False)
time.sleep(2)    
   

while True:
    
    print("LED off")
    GPIO.output(23,GPIO.LOW)
    
    #wait for button press
    while GPIO.input(24)==1:
        time.sleep(0.2)
        
    #LED ON
    print("LED ON")
    GPIO.output(23,GPIO.HIGH)
    
    #wait for button release
    while GPIO.input(24) ==0:
        time.sleep(0.2)

    # if GPIO.input(24) == 0:
        # print("press")
        # GPIO.output(25, True)
        # time.sleep(1)
        # GPIO.output(25, False)
    # else:
        # GPIO.output(25, False)
    
    # GPIO.output(25, False)
    # time.sleep(2)  
