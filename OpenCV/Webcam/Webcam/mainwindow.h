/** \file mainwindow.h
 * Simple Qt Application that shows and Image in a QLabel
 * Created by: Luis Parra - 26/06/2014
 * PutImage Method from -> qt-opencv-multithreaded:  2012-2013 Nick D'Ademo
 */

#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QDebug>
#include <QMessageBox>
#include <QTimer>
#include <QString>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>

#include "imagemodifier.h"

using namespace cv;

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow{
    Q_OBJECT

    public:
        explicit MainWindow(QWidget *parent = 0);
        ~MainWindow();

    private:
        Ui::MainWindow *ui;
        VideoCapture cap;
        bool camOpenResult;
        QTimer *timer;
        int modify; // Private attribute that tells how image should be modified.
        ImageModifier *imgMod;

        /** @brief Convert a OpenCV Mat Image to a QImage, it doesn't change original image
        */
        QImage putImage(const Mat& mat);

        /** @brief This method gets a Frame and modifies it according to especified
         *  @param mat Pointer to the current frame
        */
        Mat modifyImage(Mat& mat);

    private slots:
        /** @brief Slot to button start signal - connect to OpenCV Webcam
        */
        void connectToCamera();

        /** @brief Slot for timer to update display from a given frame
        */
        void updateDisplay();
        void on_actionCanny_triggered();
        void on_actionClear_modifications_triggered();
        void on_actionSobel_triggered();
        void on_actionScharr_triggered();
        void on_actionMorphological_Gradient_triggered();
        void on_actionLaplace_triggered();
};

#endif // MAINWINDOW_H
