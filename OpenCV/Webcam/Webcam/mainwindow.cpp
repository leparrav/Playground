#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow){
    // Setup UI
    ui->setupUi(this);



    // Initiate variables
    camOpenResult = false;


    // Connect signals and slots
    connect(ui->actionStart,SIGNAL(triggered()),this, SLOT(connectToCamera()));
    //connect(ui->actionCanny,SIGNAL(triggered()),this,SLOT(updateDisplay()));
}

MainWindow::~MainWindow(){
    delete ui;
}

void MainWindow::connectToCamera(){

    // Suposse there is only one camera
    int deviceNumber = 0;

    // We cannot connect to a camera if devices are already connected
    if(camOpenResult) {
        // Alert user to disconnect camera
        QMessageBox::warning(this,  tr("Webcam"),
                                    tr("Webcam already started, disconnect it first"),
                                    QMessageBox::Ok);
    }
    // Open camera
    else {
        camOpenResult = cap.open(deviceNumber);
        if (!cap.isOpened()){
            QMessageBox::warning(this,tr("Webcam"),tr("Coudn't open webcam"),QMessageBox::Ok);
        }
        else {
            // Start timer
            timer = new QTimer(this);
            connect(timer, SIGNAL(timeout()), this, SLOT(updateDisplay()));
            timer->start(10);
        }
    }
}

void MainWindow::updateDisplay(){
    // Read frame from Video Capture
    Mat frame;
    bool bSuccess = cap.read(frame);
    if (!bSuccess) {
        QMessageBox::warning(this,tr("Webcam"),tr("Can't read frame from video"),QMessageBox::Ok);
    }
    // We have our video as cv::Mat change it to QImage
    else {
        QImage current = this->putImage(frame);
        ui->lvideoDisplay->setPixmap(QPixmap::fromImage(current));
    }
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
