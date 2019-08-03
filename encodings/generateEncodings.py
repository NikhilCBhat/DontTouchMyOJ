from os import listdir
import face_recognition
import numpy as np

i = 0
for filePath in listdir("."):

    # Checks to see if the file is an image based on the extension
    if any(filePath[-3:].lower() == extension for extension in ["png", "jpg"]):

        # Load the file for use with the face recognition module
        imageFile = face_recognition.load_image_file(filePath)

        # Attempts to generate a CSV with the facial features.
        try:
            encoding = face_recognition.face_encodings(imageFile)[0]
            np.savetxt("encoding"+str(i)+".csv", encoding, delimiter=",")
            i += 1
        except:
            pass
