from pseyepy import Camera, Display
import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image
import sys, tty, termios

# initialize all connected cameras
c1 = Camera([0, 1], resolution=[Camera.RES_LARGE, Camera.RES_LARGE])

num = 0

while num < 20:
	# check for char
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
	    tty.setraw(sys.stdin.fileno())
	    ch = sys.stdin.read(1)
	finally:
	    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

	# read from the camera/s
	frame, timestamp = c1.read()
	#print(frame)
	nparr = np.asarray(frame)
	print(nparr.shape)

	im1 = Image.fromarray(nparr[0])
	im2 = Image.fromarray(nparr[1])
	im1.save("left/left_{}.jpg".format(num))
	im2.save("right/right_{}.jpg".format(num))

	num = num + 1

# # im1 = cv2.imread("im0.png", 0)
# # im2 = cv2.imread("im1.png", 0)
# # cv2.imshow('image',im2)

# # stereo = cv2.StereoBM_create(numDisparities=256, blockSize=29)
# # disparity = stereo.compute(im1, im2)

# # plt.imshow(disparity, 'gray')
# # plt.show()

# plt.figure()
# plt.imshow(frame[0])
# plt.figure()
# plt.imshow(frame[1])
# plt.show()

# # when finished, close the camera
# c1.end()