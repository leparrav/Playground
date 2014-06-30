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
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_ThresholdDialog
{
public:
    QGridLayout *gridLayout;
    QVBoxLayout *verticalLayout;
    QLineEdit *lineEdit;
    QPushButton *pushButton;

    void setupUi(QDialog *ThresholdDialog)
    {
        if (ThresholdDialog->objectName().isEmpty())
            ThresholdDialog->setObjectName(QStringLiteral("ThresholdDialog"));
        ThresholdDialog->resize(300, 300);
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(ThresholdDialog->sizePolicy().hasHeightForWidth());
        ThresholdDialog->setSizePolicy(sizePolicy);
        ThresholdDialog->setMinimumSize(QSize(300, 300));
        ThresholdDialog->setMaximumSize(QSize(300, 300));
        gridLayout = new QGridLayout(ThresholdDialog);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        verticalLayout = new QVBoxLayout();
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        lineEdit = new QLineEdit(ThresholdDialog);
        lineEdit->setObjectName(QStringLiteral("lineEdit"));

        verticalLayout->addWidget(lineEdit);

        pushButton = new QPushButton(ThresholdDialog);
        pushButton->setObjectName(QStringLiteral("pushButton"));

        verticalLayout->addWidget(pushButton);


        gridLayout->addLayout(verticalLayout, 0, 0, 1, 1);


        retranslateUi(ThresholdDialog);

        QMetaObject::connectSlotsByName(ThresholdDialog);
    } // setupUi

    void retranslateUi(QDialog *ThresholdDialog)
    {
        ThresholdDialog->setWindowTitle(QApplication::translate("ThresholdDialog", "Dialog", 0));
        pushButton->setText(QApplication::translate("ThresholdDialog", "PushButton", 0));
    } // retranslateUi

};

namespace Ui {
    class ThresholdDialog: public Ui_ThresholdDialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_THRESHOLDDIALOG_H
