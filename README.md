# DontTouchMyOJ

Currently a work in progress. 

The goal of the project is to have a fridge "security system" consisting of a Raspberry Pi with a Camera Module which will text the user when food has been taken from the fridge by a roomate.

Operating Procedure: 

1) The Raspberry Pi will always be locally saving the last 30 seconds of video data.
2) If a food item is taken face detection will run on the the saved video data.
3) If the detected face does not match the user's face, a text will be sent to the user, with a image of the person who took the food.

How it Works:

Texting Images
The image is uploaded to this Git repository to the file image.jpg using GitPython.
Using the twillo python library, this image is made into a media url and then the mms message is sent to the target phone number.

