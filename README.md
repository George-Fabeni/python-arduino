# python-arduino
Communication between Python and Arduino for a gesture controlled robot arm. Arduino is responsible for controlling the servos and depth data (ultrassonic sensor), and python identifies hand positions and send them to arduino (mediapipe, opencv).

Coding is still in progress. I intend to use, in the future, an xbox 360 kinect (1414) for capturing image and depth, but I couldn't manage to gather data from kinect so far (can't use pykinect, libfreenect, etc).

So far, you can use the input in Python to control the angle of the servo (considering 180° range of motion). Servos's control is connected to pin 9. You have to install the cvzone package in arduino. Got it from this site: https://www.computervision.zone/courses/computer-vision-arduino-chapter-1/
