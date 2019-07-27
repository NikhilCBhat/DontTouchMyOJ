from git import Repo
from twilio.rest import Client
from picamera import PiCamera
from time import sleep

def getTwilloInfo(fPath):
	with open(fPath) as fp:
		ssid = fp.readline()
		token = fp.readline()
	return ssid[:-1], token[:-1]

def takePicture(fPath="/home/pi/Documents/DontTouchMyOJ/image.jpg"):
	camera = PiCamera()
	sleep(1)
	camera.capture(fPath)

def sendPicture(client, url, fromNumber='18604304141', toNumber='18602667815'):
	message = client.messages.create(body="Here is your photo :)",from_=fromNumber,media_url=[url],to=toNumber)

def uploadFile(fName='image.jpg'):
        repo = Repo('.')
        repo.index.add([fName])
        repo.index.commit('Auto image commit from python script')
        origin = repo.remote('origin')
        origin.push()

if __name__ == "__main__":

	account_sid, auth_token = getTwilloInfo("twillo_keys.txt")
	print(account_sid, auth_token)
	client = Client(account_sid, auth_token)
	url = "https://raw.githubusercontent.com/NikhilCBhat/DontTouchMyOJ/master/image.jpg"

	takePicture()
	print("Took picture")
	uploadFile()
	print("Uploaded file")
	sendPicture(client, url)
	print("Sent text")
