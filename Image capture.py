import cv2
import matplotlib.pyplot as plt

#Getting Image
webcam = cv2.VideoCapture(0)                   #Opening the camera
#cap=int(input("Enter '1' to capture: "))
if(True):
    check, image = webcam.read()               #Capturing the Image
    #cv2.imshow('Test image',image)             #Displaying the Image
    cv2.imwrite('capture.jpg',image)             #Saving_Image
    cv2.waitKey(1)
webcam.release()                               #Closing _webcam
cv2.destroyAllWindows()                        #Closing the window

#Reading Image
Img=cv2.imread("capture.jpg")

#Filtering the Image
bilateral = cv2.Laplacian(Img,cv2.CV_64F)      #Filtering Using laplacian filter
bilateral = cv2.GaussianBlur(bilateral,(3,3),0)#Blurring Using GaussianBlur
bilateral = bilateral * 15                     #Increasing the Brightness 

Img_resize=cv2.resize(bilateral,(640,480))     #Resizing the image with a resolution of (640*480)

cv2.imwrite('first.jpg',Img_resize)            #saving the Filtered Image



Img1=cv2.imread("first.jpg")
#plt.imshow(Img1)
