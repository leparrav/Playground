#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow){
    // Setup UI
    ui->setupUi(this);

    // Initiate variables
    camOpenResult = false;
    modify = 0;

    // Connect signals and slots
    connect(ui->actionStart,SIGNAL(triggered()),this, SLOT(connectToCamera()));
}

MainWindow::~MainWindow(){
    delete ui;
}

void MainWindow::connectToCamera(){

    // Suposse there is only one camera
    int deviceNumber = 0;

    // We cannot connect to a camera if devices are already connected
    if(camOpenResult) {
        // Alert user to disconnect camera first
        QMessageBox::warning(this,  tr("Webcam"),
                                    tr("Webcam already started, disconnect it first"),
                                    QMessageBox::Ok);
    }
    // Else - Open camera
    else {
        camOpenResult = cap.open(deviceNumber);
        if (!cap.isOpened()){
            QMessageBox::warning(this,tr("Webcam"),tr("Coudn't open webcam"),QMessageBox::Ok);
        }
        else {
            // Start timer to update Display
            timer = new QTimer(this);
            connect(timer, SIGNAL(timeout()), this, SLOT(updateDisplay()));
            timer->start(10);
        }
    }
}

void MainWindow::updateDisplay(){
    Mat frame;
    bool bSuccess = cap.read(frame); // Read frame from Video Captureframe
    if (!bSuccess) {
        QMessageBox::warning(this,tr("Webcam"),tr("Can't read frame from video"),QMessageBox::Ok);
    }
    // We have our video as cv::Mat change it to QImage
    else {
        // Modify frame if a modification was asked (Depending on modification might slow down display)
        if (modify != 0) {
           frame = modifyImage(frame);
        }
        QImage current = putImage(frame); // Change from Mat to QImage
        ui->lvideoDisplay->setPixmap(QPixmap::fromImage(current)); // Show in Label
    }
}

Mat MainWindow::modifyImage(Mat& src){
    Mat src_gray, detected_edges;
    int kernel_size = 3;

    /// Convert the image to grayscale
    cvtColor( src, src_gray, CV_BGR2GRAY );

    switch(modify){
        case 1:
        /// Canny detector
        Canny( src_gray, detected_edges, 30, 120, kernel_size );
        return detected_edges;
        case 2:
        break;
    }

    return src_gray;
}


QImage MainWindow::putImage(const Mat& mat){
    // 8-bits unsigned, NO. OF CHANNELS=1
    if(mat.type()==CV_8UC1){
        // Set the color table (used to translate colour indexes to qRgb values)
        QVector<QRgb> colorTable;
        for (int i=0; i<256; i++)
            colorTable.push_back(qRgb(i,i,i));
        // Copy input Mat
        const uchar *qImageBuffer = (const uchar*)mat.data;
        // Create QImage with same dimensions as input Mat
        QImage img(qImageBuffer, mat.cols, mat.rows, mat.step, QImage::Format_Indexed8);
        img.setColorTable(colorTable);
        return img;
    }

    // 8-bits unsigned, NO. OF CHANNELS=3
    if(mat.type()==CV_8UC3){
        // Copy input Mat
        const uchar *qImageBuffer = (const uchar*)mat.data;
        // Create QImage with same dimensions as input Mat
        QImage img(qImageBuffer, mat.cols, mat.rows, mat.step, QImage::Format_RGB888);
        return img.rgbSwapped();
    }
    else {
        qDebug() << "ERROR: Mat could not be converted to QImage.";
        return QImage();
    }
}

void MainWindow::on_actionCanny_triggered(){
    if (modify != 0){
        QMessageBox::warning(this,tr("Webcam"),tr("Clear image before changing it"),QMessageBox::Ok);
        return;
    }
        modify = 1;
}

void MainWindow::on_actionClear_modifications_triggered(){
    modify = 0;
}
