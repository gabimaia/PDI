import numpy as np
import cv2 as cv
#import matplotlib.pyplot as plt
from numpy import array, int32

def pgmread(nome_do_arquivo):
  """  essa funcao le um arquivo pgm e transforma em um array"""
  f = open(nome_do_arquivo,'r')
  count = 0
  while count < 3: # Le as informacoes do cabecalho
    line = f.readline()
    if line[0] == '#': # Ignora comentarios
      continue
    count = count + 1
    if count == 1: # informacao do numero magico do cabecalho
      magicNum = line.strip()
      if magicNum != 'P2' and magicNum != 'P5':
        f.close()
        print ('Not a valid PGM file')
        exit()
    elif count == 2: # pega numero de linhas e colunas da matriz 
      [width, height] = (line.strip()).split()
      width = int(width)
      height = int(height)
    elif count == 3: # nivel maximo de intensidade
      maxVal = int(line.strip())
  # Lendo as informacoes dos pixels
  img = []
  buf = f.read()
  elem = buf.split()
  if len(elem) != width*height:
    print ('erro no numero de pixels')
    exit()
  for i in range(height):
    tmpList = []
    for j in range(width):
      tmpList.append(elem[i*width+j])
    img.append(tmpList)
  return (array(img), width, height, maxVal)

def pgmwrite(img, file, maxVal=255, magicNum='P2'):
  """  Essa funcao transforma um array em um histograma com formato PGM """

  img = int32(img).tolist()
  f = open(file,'w')
  width = 0
  height = 0
  for row in img: #adiciona as informacoes do cabecalho pgm
    height = height + 1
    width = len(row)
  f.write(magicNum + '\n')
  f.write(str(width) + ' ' + str(height) + '\n')
  f.write(str(maxVal) + '\n')
  for i in range(height): #escreve o array de entrada em pixels
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

  
def PMF(hist, totpixel, max): #funcao massa de probabilidade
    for i in range (0,max+1):
      hist[i] = hist[i]/(totpixel)
    #return hist

def CDF(hist, max): #funcao de distribuicao acumulada
    for i in range (1,max+1):
        hist[i] += hist[i-1]
    #return hist

def normalize(hist, max): #normaliza os valores armazenados em hist[] entre 0 e max.
  for i in range(0,max+1):
    hist[i]=hist[i]*max


img_in = input('digite o nome do arquivo de entrada com extensao .pgm: ')
img_in = str(img_in)

imagem, col, row, max_value=pgmread(img_in) #le o arquivo de entrada pgm e armazena as variaveis correspondentes
img2 = np.asfarray(imagem,float) #transforma o array de string em array de floats.



#criando o histograma

hist=[] #inicializando

for i in range (max_value+1): #armazenando zeros no array do histograma
  hist.append(0)

for i in range (0,row): #armazenando as intensidades dos pixels da imagem de entrada na posicao correspondente do histograma em formato inteiro.
  for j in range (0,col):
    hist[int(img2[i][j])] += 1.0


#aplicando a transformacao no histograma de entrada

totpixel = col * row #calcula o total de pixel da imagem de entrada

PMF(hist, totpixel, max_value)  #aplica a PMF ao histograma
CDF(hist, max_value)            #aplica a CDF ao histograma
normalize(hist,max_value)       #aplica a normalizacao ao histograma

#criando uma nova matriz de saida a partir do histograma processado

for i in range (0,row):
  for j in range (0,col):
    img2[i][j] = hist[int(img2[i][j])] #armazena as intensidades nas suas posicoes correspondentes na matriz de saida

#criando o arquivo de saida a partir da matriz correspondente

img_out= input('digite o nome do arquivo de saida com extensao .pgm: ')
img_out=str(img_out)

pgmwrite(img2,img_out)

