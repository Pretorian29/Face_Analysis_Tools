"""
Script 1 - Executor

1. Captures de choosen coordinates X,Y from an image.
2. Returns the corresponding landmark points for further use.

Paola Montoya 2022
"""
#------------------------------------------------------------------
#import sys # to access the system
import cv2

#------------------------------------------------------------------
# Loading Image

file_path = './images/10405424_1.jpg'

 
point_num = 0

# function to display the coordinates of
# of the points clicked on the image

def click_event(event, x, y, flags, params):
    global point_num
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        point_num = point_num + 1
        cv2.circle(img,(x,y),2,(255,0,0),-1) #Displaying Landmark point
        
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y, ' ', point_num)
         
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(point_num) +
                    str(''), (x,y), font,
                    0.5, (255, 0, 255), 2)
        cv2.imshow('image', img)
 
    # checking for right mouse clicks    
    if event==cv2.EVENT_RBUTTONDOWN:
        point_num = point_num + 1
        cv2.circle(img,(x,y),2,(255,0,255),-1) #Displaying Landmark point
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y,' ', point_num)
 
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv2.putText(img, str(point_num),
                    (x,y), font, 1,
                    (255, 0, 0), 2)
        cv2.imshow('image', img)
 
# driver function
if __name__=="__main__":
 
    # reading the image
    img = cv2.imread(file_path, 1)
 
    # displaying the image
    cv2.imshow('image', img)
 
    # setting mouse handler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event)
 
    # wait for a key to be pressed to exit
    cv2.waitKey(0)
 
    # close the window
    cv2.destroyAllWindows()



#-----------------------------------------------------------------





#------------------------------------------------------------------
__author__ = 'Paola Montoya 2022'