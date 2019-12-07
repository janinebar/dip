import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image
import matplotlib
import sys

# Camera baselines in mm
baselines = [176.252, 174.945, 177.288, 171.548, 174.724, 174.019, 193.001, 178.089, 178.232]

# Focal lengths in pixels
fs = [4161.221, 7190.247, 5299.313, 6338.47, 6872.874, 5806.559, 3979.911, 2826.171, 2945.377]

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
	num = 9 # change this value depending on the picture

	disp = cv2.imread("./perfect_disparity/disparity_{}.png".format(num), 0)
	print(disp.shape)

	maxed = np.amax(disp)
	print(maxed)
	coor = np.where(disp == maxed)
	coor2 = list(zip(coor[0], coor[1]))
	print("Max at {}".format(coor2))

	baseline = baselines[num]
	f = fs[num]
	dist = baseline*f/maxed 
	print("Distance is {}mm".format(dist))

	plt.imshow(disp)
	plt.title("Distance is {}mm".format(dist))
	plt.show()

	
np.set_printoptions(threshold=sys.maxsize)
#save_disparity()
get_distance()