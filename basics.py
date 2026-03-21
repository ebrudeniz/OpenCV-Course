import cv2
import numpy as np
import matplotlib.pyplot as plt

# opencv reads images in BGR format
# matplotlib reads images in RGB format
# to convert from BGR to RGB, we can use cv2.cvtColor function
img = cv2.imread("rgb.jpeg")
img_rgb = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)

# Splitting the image into its color channels
b,g,r = cv2.split(img)

img_gray = cv2.imread('rgb.jpeg', 0)
cv2.imshow("Gray", img_gray)
# plots
# mixed
plt.subplot(2,2,1)
plt.imshow(img_rgb)
plt.title("Mixed")

# red
plt.subplot(2,2,2)
plt.imshow(r, cmap="gray")
plt.title("Red")    

# green
plt.subplot(2,2,3)
plt.imshow(g, cmap="gray")
plt.title("Green")

# blue
plt.subplot(2,2,4)
plt.imshow(b, cmap="gray")
plt.title("Blue")



plt.tight_layout()
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()