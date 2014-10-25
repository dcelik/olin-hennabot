import cv2
import numpy as np

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)

def nothing(x):
    pass

cap = cv2.VideoCapture(1)
# Create a black image, a window
cv2.namedWindow('image')
# create trackbars for color change
cv2.createTrackbar('Value1','image',11,11,nothing)
cv2.createTrackbar('Value2','image',2,2,nothing)
cv2.createTrackbar('Value3','image',255,255,nothing)
cv2.createTrackbar('Value4','image',0,255,nothing)
cv2.createTrackbar('Value5','image',255,255,nothing)

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
    Value3 = cv2.getTrackbarPos('Value3','image')
    Value4 = cv2.getTrackbarPos('Value4','image')
    Value5 = cv2.getTrackbarPos('Value5','image')
    s = cv2.getTrackbarPos(switch,'image')

    if s == 0:
        v1 = 11
        v2 = 2
        v3 = 255
        v4 = 65
        v5 = 8
    else:
        v1 = Value1
        v2 = Value2
        v3 = Value3
        v4 = Value4
        v5 = Value5

    # Our operations on the frame come here
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray,v4,v5,cv2.THRESH_BINARY)
    th2 = cv2.adaptiveThreshold(thresh,v3,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                cv2.THRESH_BINARY,v1,v2)
    # Display the resulting frame
    cv2.imshow('image',th2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
