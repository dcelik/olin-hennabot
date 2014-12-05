import cv2
import numpy as np
import csv

drawing = False # true if mouse is pressed
ix,iy = -1,-1


store_draw = [];
final_store = [];
# mouse callback function

def makeDrawingWindow():

    # mouse callback functio
    def draw_image(event,x,y,flags,param):
        global ix,iy,drawing,store_draw,final_store
        #print img[x,y]
        #print img.size
        if event == cv2.EVENT_LBUTTONDOWN:
            if img[y,x][0] == 255:
                drawing = True
                ix,iy = x,y
                final_store.append(store_draw)
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
                #store_draw.append((x,y))
            #store_draw.append((x,y))
            print 'New:' 
            print store_draw
            final_store.append(store_draw)
        elif final_store[end] != store_draw:
            final_store.append(store_draw)
    img = cv2.imread('thresholdedimage.png')
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',draw_image)

    while(1):
        cv2.imshow('image',img)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('q'):
            #print final_store
            return final_store
            break
        if k == ord('s'):
            cv2.imwrite('handimage.png',img)
            #print final_store
            return final_store
            break
        elif k == 27:
            break

    cv2.destroyAllWindows()