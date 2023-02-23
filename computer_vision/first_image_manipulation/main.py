import cv2
import numpy as np

#loading and reading the image
img = cv2.imread("computer_vision\\first_image_manipulation\\image.jpg")
img = cv2.resize(img, (0,0), fx=0.25, fy=0.25)

#image based on edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray,5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

#cartoonization (blur + edges)
color = cv2.bilateralFilter(img, 8, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

cv2.imshow("Image",img) #window for original image
cv2.imshow("edges",edges) #window for image based on edges
cv2.imshow("Cartoon",cartoon) #window for cartoon image (not looking good yet)

cv2.waitKey(0)
cv2.destroyAllWindows()