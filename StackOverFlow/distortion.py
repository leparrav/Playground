'''
@file: distortion.py
Luis Parra - 16/11/2014
Undistort an image, without information
http://stackoverflow.com/questions/26954059/
'''

import numpy as np
import cv2
import regiongrowth as rg
from matplotlib import pyplot as plt


## PREPROCESSING
img = cv2.imread('leaf2.jpg')