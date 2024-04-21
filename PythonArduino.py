import serial
from time import sleep

arduinoData = serial.Serial('COM5', 9600)
sleep(2)

try:
    while True:
        cmd = input("Digite o ângulo: ")
        if int(cmd) < 10:
            print(int(cmd))
            cmd = "$00" + cmd + "\r"
            print(cmd)
        elif 100 > int(cmd) > 9:
            cmd = "$0" + cmd + "\r"
        elif 181 > int(cmd) > 99:
            cmd = "$" + cmd + "\r"
        arduinoData.write(cmd.encode())
        sleep(0.01)

except Exception as e:
    print("Ocorreu um erro:", e)
finally:
    arduinoData.close()
