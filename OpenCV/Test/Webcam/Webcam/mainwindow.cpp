#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <QDebug>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_btnDisplay_clicked(){
    cv::Mat matInput = cv::imread("LP.jpg");
    if( matInput.empty()){
         qDebug() << "Can't load image";
         return;
    }
    cv::namedWindow("Show");
    cv::imshow("Show", matInput);
    cv::waitKey();
}
