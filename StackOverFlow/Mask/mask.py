import numpy as np
import cv2
from matplotlib import pyplot as plt


## LOAD IMAGE AND MASK
img = cv2.imread('suv.jpeg')
mask = cv2.imread('mask.jpg')