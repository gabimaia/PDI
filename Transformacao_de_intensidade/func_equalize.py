import numpy as np
#import cv2 as cv
import matplotlib.pyplot as plt
from numpy import array, int32

def pgmread(filename):

  """  This function write a portable gray map (PGM) to a numpy array"""
  
  f = open(filename,'r')
  # lendo informacoes do cabecalho
  count = 0
  while count < 3:
    line = f.readline()
    if line[0] == '#': # Ignore comments
      continue
    count = count + 1
    if count == 1: # Magic num info
      magicNum = line.strip()
      if magicNum != 'P2' and magicNum != 'P5':
        f.close()
        print ('arquivo pgm invalido')
        exit()
    elif count == 2: # numero de linhas e colunas da matriz
      [colunas, linhas] = (line.strip()).split()
      colunas = int(colunas)
      linhas = int(linhas)
    elif count == 3: # Max gray level
      maxVal = int(line.strip())
  # Read pixels information
  img = []
  buf = f.read()
  elem = buf.split()
  if len(elem) != colunas*linhas:
    print ('Error in number of pixels')
    exit()
  for i in range(linhas):
    tmpList = []
    for j in range(colunas):
      tmpList.append(elem[i*colunas+j])
    img.append(tmpList)
  return (array(img), colunas, linhas, maxVal)

def pgmwrite(img, filename, maxVal=255, magicNum='P2'):

  """  This function writes a numpy array to a Portable GrayMap (PGM) image file """
  
  img = int32(img).tolist()
  f = open(filename,'w')
  colunas = 0
  linhas = 0
  for row in img:
    linhas = linhas + 1
    colunas = len(row)
  f.write(magicNum + '\n')
  f.write(str(colunas) + ' ' + str(linhas) + '\n')
  f.write(str(maxVal) + '\n')
  for i in range(linhas):
    count = 1
    for j in range(colunas):
      f.write(str(img[i][j]) + ' ')
      if count >= 17:
        # No line should contain gt 70 chars (17*4=68)
        # Max three chars for pixel plus one space
        count = 1
        f.write('\n')
      else:
        count = count + 1
    f.write('\n')
  f.close()
 
def PMF(hist, totpixel, max):
    for i in range (0,max+1):
      hist[i] = hist[i]/(totpixel)
    #return hist

def CDF(hist, max):
    for i in range (1,max+1):
        hist[i] += hist[i-1]
    #return hist

def normalize(hist, max):
  for i in range(0,max+1):
    hist[i]=hist[i]*max
  return hist

img_in = input('digite o nome do arquivo de entrada .pgm: ')
img_in = str(img_in)

#lendo o arquivo de entrada e separando as informacoes principais do arquivo

imagem, col, row, max_value = pgmread(img_in)

img2=np.asfarray(imagem,float) #transforma o array de entrada do tipo string em float

#criando meu histograma

hist=[]
for i in range (max_value+1):
  hist.append(0)

for i in range (0,row):
  for j in range (0,col):
    hist[int(img2[i][j])] += 1.0

#plotando o histograma da imagem de entrada

plt.plot(hist)
plt.show()

#processando meu histograma de entrada

totpixel = col * row 

PMF(hist, totpixel, max_value)
CDF(hist, max_value)
normalize(hist,max_value)

# plotando o hisograma da imagem de saida

#transformando meu histograma processado em um array de saida

for i in range (0,row):
  for j in range (0,col):
    img2[i][j] = hist[int(img2[i][j])]

hist2=[]
for i in range (max_value+1):
  hist2.append(0)

for i in range (0,row):
  for j in range (0,col):
    hist2[int(img2[i][j])] += 1.0

#transformando o meu array de saida em um arquivo .pgm

plt.plot(hist2)
plt.show()

img3 = input('digite o nome do arquivo de saida .pgm: ')
img3 = str(img3)


pgmwrite(img2,img3)