import cv2
import numpy as np

def nothing(x):
    pass

def makeThresholdingWindow():
    cap = cv2.VideoCapture(0)
    # Create a black image, a window
    cv2.namedWindow('video')
    # create trackbars for color change
    cv2.createTrackbar('Value1','video',127,255,nothing)
    # create switch for ON/OFF functionality
    switch = '0 : OFF \n1 : ON'
    cv2.createTrackbar(switch, 'video',0,1,nothing)

    while(1):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # get current positions of four trackbars
        Value1 = cv2.getTrackbarPos('Value1','video')
        s = cv2.getTrackbarPos(switch,'video')

        if s == 0:
            v1 = 127
        else:
            v1 = Value1

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray,v1,255,cv2.THRESH_BINARY)
        # Display the resulting frame
        cv2.imshow('video',thresh)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('q'):
            break
        if k == ord('s'):
            cv2.imwrite('thresholdedimage.png',thresh)
            break

    cap.release()
    cv2.destroyAllWindows()