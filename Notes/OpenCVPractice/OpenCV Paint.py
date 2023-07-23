import cv2 as cv
import numpy as np

drawing=False
mode=True
ix,iy=-1,-1
# b, g, r = 0, 0, 0

def nothing():
    pass

def crate_trackbar():
    cv.createTrackbar('R','image',0,255,nothing)
    cv.createTrackbar('G','image',0,255,nothing)
    cv.createTrackbar('B','image',0,255,nothing)
    cv.createTrackbar('Brush Size','image',0,20,nothing)

def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode,b,g,r
    
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy=x,y
    
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(img,(ix,iy),(x,y),(b,g,r),2)
            
            else:
                cv.circle(img,(x,y),size,(b,g,r),-1)
                
    if event == cv.EVENT_LBUTTONUP:
        drawing = False
        
        if mode ==  True:
            cv.rectangle (img,(ix,iy),(x,y),(255,255,255),-1)
            
        else:
            cv.circle(img,(x,y),size,(b,g,r),-1)
            
            
img=np.full((512,512,3),255,dtype=np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
crate_trackbar()

while (1):
    r=cv.getTrackbarPos('R','image')
    g=cv.getTrackbarPos('G','image')
    b=cv.getTrackbarPos('B','image')
    size=cv.getTrackbarPos('Brush Size','image')
    
    
    cv.imshow('image',img)
    k=cv.waitKey(1) & 0xFF
    
    if k == ord('m'):
        mode= not mode
        
    elif k == 27 or k== ord('q'):
        break
    
    elif k == ord('c'):
        img=np.full((512,512,3),255,np.uint8)
        


    
    
cv.destroyAllWindows()
