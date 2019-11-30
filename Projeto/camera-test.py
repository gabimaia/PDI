import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # captura dos frames
    ret, frame = cap.read()

    # trabalhando em cima dos frames
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # exibindo resultado
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()