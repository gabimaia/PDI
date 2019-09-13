import numpy as np
#import cv2 as cv
import matplotlib.pyplot as plt
from numpy import array, int32

def pgmread(filename):
  """  essa função lê um arquivo PGM e retorna um array"""
  
  f = open(filename,'r')
  # Read header information
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
        print ('Not a valid PGM file')
        exit()
    elif count == 2: # Width and Height
      [width, height] = (line.strip()).split()
      width = int(width)
      height = int(height)
    elif count == 3: # Max gray level
      maxVal = int(line.strip())
  # Read pixels information
  img = []
  buf = f.read()
  elem = buf.split()
  if len(elem) != width*height:
    print ('Error in number of pixels')
    exit()
  for i in range(height):
    tmpList = []
    for j in range(width):
      tmpList.append(elem[i*width+j])
    img.append(tmpList)
  return (array(img), width, height, maxVal)

def pgmwrite(img, filename, maxVal=208, magicNum='P2'):
  """  This function writes a numpy array to a Portable GrayMap (PGM) 
  image file. By default, header number P2 and max gray level 255 are 
  written. Width and height are same as the size of the given list."""

  img = int32(img).tolist()
  f = open(filename,'w')
  width = 0
  height = 0
  for row in img:
    height = height + 1
    width = len(row)
  f.write(magicNum + '\n')
  f.write(str(width) + ' ' + str(height) + '\n')
  f.write(str(maxVal) + '\n')
  for i in range(height):
    count = 1
    for j in range(width):
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

imagem, col, row, max_value=pgmread('balloons.ascii.pgm')
img2=np.asfarray(imagem,float)
print (row, col)
print(type(imagem))
print(type(max_value))
hist=[]

#criando meu histograma

for i in range (max_value+1):
  hist.append(0)
print(hist)

for i in range (0,row):
  for j in range (0,col):
    hist[int(img2[i][j])] += 1.0

totpixel = col * row 

PMF(hist, totpixel, max_value)
CDF(hist, max_value)
normalize(hist,max_value)

for i in range (0,row):
  for j in range (0,col):
    img2[i][j] = hist[int(img2[i][j])]

pgmwrite(img2,'teste5.pgm')

