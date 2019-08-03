import picamera
import numpy as np
import time
from pushButton import buttonListener
from detectFace import sameFace
from pictureFunctions import sendPicture, getAPIKeys, uploadFile
import argparse
from imgurpython import ImgurClient
from twilio.rest import Client

## Add verbose argument
parser = argparse.ArgumentParser(description='Use --verbose <True> to print debugging output')
parser.add_argument('--verbose')
args = parser.parse_args()

# Prints if in verbose mode
# vprint for verbose printing
def vprint(a):
    if args.verbose is not None:
        print(a)

## -- Main -- ##
if __name__ == "__main__":

    ## Create twilio & imgur clients
    twilioSid, twilioToken = getAPIKeys("twillo_keys.txt")
    twilioClient = Client(twilioSid, twilioToken)
    imgurID, imgurKey = getAPIKeys("imgur_keys.txt")
    imgurClient = ImgurClient(imgurID, imgurKey)

    ## Createa a reference to the Pi Camera
    camera = picamera.PiCamera()
    someoneElse = None

    ## Start the button listener
    bl = buttonListener()

    ## Initialize the time & image variables
    imageIndex = 0
    pressedTime = time.time()
    captureTime = time.time()

    ## Main loop
    vprint("Starting the loop")
    while True:

        foundNikhil = False

        ## Take a picture every second
        if time.time() - captureTime > 1:
            camera.capture(str(imageIndex)+".jpg")
            captureTime = time.time()
            imageIndex += 1

        ## If the button has been pressed
        if not(bl.buttonState) and time.time() - pressedTime > 0.2:

            vprint("button pressed")


            ## Runs face detection on each image
            for i in range(30):
                ret = sameFace(filePath=str(i)+".jpg")

                ## If the list is length 1 or 0, no faces were found
                if len(ret) > 1:
                    if any(ret):
                        vprint("Found nikhil at %s"%i)
                        vprint(ret)
                        foundNikhil = True
                        break
                    someoneElse = i

            ## If you didn't find Nikhil - send a text
            if not foundNikhil:

                ## If you found someone else, send their picture
                if someoneElse is not None:
                    url = uploadFile(imgurClient, fName=str(someoneElse)+".jpg")
                    sendPicture(twilioClient, url)
                    vprint("Someone else took your OJ check frame %s"%someoneElse)
                
                ## Otherwise just send a message
                else:
                    vprint("No one found!")

        someoneElse = None
        if imageIndex == 30:
            imageIndex = 0
