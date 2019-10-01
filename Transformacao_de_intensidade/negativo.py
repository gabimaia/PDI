#from PIL import image
import cv2 
import numpy
import matplotlib.pyplot as plt
 
img = cv2.imread('einstein.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_inverte = cv2.bitwise_not(img)
cv2.imshow('imagem', img_inverte)
cv2.waitKey(0)