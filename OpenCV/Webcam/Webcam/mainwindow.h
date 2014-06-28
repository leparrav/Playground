/******************************************************************************
 * Simple Qt Application that shows and Image in a QLabel
 * Created by: Luis Parra - 26/06/2014
 * PutImage Method from -> qt-opencv-multithreaded:  2012-2013 Nick D'Ademo
 *
 *
 *
 * ****************************************************************************/

#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QDebug>
#include <QMessageBox>
#include <QTimer>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>

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

        /** @brief Convert a OpenCV Mat Image to a QImage, it doesn't change original image
        */
        QImage putImage(const Mat& mat);

    private slots:
        /** @brief Slot to button start signal - connect to OpenCV Webcam
        */
        void connectToCamera();

        /** @brief Slot for timer to update display from a given frame
        */
        void updateDisplay();
};

#endif // MAINWINDOW_H
