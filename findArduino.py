__author__ = 'randall'

import platform
import subprocess
import serial
# detect os type, the usb connection is stored differently on various platforms

# currently the code only expects to run on a Raspberry Pi
if platform.system() == 'Darwin':
    # do OSX things
    proc = subprocess.Popen('ls /dev/tty.*', stdout=subprocess.PIPE, shell=True)
    output = proc.stdout.read()
    usbList = output.decode('utf-8').rsplit()
    print('Looking for connected arduinos on usb coneections...')
    for usb in usbList:
        print('Testing connection at: ' + usb)
        try:
            ser = serial.Serial(usb, 9600, timeout=3)

            # flush any partial transmission from the buffer by reading once and then
            # attempt to detect an actual transmission

            handshakeText = 'hello';
            ser.write(handshakeText.encode('utf-8'))

            reading = ser.readline().decode('utf-8').rstrip()
            if reading == 'Found you!':
                print('Found a valid connection at: ' + usb)
                break
            else:
                print(usb + ' not a valid arduino connection')

        except serial.SerialException:
            print("unable to connect with current usb")
            continue