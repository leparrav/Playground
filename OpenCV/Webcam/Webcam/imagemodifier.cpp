#include "imagemodifier.h"

ImageModifier::ImageModifier(QObject *parent) :
    QObject(parent){

}

Mat ImageModifier::edgeCanny(Mat &src){
    // Data Initialization for Canny
    Mat src_gray, canny_edges;
    int kernel_size = 3;

    /// Convert the image to grayscale
    cvtColor( src, src_gray, CV_BGR2GRAY );

    /// Canny detector
    Canny( src_gray, canny_edges, 30, 120, kernel_size );
    return canny_edges;
}

Mat ImageModifier::edgeLaplace(Mat &src){
    Mat src_gray, dst;
    int kernel_size = 3;
    int scale = 1;
    int delta = 0;
    int ddepth = CV_8UC1;

    cvtColor( src, src_gray, CV_BGR2GRAY );     /// Convert the image to grayscale
    GaussianBlur( src_gray, src_gray, Size(3,3), 0, 0, BORDER_DEFAULT );
    Laplacian( src_gray, dst, ddepth, kernel_size, scale, delta, BORDER_DEFAULT );


    return dst;
}

Mat ImageModifier::edgeMorph(Mat &src){
    Mat result, src_gray;
    cvtColor( src, src_gray, CV_BGR2GRAY );     /// Convert the image to grayscale
    morphologyEx(src_gray,result,MORPH_GRADIENT,Mat());
    return result;
}

Mat ImageModifier::edgeScharr(Mat &src){
    /// Data Initialization for Sobel and Scharr
    Mat grad_x, grad_y, grad,src_gray;
    Mat abs_grad_x, abs_grad_y;
    int scale = 1;
    int delta = 0;
    int ddepth = CV_16UC1;

    /// Convert the image to grayscale
    cvtColor( src, src_gray, CV_BGR2GRAY );

    /// Gradient X
    Scharr( src_gray, grad_x, ddepth, 1, 0, scale, delta, BORDER_DEFAULT );
    convertScaleAbs( grad_x, abs_grad_x );

    /// Gradient Y
    Scharr( src_gray, grad_y, ddepth, 0, 1, scale, delta, BORDER_DEFAULT );
    convertScaleAbs( grad_y, abs_grad_y );

    /// Total Gradient (approximate)
    addWeighted( abs_grad_x, 0.5, abs_grad_y, 0.5, 0, grad );
    return grad;
}

Mat ImageModifier::edgeSobel(Mat &src){
    /// Data Initialization for Sobel and Scharr
    Mat grad_x, grad_y, grad,src_gray;
    Mat abs_grad_x, abs_grad_y;
    int scale = 1;
    int delta = 0;
    int ddepth = CV_16UC1;

    /// Convert the image to grayscale
    cvtColor( src, src_gray, CV_BGR2GRAY );

    /// Gradient X
    Sobel( src_gray, grad_x, ddepth, 1, 0, 3, scale, delta, BORDER_DEFAULT );
    convertScaleAbs( grad_x, abs_grad_x );

    /// Gradient Y
    Sobel( src_gray, grad_y, ddepth, 0, 1, 3, scale, delta, BORDER_DEFAULT );
    convertScaleAbs( grad_y, abs_grad_y );

    /// Total Gradient (approximate)
    addWeighted( abs_grad_x, 0.5, abs_grad_y, 0.5, 0, grad );
    return grad;
}
