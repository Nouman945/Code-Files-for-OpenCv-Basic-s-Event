#import the libraries
import cv2
import numpy as np

#Read the Image 
img = np.zeros((50,50,3),dtype='uint8')
# print(img)
i = 0

while True:
    cv2.imshow("Image",img)

    k = cv2.waitKey(0)
    # print(k)
    #Specify the font and draw the key using puttext
    font = cv2.FONT_HERSHEY_COMPLEX

    cv2.putText(img, chr(k), (140+i,250), font, .5, (255,255,255),2, cv2.LINE_AA)
    i+=10

    if k == ord('q'):
        break

cv2.destroyAllWindows()
cv2.waitKey(0)