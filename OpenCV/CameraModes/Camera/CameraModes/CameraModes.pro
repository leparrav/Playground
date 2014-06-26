#-------------------------------------------------
#
# Project created by QtCreator 2014-06-26T12:03:15
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = CameraModes
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    ../../CartoonCamera/Cartoonifier_Desktop/cartoon.cpp \
    ../../CartoonCamera/Cartoonifier_Desktop/ImageUtils_0.7.cpp

HEADERS  += mainwindow.h

FORMS    += mainwindow.ui

CONFIG += mobility
MOBILITY = 

