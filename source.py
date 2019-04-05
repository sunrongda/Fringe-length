#-*- coding:utf-8 -*-
import cv2
import numpy as np
from decimal import Decimal
def single_np(arr, target):
    arr = np.array(arr)
    mask = (arr == target)
    arr_new = arr[mask]
    return arr_new.size
# 黑色
lower_black = np.array([0, 0, 0])
upper_black = np.array([180, 255, 46])

img = cv2.imread('/Users/sunrongda/Downloads/face_photo/778_0.jpg')
cropImg = img[0:19,24:104]
# get a frame and show


frame = cropImg

cv2.imshow('Capture', frame)

# change to hsv model
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# get mask
mask = cv2.inRange(hsv, lower_black, upper_black)
cv2.imshow('Mask', mask)
size = mask.shape
print size
print Decimal(single_np(mask,255))/Decimal(1500)
if Decimal(single_np(mask,255))/Decimal(1500)>Decimal('0.3'):
    print "长刘海"
else :
    print "短刘海"
cv2.waitKey(0)
cv2.destroyAllWindows()

