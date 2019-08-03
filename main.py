import picamera
import numpy as np
import time
from pushButton import buttonListener
from detectFace import sameFace
import png
from pictureFunctions import sendPicture, getAPIKeys, uploadFile

twilioSid, twilioToken = getAPIKeys("twillo_keys.txt")
twilioClient = Client(twilioSid, twilioToken)
imgurID, imgurKey = getAPIKeys("imgur_keys.txt")
imgurClient = ImgurClient(imgurID, imgurKey)

camera = picamera.PiCamera()
print(camera.resolution)
#camera.resolution = (320, 240)
someoneElse = None

if __name__ == "__main__":
    print("Entered main")

    i = 0
    bl = buttonListener()
    pressedTime = time.time()
    captureTime = time.time()

    while True:

        foundNikhil = False

        if time.time() - captureTime > 1:
            camera.capture(str(i)+".jpg")
            captureTime = time.time()
            i += 1

        if not(bl.buttonState) and time.time() - pressedTime > 0.2:

            print("button pressed")

            for j in range(30):
                ret = sameFace(filePath=str(j)+".jpg")
                if len(ret) > 1:
                    if any(ret):
                        print("Found nikhil at", j)
                        print(ret)
                        foundNikhil = True
                        break
                    someoneElse = j

            if not foundNikhil:
                if someoneElse is not None:
                     url = uploadFile(imgurClient, fName=str(someoneElse)+".jpg")
                     sendPicture(twilioClient, url)
                     print("Someone else took your OJ check frame",someoneElse)
                else:
                     print("No one found!")

        someoneElse = None
        if i == 30:
            i = 0
