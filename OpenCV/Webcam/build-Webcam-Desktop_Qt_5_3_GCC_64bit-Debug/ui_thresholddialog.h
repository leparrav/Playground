/********************************************************************************
** Form generated from reading UI file 'thresholddialog.ui'
**
** Created by: Qt User Interface Compiler version 5.3.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_THRESHOLDDIALOG_H
#define UI_THRESHOLDDIALOG_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QDialog>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QSlider>
#include <QtWidgets/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_ThresholdDialog
{
public:
    QGridLayout *gridLayout;
    QVBoxLayout *verticalLayout_2;
    QSlider *minSlider;
    QSlider *maxSlider;
    QSlider *sliderCorners;
    QSlider *sliderHessian;
    QHBoxLayout *horizontalLayout;
    QVBoxLayout *verticalLayout;
    QLabel *label_2;
    QLabel *label;
    QLabel *label_3;
    QLabel *label_4;

    void setupUi(QDialog *ThresholdDialog)
    {
        if (ThresholdDialog->objectName().isEmpty())
            ThresholdDialog->setObjectName(QStringLiteral("ThresholdDialog"));
        ThresholdDialog->resize(500, 200);
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(ThresholdDialog->sizePolicy().hasHeightForWidth());
        ThresholdDialog->setSizePolicy(sizePolicy);
        ThresholdDialog->setMinimumSize(QSize(500, 200));
        ThresholdDialog->setMaximumSize(QSize(500, 200));
        gridLayout = new QGridLayout(ThresholdDialog);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        verticalLayout_2 = new QVBoxLayout();
        verticalLayout_2->setObjectName(QStringLiteral("verticalLayout_2"));
        minSlider = new QSlider(ThresholdDialog);
        minSlider->setObjectName(QStringLiteral("minSlider"));
        minSlider->setMaximum(100);
        minSlider->setValue(25);
        minSlider->setOrientation(Qt::Horizontal);

        verticalLayout_2->addWidget(minSlider);

        maxSlider = new QSlider(ThresholdDialog);
        maxSlider->setObjectName(QStringLiteral("maxSlider"));
        maxSlider->setMinimum(0);
        maxSlider->setMaximum(100);
        maxSlider->setValue(75);
        maxSlider->setOrientation(Qt::Horizontal);

        verticalLayout_2->addWidget(maxSlider);

        sliderCorners = new QSlider(ThresholdDialog);
        sliderCorners->setObjectName(QStringLiteral("sliderCorners"));
        sliderCorners->setMinimum(1);
        sliderCorners->setMaximum(100);
        sliderCorners->setValue(20);
        sliderCorners->setOrientation(Qt::Horizontal);

        verticalLayout_2->addWidget(sliderCorners);

        sliderHessian = new QSlider(ThresholdDialog);
        sliderHessian->setObjectName(QStringLiteral("sliderHessian"));
        sliderHessian->setMinimum(100);
        sliderHessian->setMaximum(5000);
        sliderHessian->setOrientation(Qt::Horizontal);

        verticalLayout_2->addWidget(sliderHessian);


        gridLayout->addLayout(verticalLayout_2, 1, 3, 1, 1);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        verticalLayout = new QVBoxLayout();
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        label_2 = new QLabel(ThresholdDialog);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setScaledContents(false);

        verticalLayout->addWidget(label_2);

        label = new QLabel(ThresholdDialog);
        label->setObjectName(QStringLiteral("label"));

        verticalLayout->addWidget(label);

        label_3 = new QLabel(ThresholdDialog);
        label_3->setObjectName(QStringLiteral("label_3"));

        verticalLayout->addWidget(label_3);

        label_4 = new QLabel(ThresholdDialog);
        label_4->setObjectName(QStringLiteral("label_4"));

        verticalLayout->addWidget(label_4);


        horizontalLayout->addLayout(verticalLayout);


        gridLayout->addLayout(horizontalLayout, 1, 0, 1, 1);


        retranslateUi(ThresholdDialog);

        QMetaObject::connectSlotsByName(ThresholdDialog);
    } // setupUi

    void retranslateUi(QDialog *ThresholdDialog)
    {
        ThresholdDialog->setWindowTitle(QApplication::translate("ThresholdDialog", "Parameters", 0));
        label_2->setText(QApplication::translate("ThresholdDialog", "Minimum threshold", 0));
        label->setText(QApplication::translate("ThresholdDialog", "Maximum threshold", 0));
        label_3->setText(QApplication::translate("ThresholdDialog", "Number of corners / keypoints", 0));
        label_4->setText(QApplication::translate("ThresholdDialog", "Hessian Threshold (SURF)", 0));
    } // retranslateUi

};

namespace Ui {
    class ThresholdDialog: public Ui_ThresholdDialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_THRESHOLDDIALOG_H
