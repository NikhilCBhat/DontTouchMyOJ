from pushButton import buttonListener
from picamera import PiCamera
import time
from pictureFunctions import takePicture
from detectFace import sameFace

print("Completed imports")

if __name__ == "__main__":
	camera = PiCamera()
	lastPressed = time.time()

	bl = buttonListener()
	while True:
		if not(bl.buttonState) and time.time()-lastPressed > 1:
			print("Button pressed")
			takePicture(camera)
			print("Took picture")
			result = sameFace()
			if any(result):
				print("Yeah, that's Nikhil!")
			else:
				print("Nope! Someone else took your OJ")
			lastPressed = time.time()
