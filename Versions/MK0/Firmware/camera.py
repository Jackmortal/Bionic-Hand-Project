import cv2 as cv
from picamera2 import Picamera2
from libcamera import Transform

# Initializes the camera object, sets the camera configurations, passes the
# configurations into the camera object, and starts the camera.
def setup():
   picam = Picamera2()
   config = picam.create_preview_configuration({'size': (640,480), 'format': 'RGB888'}, transform=Transform(hflip=1))
   picam.configure(config)
   picam.start()
   run_camera(picam)

# Runs infinitely capturing one frame at a time with said frame being passed
# into 'imshow' which displays the frames in a window called 'Live Feed'.
def frame_stream(picam):
   while True:
      frame = picam.capture_array()

      cv.imshow('Live Feed', frame)
      yield frame

      # Shows the next frame after 20ms and closes the 'Live Feed' if the
      # keybind 'd' is pressed.
      if cv.waitKey(20) & 0xFF==ord('d'):
         break
