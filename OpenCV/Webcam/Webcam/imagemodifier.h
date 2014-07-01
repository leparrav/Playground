#ifndef IMAGEMODIFIER_H
#define IMAGEMODIFIER_H

#include <QObject>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>

using namespace cv;

class ImageModifier : public QObject{
    Q_OBJECT

private:
    int kernel;

public:
    explicit ImageModifier(QObject *parent = 0);
    Mat edgeLaplace(Mat& src);
    Mat edgeCanny(Mat& src);
    Mat edgeSobel(Mat& src);
    Mat edgeScharr(Mat& src);
    Mat edgeMorph(Mat& src);

signals:

public slots:

};

#endif // IMAGEMODIFIER_H
