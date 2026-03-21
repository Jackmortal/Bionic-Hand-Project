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

    move_pointer_finger(pca, 0, 90) # Move pointer finger down 180 degrees.
    move_middle_finger(pca, 1, 180)
    move_ring_finger(pca, 3, 101)
    move_pinky_finger(pca, 4, 0)
    move_thumb_finger(pca, 2, 90)

# Moves the pointer finger 180 degrees down, pauses for 2 seconds, then moves 
# back up 0 degrees.
def move_pointer_finger(pca, channel, angle):
    # Sets servo1 to channel 0 on servo driver and defines min and max pulse width paramenters.
    servo1 = servo.Servo(pca.channels[channel], min_pulse=650, max_pulse=2650)

    print("Set pointer finger to vertical position")
    servo1.angle = angle   
    
    print("move pointer finger 180 degrees down and pause for 2 seconds.")
    servo1.angle = 180
    time.sleep(2)
    
    print("Moving pointer finger back up to 0 degrees.")
    servo1.angle = angle  

def move_middle_finger(pca, channel, angle):
    servo2 = servo.Servo(pca.channels[channel], min_pulse=650, max_pulse=2400)

    print("Move middle finger 180 degrees down and pause for 2 seconds.")
    servo2.angle = angle
    time.sleep(2)

    print("Move middle finger back up to vertical position 0 degrees.")
    servo2.angle = 0

def move_ring_finger(pca, channel, angle):
    servo3 = servo.Servo(pca.channels[channel], min_pulse=400, max_pulse=2850)

    print("Move ring finger to vertical position")
    servo3.angle = angle

    print("Move ring finger 180 degrees down and pause for 2 seconds.")
    servo3.angle = 180
    time.sleep(2)

    print("Move ring finger back up vertical position.")
    servo3.angle = angle

def move_pinky_finger(pca, channel, angle):
    servo4 = servo.Servo(pca.channels[channel], min_pulse=400, max_pulse=2500)

    print("Move pinky finger to vertical position")
    servo4.angle = 90

    print("Move pinky finger 180 degrees down and pause for 2 seconds.")
    servo4.angle = angle
    time.sleep(2)

    print("Move pinky finger back up to vertical position.")
    servo4.angle = 90

def move_thumb_finger(pca, channel, angle):
    servo5 = servo.Servo(pca.channels[channel], min_pulse=750, max_pulse=2650)

    print("Move thumb to vertical position")
    servo5.angle = angle

    print("Move thumb down 180 degrees and pause for 2 seconds.")
    servo5.angle = 180
    time.sleep(2)

    print("Move thumb back up to vertical angle.")
    servo5.angle = angle
if __name__ == "__main__":
    main()
