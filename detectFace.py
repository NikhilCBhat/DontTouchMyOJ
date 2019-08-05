import face_recognition
import numpy as np

numEncodings = 4
allEncodings = [np.loadtxt("encodings/encoding"+str(i)+".csv") for i in range(numEncodings)]

def sameFace(image=None, filePath=""):
	if image is None:
		image = face_recognition.load_image_file(filePath)
	print("Loaded Image")
	try:
		newEncoding = face_recognition.face_encodings(image)[0]
	except:
		return []
	print("Got new encoding")
	return face_recognition.compare_faces(allEncodings, newEncoding)



