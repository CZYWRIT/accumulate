# coding: 'utf-8'
import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('F:/pycharm/1022/venv/box.jpg', 0)
img2 = cv2.imread('F:/pycharm/1022/venv/test.jpg', 0)

sift = cv2.SIFT()
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)
bf = cv.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)
good = []
for m, n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])
img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good[:10], flags)
plt.imshow(img3), plt.show()
# img = cv2.imread('F:/pycharm/1022/venv/test.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
#
# corners = np.int0(corners)

# sift = cv2.SIFT()
# kp = sift.detect(gray, None)
#
# img = cv2.drawKeypoints(gray, kp)
# cv2.imwrite('0.jpg', img)

# for i in corners:
#     x, y = i.ravel()
#     cv2.circle(img, (x, y), 3, 255, -1)
# plt.imshow(img), plt.show()
