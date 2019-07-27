# DontTouchMyOJ

Currently a work in progress. 

About:
A fridge "security system" consisting of a Raspberry Pi with a Camera Module which will text the user when Orange Juice has been taken from the fridge by a roomate.

Operating Procedure: 
1) The Raspberry Pi will always be locally saving the last 30 seconds of video data.
2) If the carton of orange juice is taken from the fridge, face detection will run on the the saved video data.
3) If the detected face does not match the user's face, a text will be sent to the user, containing a image of the person who took the OJ.

How it Works:

Texting Images
1) The image is uploaded to this Git repository to the file image.jpg using GitPython.
2) Using the twillo python library, this image is made into a media url and then the mms message is sent to the target phone number.

Detecting Taken Food:
1) A push button is connected to the Raspberry Pi GPIO Pins. 
2) The output from the push button is read using the PI GPIO library
3) The button is placed under the OJ carton, when the button is released the output is registered. 
