import busio # I2C.
import board # SCL, SDA (named pin control).
import time # sleep.
from adafruit_pca9685 import PCA9685 # Servo Driver Library.
from adafruit_motor import servo # Angle control.

MIN_PULSE = 500
MAX_PULSE = 2500

def main():
    # Initialize I2C and PCA9685 driver.
    i2c = busio.I2C(board.SCL, board.SDA)
    driver = PCA9685(i2c)
    # Set servo driver frequency to 50Hz.
    driver.frequency = 50 

    servos = finger_channels(driver)

    close_hand(servos)
    open_hand(servos)

def finger_channels(driver):
    fingers = {
        "pointer": servo.Servo(driver.channels[0], min_pulse = MIN_PULSE, max_pulse = MAX_PULSE),
        "middle": servo.Servo(driver.channels[1], min_pulse = MIN_PULSE,  max_pulse = MAX_PULSE),
        "ring": servo.Servo(driver.channels[4], min_pulse = MIN_PULSE, max_pulse = MAX_PULSE),
        "pinky": servo.Servo(driver.channels[3], min_pulse = MIN_PULSE, max_pulse = MAX_PULSE),
        "thumb": servo.Servo(driver.channels[2], min_pulse = MIN_PULSE, max_pulse = MAX_PULSE)
    }
    return fingers

def close_hand(servos):
    for x in range(20, 180, 20):
        servos["pointer"].angle = x
        servos["middle"].angle = x
        servos["ring"].angle = x
        servos["pinky"].angle = x
        servos["thumb"].angle = x
        time.sleep(0.5)

def open_hand(servos):
    for x in range(180, 0, 20):
        servos["pointer"].angle = x
        servos["middle"].angle = x
        servos["ring"].angle = x
        servos["pinky"].angle = x
        servos["thumb"].angle = x
        time.sleep(0.5)

if __name__ == "__main__": 
    main()