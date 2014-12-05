import serial
import cv2
import numpy as np
from math import *

def startComms(coord_list):

    PORT = '/dev/ttyACM0'
    SPEED = 9600
    def send_command(val):
        connection = serial.Serial( PORT, 
                                    SPEED,
                                    timeout=0,
                                    stopbits=serial.STOPBITS_TWO
                                    )
        connection.write(val)
        connection.close()
    def button(x):
        s = cv2.getTrackbarPos(switch,'video')
        if(s==0):
            send_command('2')
        if(s==1):
            send_command('1131111111111131111111111111113')


    cv2.namedWindow('video')
    #switch = '0 : OFF \n1 : ON'
    #cv2.createTrackbar(switch, 'video',0,1,button)
    img = cv2.imread('handimage.png')
    cv2.imshow('video',img)
    coord_list[0] = [(1,1)]
    while(True):
        # Capture frame-by-frame

        for i in range(1, len(coord_list)):
            for j in range(1, len(coord_list[i])):
                if len(coord_list[i][j]) > 1:
                    move_x = coord_list[i][j][0] - coord_list[i-1][j-1][0]
                    move_y = coord_list[i][j][1] - coord_list[i-1][j-1][1]
                    for u in range(1, math.abs(move_x)):
                        if move_x >= 0:
                            send_command('4')
                        if move_x < 0:
                            send_command('2')
                    for v in range(1, math.abs(move_y)):
                        if move_y >= 0:
                            send_command('1')
                        if move_y < 0:
                            send_command('3')
                if
        # Our operations on the frame come here
        # Display the resulting frame
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        k = cv2.waitKey(1) & 0xFF
        if k == ord('w'):
            send_command('1')
        elif k == ord('a'):
            send_command('2')
        elif k == ord('s'):
            send_command('3')
        elif k == ord('d'):
            send_command('4')
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()