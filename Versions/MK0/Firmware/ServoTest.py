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

    move_pointer_finger(pca, 0, 101) # Move pointer finger down 180 degrees.
    move_middle_finger(pca, 1, 180)

# Moves the pointer finger 180 degrees down, pauses for 2 seconds, then moves 
# back up 0 degrees.
def move_pointer_finger(pca, channel, angle):
    # Sets servo1 to channel 0 on servo driver and defines min and max pulse width paramenters.
    servo1 = servo.Servo(pca.channels[channel], min_pulse=650, max_pulse=2650)

    print("Set to vertical position")
    servo1.angle = angle   
    
    print("move 180 degrees down and pause for 2 seconds.")
    servo1.angle = 180
    time.sleep(2)
    
    print("Moving back up to 0 degrees.")
    servo1.angle = angle  

def move_middle_finger(pca, channel, angle):
    servo2 = servo.Servo(pca.channels[channel], min_pulse=650, max_pulse=2400)

    print("Move middle finger 180 degrees down and pause for 2 seconds.")
    servo2.angle = angle
    time.sleep(2)

    print("Move back up to vertical position 0 degrees.")
    servo2.angle = 0

if __name__ == "__main__":
    main()
