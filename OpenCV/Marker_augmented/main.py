import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    # First convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Second median blur and threshold our image
    gray = cv2.medianBlur(gray,5)
    adaptive_th = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,7,7)

    # Third - Find contours - Filter the interesting ones.
    minimum_points = 100;
    contours, hierarchy = cv2.findContours(adaptive_th,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    filtered_contours = []
    for each_contour in contours:
        if len(each_contour)>minimum_points:
            filtered_contours.append(each_contour)

    #cv2.drawContours(frame,filtered_contours,-1,(0,255,0),2)

    # Display the resulting frame
    cv2.imshow('Simple Augmented Reality',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()