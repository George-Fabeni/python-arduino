# Project goals

Communication between Python and Arduino for a **gesture controlled robot arm!** Arduino is responsible for controlling the servos and depth data (ultrassonic sensor), and python identifies hand positions and send them to arduino (mediapipe, opencv).


# Current Status

So far, you can use the input in Python to control the angle of 2 servos (considering 180° range of motion). One corresponds to  *'x'* axis and the other to *'y'* axis position of the tip of your index finger in your hand. Servos's controls are connected to pin 9 and pin 10.

Coding is still in progress. I intend to use, in the future, an xbox 360 kinect (1414) for capturing image and depth, but I couldn't manage to gather data from kinect so far (can't use pykinect, libfreenect, etc).



## How to use it
### Arduino

In Arduino IDE, just upload the code from the .ino file. It defines the servo's pins and commands, based on Serial communication. 
- You need to install the cvzone library. Download it and install using "Sketch" > "Include Library" > "Add .ZIP Library..."

The library was created by Murtaza Hassan. It's a mix of opencv and mediapipe, and he also has a complete library for python with the same name, which I used a lot in the Python code.
His GitHub: [murtazahassan (Murtaza Hassan) (github.com)](https://github.com/murtazahassan)
His YouTube channel: https://www.youtube.com/@murtazasworkshop

### Python

Install mediapipe, opencv-python and pyserial libraries. Python version 3.10.0 worked well for me, but newer versions have many incompabilities with mediapipe.

First of all, you have to check the COM port in python code, as well as the baud rate. Both should match Arduino's values. By default, the baud rate is 9600 in Python and Arduino.
> arduinoData = serial.Serial('COM7', 9600)

 Inside the code, you can change the "anguloX, anguloY" values based on your camera resolution. The funcion "ajustar_angulo" defines the value of minimum and maximum positions where you can control the servos. For example, I'm using a resolution of 640x480, so I'm starting the hand-control of the servo at the value of 100 and ending it at 500 for the *'x'* axis. If I wanted a smaller range, I could change these values.

> anguloX = str(ajustar_angulo(x1, 100, 500))

The camera shoud be set in
> cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

Your default camera should be 0. If you have more than one camera, try 1 or 2. The "cv2.CAP_DSHOW" displays the camera faster, but I'm not sure how it works, and I think it's only for Windows users. If it is not working, consider removing it, or search for the documentation of cv2.

If your servo's range of motion is different than 180º, it's very simple to change it inside the code. Search for 180 or 181 and change it as you wish.

### Boards and electronics

![2 servos tinkercad](https://github.com/George-Fabeni/python-arduino/assets/162236620/1c79de54-2ba0-4d74-8315-7f4d52bd2c24)
