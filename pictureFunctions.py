#from git import Repo
from twilio.rest import Client
#from picamera import PiCamera
from time import sleep
from imgurpython import ImgurClient

def getAPIKeys(fPath):
	with open(fPath) as fp:
		ssid = fp.readline()
		token = fp.readline()
	return ssid[:-1], token[:-1]

def takePicture(cameraObject, fPath="/home/pi/Documents/DontTouchMyOJ/image.jpg"):
	cameraObject.capture(fPath)

def sendPicture(client, url, fromNumber='14132878699', toNumber='18608164865'):
	message = client.messages.create(body="Here is your photo :)",from_=fromNumber,media_url=[url],to=toNumber)

def uploadFile(client, fName='image.jpg'):
	image = client.upload_from_path(fName, anon=False)
	return image['link']

def snapAndSend(client, co):
        takePicture(co)
        print("Took picture")
        url = uploadFile()
        print("Uploaded file")
        sendPicture(client, url)
        print("Sent text message")

if __name__ == "__main__":

	twilioSid, twilioToken = getAPIKeys("twillo_keys.txt")
	twilioClient = Client(twilioSid, twilioToken)
	imgurID, imgurKey = getAPIKeys("imgur_keys.txt")
	imgurClient = ImgurClient(imgurID, imgurKey)

	url = uploadFile(imgurClient, fName="image.jpg")
	sendPicture(twilioClient, url)
