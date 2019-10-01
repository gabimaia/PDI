import matplotlib.pyplot as plt
import cv2
import numpy as np 

img = cv2.imread('einstein.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hist_equalized = cv2.equalizeHist(img)

#hist_equalized=cv2.equalizeHist(img, 0)
plt.figure()
plt.title("Histograma Equalizado")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.hist(hist_equalized.ravel(), 256, [0,256])
plt.xlim([0, 256])
plt.show()

plt.figure()
plt.title("Histograma Original")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.hist(img.ravel(), 256, [0,256])
plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)