#include "thresholddialog.h"
#include "ui_thresholddialog.h"

ThresholdDialog::ThresholdDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::ThresholdDialog){
    ui->setupUi(this);
}

ThresholdDialog::~ThresholdDialog()
{
    delete ui;
}

int ThresholdDialog::getMinSlider(){
    return ui->minSlider->value();
}

int ThresholdDialog::getMaxSlider(){
    return ui->maxSlider->value();
}

int ThresholdDialog::getMaxCorners(){
    return ui->sliderCorners->value();
}

int ThresholdDialog::getHessian(){
    return ui->sliderHessian->value();
}
