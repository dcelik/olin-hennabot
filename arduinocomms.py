import serial
import cv2
import numpy as np

PORT = '/dev/ttyACM1'
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
        send_command('0')
    if(s==1):
        send_command('1')


cv2.namedWindow('video')
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'video',0,1,button)
cap = cv2.VideoCapture(0);

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    th2 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                cv2.THRESH_BINARY,11,2)
    # Display the resulting frame
    cv2.imshow('video',th2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()