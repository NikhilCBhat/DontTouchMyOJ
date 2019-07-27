import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
buttonState = True
lastPressed = time.time()

class buttonListener(object):

	def __init__(self):
		thread = threading.Thread(target=self.run, args=())
		thread.daemon = True
		thread.start()

	def run(self):
		global buttonState
		while True:
			buttonState = GPIO.input(15)

if __name__ == "__main__":
	buttonListener()
	while True:
		if not(buttonState) and time.time()-lastPressed > 0.2:
			print("Button pressed")
			lastPressed = time.time()
