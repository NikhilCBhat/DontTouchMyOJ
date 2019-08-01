from os import listdir
import face_recognition
import numpy as np

i = 0
for filePath in listdir("."):

    if any(filePath[-3:].lower() == extension for extension in ["png", "jpg"]):

        imageFile = face_recognition.load_image_file(filePath)
        try:
            encoding = face_recognition.face_encodings(imageFile)[0]
            np.savetxt("encoding"+str(i)+".csv", encoding, delimiter=",")
            i += 1
        except:
            pass
