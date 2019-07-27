import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)

class buttonListener(object):

	def __init__(self):
		thread = threading.Thread(target=self.run, args=())
		thread.daemon = True
		thread.start()
		self.buttonState = True

	def run(self):
		while True:
			self.buttonState = GPIO.input(15)


if __name__ == "__main__":

	bl = buttonListener()
	while True:
		if not(bl.buttonState):
			print("Button pressed")
