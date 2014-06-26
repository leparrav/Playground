/*****************************************************************************
*   Cartoonifier_Desktop.cpp, for Desktop.
*   Converts a real-life camera stream to look like a cartoon.
*   This file is for a desktop executable, but the cartoonifier can also be used in an Android / iOS project.
******************************************************************************
*   Modified by Luis Parra, 25th June 2014 
******************************************************************************/



// Try to set the camera resolution. Note that this only works for some cameras on
// some computers and only for some drivers, so don't rely on it to work!
const int DESIRED_CAMERA_WIDTH = 640;
const int DESIRED_CAMERA_HEIGHT = 480;

const int NUM_STICK_FIGURE_ITERATIONS = 200; // Sets how long the stick figure face should be shown for skin detection.

const char *windowName = "Cartoonifier";   // Name shown in the GUI window.

#include <stdio.h>
#include <stdlib.h>

// Include OpenCV's C++ Interface
#include "opencv2/opencv.hpp"

#include "cartoon.h"            // Cartoonify a photo.
#include "ImageUtils.h"      // Shervin's handy OpenCV utility functions.

using namespace cv;
using namespace std;

#if !defined VK_ESCAPE
    #define VK_ESCAPE 0x1B      // Escape character (27)
#endif



/**
@brief Initialize webcam
@param &videoCapture pointer to camera 
@param cameraNumber if there is more than 1 camera connected
*/
void initWebcam(VideoCapture &videoCapture, int cameraNumber)
{
    // Get access to the default camera.
    try {   // Surround the OpenCV call by a try/catch block so we can give a useful error message!
        videoCapture.open(cameraNumber);
    } catch (cv::Exception &e) {}
    if ( !videoCapture.isOpened() ) {
        cerr << "ERROR: Could not access the camera!" << endl;
        exit(1);
    }
    cout << "Loaded camera " << cameraNumber << "." << endl;
}


/** @brief: Keypress event handler. Note that it should be a 'char' and not an 'int' to better support Linux. 
*/
int onKeypress( char key, 
                bool& m_sketchMode, 
                bool& m_alienMode, 
                bool& m_evilMode, 
                bool& m_debugMode,
                bool& m_flipped,
                bool& m_mirror)
{
    switch (key) {
    case 's':
        m_sketchMode = !m_sketchMode;
        cout << "Sketch / Paint mode: " << m_sketchMode << endl;
        break;
    case 'a':
        m_alienMode = !m_alienMode;
        cout << "Alien / Human mode: " << m_alienMode << endl;
        // Display a stick figure outline when alien skin is enabled,
        // so the user puts their face in the correct place.
        if (m_alienMode) {
            return NUM_STICK_FIGURE_ITERATIONS;
        }
        break;
    case 'e':
        m_evilMode = !m_evilMode;
        cout << "Evil / Good mode: " << m_evilMode << endl;
        break;
    case 'd':
        m_debugMode = !m_debugMode;
        cout << "Debug mode: " << m_debugMode << endl;
        break;
    case 'f':
        m_flipped = !m_flipped;
        cout << "Flipped / Normal mode: " << m_flipped << endl;
        break;
    case 'm':
        m_mirror = !m_mirror;
        cout << "Mirror / Normal mode: " << m_mirror << endl;
        break;
    }
    return 0;
}


int main(int argc, char *argv[])
{
    cout << "Carrton, by Luis Parra (www.shervinemami.info), June 2014." << endl;
    cout << "Converts real-life images to cartoon-like images." << endl;
    cout << "Compiled with OpenCV version " << CV_VERSION << endl;
    cout << endl;

    cout << "Keyboard commands (press in the GUI window):" << endl;
    cout << "    Esc:  Quit the program." << endl;
    cout << "    s:    change Sketch / Paint mode." << endl;
    cout << "    a:    change Alien / Human mode." << endl;
    cout << "    e:    change Evil / Good character mode." << endl;
    cout << "    d:    change debug mode." << endl;
    cout << "    f:    change flipped mode." << endl;
    cout << "    m:    change mirror mode." << endl;
    cout << endl;


    // Set to true if you want to see line drawings instead of paintings.
    bool m_sketchMode = false;
    // Set to true if you want to change the skin color of the character to an alien color.
    bool m_alienMode = false;
    // Set to true if you want an evil "bad" character instead of a "good" character.
    bool m_evilMode = false;
    // Set to true if you want to see many windows created, showing various debug info. Set to 0 otherwise.
    bool m_debugMode = false;
    // Set to true if you want to flip the image!
    bool m_flipped = false;
    // Set to true if you want to mirror the image!
    bool m_mirror = false;

    // Allow the user to specify a camera number, since not all computers will be the same camera number.
    int cameraNumber = 0;   // Change this if you want to use a different camera device.
    if (argc > 1) {
        cameraNumber = atoi(argv[1]);
    }

    // Get access to the camera.
    VideoCapture camera;
    initWebcam(camera, cameraNumber);

    // Try to set the camera resolution. Note that this only works for some cameras on
    // some computers and only for some drivers, so don't rely on it to work!
    camera.set(CV_CAP_PROP_FRAME_WIDTH, DESIRED_CAMERA_WIDTH);
    camera.set(CV_CAP_PROP_FRAME_HEIGHT, DESIRED_CAMERA_HEIGHT);

    // Create a GUI window for display on the screen.
    namedWindow(windowName); // Resizable window, might not work on Windows.

    // Run forever, until the user hits Escape to "break" out of this loop.

    int m_stickFigureIterations =  0;

    while (true) {

        // Grab the next camera frame. Note that you can't modify camera frames.
        Mat cameraFrame;
        camera >> cameraFrame;
        if( cameraFrame.empty() ) {
            cerr << "ERROR: Couldn't grab the next camera frame." << endl;
            exit(1);
        }

        Mat displayedFrame = Mat(cameraFrame.size(), CV_8UC3);

        // Use debug type 2 (for desktop) if debug mode is enabled.
        int debugType = 0;
        if (m_debugMode)
            debugType = 2;

        // Run the cartoonifier filter using the selected mode.
        cartoonifyImage(cameraFrame, displayedFrame, debugType, m_sketchMode, m_alienMode, m_evilMode, m_flipped, 
                            m_mirror);

        // Show a stick-figure outline of a face for a short duration, so the user knows where to put their face.
        if (m_stickFigureIterations > 0) {
            drawFaceStickFigure(displayedFrame);
            m_stickFigureIterations--;
        }

        imshow(windowName, displayedFrame);

        // IMPORTANT: Wait for atleast 20 milliseconds, so that the image can be displayed on the screen!
        // Also checks if a key was pressed in the GUI window. Note that it should be a "char" to support Linux.
        char keypress = waitKey(5);  // This is needed if you want to see anything!
        if (keypress == VK_ESCAPE) {   // Escape Key
            // Quit the program!
            break;
        }
        // Process any other keypresses.
        if (keypress > 0) {
            m_stickFigureIterations = onKeypress(keypress, m_sketchMode, m_alienMode, m_evilMode, 
                                                    m_debugMode, m_flipped, m_mirror);
        }

    }//end while

    return EXIT_SUCCESS;
}
