import cv2
import imutils
import csv
import numpy as np

img = cv2.imread('1.bmp')



rects = []
nums = []

# conver yolo to cv rect
with open ('1.txt', 'r') as f:
    for row in csv.reader(f,delimiter=' '):
        nums.append(row[0])
        rects.append(((float(row[1])*img.shape[1], float(row[2])*img.shape[0]),(float(row[3])*img.shape[1],float(row[4])*img.shape[0]), 0))


i = 0
j = 0
for rect in rects:
    if (i != 0):
        if (nums[i-1][0] != nums[i][0]):
            j = 0
    nums[i] = nums[i]+"_"+str(j)
    box = cv2.cv.BoxPoints(rect) if imutils.is_cv2() else cv2.boxPoints(rect)    
    box = np.int0(box)
    img_crop = img[box[1][1]:box[0][1], box[1][0]:box[2][0]]
    #cv2.drawContours(img, [box], -1, (0, 255, 0), 1)

    cv2.imshow('img', img_crop)
    cv2.waitKey(0)
    print(nums[i])
    j+=1
    i+=1
    

cv2.imwrite('img.bmp', img)
cv2.waitKey(0)