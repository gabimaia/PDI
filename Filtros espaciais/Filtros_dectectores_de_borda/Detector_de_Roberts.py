import sys
import numpy as np
from scipy import ndimage
from PIL import Image
from matplotlib import pyplot as plt

roberts_cross_v = np.array( [[ 0, 0, 0 ],
                             [ 0, 1, 0 ],
                             [ 0, 0,-1 ]] )

roberts_cross_h = np.array( [[ 0, 0, 0 ],
                             [ 0, 0, 1 ],
                             [ 0,-1, 0 ]] )

def load_image( infilename ) :
    img = Image.open(infilename)
    img.load()
    return np.asarray( img, dtype="uint32" )

def save_image( data, outfilename ) :
    img = Image.fromarray( np.asarray( np.clip(data,0,255), dtype="uint8"), "L" )
    img.save( outfilename )

def roberts_cross( infilename ) :
    image = load_image(infilename)

    vertical = ndimage.convolve( image, roberts_cross_v )
    horizontal = ndimage.convolve( image, roberts_cross_h )

    output_image = np.sqrt( np.square(horizontal) + np.square(vertical))

    plt.subplot(1,2,1),plt.imshow(image,cmap = 'gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(1,2,2),plt.imshow(output_image,cmap = 'gray')
    plt.title('Roberts'), plt.xticks([]), plt.yticks([])
    plt.show()

    #save_image(output_image, outfilename)
    #borda = np.vstack([np.hstack([image, output_image]) ])
    #cv2.imshow("Deteccao de borda de Roberts", borda)
    #cv2.waitKey(0)

infilename = input('digite o nome do arquivo de entrada: ')
#outfilename = input('digite o nome do arquivo de saida: ')
roberts_cross( infilename )