#!/usr/bin/env python2.7
# ------------------------------------------------------------------------------------------------------
# @ handle a picture
# import cv2
#
# if __name__ == '__main__':
#     # @ read
#     img = cv2.imread("c:/cap.png", cv2.IMREAD_COLOR)
#     # @ windows size setting
#     cv2.namedWindow('image', cv2.WINDOW_NORMAL)
#     # @ show
#     cv2.imshow("image", img)
#     # @ write
#     cv2.imwrite('c:/tst.jpg',img)
#     # @ pause
#     cv2.waitKey(0)
#     # @ windows distroy
#     cv2.destroyAllWindows()

# ------------------------------------------------------------------------------------------------------
# @ key handle

import numpy as np
import cv2

img = cv2.imread('c:/tst.jpg', cv2.IMREAD_COLOR)
cv2.imshow('image', img)

# @ key input handle
k = cv2.waitKey(0)
if k == 27:
    # @ wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):
    # @ wait for 's' key to save and exit
    cv2.imwrite('messigray.png', img)
    cv2.destroyAllWindows()
