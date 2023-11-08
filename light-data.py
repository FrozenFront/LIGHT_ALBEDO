from time import sleep
from picamera import PiCamera

camera = PiCamera(resolution=(2480, 2480), framerate=30)
# Set ISO to the desired value
camera.iso = 100
# Wait for the automatic gain control to settle
camera.start_preview()
# Camera warm-up time
sleep(2)
camera.capture('yellow-tungsten.jpg')