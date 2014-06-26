#-------------------------------------------------
#
# Project created by QtCreator 2014-06-26T18:44:22
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = Webcam
TEMPLATE = app

# OPENCV INCLUDE
LIBS += `pkg-config opencv --libs`

SOURCES += main.cpp\
        mainwindow.cpp

HEADERS  += mainwindow.h

FORMS    += mainwindow.ui
