import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('einstein.jpg', 0)
height, width = img.shape

plt.figure("Input")
plt.subplot(221),plt.imshow(img, cmap = 'gray')
plt.title('Image'), plt.xticks([]), plt.yticks([])

fft = np.log(np.abs(np.fft.fftshift(np.fft.fft2(img))))
plt.subplot(222),plt.imshow(fft, cmap = 'gray')
plt.title('Fourier Transform'), plt.xticks([]), plt.yticks([])

r = 20
h_Filter_Low_Pass = np.zeros(img.size, img.dtype).reshape(img.shape)
for icounter in range(1, height):
    for jcounter in range(1, width):
        if ((icounter - height/2)**2 + (jcounter - width/2)**2) < r**2:
            h_Filter_Low_Pass[icounter, jcounter] = 1
plt.subplot(223),plt.imshow(h_Filter_Low_Pass, cmap = 'gray')
plt.title('Filter'), plt.xticks([]), plt.yticks([])

h_fft = np.log(np.abs(np.fft.fftshift(np.fft.fft2(h_Filter_Low_Pass))))
plt.subplot(224),plt.imshow(h_fft, cmap = 'gray')
plt.title('Fourier Transform (Filter)'), plt.xticks([]), plt.yticks([])


plt.figure("Output")
g = fft * h_fft
g_ifft = np.abs(np.fft.ifftshift(np.fft.ifft2(g)).real)
plt.subplot(),plt.imshow(g_ifft, cmap = 'gray')
plt.title(''), plt.xticks([]), plt.yticks([])
plt.show()