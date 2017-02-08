import cv2
import numpy as np


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade= cv2.CascadeClassifier('haarcascade_eye.xml')

watch_cascade = cv2.CascadeClassifier('cascade.xml')

cap = cv2.VideoCapture(0)
 
# while True:
	# ret,frame = cap.read()
	# cv2.imshow('frame',frame)
	# if cv2.waitKey(1) & 0xff == ord('q'):
		# break
# cap.release()
# cv2.destroyAllWindows()


while True:
	ret,img=cap.read()
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray,1.3,5)
	
	watches = watch_cascade.detectMultiScale(gray,50,50)
	
	for(x,y,w,h) in watches:
		cv2.rectangle(img,(x,y),(x+w,y+h), (255,255,0),2)
	
	for(x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h), (255,0,0),2)
		roi_gray=gray[y:y+h, x:x+w]
		roi_color=img[y:y+h, x:x+w]
		
		eyes=eye_cascade.detectMultiScale(roi_gray)
		
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh), (0,255,255),2)
			
	cv2.imshow('img',img)
	
	k=cv2.waitKey(30)&0xff
	
	if k==27:
		break
		
cap.release()
cv2.destroyAllWindows()


		