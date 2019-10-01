import cv2
import numpy as np

img = cv2.imread('lena.pgm')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converte P&B

def adjust_gama(image, gama=1.0):
    invGama = 1.0/gama
    table = np.array([
        ((i / 255.0)** invGama) * 255 
        for i in np.arange(0,256)])
    return cv2.LUT(image.astype(np.uint8), table.astype(np.uint8))


for gama in [0.1, 0.5, 1.2, 2.2]:
#gama = 0.5
    adjusted = adjust_gama(img, gama=gama)
    cv2.imshow('gama_transformed'+str(gama)+'.jpg', adjusted)
    cv2.waitKey(0)
#cv2.waitKey(0)