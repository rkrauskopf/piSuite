import serial

ser = serial.Serial('/dev/tty.usbmodem1411', 9600)

while 1:
    x = ser.readline()
    print(str(x))
