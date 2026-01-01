import busio # Import CircuitPython library (I2C communication)
import board # Import board library for pins
import time # Import time library
from adafruit_pca9685 import PCA9685 # import servo driver library
from adafruit_motor import servo # Import servo library (Ex: .angle)

def main():
    # Sets up the I2C bus on the board and initializes the PCA9685 servo driver
    # with the I2C bus (communicaton).
    i2c = busio.I2C(board.SCL, board.SDA)
    pca = PCA9685(i2c)

    # Sets the frequency to 50Hz. Basically how often signals are passed from the 
    # servo driver to the servo motors.
    pca.frequency = 50

    move_pointer_finger(pca, 0, 180) # Move pointer finger down 180 degrees.

# Moves the pointer finger 180 degrees down, pauses for 2 seconds, then moves 
# back up 0 degrees.
def move_pointer_finger(pca, channel, angle):
    servo1 = servo.Servo(pca.channels[channel]) # Sets servo1 to channel 0 on servo driver.

    print("Moving 180 degrees down.")
    servo1.angle = angle
    
    print("Pausing for 2 seconds.")
    time.sleep(2)
    print("Moving back up to 0 degrees.")
    servo1.angle = 0 

if __name__ == "__main__":
    main()
