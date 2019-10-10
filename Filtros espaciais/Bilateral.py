import cv2
import numpy as np

image = input('digite o nome da imagem de entrada: ')
img = cv2.imread(image)
#img = img[::2,::2] # Diminui a imagem
suave = np.vstack([
np.hstack([img, cv2.bilateralFilter(img, ( 3, 3), 0)]) ])
cv2.imshow("Imagens suavisadas pelo filtro Bilateral", suave)
cv2.waitKey(0)