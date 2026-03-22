import cv2

img = cv2.imread("panda.jpeg")
print(img.shape)
cv2.imshow("Panda", img)

img_line = img.copy()

# drawing a line on the image
# img = cv2.line(img, pt1, pt2, color[, thickness[, lineType[, shift]]])
cv2.line(img_line, (50,50), (200,150),(0,255,255), thickness=5, lineType=cv2.LINE_AA) # lineType=cv2.LINE_AA for anti-aliased line
cv2.imshow("Line", img_line)

# drawing a circle on the image
# img = cv2.circle(img, center, radius, color[, thickness[, lineType[, shift]]])
img_circle = img.copy()
cv2.circle(img_circle , (144,74), 10, (255,0,0), thickness=5, lineType=cv2.LINE_AA)
cv2.imshow("Circle", img_circle)

# drawing a rectangle on the image
# img = cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]])
img_rectangle = img.copy()
cv2.rectangle(img_rectangle, (90,8), (245,150), (0,255,0), thickness=5, lineType=cv2.LINE_AA)
cv2.imshow("Rectangle", img_rectangle)

#adding text to the image
# img = cv2.putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
img_text = img.copy()
text = "Panda"
cv2.putText(img_text, text, (110,165), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), thickness=2, lineType=cv2.LINE_AA)
cv2.imshow("Text", img_text)

# when fontScale is negative , it means the text will be reversed or mirrored
img_reversed_text = img.copy()
cv2.putText(img_reversed_text, text, (110,165), cv2.FONT_HERSHEY_SIMPLEX, -1, (255,255,0), thickness=2, lineType=cv2.LINE_AA)
cv2.imshow("Reversed Text", img_reversed_text)

# When thickness is negative, it means that the shape will be filled
img_filled_circle = img.copy()
cv2.circle(img_filled_circle , (144,74), 10, (255,0,0), thickness=-1, lineType=cv2.LINE_AA)
cv2.imshow("Filled Circle", img_filled_circle)

cv2.waitKey(0)
cv2.destroyAllWindows()

