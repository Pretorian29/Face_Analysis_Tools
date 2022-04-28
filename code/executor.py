"""
Script 1 - Executor

1. Captures de choosen coordinates X,Y from an image.
2. Returns the corresponding landmark points for further use.

Paola Montoya 2022
"""
#------------------------------------------------------------------
import sys # to access the system
import cv2

#------------------------------------------------------------------
# Loading Image

file_path = './images/10405424_1.jpg'

img = cv2.imread(file_path, cv2.IMREAD_ANYCOLOR)
 
while True:
    cv2.imshow("Image in Process", img)
    cv2.waitKey(0)
    sys.exit() # to exit from all the processes
 
cv2.destroyAllWindows() # destroy all windows




#-----------------------------------------------------------------





#------------------------------------------------------------------
__author__ = 'Paola Montoya 2022'