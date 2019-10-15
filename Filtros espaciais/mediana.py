import cv2
import numpy as np

image = input('digite o nome da imagem de entrada: ')
img = cv2.imread(image)
suave = np.vstack([ np.hstack([img, cv2.medianBlur(img, ( 3, 3), 0)]) ])
cv2.imshow("Imagem original e suavisadas pelo filtro Gaussiano", suave)
cv2.waitKey(0)