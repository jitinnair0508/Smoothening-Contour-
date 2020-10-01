import cv2
import numpy as np
from scipy.interpolate import splprep, splev
from array import *
         
img = cv2.imread("crop5.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
contours, hier = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
smoothened = []
for contour in contours:
    #cv2.drawContours(img, contour, -1, (255,0,0), 3)
    #contour1 = np.vstack(contour).squeeze()
    #print(contour1)
    #print(contour)
    im1 = np.zeros([512,512,3],np.uint8)
    #center = tuple(map(tuple, contour))
    x,y = contour.T    
    x = x.tolist()[0]
    y = y.tolist()[0]    
    tck, u = splprep([x,y], u=None, s=1.0, per=1)    
    u_new = np.linspace(u.min(), u.max(), 30)    
    x_new, y_new = splev(u_new, tck, der=0)    
    res_array = [(int(i[0]), int(i[1])) for i in zip(x_new,y_new)]
    #smoothened.append(np.asarray(res_array, dtype=np.int32))
    #print(res_array)
    #c1 = np.vstack(res_array).squeeze()
    print(type(res_array))
    #list1 = res_array.tolist()
    #print(list1)


    center1 = tuple(map(tuple, res_array))
    #print(c1)
    #print(center1)

    #print(res_array)
    for i in center1:
        #print(i)
        cv2.circle(im1,i,2,(255,0,0),2)
    
    

    


#cv2.drawContours(img, smoothened, -1, (255,0,0), 3)
cv2.imwrite("test3.png",im1)

#img1 = cv2.imread("bottle.png")
#cv2.fillPoly(img, pts =smoothened, color=(255,0,0))
#cv2.imwrite("output-bottle.png",img)
#cv2.imshow('Contours', img) 
#cv2.waitKey(0) 
#cv2.destroyAllWindows()
#print(contours)