from cvzone.HandTrackingModule import HandDetector
import cv2
from time import sleep
import serial

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
detector = HandDetector(detectionCon=0.5)
arduinoData = serial.Serial('COM7', 9600, timeout=1)  # Select the corresponding COM port
sleep(2)


# Function that translates pixel positions into degrees for servo control
def ajustar_angulo(position, startpoint, endpoint):
    if position < startpoint:
        position = startpoint
    if position > endpoint:
        position = endpoint
    size = endpoint - startpoint
    angle = ((position-startpoint)/size)*180
    return int(angle)


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img=img, draw=True)

    if hands:
        hand1 = hands[0]
        lmList1 = hand1['lmList']

        # calculates depth based on distance between index tip and wrist
        x1, y1 = lmList1[8][0], lmList1[8][1]
        zx, zy = lmList1[0][0], lmList1[0][1]
        z1 = ((zx - x1)**2 + (zy - y1)**2)**0.5

        anguloX = str(ajustar_angulo(x1, 200, 400))
        anguloY = str(ajustar_angulo(y1, 70, 180))
        anguloZ = str(ajustar_angulo(z1, 180, 300))

        # Transforms each axis angle into a 3 digits code. Put them all together to form a 9 digits code
        try:
            if int(anguloX) < 10:
                codigoX = "00" + anguloX
            elif 100 > int(anguloX) > 9:
                codigoX = "0" + anguloX
            elif 181 > int(anguloX) > 99:
                codigoX = anguloX
            if int(anguloY) < 10:
                codigoY = "00" + anguloY
            elif 100 > int(anguloY) > 9:
                codigoY = "0" + anguloY
            elif 181 > int(anguloY) > 99:
                codigoY = anguloY
            if int(anguloZ) < 9:
                codigoZ = "00" + str(anguloZ)
            elif 100 > int(anguloZ) > 9:
                codigoZ = "0" + str(anguloZ)
            else:
                codigoZ = str(anguloZ)
            codigoTotal = "$" + codigoX + codigoY + codigoZ + "\r"
            arduinoData.write(codigoTotal.encode())
            print(codigoTotal)
            sleep(0.01)

        except Exception as e:
            print("Ocorreu um erro:", e)

    cv2.imshow("Image", img)

    # Keep the window open and update it for each frame; wait for 1 millisecond between frames
    key = cv2.waitKey(1)
    if key == ord('q') or key == 27:  # Press "q" or "esc" to close the window
        break

cap.release()
arduinoData.close()
cv2.destroyAllWindows()
