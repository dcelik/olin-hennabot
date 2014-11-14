import os
import sys
import serial
import time
import signal

PORT = '/dev/ttyACM0'
SPEED = 9600

cv2.namedWindow('video')
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'video',1,1,nothing)

def on_button_toggled(self, button):
    if button.get_active():
        state = ['1', 'on']
        button.set_label(state[1].upper())
        self.send_command(state[0])
    else:
        state = ['0', 'off']
        button.set_label(state[1].upper())
        self.send_command(state[0])

def send_command(self, val):
    connection = serial.Serial( PORT, 
                                SPEED,
                                timeout=0,
                                stopbits=serial.STOPBITS_TWO
                                )
    connection.write(val)
    connection.close()