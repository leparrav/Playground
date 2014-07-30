import cv2


def updateImage():
    return 0

window_name = 'level control'
cv2.namedWindow(window_name)
level_count = 7

for i in xrange(level_count):
    cv2.createTrackbar(str(i), window_name, 1, 10,updateImage)

print cv2.__version__

cv2.waitKey(0)
