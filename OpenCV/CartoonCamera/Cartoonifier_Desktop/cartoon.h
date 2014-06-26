/*****************************************************************************
*   cartoon.h
*   Create a cartoon-like or painting-like image filter.
******************************************************************************
* 	Modified by Luis  Parra, 24th June 2014 
******************************************************************************/

#pragma once


#include <stdio.h>
#include <iostream>
#include <vector>

// Include OpenCV's C++ Interface
#include "opencv2/opencv.hpp"


using namespace cv;
using namespace std;


/** 
@brief: Convert the given photo into a cartoon-like or painting-like image.
@param: debugType to 1 to show where skin color is taken from, and 2 to show the skin mask in a new window (for desktop).
@param: sketchMode true if you want a line drawing instead of a painting
@param: alienMode true if you want alien skin instead of human
@param: evilMode true if you want an "evil" character
@param: flippedMode true if you want to flip the image
@param: mirroMode true of you want mirror mode
*/
void cartoonifyImage(	Mat srcColor, 
						Mat dst, 
						int debugType, 
						bool sketchMode, 
						bool alienMode, 
						bool evilMode,					
						bool flippedMode,
						bool mirrorMode);


// Draw an anti-aliased face outline, so the user knows where to put their face.
void drawFaceStickFigure(Mat dst);


void changeFacialSkinColor(Mat smallImgBGR, Mat bigEdges, int debugType);
void removePepperNoise(Mat &mask);
void drawFaceStickFigure(Mat dst);
