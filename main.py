#!/usr/bin/env python2.7
# ------------------------------------------------------------------------------------------------------
# @ write frame to the file
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(q, 0)
        # @ write the flipped frame
        out.write(frame)
        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
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

# import numpy as np
# import cv2
#
# img = cv2.imread('c:/tst.jpg', cv2.IMREAD_COLOR)
# cv2.imshow('image', img)
#
# # @ key input handle
# k = cv2.waitKey(0)
# if k == 27:
#     # @ wait for ESC key to exit
#     cv2.destroyAllWindows()
# elif k == ord('s'):
#     # @ wait for 's' key to save and exit
#     cv2.imwrite('messigray.png', img)
#     cv2.destroyAllWindows()
# ------------------------------------------------------------------------------------------------------
# @ matplotlib
# import numpy as np
# import cv2
# from matplotlib import pyplot as plt
#
# img = cv2.imread('c:/cap.png', cv2.IMREAD_COLOR)
# # @ high level
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# # @ to hide tick values on X and Y axis
# plt.xticks([]), plt.yticks([])
# plt.show()

# ------------------------------------------------------------------------------------------------------
# @ vedio handle
import cv2

# ------------------------------------------------------------------------------------------------------
# @ get vedio steam from camera of computer
# cap = cv2.VideoCapture(0)
# if cap.isOpened():
#     print 'camera is open'
# else:
#     cap.open()
#     print 'open the camera'
#     cap = cv2.VideoCapture(0)
# wt = cap.get(3)
# hi = cap.get(4)
# print wt,
# print 'X',
# print hi
# # @ change the width and high
# print cap.set(3, 1280)
# print cap.set(4, 640)
# print wt,
# print 'X',
# print hi
#
# while (True):
#     # @ cap frame by frame
#     ret, frame_pic = cap.read()
#     # @ handle the pic
#     gray = cv2.cvtColor(frame_pic, cv2.COLOR_BGR2GRAY)
#     # @ display the ret fame
#     cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
#     cv2.imshow('frame', gray)
#     key = cv2.waitKey(1)
#     if (27 == key) | (ord('q') == key):
#         break
# # @ release cap
# cap.release()
# cv2.destroyAllWindows()
