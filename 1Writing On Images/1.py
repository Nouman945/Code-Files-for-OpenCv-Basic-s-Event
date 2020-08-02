#importing the libriries
import cv2
import numpy as np

img = cv2.imread('image.jpg')

window_name = 'Image'

font = cv2.FONT_HERSHEY_COMPLEX

font_Scale = 1

color = (255,255,255)

thickness = 2

org = (200,200)

image = cv2.putText(img, 'Open CV', org, font, font_Scale, color, thickness, cv2.LINE_AA)

cv2.imshow(window_name,image)

cv2.waitKey(0)
