#!/usr/bin/env python2.7

# ------------------------------------------------------------------------------------------------------
# @ draw with color pen
import cv2
import numpy as np

drawing = False


def nothing(x):
    pass


def draw_circle(event, x, y, flags, param):
    # @ global value in this file
    global drawing, mode, b, g, r
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing == True:
            cv2.circle(img, (x, y), 1, (b, g, r), -1)  # draw little circle
    elif event == cv2.EVENT_LBUTTONUP:
        drawing == False


# @ create one pic handle
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')

# @ create and show the slider
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)
switch = '0:OFF\n1:ON'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

# @ bind mouse listen
cv2.setMouseCallback('image', draw_circle)

while (1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch, 'image')
cv2.destroyAllWindows()

# ------------------------------------------------------------------------------------------------------
# @ change the color via slider
# import cv2
# import numpy as np
#
#
# def nothing(x):
#     pass
#
#
# # @ create one pic handle
# img = np.zeros((300, 512, 3), np.uint8)
# cv2.namedWindow('image')
#
# # @ create and show the slider
# cv2.createTrackbar('R', 'image', 0, 255, nothing)
# cv2.createTrackbar('G', 'image', 0, 255, nothing)
# cv2.createTrackbar('B', 'image', 0, 255, nothing)
# switch = '0:OFF\n1:ON'
# cv2.createTrackbar(switch, 'image', 0, 1, nothing)
#
# while (1):
#     cv2.imshow('image', img)
#     k = cv2.waitKey(1) & 0xFF
#     if k == 27:
#         break
#     r = cv2.getTrackbarPos('R', 'image')
#     g = cv2.getTrackbarPos('G', 'image')
#     b = cv2.getTrackbarPos('B', 'image')
#     s = cv2.getTrackbarPos(switch, 'image')
#     if s == 0:
#         img[:] = 0
#     else:
#         img[:] = [b, g, r] # imge color
# cv2.destroyAllWindows()

# ------------------------------------------------------------------------------------------------------
# @ draw line and rectangle
# import cv2
# import numpy as np
#
# # @ drawing flag
# drawing = False
# # @ mode flag
# mode = True
# ix, iy = -1, -1
#
#
# def draw_circle(event, x, y, flags, param):
#     # @ global value in this file
#     global ix, iy, drawing, mode
#     if event == cv2.EVENT_LBUTTONDOWN:
#         drawing = True
#
#         # @ mapping
#         ix, iy = x, y
#         print "---------"
#         print ix
#         print iy
#         print x
#         print y
#     elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
#         if drawing == True:
#             if mode == True:
#                 cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
#             else:
#                 cv2.circle(img, (x, y), 1, (255, 0, 255), -1)  # draw little circle
#     elif event == cv2.EVENT_LBUTTONUP:
#         drawing == False
#
#
# # @ creat img
# img = np.zeros((512, 512, 3), np.uint8)
# cv2.namedWindow('image')
#
# # @ bind mouse listen
# cv2.setMouseCallback('image', draw_circle)
#
# # @  show image and listen key
# while (1):
#     cv2.imshow('image', img)
#     # @ listen key
#     k = cv2.waitKey(1) & 0xFF
#     if k == ord('m'):
#         mode = not mode
#     elif k == 27:
#         break

# ------------------------------------------------------------------------------------------------------
# @  mouse draw a circle
# import cv2
# import numpy as np
#
#
# # @ mouse callback function
# def draw_circle(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         cv2.circle(img, (x, y), 100, (0, 255, 0), -1) # draw a circle
#
#
# img = np.zeros((1024, 512, 3), np.uint8)
# # @ set mouse event callback
# cv2.namedWindow('image')
# cv2.setMouseCallback('image', draw_circle)
# while (1):
#     cv2.imshow('image', img)
#     if cv2.waitKey(20) & 0xFF == 27:
#         break
# cv2.destroyAllWindows()

# import cv2
#
# # @ get all event and print it
# events = [i for i in dir(cv2) if 'EVENT' in i]
# print events

# ------------------------------------------------------------------------------------------------------
# @ draw
# import numpy as np
# import cv2
#
# # @   Create a black image
# img = np.zeros((512, 512, 3), np.uint8)
#
# # @  Draw a diagonal blue line with thickness of 5 px
#
# # @ line
# cv2.line(img, (0, 0), (511, 511), (0, 0, 255), 3)
# # @ rectangle
# cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
# # @ circle
# cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)
# # @ ellipse
# cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
#
# # pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
# # pts = pts.reshape((-1, 1, 2))
#
# # @ text
# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2)
#
# # @ windows show
# winname = 'shencp'
# cv2.namedWindow(winname)
# cv2.imshow(winname, img)
# cv2.waitKey(0)
# cv2.destroyWindow(winname)

# ------------------------------------------------------------------------------------------------------
# @ write frame to the file
# import cv2
#
# cap = cv2.VideoCapture(0)
#
# # @  Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'XVID')

# @ open file
# out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
#
# while (cap.isOpened()):
#     ret, frame = cap.read()
#     if ret == True:
#         # @ inverted image
#         # frame = cv2.flip(q, 0)
#         # @ write the frame to the file
#         out.write(frame)
#         cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
#         cv2.imshow('frame', frame)
#         if cv2.waitKey(1) == ord('q'):
#             break
#     else:
#         break

# @  Release everything if job is finished
# cap.release()
# out.release()
# cv2.destroyAllWindows()
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
