#teste do projeto para a terceira unidade de PDI
#objetivo de inservir gadgets especificos nos pontos fiduciais detectados na face
#processamento digital de imagens

import numpy as np
import cv2
import PIL
import matplotlib as plt
#import pandas

from utils import CFEVideoConf, image_resize

cap = cv2.VideoCapture(0)

save_path           = 'images/teste.mp4'
frames_per_seconds  = 24
config              = CFEVideoConf(cap, filepath=save_path, res='720p')
out                 = cv2.VideoWriter(save_path, config.video_type, frames_per_seconds, config.dims)
face_cascade        = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')
olhos_cascade       = cv2.CascadeClassifier('cascades/third-party/frontalEyes35x16.xml')
nariz_cascade       = cv2.CascadeClassifier('cascades/third-party/Nose18x15.xml')
boca_cascade        = cv2.CascadeClassifier('cascades/data/mouth.xml')
lingua              = cv2.imread('images/fun/doggy_tongue.png', -1)
oculos              = cv2.imread("images/fun/glasses.png", -1)
mustache            = cv2.imread('images/fun/mustache.png',-1)
nariz               = cv2.imread('images/fun/doggy_noise.png',-1)


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

    for (x, y, w, h) in faces:
        ri_gray    = gray[y:y+h, x:x+h] # rec
        ri_color   = frame[y:y+h, x:x+w]
        #cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 3)

        '''olhos = olhos_cascade.detectMultiScale(ri_gray, scaleFactor=1.5, minNeighbors=5)
        for (ox, oy, ow, oh) in olhos:
            #cv2.rectangle(roi_color, (ox, oy), (ox + ow, oy + oh), (0, 255, 0), 3)
            ri_olhos = ri_gray[oy: oy + oh, ox: ox + ow]
            oculos2 = image_resize(oculos.copy(), width=ow)

            gw, gh, gc = oculos2.shape
            for i in range(0, gw):
                for j in range(0, gh):
                    #print(oculos[i, j]) #RGBA
                    if oculos2[i, j][3] != 0: # alpha 0
                        ri_color[oy + i, ox + j] = oculos2[i, j]'''


        nose = nariz_cascade.detectMultiScale(ri_gray, scaleFactor=1.5, minNeighbors=5)
        for (nx, ny, nw, nh) in nose:
            #cv2.rectangle(roi_color, (nx, ny), (nx + nw, ny + nh), (255, 0, 0), 3)
            ri_nose = ri_gray[ny: ny + nh, nx: nx + nw]
            mustache2 = image_resize(mustache.copy(), width=nw)

            mw, mh, mc = mustache2.shape
            for i in range(0, mw):
                for j in range(0, mh):
                    #print(glasses[i, j]) #RGBA
                    if mustache2[i, j][3] != 0: # alpha 0
                        ri_color[ny + int(nh/2.0) + i, nx + j] = mustache2[i, j]

        '''mouth = boca_cascade.detectMultiScale(ri_gray, scaleFactor=1.5, minNeighbors=5)
        for (tx, ty, tw, th) in mouth:
            ri_mouth = ri_gray[ty: ty + th, tx: tx + tw]
            tongue2 = image_resize(tongue.copy(), wisth=tw)

            thw, thh, thc = tongue2.shape
            for i in range(0, thw):
                for j in range(0, thh):
                    #print(glasses[i, j]) #RGBA
                    if tongue2[i, j][3] != 0: # alpha 0
                        ri_color[ty + i, tx + j] = tongue2[i, j]'''

    # show frame
    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
    out.write(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# finalizando
cap.release()
out.release()
cv2.destroyAllWindows()