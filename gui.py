import cv2
import numpy as np

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
# Create a black image, a window
cv2.namedWindow('image')
# create trackbars for color change
cv2.createTrackbar('Value1','image',255,255,nothing)
cv2.createTrackbar('Value2','image',0,255,nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing) 
cv2.setMouseCallback('image',draw_circle)

while(1):

    # Capture frame-by-frame
    ret, image = cap.read()

    # get current positions of four trackbars
    Value1 = cv2.getTrackbarPos('Value1','image')
    Value2 = cv2.getTrackbarPos('Value2','image')
    s = cv2.getTrackbarPos(switch,'image')

    if s == 0:
        v1 = 127
        v2 = 255
    else:
        v1 = Value1
        v2 = Value2

    # Our operations on the frame come here
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray,v1,v2,cv2.THRESH_BINARY)
    th2 = cv2.adaptiveThreshold(thresh,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                cv2.THRESH_BINARY,11,2)
    # Display the resulting frame
    cv2.imshow('image',thresh)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
