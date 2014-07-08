'''
@file: leaf.py
Luis Parra - 04/07/2014
Segments a Leaf in a real world environment without any prior information
'''

import numpy as np
import cv2
import regiongrowth as rg
from matplotlib import pyplot as plt

'''
Adative threshold with gaussian filtering
'''
def threshold(img_gray):
	# Adaptive thresholding after Gaussian filtering
	blur = cv2.GaussianBlur(img_gray,(5,5),0)
	thr = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
	return thr

def filtering(img_gray,esp):
	if esp == "median":
		return cv2.medianBlur(img_gray,5)
	elif esp == "gaussian":
		return cv2.GaussianBlur(img_gray,(5,5),0)
	elif esp == "bilateral":
		return cv2.bilateralFilter(img_gray,5,50,100)


''' 
Given a img list of 4 items and a title list displays them
'''
def showImages(imgs,titles):
	for i in range(0,4):
		plt.subplot(141+i),plt.imshow(imgs[i],'gray'),plt.title(titles[i])
		plt.xticks([]), plt.yticks([])
	plt.show()


'''
Sort all perimeters obtained
'''
def quick_sort(p):
	if len(p) <= 1:
		return p

	pivot = p.pop(0)
	low,high = [],[]
	for entry in p:
		if entry[0] > pivot[0]:
			high.append(entry)
		else: 
			low.append(entry)
	return quick_sort(high) + [pivot] + quick_sort(low)


'''
Find the contours of a canny image, returns an image with the 3 largest contours, 
a bounding box around them, th bounding box, the contours and perimeters sorted
'''
def largestContours(canny,img,img_gray):

	contours, hierarchy = cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
	img_contour = np.copy(img) # Contours change original image.
 	#cv2.drawContours(img_contour, contours, -1, (0,255,0), 3) # Draw all - For visualization only

	# Contours -  maybe the largest perimeters pinpoint to the leaf?
	perimeter = []
	max_perim = [0,0]
	i = 0

	# Find perimeter for each contour i = id of contour
	for each_cnt in contours:
		prm = cv2.arcLength(each_cnt,False)
		perimeter.append([prm,i])
		i += 1

	# Sort them
	perimeter = quick_sort(perimeter)
	
	unified = []
	max_index = []
	# Draw max contours
	for i in range(0,3):
		index = perimeter[i][1]
		max_index.append(index)
		cv2.drawContours(img_contour, contours, index, (255,0,0), 3)

	# Get convex hull for max contours and draw them
	cont = np.vstack(contours[i] for i in max_index)
	hull = cv2.convexHull(cont)
	unified.append(hull)
	cv2.drawContours(img_contour,unified,-1,(0,0,255),3)

	return img_contour, contours, perimeter, hull

'''
Given a convex hull apply graph cut to the image
Assumptions: 
- Everything inside convex hull is the foreground object - cv2.GC_FGD or 1
- Everything outside the rectangle is the background -  cv2.GC_BGD or 0
- Between the hull and the rectangle is probably foreground - cv2.GC_PR_FGD or 3
'''
def grCut(chull,img):
	# First create our rectangle that contains the object
	y_corners = np.amax(chull, axis=0)
	x_corners = np.amin(chull,axis=0)
	x_min = x_corners[0][0]
	x_max = x_corners[0][1]
	y_min = y_corners[0][0]
	y_max = y_corners[0][1]
	rect = (x_min,x_max,y_min,y_max)

	# Our mask 
	mask = np.zeros(img.shape[:2],np.uint8)

	# Values needed for algorithm
	bgdModel = np.zeros((1,65),np.float64)
	fgdModel = np.zeros((1,65),np.float64)

	# Grabcut
	cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

	mask2 = np.where((mask==cv2.GC_PR_BGD)|(mask==cv2.GC_BGD),0,1).astype('uint8')
	img = img*mask2[:,:,np.newaxis]

	return img

'''
Main loop  
'''
## PREPROCESSING
img = cv2.imread('leaf2.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# thresh = threshold(img_gray) 	# Threshold the image
filtered = filtering(img_gray,"bilateral")
canny = cv2.Canny(filtered,100,200)
canny_unfiltered = cv2.Canny(img_gray,100,200)


## SEGMENTATION
# Largest Contour - Not the best segmentation
img_contour, contours, perimeters, hull = largestContours(canny,img,img_gray)

# Grabcut - Same bounding box than contours... 
img_grcut = grCut(hull,img)


# Region grow method - Where to place the seeds, how do I stop growing?
#  \todo
#img_grow = cv2.add(mask,img_gray)
size = img.shape

# Interactive grab-cut



## Show images
images = [img_contour,img_grcut,canny_unfiltered,img_gray]
titles = ["Largest Contours", "Graph cut", "Region grow", "Interactive"]
showImages(images, titles)