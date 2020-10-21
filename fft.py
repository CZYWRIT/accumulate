import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imrad('xxx.jpg', 0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

magitude = 20*np.log(np.abs(fshift))


plt.subplot(121),plt.imshow(img, cmap=''gray')
plt.title('Input Image'),plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, xmap= 'gray')
plt.title('Magnitude Spectrum'), plt.xtricks([]), plt.ytricks([])
plt.show()
