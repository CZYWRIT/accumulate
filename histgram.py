import cv2
import numpy as np
from matplotlib import pyplot as plt
# 画直方图
img = cv2.imread('home.jpg', 0)
plt.hist(img.ravel(),256,[0,256])
plt.show()


#  改善对比度
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 =clahe.apply(img)
cv2.imwrite('clahe_2.jpg',cl1)
