import cv2
import numpy as np

image = input('digite o nome da imagem de entrada: ')
img = cv2.imread(image)
#img = img[::2,::2] # Diminui a imagem
suave = np.vstack([
np.hstack([img, cv2.blur(img, ( 3, 3))]) ])
cv2.imshow("Imagens suavisadas (Blur)", suave)
cv2.waitKey(0)