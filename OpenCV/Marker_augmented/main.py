import numpy as np
import itertools
import math
import cv2
import pdb

cap = cv2.VideoCapture(0)
debug = False
MIN_DISTANCE = 100
MAX_DISTANCE = 400
MARKER_SIZE = np.float32([[0,0],[100,0],[100,100], [0,100]])

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if debug:
        cv2.imshow('Frame',frame)

    size_x = len(frame[0])
    size_y = len(frame)

    MIN_DISTANCE = math.ceil(len(frame)*0.05)
    MAX_DISTANCE = math.ceil(len(frame)*0.4)

    # Our operations on the frame come here
    # First convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if debug:
        cv2.imshow('Gray',gray)

    # Second median blur and threshold our image
    blur = cv2.medianBlur(gray,5)
    #adaptive_th = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,5,5)
    ret2,adaptive_th = cv2.threshold(blur,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    
    if debug:
        cv2.imshow('Threshold',adaptive_th)

    # Third - Find contours - Filter the interesting ones.
    minimum_points = 50;
    contours, hierarchy = cv2.findContours(adaptive_th,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    filtered_contours = []
    for each_contour in contours:
        if len(each_contour)>minimum_points:
            filtered_contours.append(each_contour)

    if debug:
        cv2.drawContours(frame,filtered_contours,-1,(0,0,255),2)
        cv2.imshow('Contours',frame)

    # Four - Find Canditates - Approximate Curve - Get markers
    markers, drawMarkers = [], []
    for each_contour in filtered_contours:
        eps = len(each_contour)*0.025 # aproximation accuracy
        closed = True # Contour is closed
        current_curve = cv2.approxPolyDP(each_contour,eps,closed)

        # Candidates must have 4 corners
        if len(current_curve) != 4:
            continue

        # Must be convex
        if not cv2.isContourConvex(current_curve):
            continue

        #Not good if any of the corners lies on the edge
        for corner in current_curve:
            if corner[0][0] > 0.7*size_x or corner[0][1] > 0.7*size_y:
                continue
        
        # Enough distance between each corner
        side = []
        for i in range(0,4):
            if i == 3:
                side.append(np.linalg.norm(current_curve[i]-current_curve[0]))
                continue
            side.append(np.linalg.norm(current_curve[i]-current_curve[i+1]))

        minSide = min(side)
        if minSide < MIN_DISTANCE or minSide > MAX_DISTANCE:
            continue

        # Small fix to draw markers
        drawMarkers.append(current_curve)

        #Sort points in counter clock wise and save as np
        np.reshape(current_curve,MARKER_SIZE.shape)
        np.sort(current_curve)
        current_curve = current_curve.astype(np.float32)

        #If we got so far this marker is valid
        markers.append(current_curve)

    # Five - Perspective Transformation 
    # Define our marker size - cast to numpy array
    if markers:
        for each_marker in markers:
            perspectiveMatrix = cv2.getPerspectiveTransform(each_marker,MARKER_SIZE)

    


    #Display simple augmented reality
    cv2.drawContours(frame,drawMarkers,-1,(0,0,255),3)
    cv2.imshow('Simple Augmented Reality',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()