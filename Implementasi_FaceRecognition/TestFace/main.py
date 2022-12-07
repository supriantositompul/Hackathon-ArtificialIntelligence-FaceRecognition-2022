import cv2

img = cv2.imread('download.png', cv2.IMREAD_COLOR)

cv2.imshow('download', img)


cv2.waitKey(0)
cv2.destroyAllWindows()

