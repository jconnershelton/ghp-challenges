import serial
import time

arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)

while True:
    num = input("Enter a height: ")
    write_read(num)
    num = input("Enter a turn: ")
    write_read(num)
    num = input("Type to FIRE: ")
    write_read(num)
    print('HEADSHOT')