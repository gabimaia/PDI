import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from PIL import Image

def plot(data, title):
    plot.i += 1
    plt.subplot(2,2,plot.i)
    plt.imshow(data)
    plt.gray()
    plt.title(title)
plot.i = 0

# Carregando a imagem de entrada...
im = Image.open('einstein.jpg')
data = np.array(im, dtype=float)
plot(data, 'Original')


kernel = np.array([[-1, -1, -1],
                   [-1,  8, -1],
                   [-1, -1, -1]])

highpass_3x3 = ndimage.convolve(data, kernel)

#plot(highpass_3x3, 'Simple 3x3 Highpass')


kernel = np.array([[-1, -1, -1, -1, -1],
                   [-1,  1,  2,  1, -1],
                   [-1,  2,  4,  2, -1],
                   [-1,  1,  2,  1, -1],
                   [-1, -1, -1, -1, -1]])
highpass_5x5 = ndimage.convolve(data, kernel)

#plot(highpass_5x5, '5x5 passa-alta')

# fazer um passa alta subtraindo um passa baixa

lowpass = ndimage.gaussian_filter(data,3)
lowpass1 = ndimage.median_filter(data, 3)
lowpass2 = ndimage.minimum_filter(data,3)
lowpass3 = ndimage.maximum_filter(data,3)

#gauss_highpass = data - lowpass

plot(lowpass2, r'minimo')
plot(lowpass3, r'maximo')
plt.show()