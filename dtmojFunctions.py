'''
Functions for DontTouchMyOJ
'''
from imgurpython import ImgurClient
from twilio.rest import Client

## Gets the API Keys from a file
def getAPIKeys(fName):
    with open(fName) as fp:
        ssid = fp.readline()
        token = fp.readline()
    return ssid[:-1], token[:-1]

## Uses Twilio to send a message to your phone number
def sendPicture(twilioClient, url=None, fromNumber='14132878699', toNumber='18608164865'):
	twilioClient.messages.create(body="This person took your OJ!",from_=fromNumber,media_url=[url],to=toNumber)

## Uploads a file to imgur
## Returns a link to the image
def uploadFile(imgurClient, fName):
	image = imgurClient.upload_from_path(fName, anon=False)
	return image['link']

## Convenient wrapper for the above two functions
def uploadAndSend(iClient, tClient, fName):
    url = uploadFile(iClient, fName)
    sendPicture(tClient, url)
