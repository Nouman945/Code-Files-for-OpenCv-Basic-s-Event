#import the libraries
import cv2
import numpy as np

#reading the image
img = cv2.imread('image.jpg', cv2.IMREAD_COLOR)


#Drawing the Line
# cv2.line(img,(0,0),(350,350),(255,255,255),15)

#Circle
# cv2.circle(img,(200,126),55,(255,0,0),1)

#Points
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)

# Integer(-9223372036854775808 to 9223372036854775807)

cv2.polylines(img,[pts], True, (0,255,255), 4)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
