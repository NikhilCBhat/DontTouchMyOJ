# DontTouchMyOJ

### About:
A fridge "security system" consisting of a Raspberry Pi with a Camera Module which will text the user when Orange Juice has been taken from the fridge by a roommate. This system can be used for any security purpose in any location - not necessarily OJ in the fridge :)

### Setup Guide: 
1. Install Raspian on a Raspberry Pi. Instructions for doing so can be found [here](https://www.raspberrypi.org/documentation/installation/installing-images/).
2. Install Python3, with the PiCamera, dlib and face_recognition modules. Instructions can be found [here](https://gist.github.com/ageitgey/1ac8dbe8572f3f533df6269dab35df65).
3. Connect the Raspberry Pi Camera Module to the Raspberry Pi using the CSI cable. See the image after step 5 for an example.
4. Run `sudo raspi-config` and enable the camera in the _Interfacing_ section.
5. Connect the push-button to the Raspberry Pi's GND and GPIO15 pins as shown in the image below:
![connectionGuide](https://raw.githubusercontent.com/NikhilCBhat/DontTouchMyOJ/master/connectionGuide.jpg)
6. Clone this Git repo.
7. Edit the Raspberry Pi crontab with the command `crontab -e`. Add the following line to the crontab: `@reboot python3 <path to the main.py file>`. For example, if you cloned the repo into the home directory, the path would be `/home/pi/DontTouchMyOJ/main.py`
8. Generate a Twilio API key from the [Twilio website](https://www.twilio.com). 
9. Create a file, `twilio_keys.txt` with the Twilio auth token on the first line and private key on the second.
10. Generate an Imgur API key from the [Imgur API website](https://api.imgur.com). 
11. Create a file, `imgur_keys.txt` with the Twilio auth token on the first line and private key on the second.
12. Connect the PI to the internet by modifying the `wpa_supplicant.conf` file located in the `/etc/`folder.
13. Replace the pictures of nikhil, with pictures of yourself in the `/encodings/` folder. The default is four images, but if you choose to use more/less, update the `numEncodings` value in the `detectFace.py` script. 
14. Run `python3 generateEncodings.py` to generate the face encodings.
15. Place the PI as necessary, so that the camera will have a good view of the person, and the object can rest on the button. 
16. Reboot the Pi and the program should automatically begin.

### Operating Procedure: 
1) The Raspberry Pi will always be locally saving the last 30 seconds of video data.
2) If the carton of orange juice is taken from the fridge, face detection will run on the saved video data.
3) If the detected face does not match the user's face, a text will be sent to the user, containing an image of the person who took the OJ.

### How it Works:

#### Texting Images
1) The image is uploaded to Imgur using the Imgur API.
2) Using the Twillo python library, this image is made into a media URL and then the MMS message is sent to the target phone number.

#### Detecting Taken OJ
1) A push-button is connected to the Raspberry Pi GPIO Pins. 
2) The output from the push button is read using the PI GPIO library
3) The button is placed under the OJ carton when the button is released the output is registered.

#### Face Recognition
1) The initial encodings script analysis the facial features present in the images and saves them to a CSV containing the necessary facial features.
2) For each of the 30 frames captured, the facial features are captured and compared against each of the face encodings. 
