'''
Main code for DontTouchMyOJ
'''

import time
import argparse
import picamera
import numpy as np
from imgurpython import ImgurClient
from twilio.rest import Client

from detectFace import sameFace
from pushButton import buttonListener
from dtmojFunctions import getAPIKeys, uploadFile, uploadAndSend, sendMessage

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

    vprint("Entered Main")

    ## Create twilio & imgur clients
    twilioSid, twilioToken = getAPIKeys("twilio_keys.txt")
    twilioClient = Client(twilioSid, twilioToken)
    imgurID, imgurKey = getAPIKeys("imgur_keys.txt")
    imgurClient = ImgurClient(imgurID, imgurKey)

    ## Createa a reference to the Pi Camera
    camera = picamera.PiCamera()

    ## Start the button listener
    bl = buttonListener()

    ## Initialize variables
    strangerPhoto = None
    previouslyPressed = True
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

        ## If the OJ has been taken - detected when
        ## the button has been released, but it was previously pressed
        if bl.buttonState and previouslyPressed and time.time() - pressedTime > 0.2:

            vprint("button pressed")
            previouslyPressed = False

            ## Runs face detection on each image
            for i in range(30):
                ret = sameFace(filePath=str(i)+".jpg")

                ## If the list is length 0, no faces were found
                if len(ret):
                    if any(ret):
                        vprint("Found nikhil at %s"%i)
                        vprint(ret)
                        foundNikhil = True
                        break
                    strangerPhoto = i

            ## If you didn't find Nikhil - send a text
            if not foundNikhil:

                ## If you found someone else, send their picture
                if strangerPhoto is not None:
                    uploadAndSend(imgurClient, twilioClient, str(strangerPhoto)+".jpg")
                    vprint("Someone else took your OJ check frame %s"%strangerPhoto)

                ## Otherwise just send a message
                else:
                    sendMessage(twilioClient)
                    vprint("No one found!")
            
            ## Once the OJ has been returned, and the button is pressed again
            ## update the previously pressed variable
            elif not(b1.buttonState):
                previouslyPressed = True

        ## Reset the variables at the end of the loop
        strangerPhoto = None
        if imageIndex == 30:
            imageIndex = 0
