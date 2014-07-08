/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.3.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionStart;
    QAction *actionCanny;
    QAction *actionSobel;
    QAction *actionHarris;
    QAction *actionSIFT;
    QAction *actionSURF;
    QAction *actionStop;
    QAction *actionClear_modifications;
    QAction *actionMorphological_Gradient;
    QAction *actionScharr;
    QAction *actionLaplace;
    QWidget *centralWidget;
    QGridLayout *gridLayout;
    QLabel *lvideoDisplay;
    QMenuBar *menuBar;
    QMenu *menuCamera;
    QMenu *menuFunctions;
    QMenu *menuDescriptors;
    QToolBar *mainToolBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(400, 300);
        actionStart = new QAction(MainWindow);
        actionStart->setObjectName(QStringLiteral("actionStart"));
        actionCanny = new QAction(MainWindow);
        actionCanny->setObjectName(QStringLiteral("actionCanny"));
        actionSobel = new QAction(MainWindow);
        actionSobel->setObjectName(QStringLiteral("actionSobel"));
        actionHarris = new QAction(MainWindow);
        actionHarris->setObjectName(QStringLiteral("actionHarris"));
        actionSIFT = new QAction(MainWindow);
        actionSIFT->setObjectName(QStringLiteral("actionSIFT"));
        actionSURF = new QAction(MainWindow);
        actionSURF->setObjectName(QStringLiteral("actionSURF"));
        actionStop = new QAction(MainWindow);
        actionStop->setObjectName(QStringLiteral("actionStop"));
        actionClear_modifications = new QAction(MainWindow);
        actionClear_modifications->setObjectName(QStringLiteral("actionClear_modifications"));
        actionMorphological_Gradient = new QAction(MainWindow);
        actionMorphological_Gradient->setObjectName(QStringLiteral("actionMorphological_Gradient"));
        actionScharr = new QAction(MainWindow);
        actionScharr->setObjectName(QStringLiteral("actionScharr"));
        actionLaplace = new QAction(MainWindow);
        actionLaplace->setObjectName(QStringLiteral("actionLaplace"));
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        gridLayout = new QGridLayout(centralWidget);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        lvideoDisplay = new QLabel(centralWidget);
        lvideoDisplay->setObjectName(QStringLiteral("lvideoDisplay"));

        gridLayout->addWidget(lvideoDisplay, 0, 0, 1, 1);

        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 400, 25));
        menuCamera = new QMenu(menuBar);
        menuCamera->setObjectName(QStringLiteral("menuCamera"));
        menuFunctions = new QMenu(menuBar);
        menuFunctions->setObjectName(QStringLiteral("menuFunctions"));
        menuDescriptors = new QMenu(menuBar);
        menuDescriptors->setObjectName(QStringLiteral("menuDescriptors"));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);

        menuBar->addAction(menuCamera->menuAction());
        menuBar->addAction(menuFunctions->menuAction());
        menuBar->addAction(menuDescriptors->menuAction());
        menuCamera->addAction(actionStart);
        menuCamera->addAction(actionStop);
        menuCamera->addAction(actionClear_modifications);
        menuFunctions->addAction(actionCanny);
        menuFunctions->addAction(actionSobel);
        menuFunctions->addAction(actionScharr);
        menuFunctions->addAction(actionMorphological_Gradient);
        menuFunctions->addAction(actionLaplace);
        menuDescriptors->addAction(actionHarris);
        menuDescriptors->addAction(actionSIFT);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "Webcam OpenCV", 0));
        actionStart->setText(QApplication::translate("MainWindow", "Start", 0));
        actionCanny->setText(QApplication::translate("MainWindow", "Canny", 0));
        actionSobel->setText(QApplication::translate("MainWindow", "Sobel", 0));
        actionHarris->setText(QApplication::translate("MainWindow", "Harris", 0));
        actionSIFT->setText(QApplication::translate("MainWindow", "Shi-tomasi", 0));
        actionSURF->setText(QApplication::translate("MainWindow", "SURF", 0));
        actionStop->setText(QApplication::translate("MainWindow", "Stop", 0));
        actionClear_modifications->setText(QApplication::translate("MainWindow", "Clear", 0));
        actionMorphological_Gradient->setText(QApplication::translate("MainWindow", "Morphological Gradient", 0));
        actionScharr->setText(QApplication::translate("MainWindow", "Scharr", 0));
        actionLaplace->setText(QApplication::translate("MainWindow", "Laplace", 0));
        lvideoDisplay->setText(QString());
        menuCamera->setTitle(QApplication::translate("MainWindow", "Camera", 0));
        menuFunctions->setTitle(QApplication::translate("MainWindow", "Edges", 0));
        menuDescriptors->setTitle(QApplication::translate("MainWindow", "Corners", 0));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
