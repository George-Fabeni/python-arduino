from cvzone.HandTrackingModule import HandDetector
import cv2
from time import sleep
import serial

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
detector = HandDetector(detectionCon=0.5)
arduinoData = serial.Serial('COM7', 9600)
sleep(2)
angulo = 0


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
        x1, y1 = lmList1[8][0], lmList1[8][1]
        anguloX = str(ajustar_angulo(x1, 100, 500))
        anguloY = str(ajustar_angulo(y1, 70, 200))
        print(anguloX, anguloY)
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
            codigoTotal = "$" + codigoX + codigoY + "\r"
            arduinoData.write(codigoTotal.encode())
            sleep(0.01)

        except Exception as e:
            print("Ocorreu um erro:", e)

    cv2.imshow("Image", img)

    # Keep the window open and update it for each frame; wait for 1 millisecond between frames
    key = cv2.waitKey(1)
    if key == ord('q') or key == 27:
        break

cap.release()
arduinoData.close()
cv2.destroyAllWindows()
