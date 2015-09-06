
import numpy as np
import cv2
import sys
import time

im = cv2.imread(sys.argv[1])
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imshow('original image', imgray)

ret,thresh = cv2.threshold(imgray, 15, 255, 0)
contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(im, contours, -1, (0,255,0),2)
cv2.imshow('finding contours', im)

x, y, w, h = cv2.boundingRect(contours[0])
cv2.rectangle(im, (x,y), (x+w,y+h), (0,255,0),2)
roi = im[y:y+h, x:x+w]
cv2.imshow('finding rectangle', im)

sift = cv2.SIFT()
tStart = time.time()
kp = sift.detect(roi,None)
tEnd = time.time()
cost_time = (tEnd - tStart) *1000
print 'detecting sift cost time per roi image:' , cost_time , 'ms'
siftimg = cv2.drawKeypoints(roi, kp,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('roi sift', siftimg)
cv2.waitKey(0)
cv2.destroyWindow('')
