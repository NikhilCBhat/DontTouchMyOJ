import picamera
import numpy as np
import time
from pushButton import buttonListener
from detectFace import sameFace
import png

camera = picamera.PiCamera()
camera.resolution = (320, 240)
frames = [np.empty((240, 320, 3), dtype=np.uint8) for _ in range(30)]
someoneElse = None

if __name__ == "__main__":
    print("Entered main")

    i = 0
    bl = buttonListener()
    pressedTime = time.time()
    captureTime = time.time()

    while True:

        foundNikhil = False

        if time.time() - captureTime > 1:
            camera.capture(frames[i], format="rgb")
            captureTime = time.time()

        if not(bl.buttonState) and time.time() - pressedTime > 0.2:

            print("button pressed")

            for frame in frames:
                ret = sameFace(image=frame)
                if len(ret) > 1:
                    if any(ret):
                        print("It's nikhil so nbd")
                        png.from_array(frame, 'L').save("nikhilsface.png")
                        foundNikhil = True
                        break
                    someoneElse = frame

            if not foundNikhil:
                if someoneElse is not None:
                     png.from_array(someoneElse, 'L').save("other.png")
                     print("Someone else took your OJ")
                else:
                     print("No one found!")
        i += 1
        someoneElse = None
        if i == 30:
            i = 0
