from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
from cv2 import cv2
plt.rcParams['figure.figsize'] = (10, 10)
plt.rcParams['image.cmap'] = 'gray'
#%matplotlib inline


cap = cv2.VideoCapture(0)
mask1 = np.zeros((400, 400))
mask2 = np.zeros((400, 400))


while True:
    _ ,frame = cap.read()
    crop = frame[0:400,0:400]
    cv2.rectangle(crop,(390,360),(370,380),(0,0,255),2)
    cv2.rectangle(crop,(390,10),(370,30),(255,0,0),2)
    cv2.imshow('frame', crop)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()