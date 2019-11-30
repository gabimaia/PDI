import cv2
import numpy as np
from matplotlib import pyplot as plt 
import glob
from scipy.stats import mode , skew , kurtosis
from scipy.fftpack import fft

#projetando filtro mace a partir de um banco de dados
#projetando matrix X
#realizar a fft de cada imagem e arranjar nas colunas de uma matriz d x N
img = cv2.imread('A00.bmp')
print(img.shape)

#X = np.fft.fft2(img)                                                        #armazenando a fft da imagem
#X = np.fft.fftshift(X)
#print(X.shape[0])
def MACE_filter(img):

    X = np.fft.fft2(img)                                                        #armazenando a fft da imagem
    X = np.fft.fftshift(X)
    X = X.reshape(X.shape[0]*X.shape[1], 3)                                     #posiciona valores em um array 1D
    D = np.diag(X.flatten())                                                      #calcula valor de D
    D_inversa = np.linalg.inv(D)                                                         #inversa de D
    Xct = np.conj(np.transpose(X))                                                #conjulgado transposta de X
    
    H = np.matmul(D_inversa,np.matmul(X,np.matmul(np.matmul(Xct,D_inversa),X)))                 #calculando H
    
    return H.reshape((input.shape[0],input.shape[1]))

#path = glob.glob("/data/*.bmp")
MACE_filter(img)
