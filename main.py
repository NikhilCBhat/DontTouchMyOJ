import picamera
import numpy as np
import time
from pushButton import buttonListener
from detectFace import sameFace()

camera = picamera.PiCamera()
camera.resolution = (320, 240)
frames = [np.empty((240, 320, 3), dtype=np.uint8) for _ in range(30)]
someoneElse = None

if __name__ == "__main__":
    i = 0
    bl = buttonListener()
    while True:
        camera.capture(output[i], format="rgb")
        if not(bl.buttonState) and time.time() - pressedTime > 0.2:
            result = []
            for frame in frames:
                ret = sameFace(image=frame)
                if len(ret) == 1:
                    pass
                else:
                    if any(ret):
                        print("It's nikhil so nbd")
                        break
                    someoneElse = frame
         if someoneElse is not None:
             print("Someone else")
         i += 1
         someoneElse = NOne
