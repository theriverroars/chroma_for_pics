import cv2
import numpy as np

img = cv2.imread('C:/Users/lenovo/Pictures/Business-woman.jpg')
img1 = cv2.imread('C:/Users/lenovo/Pictures/ocean.jpg')
cv2.imshow('original', img1)
cv2.imshow('original1', img)


lower_red = np.array([0, 70, 20])
lower_green = np.array([50, 150, 0])
upper_red = np.array([45, 45, 135])
upper_green = np.array([100, 200, 255])

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(img, lower_green, upper_green)
#cv2.imshow('mask', mask)

bg=cv2.bitwise_and(img1,img1,mask=mask)
#cv2.imshow('bg',bg)
mask_inv= cv2.bitwise_not(mask)
woman=cv2.bitwise_and(img,img,mask=mask_inv)
#cv2.imshow('woman',woman)

final=cv2.add(bg,woman)
cv2.imshow('final',final)

cv2.waitKey(0)
cv2.destroyAllWindows()