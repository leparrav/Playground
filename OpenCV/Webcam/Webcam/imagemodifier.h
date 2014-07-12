/** \file imagemodifier.h
 *  @author Luis Parra
 *  @brief This class handles all modifications done to a current frame
 */

#ifndef IMAGEMODIFIER_H
#define IMAGEMODIFIER_H

#include <QObject>
#include <QDebug>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/nonfree/nonfree.hpp>

using namespace cv;

class ImageModifier : public QObject{
    Q_OBJECT

private:
    int kernel;

public:
    explicit ImageModifier(QObject *parent = 0);
    Mat edgeLaplace(Mat& src, int sliderMin, int sliderMax);

    /** @brief Return a Edge Mat
     * The slider values are always between 0-100, so they must be converted to a format **/
    Mat edgeCanny(Mat& src, int sliderMin,  int sliderMax);
    Mat edgeSobel(Mat& src, int sliderMin, int sliderMax);
    Mat edgeScharr(Mat& src, int sliderMin, int sliderMax);
    Mat edgeMorph(Mat& src);
    Mat corHarris(Mat& src, int maxCorners, int sliderMax);
    Mat corShi(Mat& src, int maxCorners);
    Mat Sift(Mat& src, int sliderCorners);
    Mat doSurf(Mat& src, int sliderCorners);

signals:

public slots:

};

#endif // IMAGEMODIFIER_H
