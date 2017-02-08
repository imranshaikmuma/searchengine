import numpy as np
import cv2

img = cv2.imread('tissot-v8-quartz-chronograph-2009-watch.jpg',cv2.IMREAD_COLOR)


img[55,55] = [255,255,255]

px = img[55,55]

print(px)


img[100:150,100:150] = [255,255,255]

watch_face = img[30:400,200:399]

img[0:330,0:199] = watch_face


cv2.imshow('image',img)
cv2.waitKey(0)

cv2.destroyAllWindows()





