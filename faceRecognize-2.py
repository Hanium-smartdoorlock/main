import face_recognition
import cv2
#print(cv2.__version__)
donFace=face_recognition.load_image_file('/home/usr/faceRecognition/demoImages/known/Donald Trump.jpg')
donEncode=face_recognition.face_encodings(donFace)[0]

nanFace=face_recognition.load_image_file('/home/usr/faceRecognition/demoImages/known/Nancy Pelosi.jpg')
nanEncode=face_recognition.face_encodings(nanFace)[0]

Encodings=[donEncode,nanEncode]
Names=['Donald','Nancy']

font=cv2.FONT_HERSHEY_SIMPLEX
testImage=face_recognition.load_image_file('/home/usr/faceRecognition/demoImages/unknown/u3.jpg')
facePositions=face_recognition.face_locations(testImage)
allEncodings=face_recognition.face_encodings(testImage,facePositions)

testImage=cv2.cvtColor(testImage,cv2.COLOR_RGB2BGR)

for (top,right,bottom,left), face_encoding in zip(facePositions,allEncodings):
	name='UnKnown'
	matches=face_recognition.compare_faces(Encodings,face_encoding)
	if True in matches:
		first_match_index=matches.index(True)
		name=Names[first_match_index]

	cv2.rectangle(testImage,(left,top),(right,bottom),(0,0,255),2)
	cv2.putText(testImage,name,(left,top-6),font,.75,(255,0,255),1)
cv2.imshow('myWindow',testImage)
cv2.moveWindow('myWindow',0,0)
if cv2.waitKey(0)==ord('q'):
	cv2.destoryAllWindows()

