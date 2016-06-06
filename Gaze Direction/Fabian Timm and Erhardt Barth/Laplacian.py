import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../Result_Images/eye1.jpg',0)

laplacian = cv2.Laplacian(img,cv2.CV_64F)

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.show()