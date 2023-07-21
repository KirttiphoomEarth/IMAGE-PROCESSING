import cv2
import numpy as np
import math
import matplotlib.image as mpimg
import matplotlib.pyplot as plt



# Load the input image
image = cv2.imread('goldfish.jpg')
#cv2.imshow('Original', image)
cv2.waitKey(0)

# Use the cvtColor() function to grayscale the image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_image = cv2.resize(gray_image, (200,200))
plt.imshow(gray_image)
#print(gray_image)
#cv2.imshow('Grayscale', gray_image)
cv2.waitKey(0)

# Window shown waits for any key pressing event
cv2.destroyAllWindows()
