import busio #Imports the CircuitPython library for I2C communication.
import board #Imports library for microcontroller GPIO control.
import time #Imports time library for pauses.
from adafruit_pca9685 import PCA9685 #Imports servo driver library.
from adafruit_motor import servo #Imports servo library for controlling angles.

i2c = busio.I2C(board.SCL, board.SDA) #Sets up I2C on the board.
pca = PCA9685(i2c) #Initiates I2C control with the servo driver.

pca.frequency = 50 #Sets the frequency for servo control to 50Hz. (How often signals are sent to the servos for communication).

pointer = servo.Servo(pca.channels[0], min_pulse=500, max_pulse=2500)
middle = servo.Servo(pca.channels[1], min_pulse=500, max_pulse=2500)
ring = servo.Servo(pca.channels[2], min_pulse=500, max_pulse=2500)
pinky = servo.Servo(pca.channels[3], min_pulse=500, max_pulse=2500)
thumb = servo.Servo(pca.channels[4], min_pulse=500, max_pulse=2500)

servos = [pointer, middle, ring, pinky, thumb] #Instead do a while loop with three arrays that siginify the finger, the desired angle, and the starting angle for each finger.
for s in servos:
    s.angle = 0
    time.sleep(0.5)
    s.angle = 90
    time.sleep(0.5)
    s.angle = 0

time.sleep(2)