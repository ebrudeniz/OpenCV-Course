import cv2
import numpy as np

img = cv2.imread("panda.jpeg")
print(img.shape)
print(img)
cv2.imshow("Panda", img)

# accessing pixel values
print(img[0,0])

# flipping the image
img_flipped_horizontal = cv2.flip(img, 1) # 1 for horizontal flip
cv2.imshow("Flipped Image Horizontal", img_flipped_horizontal)

img_flipped_vertical = cv2.flip(img, 0) # 0 for vertical flip
cv2.imshow("Flipped Image Vertical", img_flipped_vertical)

img_flipped_both = cv2.flip(img, -1) # -1 for both flips
cv2.imshow("Flipped Image Both", img_flipped_both)

cv2.waitKey(0)
cv2.destroyAllWindows()