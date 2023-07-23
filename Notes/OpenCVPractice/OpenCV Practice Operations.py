import cv2 as cv
import numpy as np

img=cv.imread('OpenCVPractice\Calibarn.jpg')
assert img is not None,'file could not be read,check with os.path.exists()'

# px=img[100,100]
# print(px)

# print('Blue',(blue:= img[100,100,0]))

print(img.item(100,100,2))

# while(1):
#     cv.imshow('Calibarn',img)
    
#     if cv.waitKey(1) == 27:
#         break

# cv.destroyAllWindows()
