import cv2 as cv
import sys
import numpy as np

"""Open and save Image"""

# img=cv.imread("road.jpg")

# if img is None:
#     sys.exit("Could not read the image")

# cv.imshow("Display window",img)
# k=cv.waitKey(0)

# if k == ord("s"):
#     cv.imwrite("starry_night.png",img)

"""Get Video and Display"""
# cap=cv.VideoCapture(0) #Get Video from camera

# if not cap.isOpened():
#     sys.exit("Could not open the camera")
    
# # Set new frame size
# cap.set(cv.CAP_PROP_FRAME_WIDTH, 1000)  # Width in pixels
# cap.set(cv.CAP_PROP_FRAME_HEIGHT, 2000)  # Height in pixels

# while True:
#     ret,frame=cap.read()
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
#     hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
#     cv.imshow("frame",gray)
    
#     if cv.waitKey(1)==ord("q"):
#         break
    
# print("Width =",cap.get(cv.CAP_PROP_FRAME_WIDTH))
# print("Height =",cap.get(cv.CAP_PROP_FRAME_HEIGHT))
# cap.release()
# cv.destroyAllWindows()

# """Save Video"""
# cap = cv.VideoCapture(0)
# fourcc = cv.VideoWriter_fourcc(*'mp4v')
# out=cv.VideoWriter('output.mp4',fourcc,20.0,(640,480))

# while cap.isOpened():
#     ret,frame=cap.read()
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
    
#     frame=cv.flip(frame,0)
#     out.write(frame)
#     cv.imshow("frame",frame)
    
#     if cv.waitKey(1)==ord("q"):
#         break

# cap.release()
# out.release()
# cv.destroyAllWindows()


#Drawing Functions

# img=np.zeros((512,1000,3),np.uint8)
# # cv.line(img,x=(0,0),y=(511,511),BGR=(255,0,0),px=5)
# cv.line(img,(0,225),(999,225),(255,0,0),5)
# cv.rectangle(img,(450,200),(600,225),(0,255,0),3)
# cv.circle(img,(500,500),100,(0,0,255),-1)
# cv.ellipse(img,(500,500),(100,50),0,0,360,(0,255,255),-1)
# cv.polylines(img,[np.array([[100,100],[200,200],[300,100],[400,200],[500,100],[600,200],[700,100],[800,200],[900,100]])],True,(255,255,0),5)
# font=cv.FONT_HERSHEY_SIMPLEX
# cv.putText(img,"OpenCV",(10,500),font,4,(255,255,255),2,cv.LINE_AA)
# cv.imshow("line",img)
# cv.waitKey(0)

"""# ##Open CV Logo Challenge"""
# logo=np.full((512,512,3),255,np.uint8)

# img=cv.ellipse(logo,(256,200),(60,60),120,0,300,(0,0,255),-1)
# img=cv.ellipse(logo,(256,200),(20,20),0,0,360,(255,255,255),-1)

# img=cv.ellipse(logo,(190,325),(60,60),0,0,300,(0,255,0),-1)
# img=cv.ellipse(logo,(190,325),(20,20),0,0,360,(255,255,255),-1)

# img=cv.ellipse(logo,(256+(256-190),325),(60,60),300,0,300,(255,0,0),-1)
# img=cv.ellipse(logo,(256+(256-190),325),(20,20),0,0,360,(255,255,255),-1)

# font=cv.FONT_HERSHEY_SIMPLEX
# text=cv.putText(logo,"OpenCV",(165,425),font,1.5,(0,0,0),4,cv.LINE_AA)


# cv.imshow("logo",logo)
# cv.waitKey(0)
# cv.destroyAllWindows()

# """Mouse as a Paint Brush"""
# def draw_circule(event,x,y,flags,param):
#     if event==cv.EVENT_LBUTTONDBLCLK:
#         cv.circle(img,(x,y),100,(255,0,0),-1)

# img=np.full((512,512,3),255,np.uint8)
# cv.namedWindow("image")
# cv.setMouseCallback("image",draw_circule)


# while(1):
#     cv.imshow("image",img)
#     if cv.waitKey(20) & 0xFF==27:
#         break
#     elif cv.waitKey(20) & 0xFF==ord("c"):
#         img=np.full((512,512,3),255,np.uint8)
#     elif cv.waitKey(1) & 0xFF==ord("q"):
#         break
    
# cv.destroyAllWindows()

# # # #Advanced Operations
# drawing = False
# mode=True
# ix,iy=-1,-1

# def draw_circle(event,x,y,flags,param):
#     global ix,iy,drawing,mode
    
#     if event==cv.EVENT_LBUTTONDOWN:
#         drawing=True
#         ix,iy=x,y
        
#     elif event==cv.EVENT_MOUSEMOVE:
#         if drawing == True:
#             img_copy=img.copy()
#             if mode == True:
#                 cv.rectangle(img,(ix,iy),(x,y),(0,255,0),2)
#             else:
#                 cv.circle(img,(x,y),5,(0,0,255),-1)
                
#     elif event==cv.EVENT_LBUTTONUP:
#         drawing=False
#         if mode == True:
#             cv.rectangle(img,(ix,iy),(x,y),(255,255,255),-1)
#         else:
#             cv.circle(img,(x,y),5,(0,0,255),-1)
            
# img=np.full((512,512,3),255,np.uint8)
# cv.namedWindow("image")
# cv.setMouseCallback("image",draw_circle)

# while(1):
#     cv.imshow("image",img)
#     k=cv.waitKey(1) & 0xFF
#     if k==ord("m"):
#         mode=not mode
#     elif k==27:
#         break
#     elif k==ord("c"):
#         img=np.full((512,512,3),255,np.uint8)
#     elif k==ord("q"):
#         break
    
# cv.destroyAllWindows()


# # # #Trackbar as the Color Palette
def nothing(x):
    pass

img=np.zeros((512,512,3),dtype=np.uint8)
cv.namedWindow('image')

#Create Trackbar
cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)

#create switch for ON/OFF functionality
switch ='0: OFF \n 1 :ON'
cv.createTrackbar(switch,'image',0,1,nothing)

while(1):
    cv.imshow('image',img)
    k=cv.waitKey(1) & 0xFF
    if k == 27 or k == ord('q') :
        break
    r=cv.getTrackbarPos('R','image')
    g=cv.getTrackbarPos('G','image')
    b=cv.getTrackbarPos('B','image')
    s=cv.getTrackbarPos(switch,'image')
    
    if s ==0:
        img[:]=0
    else:
        img[:]=[b,g,r] 
        
cv.destroyAllWindows()


    