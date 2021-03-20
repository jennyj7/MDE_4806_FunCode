import socket

#Set host and port
HOST = '10.0.0.231'
PORT = 10003

#Create Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(5)

#update command line to show it is waiting for a connection
print("Waiting for a connection")

#accept connection
connection, address = s.accept()

while True:
    
    #update commannd line
    print("Connection accepted")
    
    #recieve data from client
    data = connection.recv(1024).decode()
    
    #read data
    command = data.encode()
    
    print("Read data: ", command.decode())
    
    #check what the command is
    if command.decode() == "start":

        #Code from: https://stackoverflow.com/questions/29447333/python-taking-a-picture-with-raspberry-pi-camera
        #Tells camera to take picture and save it as a jpg

        #import libries
        import time
        import picamera

        #name jpg
        #readImage = 'blackDot.jpg'

        #tell pi to take a picture with the camera
        #cam = picamera.PiCamera()
        #cam.capture(readImage)

        #update command line that picture has been taken
        print('Picture Taken')

        #Code from: https://stackoverflow.com/questions/60486029/how-to-find-the-center-of-black-objects-in-an-image-with-python-opencv
        #Reads jpg and finds circles in the image

        #import the necessary packages
        import numpy as np
        import cv2

        #matplotlib shows the image
        from matplotlib import pyplot as plt

        #Add image
        image = cv2.imread(readImage)

        #Make a copy of the image
        original = image.copy()

        #Read in image in grey and blur the image
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (3,3), 0)

        #Set the threshold values to find black
        thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        #Find contours
        ROI_number = 0
        cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]

        for c in cnts:
            #Obtain bounding rectangle to get measurements
            x,y,w,h, = cv2.boundingRect(c)
            
            #Check for centroid
            M = cv2.moments(c)
            
            #counter for number of retakes
            retakeCount = 0
            
            #If circle is not found take a new picture
            while int(M["m00"]) == 0:
                
                #update command line
                print("Retake Number:", retakeCount)
                
                #increment counter
                retakeCount = retakeCount + 1
                
                #tell pi to take a picture with the camera
                cam.capture(readImage)
                
                #Add image
                image = cv2.imread(readImage)

                #Make a copy of the image
                original = image.copy()

                #Read in image in grey and blur the image
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                blur = cv2.GaussianBlur(gray, (3,3), 0)

                #Set the threshold values to find black
                thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

                #Find contours
                ROI_number = 0
                cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                cnts = cnts[0] if len(cnts) == 2 else cnts[1]
                
                #Obtain bounding rectangle to get measurements
                x,y,w,h, = cv2.boundingRect(c)
                
                #Check for centerioid
                M = cv2.moments(c)
                
                #Show the image in a new window
                plt.imshow(image, cmap = 'gray', interpolation = 'bicubic')
                plt.xticks([]), plt.yticks([])
                plt.show()
                
                
            #update command line
            print("Dot Found!")
            
            #Find centroid
            cX = int(M["m10"]/M["m00"])
            cY = int(M["m01"]/M["m00"])
            
            #Crop and save ROI
            ROI = original[y:y+h, x:x+w]
            cv2.imwrite('ROI_{}.png'.format(ROI_number),ROI)
            ROI_number += 1
            
            #Draw the contour and center of the shape on the image
            cv2.rectangle(image,(x,y),(x+w,y+h),(36,255,12),4)
            cv2.circle(image,(cX,cY),10,(320,159,22),-1)

            #Show the image in a new window
            plt.imshow(image, cmap = 'gray', interpolation = 'bicubic')
            plt.xticks([]), plt.yticks([])
            
            #Send data back to first raspberry pi
            contents = "LED On"
            connection.send(contents.encode())
            
            #update command line
            print("Sent Information Back to Client")
            print("Waiting for a new connection")
            
            
            


