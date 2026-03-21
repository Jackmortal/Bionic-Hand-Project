import busio # I2C.
import board # SCL, SDA (named pin control).
import time # sleep.
from adafruit_pca9685 import PCA9685 # Servo Driver Library.
from adafruit_motor import servo # Angle control.

MIN_PULSE = 500
MAX_PULSE = 2500

current_state = "open"

def setup():
    # Initialize I2C and PCA9685 driver.
    i2c = busio.I2C(board.SCL, board.SDA)
    driver = PCA9685(i2c)
    # Set servo driver frequency to 50Hz.
    driver.frequency = 50 

    servos = finger_channels(driver)

    return servos

def finger_channels(driver):
    fingers = {
        "pointer": servo.Servo(driver.channels[0], min_pulse = MIN_PULSE, max_pulse = MAX_PULSE),
        "middle": servo.Servo(driver.channels[1], min_pulse = MIN_PULSE,  max_pulse = MAX_PULSE),
        "ring": servo.Servo(driver.channels[4], min_pulse = MIN_PULSE, max_pulse = MAX_PULSE),
        "pinky": servo.Servo(driver.channels[3], min_pulse = MIN_PULSE, max_pulse = MAX_PULSE),
        "thumb": servo.Servo(driver.channels[2], min_pulse = MIN_PULSE, max_pulse = 2600)
    }
    return fingers

def close_hand(servos):
    global current_state

    if current_state == "peace":
        for x in range(162, -2, -2):
            servos["pointer"].angle = x
            servos["middle"].angle = x
            time.sleep(0.02)


    elif current_state != "closed":
        for x in range(0, 162, 2):
            servos["pointer"].angle = x
            servos["middle"].angle = x
            servos["ring"].angle = x
            servos["pinky"].angle = x
            servos["thumb"].angle = x
            time.sleep(0.02)

    current_state = "closed"

def open_hand(servos):
    global current_state

    if current_state == "peace":
        for x in range(162, -2, -2):
            servos["ring"].angle = x
            servos["pinky"].angle = x
            servos["thumb"].angle = x
            time.sleep(0.02)

    elif current_state != "open":
        for x in range(160, -2, -2):
            servos["pointer"].angle = x
            servos["middle"].angle = x
            servos["ring"].angle = x
            servos["pinky"].angle = x
            servos["thumb"].angle = x
            time.sleep(0.02)

    current_state = "open"

def peace_sign(servos):
    global current_state

    # Closes the ring, pinky, and thumb.
    if current_state == "open":
        for x in range(0, 162, 2):
            servos["ring"].angle = x
            servos["pinky"].angle = x
            servos["thumb"].angle = x
            time.sleep(0.02)
    
    # Opens the pointer and middle fingers.
    elif current_state == "closed":
        for x in range(162, -2, -2):
            servos["pointer"].angle = x
            servos["middle"].angle = x
            time.sleep(0.02)

    current_state = "peace"

#def thumbs_up(servos):

#def pointing(servos):

#def rock_on(servos):