import cv2
import numpy as np
img = cv2.imread("crop5.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
contours, hier = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(img, contours, -1, (255,0,0), 3)
cv2.imwrite("contourbottle.png",img)

