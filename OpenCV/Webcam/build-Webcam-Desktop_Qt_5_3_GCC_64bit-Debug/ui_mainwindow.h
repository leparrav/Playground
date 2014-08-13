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
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QVBoxLayout>
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
    QAction *actionSIFT_2;
    QAction *actionSURFT;
    QAction *actionOptical_Flow;
    QAction *actionBackground_substract;
    QAction *actionFeature_matching;
    QAction *actionFace;
    QAction *actionEyes;
    QAction *actionObject;
    QWidget *centralWidget;
    QVBoxLayout *verticalLayout;
    QLabel *lvideoDisplay;
    QMenuBar *menuBar;
    QMenu *menuCamera;
    QMenu *menuFunctions;
    QMenu *menuDescriptors;
    QMenu *menuDescriptors_2;
    QMenu *menuMotion;
    QMenu *menuDetect;
    QToolBar *mainToolBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(528, 348);
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
        actionSIFT_2 = new QAction(MainWindow);
        actionSIFT_2->setObjectName(QStringLiteral("actionSIFT_2"));
        actionSURFT = new QAction(MainWindow);
        actionSURFT->setObjectName(QStringLiteral("actionSURFT"));
        actionOptical_Flow = new QAction(MainWindow);
        actionOptical_Flow->setObjectName(QStringLiteral("actionOptical_Flow"));
        actionBackground_substract = new QAction(MainWindow);
        actionBackground_substract->setObjectName(QStringLiteral("actionBackground_substract"));
        actionFeature_matching = new QAction(MainWindow);
        actionFeature_matching->setObjectName(QStringLiteral("actionFeature_matching"));
        actionFace = new QAction(MainWindow);
        actionFace->setObjectName(QStringLiteral("actionFace"));
        actionEyes = new QAction(MainWindow);
        actionEyes->setObjectName(QStringLiteral("actionEyes"));
        actionObject = new QAction(MainWindow);
        actionObject->setObjectName(QStringLiteral("actionObject"));
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        verticalLayout = new QVBoxLayout(centralWidget);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        lvideoDisplay = new QLabel(centralWidget);
        lvideoDisplay->setObjectName(QStringLiteral("lvideoDisplay"));

        verticalLayout->addWidget(lvideoDisplay);

        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 528, 25));
        menuCamera = new QMenu(menuBar);
        menuCamera->setObjectName(QStringLiteral("menuCamera"));
        menuFunctions = new QMenu(menuBar);
        menuFunctions->setObjectName(QStringLiteral("menuFunctions"));
        menuDescriptors = new QMenu(menuBar);
        menuDescriptors->setObjectName(QStringLiteral("menuDescriptors"));
        menuDescriptors_2 = new QMenu(menuBar);
        menuDescriptors_2->setObjectName(QStringLiteral("menuDescriptors_2"));
        menuMotion = new QMenu(menuBar);
        menuMotion->setObjectName(QStringLiteral("menuMotion"));
        menuDetect = new QMenu(menuBar);
        menuDetect->setObjectName(QStringLiteral("menuDetect"));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);

        menuBar->addAction(menuCamera->menuAction());
        menuBar->addAction(menuFunctions->menuAction());
        menuBar->addAction(menuDescriptors->menuAction());
        menuBar->addAction(menuDescriptors_2->menuAction());
        menuBar->addAction(menuMotion->menuAction());
        menuBar->addAction(menuDetect->menuAction());
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
        menuDescriptors_2->addAction(actionSIFT_2);
        menuDescriptors_2->addAction(actionSURFT);
        menuMotion->addAction(actionOptical_Flow);
        menuMotion->addAction(actionBackground_substract);
        menuMotion->addAction(actionFeature_matching);
        menuDetect->addAction(actionFace);
        menuDetect->addAction(actionEyes);
        menuDetect->addAction(actionObject);

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
        actionSIFT_2->setText(QApplication::translate("MainWindow", "SIFT", 0));
        actionSURFT->setText(QApplication::translate("MainWindow", "SURF", 0));
        actionOptical_Flow->setText(QApplication::translate("MainWindow", "Optical Flow", 0));
        actionBackground_substract->setText(QApplication::translate("MainWindow", "Background substract", 0));
        actionFeature_matching->setText(QApplication::translate("MainWindow", "Feature matching", 0));
        actionFace->setText(QApplication::translate("MainWindow", "Face", 0));
        actionEyes->setText(QApplication::translate("MainWindow", "Eyes", 0));
        actionObject->setText(QApplication::translate("MainWindow", "Object", 0));
        lvideoDisplay->setText(QString());
        menuCamera->setTitle(QApplication::translate("MainWindow", "Camera", 0));
        menuFunctions->setTitle(QApplication::translate("MainWindow", "Edges", 0));
        menuDescriptors->setTitle(QApplication::translate("MainWindow", "Corners", 0));
        menuDescriptors_2->setTitle(QApplication::translate("MainWindow", "Descriptors", 0));
        menuMotion->setTitle(QApplication::translate("MainWindow", "Motion", 0));
        menuDetect->setTitle(QApplication::translate("MainWindow", "Detect", 0));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
