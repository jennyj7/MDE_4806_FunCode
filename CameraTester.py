#Code from: https://stackoverflow.com/questions/60486029/how-to-find-the-center-of-black-objects-in-an-image-with-python-opencv

#import libries
import time
import picamera
import cv2 as cv2
import numpy as np

#initialize camera
cam = picamera.PiCamera()

#Reads jpg and finds circles in the image
check = False

while check == False:
    
    #name jpg
    readImage = 'black.jpg'

    #tell pi to take a picture with the camera
    #cam.capture(readImage)

    #update command line that picture has been taken
    print('[Server 04] Picture Taken')
    
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
    x,y,w,h, = cv2.boundingRect(cnts[0])

    #Check for centroid
    M = cv2.moments(cnts[0])

    #counter for number of retakes
    retakeCount = 0
    
    #update command line if no circle is found
    if(M["m00"]) == 0:
        print("[Server 00] Must Retake Picture")

    #If circle is not found take a new picture
    while int(M["m00"]) == 0:
        
        #update command line
        print("[Server 05] Retake Number:", retakeCount)
        
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
        x,y,w,h, = cv2.boundingRect(cnts[0])
        
        #Check for centerioid
        M = cv2.moments(cnts[0])

        #cv2.imshow('hello',image)
        #cv2.imwrite('thresh.png', thresh)
        #cv2.imshow('hello',thresh)

        #k = cv2.waitKey(0)
        #if k == ord('e'):
        #    cv2.destroyAllWindows()
            
    #update command line
    print("[Server 07] Dot Found!")

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

    imageTuple = image.shape
    centerX = int(imageTuple[1]/2)
    centerY = int(imageTuple[0]/2)

    cv2.circle(image,(centerX,centerY),10,(110,40,100),-1)

    #hypotenuse
    cv2.line(image, (cX,cY), (centerX,centerY), (57, 255, 20), 1)
    #x line
    cv2.line(image, (cX,cY), (centerX,cY), (57, 255, 20), 1)
    #y line
    cv2.line(image, (centerX,centerY), (centerX,cY), (57, 255, 20), 1)

    cv2.imwrite('image.png', image)
    cv2.imwrite('thresh.png', thresh)

    one = cv2.imread('image.png')
    two= cv2.imread('thresh')
    
    cv2.imshow('image',one)

    k = cv2.waitKey(0)
    print("Is this the correct dot? [y/n]")
    if k == ord('y'):
          
        xAlign = centerX - cX
        yAlign = cY - centerY
          
        cv2.destroyAllWindows()
          
        check = True
    
    elif k == ord('e'):
        cv2.destroyAllWindows()
        check = True
    else:
        cv2.destroyAllWindows()
          
       
    
