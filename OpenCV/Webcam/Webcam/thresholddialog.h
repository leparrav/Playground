#ifndef THRESHOLDDIALOG_H
#define THRESHOLDDIALOG_H

#include <QDialog>

namespace Ui {
class ThresholdDialog;
}

class ThresholdDialog : public QDialog
{
    Q_OBJECT

public:
    explicit ThresholdDialog(QWidget *parent = 0);
    ~ThresholdDialog();
    int getMinSlider();
    int getMaxSlider();
    int getMaxCorners();
    int getHessian();

private:
    Ui::ThresholdDialog *ui;
};

#endif // THRESHOLDDIALOG_H
