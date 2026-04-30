# MK0 - Ada Hand ([Open Source](https://github.com/Open-Bionics/Ada_3D_model_files/tree/master/STLs/Right%20Hand), 5 DOF)

Brief description of what MK0 is and what was achieved including challenges faced.

## Bill of Materials
See BOM folder for full parts list and costs.

## Code
See Firmware folder. Built with Python, OpenCV, MediaPipe on Raspberry Pi 5.

## Images
See Images folder for wiring and build layout.

## Vidoes
See Videos folder for links to tests and demos.

## Demo
[Watch on YouTube](https://www.youtube.com/watch?v=RLUshVP_gwQ) - Keyboard input

## Challenges
Some challenges I came across was improper alignment with the servo horn and servo motor. 

## Lessons Learned
After completing MK0 I have learned that there are some limitations with my bionic hand. One of which includes the design of the hand itself.
The hand created by OpenBionics is meant to be printed in TPU allowing the fingers to bend naturally instead of needing joints. 
However, because there are no joints the movements of the fingers are more stiff and less dexterous than if there were joints.
Another notable lesson I learned is the importance of proper tendon routing. While the printed hand was made by OpenBionics, the rest of 
the bionic hand design was originally done by me. Because of this, the inside of the hand doesn't have a proper tendon routing system. While the 
PTFE tubing I used for the tendon system helped with the flawed design and reduced friction on the fishing line a better tendon workflow and servo
enclosure would allow better torque with the servos and movement of the fingers. Additionally, the servo enclosure lacked sufficient space to secure 
hex nuts to the screws, making it difficult to properly fasten the servo motors.

## What will change for MK1

