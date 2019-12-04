import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image
import matplotlib
import sys

def save_disparity():
	num = 0

	while num < 9:

		imgL = cv2.imread("./perfect_stereo_images/left_{}.png".format(num),0)
		imgR = cv2.imread("./perfect_stereo_images/right_{}.png".format(num),0)

		stereo = cv2.StereoBM_create(numDisparities=256, blockSize=29)
		disparity = stereo.compute(imgL,imgR)
		im = Image.fromarray(disparity)
		matplotlib.image.imsave("perfect_disparity/disparity_{}.png".format(num), disparity, cmap='gray')
		#plt.imshow(disparity,'gray')
		#plt.show()

		num = num+1

def get_distance():
	disp = cv2.imread("./perfect_disparity/disparity_0.png", 0)
	print(disp.shape)

	maxed = np.amax(disp)
	print(maxed)
	coor = np.where(disp == maxed)
	coor2 = list(zip(coor[0], coor[1]))
	print("Max at {}".format(coor2))
	baseline = 176.252
	f = 4161.221
	dist = baseline*f/maxed 
	print("Distance is {}mm".format(dist))

	plt.imshow(disp)
	plt.title("Distance is {}mm".format(dist))
	plt.show()

	
np.set_printoptions(threshold=sys.maxsize)
#save_disparity()
get_distance()