import cv2
import numpy as np

drawing = False # true if mouse is pressed
ix,iy = -1,-1

store_draw = [];
final_store = [];
def saveImage(image):
    cv2.imwrite('handimage.png',image)

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,store_draw,final_store
    #print img[x,y]
    #print img.size
    if event == cv2.EVENT_LBUTTONDOWN:
        if img[y,x][0] == 255:
            drawing = True
            ix,iy = x,y
            store_draw = []
            store_draw.append((x,y))
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if img[y,x][0] == 255:
                cv2.circle(img,(x,y),2,(0,0,255),-1)
                store_draw.append((x,y))
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if img[y,x][0] == 255:
            cv2.circle(img,(x,y),2,(0,0,255),-1)
            #store_draw.append((x,y))
            #print store_draw
            final_store.append(store_draw)
        #store_draw.append((x,y))
        print 'New:' 
        print store_draw
img = cv2.imread('denizhand.png')
cv2.namedWindow('image')
cv2.imshow('image',img)
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break
    if k == ord('s'):
        saveImage(img)
    elif k == 27:
        break

cv2.destroyAllWindows()