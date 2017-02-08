import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('tissot-v8-quartz-chronograph-2009-watch.jpg',cv2.IMREAD_GRAYSCALE) #last argument is filter , if we dont specify it reads in color

#imread_color = 1
#imread_unchanged

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# plt.imshow(img,cmap='gray',interpolation='bicubic')
# plt.plot([50,100],[80,100],'c',linewidth=5)
# plt.show()


cv2.imwrite('imranfirst.png',img)