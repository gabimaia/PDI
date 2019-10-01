import cv2 
import numpy as np
#import matplotlib.pyplot as plt
 
img = cv2.imread('einstein.jpg',0)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
c = 255 / (np.log(1 + np.max(img)))
img_log = c * np.log(1+ img)
#normalize_image = cv2.normalize(img0, None, 0, 255, cv2.NORM_MINMAX, dtype = cv2.CV_8U)
img_log = np.array(img_log, dtype = np.uint8)

#mg3 = cv2.threshold(normalize_image, 55, 255, cv2.THRESH_BINARY)
#cv2.imwrite('log_transformed', img_log)

cv2.imshow('log', img_log)

cv2.waitKey(0)
