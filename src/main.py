import cv2

# This reads the image
img_grey = cv2.imread('C:/Users/kadep/ImageColorChange/doc/nature.png', cv2.IMREAD_GRAYSCALE)

# define color threshold, 128 is the middle of black and white
thresh = 128

img_binary = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)[1]

# Save
cv2.imwrite('C:/Users/kadep/ImageColorChange/doc/bnw.png', img_binary)