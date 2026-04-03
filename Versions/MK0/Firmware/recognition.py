import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from camera import setup

# To pass filepath containing pretrained gesture models.
BaseOptions = mp.taks.BaseOptions

# Contains the detector and landscapes for recognition.
GestureRecognizer = mp.tasks.vision.GestureRecognizer

# Used to set the settings for GestureRecognizer.
GestureSettings = mp.tasks.vision.GestureRecognizerOptions

# Used to display gesture results (required for LIVE_STREAM).
GestureResults = mp.tasks.vision.GestureRecognizerRestult

# Used to set the mode (ex: Image, Video, Live Stream).
VisionMode = mp.tasks.vision.RunningMode

# Required listener function when using LIVE_STREAM mode, with type hints for 
# each parameter.
# Checks if a gesture was detected and prints detected hand.
# First index for num hands, second index for highest likelihood gesture.
def print_result(result: GestureResults, output_image: mp.Image, timestamp_ms: int):
    if result.gestures:
        print(result.gestures[0][0].category_name)

# Sets the settings for the recognizer.
# Such as, filepath to models, VisionMode, and print_result.
settings = GestureSettings(base_options = BaseOptions('gesture_recognizer.task'),
                           vision_mode = VisionMode.LIVE_STREAM,
                           listener_callback = print_result)

# Using with makes it so that I dont need to close the recognizer.
# Passes the settings into the GestureRecognizer and gives the 
# alias 'recognizer'
with GestureRecognizer.create_from_options(settings) as recognizer:
    frame = setup()
