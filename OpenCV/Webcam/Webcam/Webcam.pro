#-------------------------------------------------
#
# Project created by QtCreator 2014-06-28T18:59:44
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = Webcam
TEMPLATE = app
LIBS += `pkg-config opencv --libs`


SOURCES += main.cpp\
        mainwindow.cpp \
    thresholddialog.cpp

HEADERS  += mainwindow.h \
    thresholddialog.h

FORMS    += mainwindow.ui \
    thresholddialog.ui

OTHER_FILES += \
    LICENSE.txt \
    README.md
