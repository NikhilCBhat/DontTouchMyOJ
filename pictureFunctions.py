from git import Repo
from twilio.rest import Client
from picamera import PiCamera
from time import sleep

def takePicture(fPath="/home/pi/DontTouchMyOJ/image.jpg"):
	camera = PiCamera()
	sleep(1)
	camera.capture(fPath)

def sendPicture(client, url):
	message = client.messages.create(body="Here is your photo :)",from_='+18604304141',media_url=[url],to='+18602667815')

def uploadFile(fName='image.jpg'):
        repo = Repo('.')
        repo.index.add([fName])
        repo.index.commit('Auto image commit from python script')
        origin = repo.remote('origin')
        origin.push()

if __name__ == "__main__":
	account_sid = 'AC7bb5f799b071be682bdcce8bb4a7fa05'
	auth_token = '681f82064841725ff02a840d416928ef'
	client = Client(account_sid, auth_token)
	url = "https://raw.githubusercontent.com/NikhilCBhat/DontTouchMyOJ/master/image.jpg"

	takePicture()
	print("Took picture")
	uploadFile()
	print("Uploaded file")
	sendPicture(client, url)
	print("Sent text")
