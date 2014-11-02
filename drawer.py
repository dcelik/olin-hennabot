import cv2
import numpy as np

drawing = False # true if mouse is pressed
ix,iy = -1,-1

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        if img[x,y][0] == 255:
            drawing = True
            ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if img[x,y][0] == 255:
                cv2.circle(img,(x,y),2,(0,0,255),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if img[x,y][0] == 255:
            cv2.circle(img,(x,y),2,(0,0,255),-1)

def makeDrawingWindow():
    img = cv2.imread('thresholdedimage.png')
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',draw_circle)

    while(1):
        cv2.imshow('image',img)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('q'):
            break
        if k == ord('s'):
            cv2.imwrite('handimage.png',img)
        elif k == 27:
            break

    cv2.destroyAllWindows()