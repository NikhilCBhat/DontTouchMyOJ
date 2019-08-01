from pushButton import buttonListener
from pictureFunctions import getAPIKeys, snapAndSend
from picamera import PiCamera
from twilio.rest import Client
import time
from imgurpython import ImgurClient


if __name__ == "__main__":

	twilioSid, twilioToken = getAPIKeys("twillo_keys.txt")
	twilioClient = Client(twilioSid, twilioToken)
	imgurID, imgurKey = getAPIKeys("imgur_keys.txt")
	imgurClient = ImgurClient(imgurID, imgurKey)
	camera = PiCamera()
	lastPressed = time.time()

	bl = buttonListener()
	while True:
		if not(bl.buttonState) and time.time()-lastPressed > 1:
			print("Button pressed")
			snapAndSend(twilioClient, imgurClient, camera)
			lastPressed = time.time()
