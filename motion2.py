# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'motion.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from API import motors
import _thread, time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 647))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 800, 560))
        self.stackedWidget.setMinimumSize(QtCore.QSize(800, 560))
        self.stackedWidget.setMaximumSize(QtCore.QSize(800, 560))
        self.stackedWidget.setObjectName("stackedWidget")
        self.mainPage = QtWidgets.QWidget()
        self.mainPage.setMinimumSize(QtCore.QSize(800, 600))
        self.mainPage.setMaximumSize(QtCore.QSize(800, 600))
        self.mainPage.setObjectName("mainPage")
        self.mPageMFrame = QtWidgets.QFrame(self.mainPage)
        self.mPageMFrame.setGeometry(QtCore.QRect(10, 20, 541, 531))
        self.mPageMFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.mPageMFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mPageMFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mPageMFrame.setObjectName("mPageMFrame")
        self.mId = QtWidgets.QLabel(self.mPageMFrame)
        self.mId.setGeometry(QtCore.QRect(30, 20, 31, 21))
        self.mId.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"")
        self.mId.setObjectName("mId")
        self.mAngle = QtWidgets.QLabel(self.mPageMFrame)
        self.mAngle.setGeometry(QtCore.QRect(90, 20, 61, 21))
        self.mAngle.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"\n"
"")
        self.mAngle.setObjectName("mAngle")
        self.mPos = QtWidgets.QLabel(self.mPageMFrame)
        self.mPos.setGeometry(QtCore.QRect(180, 20, 81, 21))
        self.mPos.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"\n"
"")
        self.mPos.setObjectName("mPos")
        self.m1Frame = QtWidgets.QFrame(self.mPageMFrame)
        self.m1Frame.setGeometry(QtCore.QRect(20, 50, 501, 31))
        self.m1Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m1Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m1Frame.setObjectName("m1Frame")
        self.m1 = QtWidgets.QLabel(self.m1Frame)
        self.m1.setGeometry(QtCore.QRect(10, 0, 16, 31))
        self.m1.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"")
        self.m1.setObjectName("m1")
        self.m1Ang = QtWidgets.QLabel(self.m1Frame)
        self.m1Ang.setGeometry(QtCore.QRect(70, 10, 51, 17))
        self.m1Ang.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m1Ang.setObjectName("m1Ang")
        self.m1Pos = QtWidgets.QLabel(self.m1Frame)
        self.m1Pos.setGeometry(QtCore.QRect(170, 10, 51, 17))
        self.m1Pos.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m1Pos.setObjectName("m1Pos")
        self.m10 = QtWidgets.QLabel(self.m1Frame)
        self.m10.setGeometry(QtCore.QRect(270, 0, 31, 31))
        self.m10.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"")
        self.m10.setObjectName("m10")
        self.m10Ang = QtWidgets.QLabel(self.m1Frame)
        self.m10Ang.setGeometry(QtCore.QRect(340, 10, 51, 17))
        self.m10Ang.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m10Ang.setObjectName("m10Ang")
        self.m10Pos = QtWidgets.QLabel(self.m1Frame)
        self.m10Pos.setGeometry(QtCore.QRect(430, 10, 51, 17))
        self.m10Pos.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m10Pos.setObjectName("m10Pos")
        self.m2Frame = QtWidgets.QFrame(self.mPageMFrame)
        self.m2Frame.setGeometry(QtCore.QRect(20, 100, 501, 31))
        self.m2Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m2Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m2Frame.setObjectName("m2Frame")
        self.m2 = QtWidgets.QLabel(self.m2Frame)
        self.m2.setGeometry(QtCore.QRect(10, 0, 16, 31))
        self.m2.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"")
        self.m2.setObjectName("m2")
        self.m2Ang = QtWidgets.QLabel(self.m2Frame)
        self.m2Ang.setGeometry(QtCore.QRect(70, 10, 51, 17))
        self.m2Ang.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m2Ang.setObjectName("m2Ang")
        self.label_4 = QtWidgets.QLabel(self.m2Frame)
        self.label_4.setGeometry(QtCore.QRect(250, 30, 51, 17))
        self.label_4.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.label_4.setObjectName("label_4")
        self.m2Pos = QtWidgets.QLabel(self.m2Frame)
        self.m2Pos.setGeometry(QtCore.QRect(170, 10, 51, 17))
        self.m2Pos.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m2Pos.setObjectName("m2Pos")
        self.m11 = QtWidgets.QLabel(self.m2Frame)
        self.m11.setGeometry(QtCore.QRect(270, 0, 21, 31))
        self.m11.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"")
        self.m11.setObjectName("m11")
        self.m11Pos = QtWidgets.QLabel(self.m2Frame)
        self.m11Pos.setGeometry(QtCore.QRect(430, 10, 51, 17))
        self.m11Pos.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m11Pos.setObjectName("m11Pos")
        self.m11Ang = QtWidgets.QLabel(self.m2Frame)
        self.m11Ang.setGeometry(QtCore.QRect(340, 10, 51, 17))
        self.m11Ang.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m11Ang.setObjectName("m11Ang")
        self.m3Frame = QtWidgets.QFrame(self.mPageMFrame)
        self.m3Frame.setGeometry(QtCore.QRect(20, 150, 501, 31))
        self.m3Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m3Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m3Frame.setObjectName("m3Frame")
        self.m3Ang = QtWidgets.QLabel(self.m3Frame)
        self.m3Ang.setGeometry(QtCore.QRect(70, 10, 51, 17))
        self.m3Ang.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m3Ang.setObjectName("m3Ang")
        self.m3Pos = QtWidgets.QLabel(self.m3Frame)
        self.m3Pos.setGeometry(QtCore.QRect(170, 10, 51, 17))
        self.m3Pos.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m3Pos.setObjectName("m3Pos")
        self.label_8 = QtWidgets.QLabel(self.m3Frame)
        self.label_8.setGeometry(QtCore.QRect(270, 50, 51, 17))
        self.label_8.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.label_8.setObjectName("label_8")
        self.m3 = QtWidgets.QLabel(self.m3Frame)
        self.m3.setGeometry(QtCore.QRect(10, 0, 21, 31))
        self.m3.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"")
        self.m3.setObjectName("m3")
        self.m12 = QtWidgets.QLabel(self.m3Frame)
        self.m12.setGeometry(QtCore.QRect(270, 0, 31, 31))
        self.m12.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"")
        self.m12.setObjectName("m12")
        self.m12Pos = QtWidgets.QLabel(self.m3Frame)
        self.m12Pos.setGeometry(QtCore.QRect(430, 10, 51, 17))
        self.m12Pos.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m12Pos.setObjectName("m12Pos")
        self.m12Ang = QtWidgets.QLabel(self.m3Frame)
        self.m12Ang.setGeometry(QtCore.QRect(340, 10, 51, 17))
        self.m12Ang.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m12Ang.setObjectName("m12Ang")
        self.m4Frame = QtWidgets.QFrame(self.mPageMFrame)
        self.m4Frame.setGeometry(QtCore.QRect(20, 200, 501, 31))
        self.m4Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m4Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m4Frame.setObjectName("m4Frame")
        self.m4Ang = QtWidgets.QLabel(self.m4Frame)
        self.m4Ang.setGeometry(QtCore.QRect(70, 10, 51, 17))
        self.m4Ang.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m4Ang.setObjectName("m4Ang")
        self.m4Pos = QtWidgets.QLabel(self.m4Frame)
        self.m4Pos.setGeometry(QtCore.QRect(170, 10, 51, 17))
        self.m4Pos.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m4Pos.setObjectName("m4Pos")
        self.m4 = QtWidgets.QLabel(self.m4Frame)
        self.m4.setGeometry(QtCore.QRect(10, 0, 21, 31))
        self.m4.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"")
        self.m4.setObjectName("m4")
        self.m13 = QtWidgets.QLabel(self.m4Frame)
        self.m13.setGeometry(QtCore.QRect(270, 0, 31, 31))
        self.m13.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"")
        self.m13.setObjectName("m13")
        self.m13Pos = QtWidgets.QLabel(self.m4Frame)
        self.m13Pos.setGeometry(QtCore.QRect(430, 10, 51, 17))
        self.m13Pos.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m13Pos.setObjectName("m13Pos")
        self.m13Ang = QtWidgets.QLabel(self.m4Frame)
        self.m13Ang.setGeometry(QtCore.QRect(340, 10, 51, 17))
        self.m13Ang.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m13Ang.setObjectName("m13Ang")
        self.m5Frame = QtWidgets.QFrame(self.mPageMFrame)
        self.m5Frame.setGeometry(QtCore.QRect(20, 250, 501, 31))
        self.m5Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m5Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m5Frame.setObjectName("m5Frame")
        self.m5 = QtWidgets.QLabel(self.m5Frame)
        self.m5.setGeometry(QtCore.QRect(10, 0, 16, 31))
        self.m5.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"")
        self.m5.setObjectName("m5")
        self.m5Ang = QtWidgets.QLabel(self.m5Frame)
        self.m5Ang.setGeometry(QtCore.QRect(70, 10, 51, 17))
        self.m5Ang.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m5Ang.setObjectName("m5Ang")
        self.m5Pos = QtWidgets.QLabel(self.m5Frame)
        self.m5Pos.setGeometry(QtCore.QRect(170, 10, 51, 17))
        self.m5Pos.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m5Pos.setObjectName("m5Pos")
        self.m14 = QtWidgets.QLabel(self.m5Frame)
        self.m14.setGeometry(QtCore.QRect(270, 0, 31, 31))
        self.m14.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"")
        self.m14.setObjectName("m14")
        self.m14Pos = QtWidgets.QLabel(self.m5Frame)
        self.m14Pos.setGeometry(QtCore.QRect(430, 10, 51, 17))
        self.m14Pos.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m14Pos.setObjectName("m14Pos")
        self.m14Ang = QtWidgets.QLabel(self.m5Frame)
        self.m14Ang.setGeometry(QtCore.QRect(340, 10, 51, 17))
        self.m14Ang.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m14Ang.setObjectName("m14Ang")
        self.m6Frame = QtWidgets.QFrame(self.mPageMFrame)
        self.m6Frame.setGeometry(QtCore.QRect(20, 300, 501, 31))
        self.m6Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m6Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m6Frame.setObjectName("m6Frame")
        self.m6 = QtWidgets.QLabel(self.m6Frame)
        self.m6.setGeometry(QtCore.QRect(10, 0, 21, 31))
        self.m6.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"")
        self.m6.setObjectName("m6")
        self.m6Ang = QtWidgets.QLabel(self.m6Frame)
        self.m6Ang.setGeometry(QtCore.QRect(70, 10, 51, 17))
        self.m6Ang.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m6Ang.setObjectName("m6Ang")
        self.m6Pos = QtWidgets.QLabel(self.m6Frame)
        self.m6Pos.setGeometry(QtCore.QRect(170, 10, 51, 17))
        self.m6Pos.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m6Pos.setObjectName("m6Pos")
        self.m15 = QtWidgets.QLabel(self.m6Frame)
        self.m15.setGeometry(QtCore.QRect(270, 0, 31, 31))
        self.m15.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"")
        self.m15.setObjectName("m15")
        self.m15Pos = QtWidgets.QLabel(self.m6Frame)
        self.m15Pos.setGeometry(QtCore.QRect(430, 10, 51, 17))
        self.m15Pos.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m15Pos.setObjectName("m15Pos")
        self.m15Ang = QtWidgets.QLabel(self.m6Frame)
        self.m15Ang.setGeometry(QtCore.QRect(340, 10, 51, 17))
        self.m15Ang.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m15Ang.setObjectName("m15Ang")
        self.m7Frame = QtWidgets.QFrame(self.mPageMFrame)
        self.m7Frame.setGeometry(QtCore.QRect(20, 350, 501, 31))
        self.m7Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m7Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m7Frame.setObjectName("m7Frame")
        self.m7 = QtWidgets.QLabel(self.m7Frame)
        self.m7.setGeometry(QtCore.QRect(10, 0, 16, 31))
        self.m7.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"")
        self.m7.setObjectName("m7")
        self.m7Ang = QtWidgets.QLabel(self.m7Frame)
        self.m7Ang.setGeometry(QtCore.QRect(70, 10, 51, 17))
        self.m7Ang.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m7Ang.setObjectName("m7Ang")
        self.m7Pos = QtWidgets.QLabel(self.m7Frame)
        self.m7Pos.setGeometry(QtCore.QRect(170, 10, 51, 17))
        self.m7Pos.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m7Pos.setObjectName("m7Pos")
        self.m16 = QtWidgets.QLabel(self.m7Frame)
        self.m16.setGeometry(QtCore.QRect(270, 0, 31, 31))
        self.m16.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"")
        self.m16.setObjectName("m16")
        self.m16Pos = QtWidgets.QLabel(self.m7Frame)
        self.m16Pos.setGeometry(QtCore.QRect(430, 10, 51, 17))
        self.m16Pos.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m16Pos.setObjectName("m16Pos")
        self.m16Ang = QtWidgets.QLabel(self.m7Frame)
        self.m16Ang.setGeometry(QtCore.QRect(340, 10, 51, 17))
        self.m16Ang.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m16Ang.setObjectName("m16Ang")
        self.m8Frame = QtWidgets.QFrame(self.mPageMFrame)
        self.m8Frame.setGeometry(QtCore.QRect(20, 400, 501, 31))
        self.m8Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m8Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m8Frame.setObjectName("m8Frame")
        self.m8 = QtWidgets.QLabel(self.m8Frame)
        self.m8.setGeometry(QtCore.QRect(10, 0, 21, 31))
        self.m8.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"")
        self.m8.setObjectName("m8")
        self.m8Ang = QtWidgets.QLabel(self.m8Frame)
        self.m8Ang.setGeometry(QtCore.QRect(70, 10, 51, 17))
        self.m8Ang.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m8Ang.setObjectName("m8Ang")
        self.m8Pos = QtWidgets.QLabel(self.m8Frame)
        self.m8Pos.setGeometry(QtCore.QRect(170, 10, 51, 17))
        self.m8Pos.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m8Pos.setObjectName("m8Pos")
        self.m17 = QtWidgets.QLabel(self.m8Frame)
        self.m17.setGeometry(QtCore.QRect(270, 0, 31, 31))
        self.m17.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"")
        self.m17.setObjectName("m17")
        self.m17Pos = QtWidgets.QLabel(self.m8Frame)
        self.m17Pos.setGeometry(QtCore.QRect(430, 10, 51, 17))
        self.m17Pos.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m17Pos.setObjectName("m17Pos")
        self.m17Ang = QtWidgets.QLabel(self.m8Frame)
        self.m17Ang.setGeometry(QtCore.QRect(340, 10, 51, 17))
        self.m17Ang.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m17Ang.setObjectName("m17Ang")
        self.recSavedLabel = QtWidgets.QLabel(self.mPageMFrame)
        self.recSavedLabel.setGeometry(QtCore.QRect(280, 500, 151, 20))
        self.recSavedLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"\n"
"")
        self.recSavedLabel.setObjectName("recSavedLabel")
        self.recNumLabel = QtWidgets.QLabel(self.mPageMFrame)
        self.recNumLabel.setGeometry(QtCore.QRect(450, 500, 16, 31))
        self.recNumLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"")
        self.recNumLabel.setObjectName("recNumLabel")
        self.mUpdateBtn = QtWidgets.QPushButton(self.mPageMFrame)
        self.mUpdateBtn.setGeometry(QtCore.QRect(20, 490, 171, 31))
        self.mUpdateBtn.setAutoFillBackground(False)
        self.mUpdateBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.mUpdateBtn.setAutoDefault(False)
        self.mUpdateBtn.setDefault(False)
        self.mUpdateBtn.setFlat(False)
        self.mUpdateBtn.setObjectName("mUpdateBtn")
        self.m8Frame_2 = QtWidgets.QFrame(self.mPageMFrame)
        self.m8Frame_2.setGeometry(QtCore.QRect(20, 450, 501, 31))
        self.m8Frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m8Frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m8Frame_2.setObjectName("m8Frame_2")
        self.m9 = QtWidgets.QLabel(self.m8Frame_2)
        self.m9.setGeometry(QtCore.QRect(10, 0, 21, 31))
        self.m9.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"")
        self.m9.setObjectName("m9")
        self.m9Ang = QtWidgets.QLabel(self.m8Frame_2)
        self.m9Ang.setGeometry(QtCore.QRect(70, 10, 51, 17))
        self.m9Ang.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m9Ang.setObjectName("m9Ang")
        self.m9Pos = QtWidgets.QLabel(self.m8Frame_2)
        self.m9Pos.setGeometry(QtCore.QRect(170, 10, 51, 17))
        self.m9Pos.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m9Pos.setObjectName("m9Pos")
        self.m18 = QtWidgets.QLabel(self.m8Frame_2)
        self.m18.setGeometry(QtCore.QRect(270, 0, 31, 31))
        self.m18.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"")
        self.m18.setObjectName("m18")
        self.m18Pos = QtWidgets.QLabel(self.m8Frame_2)
        self.m18Pos.setGeometry(QtCore.QRect(430, 10, 51, 17))
        self.m18Pos.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m18Pos.setObjectName("m18Pos")
        self.m18Ang = QtWidgets.QLabel(self.m8Frame_2)
        self.m18Ang.setGeometry(QtCore.QRect(340, 10, 51, 17))
        self.m18Ang.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"        ")
        self.m18Ang.setObjectName("m18Ang")
        self.mId_2 = QtWidgets.QLabel(self.mPageMFrame)
        self.mId_2.setGeometry(QtCore.QRect(290, 20, 31, 21))
        self.mId_2.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"")
        self.mId_2.setObjectName("mId_2")
        self.mAngle_2 = QtWidgets.QLabel(self.mPageMFrame)
        self.mAngle_2.setGeometry(QtCore.QRect(360, 20, 61, 21))
        self.mAngle_2.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"\n"
"")
        self.mAngle_2.setObjectName("mAngle_2")
        self.mPos_2 = QtWidgets.QLabel(self.mPageMFrame)
        self.mPos_2.setGeometry(QtCore.QRect(440, 20, 81, 21))
        self.mPos_2.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"\n"
"")
        self.mPos_2.setObjectName("mPos_2")
        self.mPageSFrame = QtWidgets.QFrame(self.mainPage)
        self.mPageSFrame.setGeometry(QtCore.QRect(560, 20, 231, 531))
        self.mPageSFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.mPageSFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mPageSFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mPageSFrame.setObjectName("mPageSFrame")
        self.inRecBtn = QtWidgets.QPushButton(self.mPageSFrame)
        self.inRecBtn.setGeometry(QtCore.QRect(30, 20, 171, 61))
        self.inRecBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.inRecBtn.setObjectName("inRecBtn")
        self.saveRecBtn = QtWidgets.QPushButton(self.mPageSFrame)
        self.saveRecBtn.setGeometry(QtCore.QRect(30, 150, 171, 61))
        self.saveRecBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.saveRecBtn.setObjectName("saveRecBtn")
        self.recNameInput = QtWidgets.QLineEdit(self.mPageSFrame)
        self.recNameInput.setGeometry(QtCore.QRect(30, 110, 171, 27))
        self.recNameInput.setObjectName("recNameInput")
        self.saveStatusLabel = QtWidgets.QLabel(self.mPageSFrame)
        self.saveStatusLabel.setGeometry(QtCore.QRect(70, 230, 101, 21))
        self.saveStatusLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;\n"
"\n"
"")
        self.saveStatusLabel.setObjectName("saveStatusLabel")
        self.newRecBtn = QtWidgets.QPushButton(self.mPageSFrame)
        self.newRecBtn.setGeometry(QtCore.QRect(30, 430, 171, 61))
        self.newRecBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.newRecBtn.setObjectName("newRecBtn")
        self.mSelect = QtWidgets.QComboBox(self.mPageSFrame)
        self.mSelect.setGeometry(QtCore.QRect(30, 280, 171, 27))
        self.mSelect.setObjectName("mSelect")
        self.mSelect.addItem("")
        self.mSelect.addItem("")
        self.mSelect.addItem("")
        self.mSelect.addItem("")
        self.mSelect.addItem("")
        self.mSelect.addItem("")
        self.mSelect.addItem("")
        self.mSelect.addItem("")
        self.mSelect.addItem("")
        self.mSelect.addItem("")
        self.mSelect.addItem("")
        self.mSelect.addItem("")
        self.mSelect.addItem("")
        self.mSelect.addItem("")
        self.mSelect.addItem("")
        self.mSelect.addItem("")
        self.mSelect.addItem("")
        self.mSelect.addItem("")
        self.mGoBtn = QtWidgets.QPushButton(self.mPageSFrame)
        self.mGoBtn.setGeometry(QtCore.QRect(30, 320, 171, 31))
        self.mGoBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.mGoBtn.setObjectName("mGoBtn")
        self.stackedWidget.addWidget(self.mainPage)
        self.m1Page = QtWidgets.QWidget()
        self.m1Page.setObjectName("m1Page")
        self.m1Label = QtWidgets.QLabel(self.m1Page)
        self.m1Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m1Label.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m1Label.setObjectName("m1Label")
        self.m1SFrame = QtWidgets.QFrame(self.m1Page)
        self.m1SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m1SFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m1SFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m1SFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m1SFrame.setObjectName("m1SFrame")
        self.m1AngLabel = QtWidgets.QLabel(self.m1SFrame)
        self.m1AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m1AngLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m1AngLabel.setObjectName("m1AngLabel")
        self.m1PosLabel = QtWidgets.QLabel(self.m1SFrame)
        self.m1PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m1PosLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m1PosLabel.setObjectName("m1PosLabel")
        self.m1TorqueLabel = QtWidgets.QLabel(self.m1SFrame)
        self.m1TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m1TorqueLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m1TorqueLabel.setObjectName("m1TorqueLabel")
        self.m1TempLabel = QtWidgets.QLabel(self.m1SFrame)
        self.m1TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m1TempLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m1TempLabel.setObjectName("m1TempLabel")
        self.m1ErrLabel = QtWidgets.QLabel(self.m1SFrame)
        self.m1ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m1ErrLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m1ErrLabel.setObjectName("m1ErrLabel")
        self.m1AngDial = QtWidgets.QDial(self.m1SFrame)
        self.m1AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m1AngDial.setMinimum(-150)
        self.m1AngDial.setMaximum(150)
        self.m1AngDial.setTracking(True)
        self.m1AngDial.setWrapping(False)
        self.m1AngDial.setNotchTarget(50.0)
        self.m1AngDial.setNotchesVisible(True)
        self.m1AngDial.setObjectName("m1AngDial")
        self.m1PosDial = QtWidgets.QDial(self.m1SFrame)
        self.m1PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m1PosDial.setMinimum(0)
        self.m1PosDial.setMaximum(1023)
        self.m1PosDial.setTracking(True)
        self.m1PosDial.setWrapping(False)
        self.m1PosDial.setNotchTarget(100.0)
        self.m1PosDial.setNotchesVisible(True)
        self.m1PosDial.setObjectName("m1PosDial")
        self.m1AngNum = QtWidgets.QLabel(self.m1SFrame)
        self.m1AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m1AngNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m1AngNum.setObjectName("m1AngNum")
        self.m1PosNum = QtWidgets.QLabel(self.m1SFrame)
        self.m1PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m1PosNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m1PosNum.setObjectName("m1PosNum")
        self.m1TorqueNum = QtWidgets.QLabel(self.m1SFrame)
        self.m1TorqueNum.setGeometry(QtCore.QRect(120, 320, 61, 21))
        self.m1TorqueNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m1TorqueNum.setObjectName("m1TorqueNum")
        self.m1ErrNum = QtWidgets.QLabel(self.m1SFrame)
        self.m1ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m1ErrNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m1ErrNum.setObjectName("m1ErrNum")
        self.m1TempNum = QtWidgets.QLabel(self.m1SFrame)
        self.m1TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m1TempNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m1TempNum.setObjectName("m1TempNum")
        self.m1CFrame = QtWidgets.QFrame(self.m1Page)
        self.m1CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m1CFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m1CFrame.setObjectName("m1CFrame")
        self.m1GoalTSpin = QtWidgets.QSpinBox(self.m1CFrame)
        self.m1GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m1GoalTSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m1GoalTSpin.setWrapping(False)
        self.m1GoalTSpin.setAccelerated(False)
        self.m1GoalTSpin.setObjectName("m1GoalTSpin")
        self.m1GoalTLabel = QtWidgets.QLabel(self.m1CFrame)
        self.m1GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m1GoalTLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m1GoalTLabel.setObjectName("m1GoalTLabel")
        self.m1UpdateBtn = QtWidgets.QPushButton(self.m1CFrame)
        self.m1UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m1UpdateBtn.setAutoFillBackground(False)
        self.m1UpdateBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m1UpdateBtn.setAutoDefault(False)
        self.m1UpdateBtn.setDefault(False)
        self.m1UpdateBtn.setFlat(False)
        self.m1UpdateBtn.setObjectName("m1UpdateBtn")
        self.m1AngleLabel = QtWidgets.QLabel(self.m1CFrame)
        self.m1AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m1AngleLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m1AngleLabel.setObjectName("m1AngleLabel")
        self.m1AngleSpin = QtWidgets.QSpinBox(self.m1CFrame)
        self.m1AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m1AngleSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m1AngleSpin.setWrapping(False)
        self.m1AngleSpin.setAccelerated(False)
        self.m1AngleSpin.setMinimum(-150)
        self.m1AngleSpin.setMaximum(150)
        self.m1AngleSpin.setObjectName("m1AngleSpin")
        self.m1PositionSpin = QtWidgets.QSpinBox(self.m1CFrame)
        self.m1PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m1PositionSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m1PositionSpin.setWrapping(False)
        self.m1PositionSpin.setAccelerated(False)
        self.m1PositionSpin.setMaximum(1023)
        self.m1PositionSpin.setObjectName("m1PositionSpin")
        self.m1PositionLabel = QtWidgets.QLabel(self.m1CFrame)
        self.m1PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m1PositionLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m1PositionLabel.setObjectName("m1PositionLabel")
        self.m1AngleBtn = QtWidgets.QPushButton(self.m1CFrame)
        self.m1AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m1AngleBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m1AngleBtn.setObjectName("m1AngleBtn")
        self.m1PositionBtn = QtWidgets.QPushButton(self.m1CFrame)
        self.m1PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m1PositionBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m1PositionBtn.setObjectName("m1PositionBtn")
        self.m1HomeBtn = QtWidgets.QPushButton(self.m1CFrame)
        self.m1HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m1HomeBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m1HomeBtn.setObjectName("m1HomeBtn")
        self.stackedWidget.addWidget(self.m1Page)
        self.m2Page = QtWidgets.QWidget()
        self.m2Page.setObjectName("m2Page")
        self.m2SFrame = QtWidgets.QFrame(self.m2Page)
        self.m2SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m2SFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m2SFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m2SFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m2SFrame.setObjectName("m2SFrame")
        self.m2AngLabel = QtWidgets.QLabel(self.m2SFrame)
        self.m2AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m2AngLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m2AngLabel.setObjectName("m2AngLabel")
        self.m2PosLabel = QtWidgets.QLabel(self.m2SFrame)
        self.m2PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m2PosLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m2PosLabel.setObjectName("m2PosLabel")
        self.m2TorqueLabel = QtWidgets.QLabel(self.m2SFrame)
        self.m2TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m2TorqueLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m2TorqueLabel.setObjectName("m2TorqueLabel")
        self.m2TempLabel = QtWidgets.QLabel(self.m2SFrame)
        self.m2TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m2TempLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m2TempLabel.setObjectName("m2TempLabel")
        self.m2ErrLabel = QtWidgets.QLabel(self.m2SFrame)
        self.m2ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m2ErrLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m2ErrLabel.setObjectName("m2ErrLabel")
        self.m2AngDial = QtWidgets.QDial(self.m2SFrame)
        self.m2AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m2AngDial.setMinimum(-150)
        self.m2AngDial.setMaximum(150)
        self.m2AngDial.setTracking(True)
        self.m2AngDial.setWrapping(False)
        self.m2AngDial.setNotchTarget(50.0)
        self.m2AngDial.setNotchesVisible(True)
        self.m2AngDial.setObjectName("m2AngDial")
        self.m2PosDial = QtWidgets.QDial(self.m2SFrame)
        self.m2PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m2PosDial.setMinimum(0)
        self.m2PosDial.setMaximum(1023)
        self.m2PosDial.setTracking(True)
        self.m2PosDial.setWrapping(False)
        self.m2PosDial.setNotchTarget(100.0)
        self.m2PosDial.setNotchesVisible(True)
        self.m2PosDial.setObjectName("m2PosDial")
        self.m2AngNum = QtWidgets.QLabel(self.m2SFrame)
        self.m2AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m2AngNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m2AngNum.setObjectName("m2AngNum")
        self.m2PosNum = QtWidgets.QLabel(self.m2SFrame)
        self.m2PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m2PosNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m2PosNum.setObjectName("m2PosNum")
        self.m2TorqueNum = QtWidgets.QLabel(self.m2SFrame)
        self.m2TorqueNum.setGeometry(QtCore.QRect(120, 320, 61, 21))
        self.m2TorqueNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m2TorqueNum.setObjectName("m2TorqueNum")
        self.m2ErrNum = QtWidgets.QLabel(self.m2SFrame)
        self.m2ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m2ErrNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m2ErrNum.setObjectName("m2ErrNum")
        self.m2TempNum = QtWidgets.QLabel(self.m2SFrame)
        self.m2TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m2TempNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m2TempNum.setObjectName("m2TempNum")
        self.m2CFrame = QtWidgets.QFrame(self.m2Page)
        self.m2CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m2CFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m2CFrame.setObjectName("m2CFrame")
        self.m2GoalTSpin = QtWidgets.QSpinBox(self.m2CFrame)
        self.m2GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m2GoalTSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m2GoalTSpin.setWrapping(False)
        self.m2GoalTSpin.setAccelerated(False)
        self.m2GoalTSpin.setObjectName("m2GoalTSpin")
        self.m2GoalTLabel = QtWidgets.QLabel(self.m2CFrame)
        self.m2GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m2GoalTLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m2GoalTLabel.setObjectName("m2GoalTLabel")
        self.m2UpdateBtn = QtWidgets.QPushButton(self.m2CFrame)
        self.m2UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m2UpdateBtn.setAutoFillBackground(False)
        self.m2UpdateBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m2UpdateBtn.setAutoDefault(False)
        self.m2UpdateBtn.setDefault(False)
        self.m2UpdateBtn.setFlat(False)
        self.m2UpdateBtn.setObjectName("m2UpdateBtn")
        self.m2AngleLabel = QtWidgets.QLabel(self.m2CFrame)
        self.m2AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m2AngleLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m2AngleLabel.setObjectName("m2AngleLabel")
        self.m2AngleSpin = QtWidgets.QSpinBox(self.m2CFrame)
        self.m2AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m2AngleSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m2AngleSpin.setWrapping(False)
        self.m2AngleSpin.setAccelerated(False)
        self.m2AngleSpin.setMinimum(-150)
        self.m2AngleSpin.setMaximum(150)
        self.m2AngleSpin.setObjectName("m2AngleSpin")
        self.m2PositionSpin = QtWidgets.QSpinBox(self.m2CFrame)
        self.m2PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m2PositionSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m2PositionSpin.setWrapping(False)
        self.m2PositionSpin.setAccelerated(False)
        self.m2PositionSpin.setMaximum(1023)
        self.m2PositionSpin.setObjectName("m2PositionSpin")
        self.m2PositionLabel = QtWidgets.QLabel(self.m2CFrame)
        self.m2PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m2PositionLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m2PositionLabel.setObjectName("m2PositionLabel")
        self.m2AngleBtn = QtWidgets.QPushButton(self.m2CFrame)
        self.m2AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m2AngleBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m2AngleBtn.setObjectName("m2AngleBtn")
        self.m2PositionBtn = QtWidgets.QPushButton(self.m2CFrame)
        self.m2PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m2PositionBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m2PositionBtn.setObjectName("m2PositionBtn")
        self.m2HomeBtn = QtWidgets.QPushButton(self.m2CFrame)
        self.m2HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m2HomeBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m2HomeBtn.setObjectName("m2HomeBtn")
        self.m2Label = QtWidgets.QLabel(self.m2Page)
        self.m2Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m2Label.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m2Label.setObjectName("m2Label")
        self.stackedWidget.addWidget(self.m2Page)
        self.m3Page = QtWidgets.QWidget()
        self.m3Page.setObjectName("m3Page")
        self.m3SFrame = QtWidgets.QFrame(self.m3Page)
        self.m3SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m3SFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m3SFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m3SFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m3SFrame.setObjectName("m3SFrame")
        self.m3AngLabel = QtWidgets.QLabel(self.m3SFrame)
        self.m3AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m3AngLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m3AngLabel.setObjectName("m3AngLabel")
        self.m3PosLabel = QtWidgets.QLabel(self.m3SFrame)
        self.m3PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m3PosLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m3PosLabel.setObjectName("m3PosLabel")
        self.m3TorqueLabel = QtWidgets.QLabel(self.m3SFrame)
        self.m3TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m3TorqueLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m3TorqueLabel.setObjectName("m3TorqueLabel")
        self.m3TempLabel = QtWidgets.QLabel(self.m3SFrame)
        self.m3TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m3TempLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m3TempLabel.setObjectName("m3TempLabel")
        self.m3ErrLabel = QtWidgets.QLabel(self.m3SFrame)
        self.m3ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m3ErrLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m3ErrLabel.setObjectName("m3ErrLabel")
        self.m3AngDial = QtWidgets.QDial(self.m3SFrame)
        self.m3AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m3AngDial.setMinimum(-150)
        self.m3AngDial.setMaximum(150)
        self.m3AngDial.setTracking(True)
        self.m3AngDial.setWrapping(False)
        self.m3AngDial.setNotchTarget(50.0)
        self.m3AngDial.setNotchesVisible(True)
        self.m3AngDial.setObjectName("m3AngDial")
        self.m3PosDial = QtWidgets.QDial(self.m3SFrame)
        self.m3PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m3PosDial.setMinimum(0)
        self.m3PosDial.setMaximum(1023)
        self.m3PosDial.setTracking(True)
        self.m3PosDial.setWrapping(False)
        self.m3PosDial.setNotchTarget(100.0)
        self.m3PosDial.setNotchesVisible(True)
        self.m3PosDial.setObjectName("m3PosDial")
        self.m3AngNum = QtWidgets.QLabel(self.m3SFrame)
        self.m3AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m3AngNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m3AngNum.setObjectName("m3AngNum")
        self.m3PosNum = QtWidgets.QLabel(self.m3SFrame)
        self.m3PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m3PosNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m3PosNum.setObjectName("m3PosNum")
        self.m3TorqueNum = QtWidgets.QLabel(self.m3SFrame)
        self.m3TorqueNum.setGeometry(QtCore.QRect(120, 320, 61, 21))
        self.m3TorqueNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m3TorqueNum.setObjectName("m3TorqueNum")
        self.m3ErrNum = QtWidgets.QLabel(self.m3SFrame)
        self.m3ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m3ErrNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m3ErrNum.setObjectName("m3ErrNum")
        self.m3TempNum = QtWidgets.QLabel(self.m3SFrame)
        self.m3TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m3TempNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m3TempNum.setObjectName("m3TempNum")
        self.m3CFrame = QtWidgets.QFrame(self.m3Page)
        self.m3CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m3CFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m3CFrame.setObjectName("m3CFrame")
        self.m3GoalTSpin = QtWidgets.QSpinBox(self.m3CFrame)
        self.m3GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m3GoalTSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m3GoalTSpin.setWrapping(False)
        self.m3GoalTSpin.setAccelerated(False)
        self.m3GoalTSpin.setObjectName("m3GoalTSpin")
        self.m3GoalTLabel = QtWidgets.QLabel(self.m3CFrame)
        self.m3GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m3GoalTLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m3GoalTLabel.setObjectName("m3GoalTLabel")
        self.m3UpdateBtn = QtWidgets.QPushButton(self.m3CFrame)
        self.m3UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m3UpdateBtn.setAutoFillBackground(False)
        self.m3UpdateBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m3UpdateBtn.setAutoDefault(False)
        self.m3UpdateBtn.setDefault(False)
        self.m3UpdateBtn.setFlat(False)
        self.m3UpdateBtn.setObjectName("m3UpdateBtn")
        self.m3AngleLabel = QtWidgets.QLabel(self.m3CFrame)
        self.m3AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m3AngleLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m3AngleLabel.setObjectName("m3AngleLabel")
        self.m3AngleSpin = QtWidgets.QSpinBox(self.m3CFrame)
        self.m3AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m3AngleSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m3AngleSpin.setWrapping(False)
        self.m3AngleSpin.setAccelerated(False)
        self.m3AngleSpin.setMinimum(-150)
        self.m3AngleSpin.setMaximum(150)
        self.m3AngleSpin.setObjectName("m3AngleSpin")
        self.m3PositionSpin = QtWidgets.QSpinBox(self.m3CFrame)
        self.m3PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m3PositionSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m3PositionSpin.setWrapping(False)
        self.m3PositionSpin.setAccelerated(False)
        self.m3PositionSpin.setMaximum(1023)
        self.m3PositionSpin.setObjectName("m3PositionSpin")
        self.m3PositionLabel = QtWidgets.QLabel(self.m3CFrame)
        self.m3PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m3PositionLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m3PositionLabel.setObjectName("m3PositionLabel")
        self.m3AngleBtn = QtWidgets.QPushButton(self.m3CFrame)
        self.m3AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m3AngleBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m3AngleBtn.setObjectName("m3AngleBtn")
        self.m3PositionBtn = QtWidgets.QPushButton(self.m3CFrame)
        self.m3PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m3PositionBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m3PositionBtn.setObjectName("m3PositionBtn")
        self.m3HomeBtn = QtWidgets.QPushButton(self.m3CFrame)
        self.m3HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m3HomeBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m3HomeBtn.setObjectName("m3HomeBtn")
        self.m3Label = QtWidgets.QLabel(self.m3Page)
        self.m3Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m3Label.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m3Label.setObjectName("m3Label")
        self.stackedWidget.addWidget(self.m3Page)
        self.m4Page = QtWidgets.QWidget()
        self.m4Page.setObjectName("m4Page")
        self.m4SFrame = QtWidgets.QFrame(self.m4Page)
        self.m4SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m4SFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m4SFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m4SFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m4SFrame.setObjectName("m4SFrame")
        self.m4AngLabel = QtWidgets.QLabel(self.m4SFrame)
        self.m4AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m4AngLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m4AngLabel.setObjectName("m4AngLabel")
        self.m4PosLabel = QtWidgets.QLabel(self.m4SFrame)
        self.m4PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m4PosLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m4PosLabel.setObjectName("m4PosLabel")
        self.m4TorqueLabel = QtWidgets.QLabel(self.m4SFrame)
        self.m4TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m4TorqueLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m4TorqueLabel.setObjectName("m4TorqueLabel")
        self.m4TempLabel = QtWidgets.QLabel(self.m4SFrame)
        self.m4TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m4TempLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m4TempLabel.setObjectName("m4TempLabel")
        self.m4ErrLabel = QtWidgets.QLabel(self.m4SFrame)
        self.m4ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m4ErrLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m4ErrLabel.setObjectName("m4ErrLabel")
        self.m4AngDial = QtWidgets.QDial(self.m4SFrame)
        self.m4AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m4AngDial.setMinimum(-150)
        self.m4AngDial.setMaximum(150)
        self.m4AngDial.setTracking(True)
        self.m4AngDial.setWrapping(False)
        self.m4AngDial.setNotchTarget(50.0)
        self.m4AngDial.setNotchesVisible(True)
        self.m4AngDial.setObjectName("m4AngDial")
        self.m4PosDial = QtWidgets.QDial(self.m4SFrame)
        self.m4PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m4PosDial.setMinimum(0)
        self.m4PosDial.setMaximum(1023)
        self.m4PosDial.setTracking(True)
        self.m4PosDial.setWrapping(False)
        self.m4PosDial.setNotchTarget(100.0)
        self.m4PosDial.setNotchesVisible(True)
        self.m4PosDial.setObjectName("m4PosDial")
        self.m4AngNum = QtWidgets.QLabel(self.m4SFrame)
        self.m4AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m4AngNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m4AngNum.setObjectName("m4AngNum")
        self.m4PosNum = QtWidgets.QLabel(self.m4SFrame)
        self.m4PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m4PosNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m4PosNum.setObjectName("m4PosNum")
        self.m4TorqueNum = QtWidgets.QLabel(self.m4SFrame)
        self.m4TorqueNum.setGeometry(QtCore.QRect(120, 320, 61, 21))
        self.m4TorqueNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m4TorqueNum.setObjectName("m4TorqueNum")
        self.m4ErrNum = QtWidgets.QLabel(self.m4SFrame)
        self.m4ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m4ErrNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m4ErrNum.setObjectName("m4ErrNum")
        self.m4TempNum = QtWidgets.QLabel(self.m4SFrame)
        self.m4TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m4TempNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m4TempNum.setObjectName("m4TempNum")
        self.m4CFrame = QtWidgets.QFrame(self.m4Page)
        self.m4CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m4CFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m4CFrame.setObjectName("m4CFrame")
        self.m4GoalTSpin = QtWidgets.QSpinBox(self.m4CFrame)
        self.m4GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m4GoalTSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m4GoalTSpin.setWrapping(False)
        self.m4GoalTSpin.setAccelerated(False)
        self.m4GoalTSpin.setObjectName("m4GoalTSpin")
        self.m4GoalTLabel = QtWidgets.QLabel(self.m4CFrame)
        self.m4GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m4GoalTLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m4GoalTLabel.setObjectName("m4GoalTLabel")
        self.m4UpdateBtn = QtWidgets.QPushButton(self.m4CFrame)
        self.m4UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m4UpdateBtn.setAutoFillBackground(False)
        self.m4UpdateBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m4UpdateBtn.setAutoDefault(False)
        self.m4UpdateBtn.setDefault(False)
        self.m4UpdateBtn.setFlat(False)
        self.m4UpdateBtn.setObjectName("m4UpdateBtn")
        self.m4AngleLabel = QtWidgets.QLabel(self.m4CFrame)
        self.m4AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m4AngleLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m4AngleLabel.setObjectName("m4AngleLabel")
        self.m4AngleSpin = QtWidgets.QSpinBox(self.m4CFrame)
        self.m4AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m4AngleSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m4AngleSpin.setWrapping(False)
        self.m4AngleSpin.setAccelerated(False)
        self.m4AngleSpin.setMinimum(-150)
        self.m4AngleSpin.setMaximum(150)
        self.m4AngleSpin.setObjectName("m4AngleSpin")
        self.m4PositionSpin = QtWidgets.QSpinBox(self.m4CFrame)
        self.m4PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m4PositionSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m4PositionSpin.setWrapping(False)
        self.m4PositionSpin.setAccelerated(False)
        self.m4PositionSpin.setMaximum(1023)
        self.m4PositionSpin.setObjectName("m4PositionSpin")
        self.m4PositionLabel = QtWidgets.QLabel(self.m4CFrame)
        self.m4PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m4PositionLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m4PositionLabel.setObjectName("m4PositionLabel")
        self.m4AngleBtn = QtWidgets.QPushButton(self.m4CFrame)
        self.m4AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m4AngleBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m4AngleBtn.setObjectName("m4AngleBtn")
        self.m4PositionBtn = QtWidgets.QPushButton(self.m4CFrame)
        self.m4PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m4PositionBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m4PositionBtn.setObjectName("m4PositionBtn")
        self.m4HomeBtn = QtWidgets.QPushButton(self.m4CFrame)
        self.m4HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m4HomeBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m4HomeBtn.setObjectName("m4HomeBtn")
        self.m4Label = QtWidgets.QLabel(self.m4Page)
        self.m4Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m4Label.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m4Label.setObjectName("m4Label")
        self.stackedWidget.addWidget(self.m4Page)
        self.m5Page = QtWidgets.QWidget()
        self.m5Page.setObjectName("m5Page")
        self.m5SFrame = QtWidgets.QFrame(self.m5Page)
        self.m5SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m5SFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m5SFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m5SFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m5SFrame.setObjectName("m5SFrame")
        self.m5AngLabel = QtWidgets.QLabel(self.m5SFrame)
        self.m5AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m5AngLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m5AngLabel.setObjectName("m5AngLabel")
        self.m5PosLabel = QtWidgets.QLabel(self.m5SFrame)
        self.m5PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m5PosLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m5PosLabel.setObjectName("m5PosLabel")
        self.m5TorqueLabel = QtWidgets.QLabel(self.m5SFrame)
        self.m5TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m5TorqueLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m5TorqueLabel.setObjectName("m5TorqueLabel")
        self.m5TempLabel = QtWidgets.QLabel(self.m5SFrame)
        self.m5TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m5TempLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m5TempLabel.setObjectName("m5TempLabel")
        self.m5ErrLabel = QtWidgets.QLabel(self.m5SFrame)
        self.m5ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m5ErrLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m5ErrLabel.setObjectName("m5ErrLabel")
        self.m5AngDial = QtWidgets.QDial(self.m5SFrame)
        self.m5AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m5AngDial.setMinimum(-150)
        self.m5AngDial.setMaximum(150)
        self.m5AngDial.setTracking(True)
        self.m5AngDial.setWrapping(False)
        self.m5AngDial.setNotchTarget(50.0)
        self.m5AngDial.setNotchesVisible(True)
        self.m5AngDial.setObjectName("m5AngDial")
        self.m5PosDial = QtWidgets.QDial(self.m5SFrame)
        self.m5PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m5PosDial.setMinimum(0)
        self.m5PosDial.setMaximum(1023)
        self.m5PosDial.setTracking(True)
        self.m5PosDial.setWrapping(False)
        self.m5PosDial.setNotchTarget(100.0)
        self.m5PosDial.setNotchesVisible(True)
        self.m5PosDial.setObjectName("m5PosDial")
        self.m5AngNum = QtWidgets.QLabel(self.m5SFrame)
        self.m5AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m5AngNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m5AngNum.setObjectName("m5AngNum")
        self.m5PosNum = QtWidgets.QLabel(self.m5SFrame)
        self.m5PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m5PosNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m5PosNum.setObjectName("m5PosNum")
        self.m5TorqueNum = QtWidgets.QLabel(self.m5SFrame)
        self.m5TorqueNum.setGeometry(QtCore.QRect(120, 320, 61, 21))
        self.m5TorqueNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m5TorqueNum.setObjectName("m5TorqueNum")
        self.m5ErrNum = QtWidgets.QLabel(self.m5SFrame)
        self.m5ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m5ErrNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m5ErrNum.setObjectName("m5ErrNum")
        self.m5TempNum = QtWidgets.QLabel(self.m5SFrame)
        self.m5TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m5TempNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m5TempNum.setObjectName("m5TempNum")
        self.m5CFrame = QtWidgets.QFrame(self.m5Page)
        self.m5CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m5CFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m5CFrame.setObjectName("m5CFrame")
        self.m5GoalTSpin = QtWidgets.QSpinBox(self.m5CFrame)
        self.m5GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m5GoalTSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m5GoalTSpin.setWrapping(False)
        self.m5GoalTSpin.setAccelerated(False)
        self.m5GoalTSpin.setObjectName("m5GoalTSpin")
        self.m5GoalTLabel = QtWidgets.QLabel(self.m5CFrame)
        self.m5GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m5GoalTLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m5GoalTLabel.setObjectName("m5GoalTLabel")
        self.m5UpdateBtn = QtWidgets.QPushButton(self.m5CFrame)
        self.m5UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m5UpdateBtn.setAutoFillBackground(False)
        self.m5UpdateBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m5UpdateBtn.setAutoDefault(False)
        self.m5UpdateBtn.setDefault(False)
        self.m5UpdateBtn.setFlat(False)
        self.m5UpdateBtn.setObjectName("m5UpdateBtn")
        self.m5AngleLabel = QtWidgets.QLabel(self.m5CFrame)
        self.m5AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m5AngleLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m5AngleLabel.setObjectName("m5AngleLabel")
        self.m5AngleSpin = QtWidgets.QSpinBox(self.m5CFrame)
        self.m5AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m5AngleSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m5AngleSpin.setWrapping(False)
        self.m5AngleSpin.setAccelerated(False)
        self.m5AngleSpin.setMinimum(-150)
        self.m5AngleSpin.setMaximum(150)
        self.m5AngleSpin.setObjectName("m5AngleSpin")
        self.m5PositionSpin = QtWidgets.QSpinBox(self.m5CFrame)
        self.m5PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m5PositionSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m5PositionSpin.setWrapping(False)
        self.m5PositionSpin.setAccelerated(False)
        self.m5PositionSpin.setMaximum(1023)
        self.m5PositionSpin.setObjectName("m5PositionSpin")
        self.m5PositionLabel = QtWidgets.QLabel(self.m5CFrame)
        self.m5PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m5PositionLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m5PositionLabel.setObjectName("m5PositionLabel")
        self.m5AngleBtn = QtWidgets.QPushButton(self.m5CFrame)
        self.m5AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m5AngleBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m5AngleBtn.setObjectName("m5AngleBtn")
        self.m5PositionBtn = QtWidgets.QPushButton(self.m5CFrame)
        self.m5PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m5PositionBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m5PositionBtn.setObjectName("m5PositionBtn")
        self.m5HomeBtn = QtWidgets.QPushButton(self.m5CFrame)
        self.m5HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m5HomeBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m5HomeBtn.setObjectName("m5HomeBtn")
        self.m5Label = QtWidgets.QLabel(self.m5Page)
        self.m5Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m5Label.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m5Label.setObjectName("m5Label")
        self.stackedWidget.addWidget(self.m5Page)
        self.m6Page = QtWidgets.QWidget()
        self.m6Page.setObjectName("m6Page")
        self.m6Label = QtWidgets.QLabel(self.m6Page)
        self.m6Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m6Label.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m6Label.setObjectName("m6Label")
        self.m6CFrame = QtWidgets.QFrame(self.m6Page)
        self.m6CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m6CFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"\n"
"\n"
"        ")
        self.m6CFrame.setObjectName("m6CFrame")
        self.m6GoalTSpin = QtWidgets.QSpinBox(self.m6CFrame)
        self.m6GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m6GoalTSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m6GoalTSpin.setWrapping(False)
        self.m6GoalTSpin.setAccelerated(False)
        self.m6GoalTSpin.setObjectName("m6GoalTSpin")
        self.m6GoalTLabel = QtWidgets.QLabel(self.m6CFrame)
        self.m6GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m6GoalTLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m6GoalTLabel.setObjectName("m6GoalTLabel")
        self.m6UpdateBtn = QtWidgets.QPushButton(self.m6CFrame)
        self.m6UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m6UpdateBtn.setAutoFillBackground(False)
        self.m6UpdateBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m6UpdateBtn.setAutoDefault(False)
        self.m6UpdateBtn.setDefault(False)
        self.m6UpdateBtn.setFlat(False)
        self.m6UpdateBtn.setObjectName("m6UpdateBtn")
        self.m6AngleLabel = QtWidgets.QLabel(self.m6CFrame)
        self.m6AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m6AngleLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m6AngleLabel.setObjectName("m6AngleLabel")
        self.m6AngleSpin = QtWidgets.QSpinBox(self.m6CFrame)
        self.m6AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m6AngleSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m6AngleSpin.setWrapping(False)
        self.m6AngleSpin.setAccelerated(False)
        self.m6AngleSpin.setMinimum(-150)
        self.m6AngleSpin.setMaximum(150)
        self.m6AngleSpin.setObjectName("m6AngleSpin")
        self.m6PositionSpin = QtWidgets.QSpinBox(self.m6CFrame)
        self.m6PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m6PositionSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m6PositionSpin.setWrapping(False)
        self.m6PositionSpin.setAccelerated(False)
        self.m6PositionSpin.setMaximum(1023)
        self.m6PositionSpin.setObjectName("m6PositionSpin")
        self.m6PositionLabel = QtWidgets.QLabel(self.m6CFrame)
        self.m6PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m6PositionLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m6PositionLabel.setObjectName("m6PositionLabel")
        self.m6AngleBtn = QtWidgets.QPushButton(self.m6CFrame)
        self.m6AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m6AngleBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m6AngleBtn.setObjectName("m6AngleBtn")
        self.m6PositionBtn = QtWidgets.QPushButton(self.m6CFrame)
        self.m6PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m6PositionBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m6PositionBtn.setObjectName("m6PositionBtn")
        self.m6HomeBtn = QtWidgets.QPushButton(self.m6CFrame)
        self.m6HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m6HomeBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m6HomeBtn.setObjectName("m6HomeBtn")
        self.m6SFrame = QtWidgets.QFrame(self.m6Page)
        self.m6SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m6SFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m6SFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m6SFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m6SFrame.setObjectName("m6SFrame")
        self.m6AngLabel = QtWidgets.QLabel(self.m6SFrame)
        self.m6AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m6AngLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m6AngLabel.setObjectName("m6AngLabel")
        self.m6PosLabel = QtWidgets.QLabel(self.m6SFrame)
        self.m6PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m6PosLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m6PosLabel.setObjectName("m6PosLabel")
        self.m6TorqueLabel = QtWidgets.QLabel(self.m6SFrame)
        self.m6TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m6TorqueLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m6TorqueLabel.setObjectName("m6TorqueLabel")
        self.m6TempLabel = QtWidgets.QLabel(self.m6SFrame)
        self.m6TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m6TempLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m6TempLabel.setObjectName("m6TempLabel")
        self.m6ErrLabel = QtWidgets.QLabel(self.m6SFrame)
        self.m6ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m6ErrLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m6ErrLabel.setObjectName("m6ErrLabel")
        self.m6AngDial = QtWidgets.QDial(self.m6SFrame)
        self.m6AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m6AngDial.setMinimum(-150)
        self.m6AngDial.setMaximum(150)
        self.m6AngDial.setTracking(True)
        self.m6AngDial.setWrapping(False)
        self.m6AngDial.setNotchTarget(50.0)
        self.m6AngDial.setNotchesVisible(True)
        self.m6AngDial.setObjectName("m6AngDial")
        self.m6PosDial = QtWidgets.QDial(self.m6SFrame)
        self.m6PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m6PosDial.setMinimum(0)
        self.m6PosDial.setMaximum(1023)
        self.m6PosDial.setTracking(True)
        self.m6PosDial.setWrapping(False)
        self.m6PosDial.setNotchTarget(100.0)
        self.m6PosDial.setNotchesVisible(True)
        self.m6PosDial.setObjectName("m6PosDial")
        self.m6AngNum = QtWidgets.QLabel(self.m6SFrame)
        self.m6AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m6AngNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m6AngNum.setObjectName("m6AngNum")
        self.m6PosNum = QtWidgets.QLabel(self.m6SFrame)
        self.m6PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m6PosNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m6PosNum.setObjectName("m6PosNum")
        self.m6TorqueNum = QtWidgets.QLabel(self.m6SFrame)
        self.m6TorqueNum.setGeometry(QtCore.QRect(120, 320, 61, 21))
        self.m6TorqueNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m6TorqueNum.setObjectName("m6TorqueNum")
        self.m6ErrNum = QtWidgets.QLabel(self.m6SFrame)
        self.m6ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m6ErrNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m6ErrNum.setObjectName("m6ErrNum")
        self.m6TempNum = QtWidgets.QLabel(self.m6SFrame)
        self.m6TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m6TempNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m6TempNum.setObjectName("m6TempNum")
        self.stackedWidget.addWidget(self.m6Page)
        self.m7Page = QtWidgets.QWidget()
        self.m7Page.setObjectName("m7Page")
        self.m7Label = QtWidgets.QLabel(self.m7Page)
        self.m7Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m7Label.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m7Label.setObjectName("m7Label")
        self.m7CFrame = QtWidgets.QFrame(self.m7Page)
        self.m7CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m7CFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m7CFrame.setObjectName("m7CFrame")
        self.m7GoalTSpin = QtWidgets.QSpinBox(self.m7CFrame)
        self.m7GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m7GoalTSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m7GoalTSpin.setWrapping(False)
        self.m7GoalTSpin.setAccelerated(False)
        self.m7GoalTSpin.setObjectName("m7GoalTSpin")
        self.m7GoalTLabel = QtWidgets.QLabel(self.m7CFrame)
        self.m7GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m7GoalTLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m7GoalTLabel.setObjectName("m7GoalTLabel")
        self.m7UpdateBtn = QtWidgets.QPushButton(self.m7CFrame)
        self.m7UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m7UpdateBtn.setAutoFillBackground(False)
        self.m7UpdateBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m7UpdateBtn.setAutoDefault(False)
        self.m7UpdateBtn.setDefault(False)
        self.m7UpdateBtn.setFlat(False)
        self.m7UpdateBtn.setObjectName("m7UpdateBtn")
        self.m7AngleLabel = QtWidgets.QLabel(self.m7CFrame)
        self.m7AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m7AngleLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m7AngleLabel.setObjectName("m7AngleLabel")
        self.m7AngleSpin = QtWidgets.QSpinBox(self.m7CFrame)
        self.m7AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m7AngleSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m7AngleSpin.setWrapping(False)
        self.m7AngleSpin.setAccelerated(False)
        self.m7AngleSpin.setMinimum(-150)
        self.m7AngleSpin.setMaximum(150)
        self.m7AngleSpin.setObjectName("m7AngleSpin")
        self.m7PositionSpin = QtWidgets.QSpinBox(self.m7CFrame)
        self.m7PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m7PositionSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m7PositionSpin.setWrapping(False)
        self.m7PositionSpin.setAccelerated(False)
        self.m7PositionSpin.setMaximum(1023)
        self.m7PositionSpin.setObjectName("m7PositionSpin")
        self.m7PositionLabel = QtWidgets.QLabel(self.m7CFrame)
        self.m7PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m7PositionLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m7PositionLabel.setObjectName("m7PositionLabel")
        self.m7AngleBtn = QtWidgets.QPushButton(self.m7CFrame)
        self.m7AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m7AngleBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m7AngleBtn.setObjectName("m7AngleBtn")
        self.m7PositionBtn = QtWidgets.QPushButton(self.m7CFrame)
        self.m7PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m7PositionBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m7PositionBtn.setObjectName("m7PositionBtn")
        self.m7HomeBtn = QtWidgets.QPushButton(self.m7CFrame)
        self.m7HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m7HomeBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m7HomeBtn.setObjectName("m7HomeBtn")
        self.m7SFrame = QtWidgets.QFrame(self.m7Page)
        self.m7SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m7SFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m7SFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m7SFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m7SFrame.setObjectName("m7SFrame")
        self.m7AngLabel = QtWidgets.QLabel(self.m7SFrame)
        self.m7AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m7AngLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m7AngLabel.setObjectName("m7AngLabel")
        self.m7PosLabel = QtWidgets.QLabel(self.m7SFrame)
        self.m7PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m7PosLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m7PosLabel.setObjectName("m7PosLabel")
        self.m7TorqueLabel = QtWidgets.QLabel(self.m7SFrame)
        self.m7TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m7TorqueLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m7TorqueLabel.setObjectName("m7TorqueLabel")
        self.m7TempLabel = QtWidgets.QLabel(self.m7SFrame)
        self.m7TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m7TempLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m7TempLabel.setObjectName("m7TempLabel")
        self.m7ErrLabel = QtWidgets.QLabel(self.m7SFrame)
        self.m7ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m7ErrLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m7ErrLabel.setObjectName("m7ErrLabel")
        self.m7AngDial = QtWidgets.QDial(self.m7SFrame)
        self.m7AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m7AngDial.setMinimum(-150)
        self.m7AngDial.setMaximum(150)
        self.m7AngDial.setTracking(True)
        self.m7AngDial.setWrapping(False)
        self.m7AngDial.setNotchTarget(50.0)
        self.m7AngDial.setNotchesVisible(True)
        self.m7AngDial.setObjectName("m7AngDial")
        self.m7PosDial = QtWidgets.QDial(self.m7SFrame)
        self.m7PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m7PosDial.setMinimum(0)
        self.m7PosDial.setMaximum(1023)
        self.m7PosDial.setTracking(True)
        self.m7PosDial.setWrapping(False)
        self.m7PosDial.setNotchTarget(100.0)
        self.m7PosDial.setNotchesVisible(True)
        self.m7PosDial.setObjectName("m7PosDial")
        self.m7AngNum = QtWidgets.QLabel(self.m7SFrame)
        self.m7AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m7AngNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m7AngNum.setObjectName("m7AngNum")
        self.m7PosNum = QtWidgets.QLabel(self.m7SFrame)
        self.m7PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m7PosNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m7PosNum.setObjectName("m7PosNum")
        self.m7TorqueNum = QtWidgets.QLabel(self.m7SFrame)
        self.m7TorqueNum.setGeometry(QtCore.QRect(120, 320, 61, 21))
        self.m7TorqueNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m7TorqueNum.setObjectName("m7TorqueNum")
        self.m7ErrNum = QtWidgets.QLabel(self.m7SFrame)
        self.m7ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m7ErrNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m7ErrNum.setObjectName("m7ErrNum")
        self.m7TempNum = QtWidgets.QLabel(self.m7SFrame)
        self.m7TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m7TempNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m7TempNum.setObjectName("m7TempNum")
        self.stackedWidget.addWidget(self.m7Page)
        self.m8Page = QtWidgets.QWidget()
        self.m8Page.setObjectName("m8Page")
        self.m8SFrame = QtWidgets.QFrame(self.m8Page)
        self.m8SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m8SFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m8SFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m8SFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m8SFrame.setObjectName("m8SFrame")
        self.m8AngLabel = QtWidgets.QLabel(self.m8SFrame)
        self.m8AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m8AngLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m8AngLabel.setObjectName("m8AngLabel")
        self.m8PosLabel = QtWidgets.QLabel(self.m8SFrame)
        self.m8PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m8PosLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m8PosLabel.setObjectName("m8PosLabel")
        self.m8TorqueLabel = QtWidgets.QLabel(self.m8SFrame)
        self.m8TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m8TorqueLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m8TorqueLabel.setObjectName("m8TorqueLabel")
        self.m8TempLabel = QtWidgets.QLabel(self.m8SFrame)
        self.m8TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m8TempLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m8TempLabel.setObjectName("m8TempLabel")
        self.m8ErrLabel = QtWidgets.QLabel(self.m8SFrame)
        self.m8ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m8ErrLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m8ErrLabel.setObjectName("m8ErrLabel")
        self.m8AngDial = QtWidgets.QDial(self.m8SFrame)
        self.m8AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m8AngDial.setMinimum(-150)
        self.m8AngDial.setMaximum(150)
        self.m8AngDial.setTracking(True)
        self.m8AngDial.setWrapping(False)
        self.m8AngDial.setNotchTarget(50.0)
        self.m8AngDial.setNotchesVisible(True)
        self.m8AngDial.setObjectName("m8AngDial")
        self.m8PosDial = QtWidgets.QDial(self.m8SFrame)
        self.m8PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m8PosDial.setMinimum(0)
        self.m8PosDial.setMaximum(1023)
        self.m8PosDial.setTracking(True)
        self.m8PosDial.setWrapping(False)
        self.m8PosDial.setNotchTarget(100.0)
        self.m8PosDial.setNotchesVisible(True)
        self.m8PosDial.setObjectName("m8PosDial")
        self.m8AngNum = QtWidgets.QLabel(self.m8SFrame)
        self.m8AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m8AngNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m8AngNum.setObjectName("m8AngNum")
        self.m8PosNum = QtWidgets.QLabel(self.m8SFrame)
        self.m8PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m8PosNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m8PosNum.setObjectName("m8PosNum")
        self.m8TorqueNum = QtWidgets.QLabel(self.m8SFrame)
        self.m8TorqueNum.setGeometry(QtCore.QRect(120, 320, 61, 21))
        self.m8TorqueNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m8TorqueNum.setObjectName("m8TorqueNum")
        self.m8ErrNum = QtWidgets.QLabel(self.m8SFrame)
        self.m8ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m8ErrNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m8ErrNum.setObjectName("m8ErrNum")
        self.m8TempNum = QtWidgets.QLabel(self.m8SFrame)
        self.m8TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m8TempNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m8TempNum.setObjectName("m8TempNum")
        self.m8Label = QtWidgets.QLabel(self.m8Page)
        self.m8Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m8Label.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m8Label.setObjectName("m8Label")
        self.m8CFrame = QtWidgets.QFrame(self.m8Page)
        self.m8CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m8CFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m8CFrame.setObjectName("m8CFrame")
        self.m8GoalTSpin = QtWidgets.QSpinBox(self.m8CFrame)
        self.m8GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m8GoalTSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m8GoalTSpin.setWrapping(False)
        self.m8GoalTSpin.setAccelerated(False)
        self.m8GoalTSpin.setObjectName("m8GoalTSpin")
        self.m8GoalTLabel = QtWidgets.QLabel(self.m8CFrame)
        self.m8GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m8GoalTLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m8GoalTLabel.setObjectName("m8GoalTLabel")
        self.m8UpdateBtn = QtWidgets.QPushButton(self.m8CFrame)
        self.m8UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m8UpdateBtn.setAutoFillBackground(False)
        self.m8UpdateBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m8UpdateBtn.setAutoDefault(False)
        self.m8UpdateBtn.setDefault(False)
        self.m8UpdateBtn.setFlat(False)
        self.m8UpdateBtn.setObjectName("m8UpdateBtn")
        self.m8AngleLabel = QtWidgets.QLabel(self.m8CFrame)
        self.m8AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m8AngleLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m8AngleLabel.setObjectName("m8AngleLabel")
        self.m8AngleSpin = QtWidgets.QSpinBox(self.m8CFrame)
        self.m8AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m8AngleSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m8AngleSpin.setWrapping(False)
        self.m8AngleSpin.setAccelerated(False)
        self.m8AngleSpin.setMinimum(-150)
        self.m8AngleSpin.setMaximum(150)
        self.m8AngleSpin.setObjectName("m8AngleSpin")
        self.m8PositionSpin = QtWidgets.QSpinBox(self.m8CFrame)
        self.m8PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m8PositionSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m8PositionSpin.setWrapping(False)
        self.m8PositionSpin.setAccelerated(False)
        self.m8PositionSpin.setMaximum(1023)
        self.m8PositionSpin.setObjectName("m8PositionSpin")
        self.m8PositionLabel = QtWidgets.QLabel(self.m8CFrame)
        self.m8PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m8PositionLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m8PositionLabel.setObjectName("m8PositionLabel")
        self.m8AngleBtn = QtWidgets.QPushButton(self.m8CFrame)
        self.m8AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m8AngleBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m8AngleBtn.setObjectName("m8AngleBtn")
        self.m8PositionBtn = QtWidgets.QPushButton(self.m8CFrame)
        self.m8PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m8PositionBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m8PositionBtn.setObjectName("m8PositionBtn")
        self.m8HomeBtn = QtWidgets.QPushButton(self.m8CFrame)
        self.m8HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m8HomeBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m8HomeBtn.setObjectName("m8HomeBtn")
        self.stackedWidget.addWidget(self.m8Page)
        self.m9Page = QtWidgets.QWidget()
        self.m9Page.setObjectName("m9Page")
        self.m9Label = QtWidgets.QLabel(self.m9Page)
        self.m9Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m9Label.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m9Label.setObjectName("m9Label")
        self.m9CFrame = QtWidgets.QFrame(self.m9Page)
        self.m9CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m9CFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m9CFrame.setObjectName("m9CFrame")
        self.m9GoalTSpin = QtWidgets.QSpinBox(self.m9CFrame)
        self.m9GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m9GoalTSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m9GoalTSpin.setWrapping(False)
        self.m9GoalTSpin.setAccelerated(False)
        self.m9GoalTSpin.setObjectName("m9GoalTSpin")
        self.m9GoalTLabel = QtWidgets.QLabel(self.m9CFrame)
        self.m9GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m9GoalTLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m9GoalTLabel.setObjectName("m9GoalTLabel")
        self.m9UpdateBtn = QtWidgets.QPushButton(self.m9CFrame)
        self.m9UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m9UpdateBtn.setAutoFillBackground(False)
        self.m9UpdateBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m9UpdateBtn.setAutoDefault(False)
        self.m9UpdateBtn.setDefault(False)
        self.m9UpdateBtn.setFlat(False)
        self.m9UpdateBtn.setObjectName("m9UpdateBtn")
        self.m9AngleLabel = QtWidgets.QLabel(self.m9CFrame)
        self.m9AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m9AngleLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m9AngleLabel.setObjectName("m9AngleLabel")
        self.m9AngleSpin = QtWidgets.QSpinBox(self.m9CFrame)
        self.m9AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m9AngleSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m9AngleSpin.setWrapping(False)
        self.m9AngleSpin.setAccelerated(False)
        self.m9AngleSpin.setMinimum(-150)
        self.m9AngleSpin.setMaximum(150)
        self.m9AngleSpin.setObjectName("m9AngleSpin")
        self.m9PositionSpin = QtWidgets.QSpinBox(self.m9CFrame)
        self.m9PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m9PositionSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m9PositionSpin.setWrapping(False)
        self.m9PositionSpin.setAccelerated(False)
        self.m9PositionSpin.setMaximum(1023)
        self.m9PositionSpin.setObjectName("m9PositionSpin")
        self.m9PositionLabel = QtWidgets.QLabel(self.m9CFrame)
        self.m9PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m9PositionLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m9PositionLabel.setObjectName("m9PositionLabel")
        self.m9AngleBtn = QtWidgets.QPushButton(self.m9CFrame)
        self.m9AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m9AngleBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m9AngleBtn.setObjectName("m9AngleBtn")
        self.m9PositionBtn = QtWidgets.QPushButton(self.m9CFrame)
        self.m9PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m9PositionBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m9PositionBtn.setObjectName("m9PositionBtn")
        self.m9HomeBtn = QtWidgets.QPushButton(self.m9CFrame)
        self.m9HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m9HomeBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m9HomeBtn.setObjectName("m9HomeBtn")
        self.m9SFrame = QtWidgets.QFrame(self.m9Page)
        self.m9SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m9SFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m9SFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m9SFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m9SFrame.setObjectName("m9SFrame")
        self.m9AngLabel = QtWidgets.QLabel(self.m9SFrame)
        self.m9AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m9AngLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m9AngLabel.setObjectName("m9AngLabel")
        self.m9PosLabel = QtWidgets.QLabel(self.m9SFrame)
        self.m9PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m9PosLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m9PosLabel.setObjectName("m9PosLabel")
        self.m9TorqueLabel = QtWidgets.QLabel(self.m9SFrame)
        self.m9TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m9TorqueLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m9TorqueLabel.setObjectName("m9TorqueLabel")
        self.m9TempLabel = QtWidgets.QLabel(self.m9SFrame)
        self.m9TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m9TempLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m9TempLabel.setObjectName("m9TempLabel")
        self.m9ErrLabel = QtWidgets.QLabel(self.m9SFrame)
        self.m9ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m9ErrLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m9ErrLabel.setObjectName("m9ErrLabel")
        self.m9AngDial = QtWidgets.QDial(self.m9SFrame)
        self.m9AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m9AngDial.setMinimum(-150)
        self.m9AngDial.setMaximum(150)
        self.m9AngDial.setTracking(True)
        self.m9AngDial.setWrapping(False)
        self.m9AngDial.setNotchTarget(50.0)
        self.m9AngDial.setNotchesVisible(True)
        self.m9AngDial.setObjectName("m9AngDial")
        self.m9PosDial = QtWidgets.QDial(self.m9SFrame)
        self.m9PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m9PosDial.setMinimum(0)
        self.m9PosDial.setMaximum(1023)
        self.m9PosDial.setTracking(True)
        self.m9PosDial.setWrapping(False)
        self.m9PosDial.setNotchTarget(100.0)
        self.m9PosDial.setNotchesVisible(True)
        self.m9PosDial.setObjectName("m9PosDial")
        self.m9AngNum = QtWidgets.QLabel(self.m9SFrame)
        self.m9AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m9AngNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m9AngNum.setObjectName("m9AngNum")
        self.m9PosNum = QtWidgets.QLabel(self.m9SFrame)
        self.m9PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m9PosNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m9PosNum.setObjectName("m9PosNum")
        self.m9TorqueNum = QtWidgets.QLabel(self.m9SFrame)
        self.m9TorqueNum.setGeometry(QtCore.QRect(120, 320, 61, 21))
        self.m9TorqueNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m9TorqueNum.setObjectName("m9TorqueNum")
        self.m9ErrNum = QtWidgets.QLabel(self.m9SFrame)
        self.m9ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m9ErrNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m9ErrNum.setObjectName("m9ErrNum")
        self.m9TempNum = QtWidgets.QLabel(self.m9SFrame)
        self.m9TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m9TempNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m9TempNum.setObjectName("m9TempNum")
        self.stackedWidget.addWidget(self.m9Page)
        self.m10Page = QtWidgets.QWidget()
        self.m10Page.setObjectName("m10Page")
        self.m10Label = QtWidgets.QLabel(self.m10Page)
        self.m10Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m10Label.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m10Label.setObjectName("m10Label")
        self.m10CFrame = QtWidgets.QFrame(self.m10Page)
        self.m10CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m10CFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m10CFrame.setObjectName("m10CFrame")
        self.m10GoalTSpin = QtWidgets.QSpinBox(self.m10CFrame)
        self.m10GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m10GoalTSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m10GoalTSpin.setWrapping(False)
        self.m10GoalTSpin.setAccelerated(False)
        self.m10GoalTSpin.setObjectName("m10GoalTSpin")
        self.m10GoalTLabel = QtWidgets.QLabel(self.m10CFrame)
        self.m10GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m10GoalTLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m10GoalTLabel.setObjectName("m10GoalTLabel")
        self.m10UpdateBtn = QtWidgets.QPushButton(self.m10CFrame)
        self.m10UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m10UpdateBtn.setAutoFillBackground(False)
        self.m10UpdateBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m10UpdateBtn.setAutoDefault(False)
        self.m10UpdateBtn.setDefault(False)
        self.m10UpdateBtn.setFlat(False)
        self.m10UpdateBtn.setObjectName("m10UpdateBtn")
        self.m10AngleLabel = QtWidgets.QLabel(self.m10CFrame)
        self.m10AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m10AngleLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m10AngleLabel.setObjectName("m10AngleLabel")
        self.m10AngleSpin = QtWidgets.QSpinBox(self.m10CFrame)
        self.m10AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m10AngleSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m10AngleSpin.setWrapping(False)
        self.m10AngleSpin.setAccelerated(False)
        self.m10AngleSpin.setMinimum(-150)
        self.m10AngleSpin.setMaximum(150)
        self.m10AngleSpin.setObjectName("m10AngleSpin")
        self.m10PositionSpin = QtWidgets.QSpinBox(self.m10CFrame)
        self.m10PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m10PositionSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m10PositionSpin.setWrapping(False)
        self.m10PositionSpin.setAccelerated(False)
        self.m10PositionSpin.setMaximum(1023)
        self.m10PositionSpin.setObjectName("m10PositionSpin")
        self.m10PositionLabel = QtWidgets.QLabel(self.m10CFrame)
        self.m10PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m10PositionLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m10PositionLabel.setObjectName("m10PositionLabel")
        self.m10AngleBtn = QtWidgets.QPushButton(self.m10CFrame)
        self.m10AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m10AngleBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m10AngleBtn.setObjectName("m10AngleBtn")
        self.m10PositionBtn = QtWidgets.QPushButton(self.m10CFrame)
        self.m10PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m10PositionBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m10PositionBtn.setObjectName("m10PositionBtn")
        self.m10HomeBtn = QtWidgets.QPushButton(self.m10CFrame)
        self.m10HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m10HomeBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m10HomeBtn.setObjectName("m10HomeBtn")
        self.m10SFrame = QtWidgets.QFrame(self.m10Page)
        self.m10SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m10SFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m10SFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m10SFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m10SFrame.setObjectName("m10SFrame")
        self.m10AngLabel = QtWidgets.QLabel(self.m10SFrame)
        self.m10AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m10AngLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m10AngLabel.setObjectName("m10AngLabel")
        self.m10PosLabel = QtWidgets.QLabel(self.m10SFrame)
        self.m10PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m10PosLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m10PosLabel.setObjectName("m10PosLabel")
        self.m10TorqueLabel = QtWidgets.QLabel(self.m10SFrame)
        self.m10TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m10TorqueLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m10TorqueLabel.setObjectName("m10TorqueLabel")
        self.m10TempLabel = QtWidgets.QLabel(self.m10SFrame)
        self.m10TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m10TempLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m10TempLabel.setObjectName("m10TempLabel")
        self.m10ErrLabel = QtWidgets.QLabel(self.m10SFrame)
        self.m10ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m10ErrLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m10ErrLabel.setObjectName("m10ErrLabel")
        self.m10AngDial = QtWidgets.QDial(self.m10SFrame)
        self.m10AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m10AngDial.setMinimum(-150)
        self.m10AngDial.setMaximum(150)
        self.m10AngDial.setTracking(True)
        self.m10AngDial.setWrapping(False)
        self.m10AngDial.setNotchTarget(50.0)
        self.m10AngDial.setNotchesVisible(True)
        self.m10AngDial.setObjectName("m10AngDial")
        self.m10PosDial = QtWidgets.QDial(self.m10SFrame)
        self.m10PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m10PosDial.setMinimum(0)
        self.m10PosDial.setMaximum(1023)
        self.m10PosDial.setTracking(True)
        self.m10PosDial.setWrapping(False)
        self.m10PosDial.setNotchTarget(100.0)
        self.m10PosDial.setNotchesVisible(True)
        self.m10PosDial.setObjectName("m10PosDial")
        self.m10AngNum = QtWidgets.QLabel(self.m10SFrame)
        self.m10AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m10AngNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m10AngNum.setObjectName("m10AngNum")
        self.m10PosNum = QtWidgets.QLabel(self.m10SFrame)
        self.m10PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m10PosNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m10PosNum.setObjectName("m10PosNum")
        self.m10TorqueNum = QtWidgets.QLabel(self.m10SFrame)
        self.m10TorqueNum.setGeometry(QtCore.QRect(120, 320, 61, 21))
        self.m10TorqueNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m10TorqueNum.setObjectName("m10TorqueNum")
        self.m10ErrNum = QtWidgets.QLabel(self.m10SFrame)
        self.m10ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m10ErrNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m10ErrNum.setObjectName("m10ErrNum")
        self.m10TempNum = QtWidgets.QLabel(self.m10SFrame)
        self.m10TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m10TempNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m10TempNum.setObjectName("m10TempNum")
        self.stackedWidget.addWidget(self.m10Page)
        self.m11Page = QtWidgets.QWidget()
        self.m11Page.setObjectName("m11Page")
        self.m11Label = QtWidgets.QLabel(self.m11Page)
        self.m11Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m11Label.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m11Label.setObjectName("m11Label")
        self.m11CFrame = QtWidgets.QFrame(self.m11Page)
        self.m11CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m11CFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m11CFrame.setObjectName("m11CFrame")
        self.m11GoalTSpin = QtWidgets.QSpinBox(self.m11CFrame)
        self.m11GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m11GoalTSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m11GoalTSpin.setWrapping(False)
        self.m11GoalTSpin.setAccelerated(False)
        self.m11GoalTSpin.setObjectName("m11GoalTSpin")
        self.m11GoalTLabel = QtWidgets.QLabel(self.m11CFrame)
        self.m11GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m11GoalTLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m11GoalTLabel.setObjectName("m11GoalTLabel")
        self.m11UpdateBtn = QtWidgets.QPushButton(self.m11CFrame)
        self.m11UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m11UpdateBtn.setAutoFillBackground(False)
        self.m11UpdateBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m11UpdateBtn.setAutoDefault(False)
        self.m11UpdateBtn.setDefault(False)
        self.m11UpdateBtn.setFlat(False)
        self.m11UpdateBtn.setObjectName("m11UpdateBtn")
        self.m11AngleLabel = QtWidgets.QLabel(self.m11CFrame)
        self.m11AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m11AngleLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m11AngleLabel.setObjectName("m11AngleLabel")
        self.m11AngleSpin = QtWidgets.QSpinBox(self.m11CFrame)
        self.m11AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m11AngleSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m11AngleSpin.setWrapping(False)
        self.m11AngleSpin.setAccelerated(False)
        self.m11AngleSpin.setMinimum(-150)
        self.m11AngleSpin.setMaximum(150)
        self.m11AngleSpin.setObjectName("m11AngleSpin")
        self.m11PositionSpin = QtWidgets.QSpinBox(self.m11CFrame)
        self.m11PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m11PositionSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m11PositionSpin.setWrapping(False)
        self.m11PositionSpin.setAccelerated(False)
        self.m11PositionSpin.setMaximum(1023)
        self.m11PositionSpin.setObjectName("m11PositionSpin")
        self.m11PositionLabel = QtWidgets.QLabel(self.m11CFrame)
        self.m11PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m11PositionLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m11PositionLabel.setObjectName("m11PositionLabel")
        self.m11AngleBtn = QtWidgets.QPushButton(self.m11CFrame)
        self.m11AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m11AngleBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m11AngleBtn.setObjectName("m11AngleBtn")
        self.m11PositionBtn = QtWidgets.QPushButton(self.m11CFrame)
        self.m11PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m11PositionBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m11PositionBtn.setObjectName("m11PositionBtn")
        self.m11HomeBtn = QtWidgets.QPushButton(self.m11CFrame)
        self.m11HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m11HomeBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m11HomeBtn.setObjectName("m11HomeBtn")
        self.m11SFrame = QtWidgets.QFrame(self.m11Page)
        self.m11SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m11SFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m11SFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m11SFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m11SFrame.setObjectName("m11SFrame")
        self.m11AngLabel = QtWidgets.QLabel(self.m11SFrame)
        self.m11AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m11AngLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m11AngLabel.setObjectName("m11AngLabel")
        self.m11PosLabel = QtWidgets.QLabel(self.m11SFrame)
        self.m11PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m11PosLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m11PosLabel.setObjectName("m11PosLabel")
        self.m11TorqueLabel = QtWidgets.QLabel(self.m11SFrame)
        self.m11TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m11TorqueLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m11TorqueLabel.setObjectName("m11TorqueLabel")
        self.m11TempLabel = QtWidgets.QLabel(self.m11SFrame)
        self.m11TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m11TempLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m11TempLabel.setObjectName("m11TempLabel")
        self.m11ErrLabel = QtWidgets.QLabel(self.m11SFrame)
        self.m11ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m11ErrLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m11ErrLabel.setObjectName("m11ErrLabel")
        self.m11AngDial = QtWidgets.QDial(self.m11SFrame)
        self.m11AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m11AngDial.setMinimum(-150)
        self.m11AngDial.setMaximum(150)
        self.m11AngDial.setTracking(True)
        self.m11AngDial.setWrapping(False)
        self.m11AngDial.setNotchTarget(50.0)
        self.m11AngDial.setNotchesVisible(True)
        self.m11AngDial.setObjectName("m11AngDial")
        self.m11PosDial = QtWidgets.QDial(self.m11SFrame)
        self.m11PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m11PosDial.setMinimum(0)
        self.m11PosDial.setMaximum(1023)
        self.m11PosDial.setTracking(True)
        self.m11PosDial.setWrapping(False)
        self.m11PosDial.setNotchTarget(100.0)
        self.m11PosDial.setNotchesVisible(True)
        self.m11PosDial.setObjectName("m11PosDial")
        self.m11AngNum = QtWidgets.QLabel(self.m11SFrame)
        self.m11AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m11AngNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m11AngNum.setObjectName("m11AngNum")
        self.m11PosNum = QtWidgets.QLabel(self.m11SFrame)
        self.m11PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m11PosNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m11PosNum.setObjectName("m11PosNum")
        self.m11TorqueNum = QtWidgets.QLabel(self.m11SFrame)
        self.m11TorqueNum.setGeometry(QtCore.QRect(120, 320, 61, 21))
        self.m11TorqueNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m11TorqueNum.setObjectName("m11TorqueNum")
        self.m11ErrNum = QtWidgets.QLabel(self.m11SFrame)
        self.m11ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m11ErrNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m11ErrNum.setObjectName("m11ErrNum")
        self.m11TempNum = QtWidgets.QLabel(self.m11SFrame)
        self.m11TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m11TempNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m11TempNum.setObjectName("m11TempNum")
        self.stackedWidget.addWidget(self.m11Page)
        self.m12Page = QtWidgets.QWidget()
        self.m12Page.setObjectName("m12Page")
        self.m12Label = QtWidgets.QLabel(self.m12Page)
        self.m12Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m12Label.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m12Label.setObjectName("m12Label")
        self.m1CFrame_2 = QtWidgets.QFrame(self.m12Page)
        self.m1CFrame_2.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m1CFrame_2.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m1CFrame_2.setObjectName("m1CFrame_2")
        self.m12GoalTSpin = QtWidgets.QSpinBox(self.m1CFrame_2)
        self.m12GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m12GoalTSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m12GoalTSpin.setWrapping(False)
        self.m12GoalTSpin.setAccelerated(False)
        self.m12GoalTSpin.setObjectName("m12GoalTSpin")
        self.m12GoalTLabel = QtWidgets.QLabel(self.m1CFrame_2)
        self.m12GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m12GoalTLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m12GoalTLabel.setObjectName("m12GoalTLabel")
        self.m12UpdateBtn = QtWidgets.QPushButton(self.m1CFrame_2)
        self.m12UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m12UpdateBtn.setAutoFillBackground(False)
        self.m12UpdateBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m12UpdateBtn.setAutoDefault(False)
        self.m12UpdateBtn.setDefault(False)
        self.m12UpdateBtn.setFlat(False)
        self.m12UpdateBtn.setObjectName("m12UpdateBtn")
        self.m12AngleLabel = QtWidgets.QLabel(self.m1CFrame_2)
        self.m12AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m12AngleLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m12AngleLabel.setObjectName("m12AngleLabel")
        self.m12AngleSpin = QtWidgets.QSpinBox(self.m1CFrame_2)
        self.m12AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m12AngleSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m12AngleSpin.setWrapping(False)
        self.m12AngleSpin.setAccelerated(False)
        self.m12AngleSpin.setMinimum(-150)
        self.m12AngleSpin.setMaximum(150)
        self.m12AngleSpin.setObjectName("m12AngleSpin")
        self.m12PositionSpin = QtWidgets.QSpinBox(self.m1CFrame_2)
        self.m12PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m12PositionSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m12PositionSpin.setWrapping(False)
        self.m12PositionSpin.setAccelerated(False)
        self.m12PositionSpin.setMaximum(1023)
        self.m12PositionSpin.setObjectName("m12PositionSpin")
        self.m12PositionLabel = QtWidgets.QLabel(self.m1CFrame_2)
        self.m12PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m12PositionLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m12PositionLabel.setObjectName("m12PositionLabel")
        self.m12AngleBtn = QtWidgets.QPushButton(self.m1CFrame_2)
        self.m12AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m12AngleBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m12AngleBtn.setObjectName("m12AngleBtn")
        self.m12PositionBtn = QtWidgets.QPushButton(self.m1CFrame_2)
        self.m12PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m12PositionBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m12PositionBtn.setObjectName("m12PositionBtn")
        self.m12HomeBtn = QtWidgets.QPushButton(self.m1CFrame_2)
        self.m12HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m12HomeBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m12HomeBtn.setObjectName("m12HomeBtn")
        self.m12SFrame = QtWidgets.QFrame(self.m12Page)
        self.m12SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m12SFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m12SFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m12SFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m12SFrame.setObjectName("m12SFrame")
        self.m12AngLabel = QtWidgets.QLabel(self.m12SFrame)
        self.m12AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m12AngLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m12AngLabel.setObjectName("m12AngLabel")
        self.m12PosLabel = QtWidgets.QLabel(self.m12SFrame)
        self.m12PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m12PosLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m12PosLabel.setObjectName("m12PosLabel")
        self.m12TorqueLabel = QtWidgets.QLabel(self.m12SFrame)
        self.m12TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m12TorqueLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m12TorqueLabel.setObjectName("m12TorqueLabel")
        self.m12TempLabel = QtWidgets.QLabel(self.m12SFrame)
        self.m12TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m12TempLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m12TempLabel.setObjectName("m12TempLabel")
        self.m12ErrLabel = QtWidgets.QLabel(self.m12SFrame)
        self.m12ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m12ErrLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m12ErrLabel.setObjectName("m12ErrLabel")
        self.m12AngDial = QtWidgets.QDial(self.m12SFrame)
        self.m12AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m12AngDial.setMinimum(-150)
        self.m12AngDial.setMaximum(150)
        self.m12AngDial.setTracking(True)
        self.m12AngDial.setWrapping(False)
        self.m12AngDial.setNotchTarget(50.0)
        self.m12AngDial.setNotchesVisible(True)
        self.m12AngDial.setObjectName("m12AngDial")
        self.m12PosDial = QtWidgets.QDial(self.m12SFrame)
        self.m12PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m12PosDial.setMinimum(0)
        self.m12PosDial.setMaximum(1023)
        self.m12PosDial.setTracking(True)
        self.m12PosDial.setWrapping(False)
        self.m12PosDial.setNotchTarget(100.0)
        self.m12PosDial.setNotchesVisible(True)
        self.m12PosDial.setObjectName("m12PosDial")
        self.m12AngNum = QtWidgets.QLabel(self.m12SFrame)
        self.m12AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m12AngNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m12AngNum.setObjectName("m12AngNum")
        self.m12PosNum = QtWidgets.QLabel(self.m12SFrame)
        self.m12PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m12PosNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m12PosNum.setObjectName("m12PosNum")
        self.m12TorqueNum = QtWidgets.QLabel(self.m12SFrame)
        self.m12TorqueNum.setGeometry(QtCore.QRect(120, 320, 61, 21))
        self.m12TorqueNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m12TorqueNum.setObjectName("m12TorqueNum")
        self.m12ErrNum = QtWidgets.QLabel(self.m12SFrame)
        self.m12ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m12ErrNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m12ErrNum.setObjectName("m12ErrNum")
        self.m12TempNum = QtWidgets.QLabel(self.m12SFrame)
        self.m12TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m12TempNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m12TempNum.setObjectName("m12TempNum")
        self.stackedWidget.addWidget(self.m12Page)
        self.m13Page = QtWidgets.QWidget()
        self.m13Page.setObjectName("m13Page")
        self.m13Label = QtWidgets.QLabel(self.m13Page)
        self.m13Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m13Label.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m13Label.setObjectName("m13Label")
        self.m13CFrame = QtWidgets.QFrame(self.m13Page)
        self.m13CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m13CFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m13CFrame.setObjectName("m13CFrame")
        self.m13GoalTSpin = QtWidgets.QSpinBox(self.m13CFrame)
        self.m13GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m13GoalTSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m13GoalTSpin.setWrapping(False)
        self.m13GoalTSpin.setAccelerated(False)
        self.m13GoalTSpin.setObjectName("m13GoalTSpin")
        self.m13GoalTLabel = QtWidgets.QLabel(self.m13CFrame)
        self.m13GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m13GoalTLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m13GoalTLabel.setObjectName("m13GoalTLabel")
        self.m13UpdateBtn = QtWidgets.QPushButton(self.m13CFrame)
        self.m13UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m13UpdateBtn.setAutoFillBackground(False)
        self.m13UpdateBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m13UpdateBtn.setAutoDefault(False)
        self.m13UpdateBtn.setDefault(False)
        self.m13UpdateBtn.setFlat(False)
        self.m13UpdateBtn.setObjectName("m13UpdateBtn")
        self.m13AngleLabel = QtWidgets.QLabel(self.m13CFrame)
        self.m13AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m13AngleLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m13AngleLabel.setObjectName("m13AngleLabel")
        self.m13AngleSpin = QtWidgets.QSpinBox(self.m13CFrame)
        self.m13AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m13AngleSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m13AngleSpin.setWrapping(False)
        self.m13AngleSpin.setAccelerated(False)
        self.m13AngleSpin.setMinimum(-150)
        self.m13AngleSpin.setMaximum(150)
        self.m13AngleSpin.setObjectName("m13AngleSpin")
        self.m13PositionSpin = QtWidgets.QSpinBox(self.m13CFrame)
        self.m13PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m13PositionSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m13PositionSpin.setWrapping(False)
        self.m13PositionSpin.setAccelerated(False)
        self.m13PositionSpin.setMaximum(1023)
        self.m13PositionSpin.setObjectName("m13PositionSpin")
        self.m13PositionLabel = QtWidgets.QLabel(self.m13CFrame)
        self.m13PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m13PositionLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m13PositionLabel.setObjectName("m13PositionLabel")
        self.m13AngleBtn = QtWidgets.QPushButton(self.m13CFrame)
        self.m13AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m13AngleBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m13AngleBtn.setObjectName("m13AngleBtn")
        self.m13PositionBtn = QtWidgets.QPushButton(self.m13CFrame)
        self.m13PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m13PositionBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m13PositionBtn.setObjectName("m13PositionBtn")
        self.m13HomeBtn = QtWidgets.QPushButton(self.m13CFrame)
        self.m13HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m13HomeBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m13HomeBtn.setObjectName("m13HomeBtn")
        self.m13SFrame = QtWidgets.QFrame(self.m13Page)
        self.m13SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m13SFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m13SFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m13SFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m13SFrame.setObjectName("m13SFrame")
        self.m13AngLabel = QtWidgets.QLabel(self.m13SFrame)
        self.m13AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m13AngLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m13AngLabel.setObjectName("m13AngLabel")
        self.m13PosLabel = QtWidgets.QLabel(self.m13SFrame)
        self.m13PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m13PosLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m13PosLabel.setObjectName("m13PosLabel")
        self.m13TorqueLabel = QtWidgets.QLabel(self.m13SFrame)
        self.m13TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m13TorqueLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m13TorqueLabel.setObjectName("m13TorqueLabel")
        self.m13TempLabel = QtWidgets.QLabel(self.m13SFrame)
        self.m13TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m13TempLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m13TempLabel.setObjectName("m13TempLabel")
        self.m13ErrLabel = QtWidgets.QLabel(self.m13SFrame)
        self.m13ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m13ErrLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m13ErrLabel.setObjectName("m13ErrLabel")
        self.m13AngDial = QtWidgets.QDial(self.m13SFrame)
        self.m13AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m13AngDial.setMinimum(-150)
        self.m13AngDial.setMaximum(150)
        self.m13AngDial.setTracking(True)
        self.m13AngDial.setWrapping(False)
        self.m13AngDial.setNotchTarget(50.0)
        self.m13AngDial.setNotchesVisible(True)
        self.m13AngDial.setObjectName("m13AngDial")
        self.m13PosDial = QtWidgets.QDial(self.m13SFrame)
        self.m13PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m13PosDial.setMinimum(0)
        self.m13PosDial.setMaximum(1023)
        self.m13PosDial.setTracking(True)
        self.m13PosDial.setWrapping(False)
        self.m13PosDial.setNotchTarget(100.0)
        self.m13PosDial.setNotchesVisible(True)
        self.m13PosDial.setObjectName("m13PosDial")
        self.m13AngNum = QtWidgets.QLabel(self.m13SFrame)
        self.m13AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m13AngNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m13AngNum.setObjectName("m13AngNum")
        self.m13PosNum = QtWidgets.QLabel(self.m13SFrame)
        self.m13PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m13PosNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m13PosNum.setObjectName("m13PosNum")
        self.m13TorqueNum = QtWidgets.QLabel(self.m13SFrame)
        self.m13TorqueNum.setGeometry(QtCore.QRect(120, 320, 61, 21))
        self.m13TorqueNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m13TorqueNum.setObjectName("m13TorqueNum")
        self.m13ErrNum = QtWidgets.QLabel(self.m13SFrame)
        self.m13ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m13ErrNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m13ErrNum.setObjectName("m13ErrNum")
        self.m13TempNum = QtWidgets.QLabel(self.m13SFrame)
        self.m13TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m13TempNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m13TempNum.setObjectName("m13TempNum")
        self.stackedWidget.addWidget(self.m13Page)
        self.m14Page = QtWidgets.QWidget()
        self.m14Page.setObjectName("m14Page")
        self.m14Label = QtWidgets.QLabel(self.m14Page)
        self.m14Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m14Label.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m14Label.setObjectName("m14Label")
        self.m14CFrame = QtWidgets.QFrame(self.m14Page)
        self.m14CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m14CFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m14CFrame.setObjectName("m14CFrame")
        self.m14GoalTSpin = QtWidgets.QSpinBox(self.m14CFrame)
        self.m14GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m14GoalTSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m14GoalTSpin.setWrapping(False)
        self.m14GoalTSpin.setAccelerated(False)
        self.m14GoalTSpin.setObjectName("m14GoalTSpin")
        self.m14GoalTLabel = QtWidgets.QLabel(self.m14CFrame)
        self.m14GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m14GoalTLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m14GoalTLabel.setObjectName("m14GoalTLabel")
        self.m14UpdateBtn = QtWidgets.QPushButton(self.m14CFrame)
        self.m14UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m14UpdateBtn.setAutoFillBackground(False)
        self.m14UpdateBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m14UpdateBtn.setAutoDefault(False)
        self.m14UpdateBtn.setDefault(False)
        self.m14UpdateBtn.setFlat(False)
        self.m14UpdateBtn.setObjectName("m14UpdateBtn")
        self.m14AngleLabel = QtWidgets.QLabel(self.m14CFrame)
        self.m14AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m14AngleLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m14AngleLabel.setObjectName("m14AngleLabel")
        self.m14AngleSpin = QtWidgets.QSpinBox(self.m14CFrame)
        self.m14AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m14AngleSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m14AngleSpin.setWrapping(False)
        self.m14AngleSpin.setAccelerated(False)
        self.m14AngleSpin.setMinimum(-150)
        self.m14AngleSpin.setMaximum(150)
        self.m14AngleSpin.setObjectName("m14AngleSpin")
        self.m14PositionSpin = QtWidgets.QSpinBox(self.m14CFrame)
        self.m14PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m14PositionSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m14PositionSpin.setWrapping(False)
        self.m14PositionSpin.setAccelerated(False)
        self.m14PositionSpin.setMaximum(1023)
        self.m14PositionSpin.setObjectName("m14PositionSpin")
        self.m14PositionLabel = QtWidgets.QLabel(self.m14CFrame)
        self.m14PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m14PositionLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m14PositionLabel.setObjectName("m14PositionLabel")
        self.m14AngleBtn = QtWidgets.QPushButton(self.m14CFrame)
        self.m14AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m14AngleBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m14AngleBtn.setObjectName("m14AngleBtn")
        self.m14PositionBtn = QtWidgets.QPushButton(self.m14CFrame)
        self.m14PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m14PositionBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m14PositionBtn.setObjectName("m14PositionBtn")
        self.m14HomeBtn = QtWidgets.QPushButton(self.m14CFrame)
        self.m14HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m14HomeBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m14HomeBtn.setObjectName("m14HomeBtn")
        self.m14SFrame = QtWidgets.QFrame(self.m14Page)
        self.m14SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m14SFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m14SFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m14SFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m14SFrame.setObjectName("m14SFrame")
        self.m14AngLabel = QtWidgets.QLabel(self.m14SFrame)
        self.m14AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m14AngLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m14AngLabel.setObjectName("m14AngLabel")
        self.m14PosLabel = QtWidgets.QLabel(self.m14SFrame)
        self.m14PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m14PosLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m14PosLabel.setObjectName("m14PosLabel")
        self.m14TorqueLabel = QtWidgets.QLabel(self.m14SFrame)
        self.m14TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m14TorqueLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m14TorqueLabel.setObjectName("m14TorqueLabel")
        self.m14TempLabel = QtWidgets.QLabel(self.m14SFrame)
        self.m14TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m14TempLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m14TempLabel.setObjectName("m14TempLabel")
        self.m14ErrLabel = QtWidgets.QLabel(self.m14SFrame)
        self.m14ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m14ErrLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m14ErrLabel.setObjectName("m14ErrLabel")
        self.m14AngDial = QtWidgets.QDial(self.m14SFrame)
        self.m14AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m14AngDial.setMinimum(-150)
        self.m14AngDial.setMaximum(150)
        self.m14AngDial.setTracking(True)
        self.m14AngDial.setWrapping(False)
        self.m14AngDial.setNotchTarget(50.0)
        self.m14AngDial.setNotchesVisible(True)
        self.m14AngDial.setObjectName("m14AngDial")
        self.m14PosDial = QtWidgets.QDial(self.m14SFrame)
        self.m14PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m14PosDial.setMinimum(0)
        self.m14PosDial.setMaximum(1023)
        self.m14PosDial.setTracking(True)
        self.m14PosDial.setWrapping(False)
        self.m14PosDial.setNotchTarget(100.0)
        self.m14PosDial.setNotchesVisible(True)
        self.m14PosDial.setObjectName("m14PosDial")
        self.m14AngNum = QtWidgets.QLabel(self.m14SFrame)
        self.m14AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m14AngNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m14AngNum.setObjectName("m14AngNum")
        self.m14PosNum = QtWidgets.QLabel(self.m14SFrame)
        self.m14PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m14PosNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m14PosNum.setObjectName("m14PosNum")
        self.m14TorqueNum = QtWidgets.QLabel(self.m14SFrame)
        self.m14TorqueNum.setGeometry(QtCore.QRect(120, 320, 61, 21))
        self.m14TorqueNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m14TorqueNum.setObjectName("m14TorqueNum")
        self.m14ErrNum = QtWidgets.QLabel(self.m14SFrame)
        self.m14ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m14ErrNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m14ErrNum.setObjectName("m14ErrNum")
        self.m14TempNum = QtWidgets.QLabel(self.m14SFrame)
        self.m14TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m14TempNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m14TempNum.setObjectName("m14TempNum")
        self.stackedWidget.addWidget(self.m14Page)
        self.m15Page = QtWidgets.QWidget()
        self.m15Page.setObjectName("m15Page")
        self.m15Label = QtWidgets.QLabel(self.m15Page)
        self.m15Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m15Label.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m15Label.setObjectName("m15Label")
        self.m15CFrame = QtWidgets.QFrame(self.m15Page)
        self.m15CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m15CFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m15CFrame.setObjectName("m15CFrame")
        self.m15GoalTSpin = QtWidgets.QSpinBox(self.m15CFrame)
        self.m15GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m15GoalTSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m15GoalTSpin.setWrapping(False)
        self.m15GoalTSpin.setAccelerated(False)
        self.m15GoalTSpin.setObjectName("m15GoalTSpin")
        self.m15GoalTLabel = QtWidgets.QLabel(self.m15CFrame)
        self.m15GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m15GoalTLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m15GoalTLabel.setObjectName("m15GoalTLabel")
        self.m15UpdateBtn = QtWidgets.QPushButton(self.m15CFrame)
        self.m15UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m15UpdateBtn.setAutoFillBackground(False)
        self.m15UpdateBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m15UpdateBtn.setAutoDefault(False)
        self.m15UpdateBtn.setDefault(False)
        self.m15UpdateBtn.setFlat(False)
        self.m15UpdateBtn.setObjectName("m15UpdateBtn")
        self.m15AngleLabel = QtWidgets.QLabel(self.m15CFrame)
        self.m15AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m15AngleLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m15AngleLabel.setObjectName("m15AngleLabel")
        self.m15AngleSpin = QtWidgets.QSpinBox(self.m15CFrame)
        self.m15AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m15AngleSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m15AngleSpin.setWrapping(False)
        self.m15AngleSpin.setAccelerated(False)
        self.m15AngleSpin.setMinimum(-150)
        self.m15AngleSpin.setMaximum(150)
        self.m15AngleSpin.setObjectName("m15AngleSpin")
        self.m15PositionSpin = QtWidgets.QSpinBox(self.m15CFrame)
        self.m15PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m15PositionSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m15PositionSpin.setWrapping(False)
        self.m15PositionSpin.setAccelerated(False)
        self.m15PositionSpin.setMaximum(1023)
        self.m15PositionSpin.setObjectName("m15PositionSpin")
        self.m15PositionLabel = QtWidgets.QLabel(self.m15CFrame)
        self.m15PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m15PositionLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m15PositionLabel.setObjectName("m15PositionLabel")
        self.m15AngleBtn = QtWidgets.QPushButton(self.m15CFrame)
        self.m15AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m15AngleBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m15AngleBtn.setObjectName("m15AngleBtn")
        self.m15PositionBtn = QtWidgets.QPushButton(self.m15CFrame)
        self.m15PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m15PositionBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m15PositionBtn.setObjectName("m15PositionBtn")
        self.m15HomeBtn = QtWidgets.QPushButton(self.m15CFrame)
        self.m15HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m15HomeBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m15HomeBtn.setObjectName("m15HomeBtn")
        self.m15SFrame = QtWidgets.QFrame(self.m15Page)
        self.m15SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m15SFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m15SFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m15SFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m15SFrame.setObjectName("m15SFrame")
        self.m15AngLabel = QtWidgets.QLabel(self.m15SFrame)
        self.m15AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m15AngLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m15AngLabel.setObjectName("m15AngLabel")
        self.m15PosLabel = QtWidgets.QLabel(self.m15SFrame)
        self.m15PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m15PosLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m15PosLabel.setObjectName("m15PosLabel")
        self.m15TorqueLabel = QtWidgets.QLabel(self.m15SFrame)
        self.m15TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m15TorqueLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m15TorqueLabel.setObjectName("m15TorqueLabel")
        self.m15TempLabel = QtWidgets.QLabel(self.m15SFrame)
        self.m15TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m15TempLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m15TempLabel.setObjectName("m15TempLabel")
        self.m15ErrLabel = QtWidgets.QLabel(self.m15SFrame)
        self.m15ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m15ErrLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m15ErrLabel.setObjectName("m15ErrLabel")
        self.m15AngDial = QtWidgets.QDial(self.m15SFrame)
        self.m15AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m15AngDial.setMinimum(-150)
        self.m15AngDial.setMaximum(150)
        self.m15AngDial.setTracking(True)
        self.m15AngDial.setWrapping(False)
        self.m15AngDial.setNotchTarget(50.0)
        self.m15AngDial.setNotchesVisible(True)
        self.m15AngDial.setObjectName("m15AngDial")
        self.m15PosDial = QtWidgets.QDial(self.m15SFrame)
        self.m15PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m15PosDial.setMinimum(0)
        self.m15PosDial.setMaximum(1023)
        self.m15PosDial.setTracking(True)
        self.m15PosDial.setWrapping(False)
        self.m15PosDial.setNotchTarget(100.0)
        self.m15PosDial.setNotchesVisible(True)
        self.m15PosDial.setObjectName("m15PosDial")
        self.m15AngNum = QtWidgets.QLabel(self.m15SFrame)
        self.m15AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m15AngNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m15AngNum.setObjectName("m15AngNum")
        self.m15PosNum = QtWidgets.QLabel(self.m15SFrame)
        self.m15PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m15PosNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m15PosNum.setObjectName("m15PosNum")
        self.m15TorqueNum = QtWidgets.QLabel(self.m15SFrame)
        self.m15TorqueNum.setGeometry(QtCore.QRect(120, 330, 61, 21))
        self.m15TorqueNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m15TorqueNum.setObjectName("m15TorqueNum")
        self.m15ErrNum = QtWidgets.QLabel(self.m15SFrame)
        self.m15ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m15ErrNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m15ErrNum.setObjectName("m15ErrNum")
        self.m15TempNum = QtWidgets.QLabel(self.m15SFrame)
        self.m15TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m15TempNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m15TempNum.setObjectName("m15TempNum")
        self.stackedWidget.addWidget(self.m15Page)
        self.m16Page = QtWidgets.QWidget()
        self.m16Page.setObjectName("m16Page")
        self.m16Label = QtWidgets.QLabel(self.m16Page)
        self.m16Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m16Label.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m16Label.setObjectName("m16Label")
        self.m16CFrame = QtWidgets.QFrame(self.m16Page)
        self.m16CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m16CFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m16CFrame.setObjectName("m16CFrame")
        self.m16GoalTSpin = QtWidgets.QSpinBox(self.m16CFrame)
        self.m16GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m16GoalTSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m16GoalTSpin.setWrapping(False)
        self.m16GoalTSpin.setAccelerated(False)
        self.m16GoalTSpin.setObjectName("m16GoalTSpin")
        self.m16GoalTLabel = QtWidgets.QLabel(self.m16CFrame)
        self.m16GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m16GoalTLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m16GoalTLabel.setObjectName("m16GoalTLabel")
        self.m16UpdateBtn = QtWidgets.QPushButton(self.m16CFrame)
        self.m16UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m16UpdateBtn.setAutoFillBackground(False)
        self.m16UpdateBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m16UpdateBtn.setAutoDefault(False)
        self.m16UpdateBtn.setDefault(False)
        self.m16UpdateBtn.setFlat(False)
        self.m16UpdateBtn.setObjectName("m16UpdateBtn")
        self.m16AngleLabel = QtWidgets.QLabel(self.m16CFrame)
        self.m16AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m16AngleLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m16AngleLabel.setObjectName("m16AngleLabel")
        self.m16AngleSpin = QtWidgets.QSpinBox(self.m16CFrame)
        self.m16AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m16AngleSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m16AngleSpin.setWrapping(False)
        self.m16AngleSpin.setAccelerated(False)
        self.m16AngleSpin.setMinimum(-150)
        self.m16AngleSpin.setMaximum(150)
        self.m16AngleSpin.setObjectName("m16AngleSpin")
        self.m16PositionSpin = QtWidgets.QSpinBox(self.m16CFrame)
        self.m16PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m16PositionSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m16PositionSpin.setWrapping(False)
        self.m16PositionSpin.setAccelerated(False)
        self.m16PositionSpin.setMaximum(1023)
        self.m16PositionSpin.setObjectName("m16PositionSpin")
        self.m16PositionLabel = QtWidgets.QLabel(self.m16CFrame)
        self.m16PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m16PositionLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m16PositionLabel.setObjectName("m16PositionLabel")
        self.m16AngleBtn = QtWidgets.QPushButton(self.m16CFrame)
        self.m16AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m16AngleBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m16AngleBtn.setObjectName("m16AngleBtn")
        self.m16PositionBtn = QtWidgets.QPushButton(self.m16CFrame)
        self.m16PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m16PositionBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m16PositionBtn.setObjectName("m16PositionBtn")
        self.m16HomeBtn = QtWidgets.QPushButton(self.m16CFrame)
        self.m16HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m16HomeBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m16HomeBtn.setObjectName("m16HomeBtn")
        self.m16SFrame = QtWidgets.QFrame(self.m16Page)
        self.m16SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m16SFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m16SFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m16SFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m16SFrame.setObjectName("m16SFrame")
        self.m16AngLabel = QtWidgets.QLabel(self.m16SFrame)
        self.m16AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m16AngLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m16AngLabel.setObjectName("m16AngLabel")
        self.m16PosLabel = QtWidgets.QLabel(self.m16SFrame)
        self.m16PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m16PosLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m16PosLabel.setObjectName("m16PosLabel")
        self.m16TorqueLabel = QtWidgets.QLabel(self.m16SFrame)
        self.m16TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m16TorqueLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m16TorqueLabel.setObjectName("m16TorqueLabel")
        self.m16TempLabel = QtWidgets.QLabel(self.m16SFrame)
        self.m16TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m16TempLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m16TempLabel.setObjectName("m16TempLabel")
        self.m16ErrLabel = QtWidgets.QLabel(self.m16SFrame)
        self.m16ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m16ErrLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m16ErrLabel.setObjectName("m16ErrLabel")
        self.m16AngDial = QtWidgets.QDial(self.m16SFrame)
        self.m16AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m16AngDial.setMinimum(-150)
        self.m16AngDial.setMaximum(150)
        self.m16AngDial.setTracking(True)
        self.m16AngDial.setWrapping(False)
        self.m16AngDial.setNotchTarget(50.0)
        self.m16AngDial.setNotchesVisible(True)
        self.m16AngDial.setObjectName("m16AngDial")
        self.m16PosDial = QtWidgets.QDial(self.m16SFrame)
        self.m16PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m16PosDial.setMinimum(0)
        self.m16PosDial.setMaximum(1023)
        self.m16PosDial.setTracking(True)
        self.m16PosDial.setWrapping(False)
        self.m16PosDial.setNotchTarget(100.0)
        self.m16PosDial.setNotchesVisible(True)
        self.m16PosDial.setObjectName("m16PosDial")
        self.m16AngNum = QtWidgets.QLabel(self.m16SFrame)
        self.m16AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m16AngNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m16AngNum.setObjectName("m16AngNum")
        self.m16PosNum = QtWidgets.QLabel(self.m16SFrame)
        self.m16PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m16PosNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m16PosNum.setObjectName("m16PosNum")
        self.m16TorqueNum = QtWidgets.QLabel(self.m16SFrame)
        self.m16TorqueNum.setGeometry(QtCore.QRect(120, 330, 61, 21))
        self.m16TorqueNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m16TorqueNum.setObjectName("m16TorqueNum")
        self.m16ErrNum = QtWidgets.QLabel(self.m16SFrame)
        self.m16ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m16ErrNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m16ErrNum.setObjectName("m16ErrNum")
        self.m16TempNum = QtWidgets.QLabel(self.m16SFrame)
        self.m16TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m16TempNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m16TempNum.setObjectName("m16TempNum")
        self.stackedWidget.addWidget(self.m16Page)
        self.m17Page = QtWidgets.QWidget()
        self.m17Page.setObjectName("m17Page")
        self.m17Label = QtWidgets.QLabel(self.m17Page)
        self.m17Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m17Label.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m17Label.setObjectName("m17Label")
        self.m17CFrame = QtWidgets.QFrame(self.m17Page)
        self.m17CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m17CFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m17CFrame.setObjectName("m17CFrame")
        self.m17GoalTSpin = QtWidgets.QSpinBox(self.m17CFrame)
        self.m17GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m17GoalTSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m17GoalTSpin.setWrapping(False)
        self.m17GoalTSpin.setAccelerated(False)
        self.m17GoalTSpin.setObjectName("m17GoalTSpin")
        self.m17GoalTLabel = QtWidgets.QLabel(self.m17CFrame)
        self.m17GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m17GoalTLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m17GoalTLabel.setObjectName("m17GoalTLabel")
        self.m17UpdateBtn = QtWidgets.QPushButton(self.m17CFrame)
        self.m17UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m17UpdateBtn.setAutoFillBackground(False)
        self.m17UpdateBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m17UpdateBtn.setAutoDefault(False)
        self.m17UpdateBtn.setDefault(False)
        self.m17UpdateBtn.setFlat(False)
        self.m17UpdateBtn.setObjectName("m17UpdateBtn")
        self.m17AngleLabel = QtWidgets.QLabel(self.m17CFrame)
        self.m17AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m17AngleLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m17AngleLabel.setObjectName("m17AngleLabel")
        self.m17AngleSpin = QtWidgets.QSpinBox(self.m17CFrame)
        self.m17AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m17AngleSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m17AngleSpin.setWrapping(False)
        self.m17AngleSpin.setAccelerated(False)
        self.m17AngleSpin.setMinimum(-150)
        self.m17AngleSpin.setMaximum(150)
        self.m17AngleSpin.setObjectName("m17AngleSpin")
        self.m17PositionSpin = QtWidgets.QSpinBox(self.m17CFrame)
        self.m17PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m17PositionSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m17PositionSpin.setWrapping(False)
        self.m17PositionSpin.setAccelerated(False)
        self.m17PositionSpin.setMaximum(1023)
        self.m17PositionSpin.setObjectName("m17PositionSpin")
        self.m17PositionLabel = QtWidgets.QLabel(self.m17CFrame)
        self.m17PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m17PositionLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m17PositionLabel.setObjectName("m17PositionLabel")
        self.m17AngleBtn = QtWidgets.QPushButton(self.m17CFrame)
        self.m17AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m17AngleBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m17AngleBtn.setObjectName("m17AngleBtn")
        self.m17PositionBtn = QtWidgets.QPushButton(self.m17CFrame)
        self.m17PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m17PositionBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m17PositionBtn.setObjectName("m17PositionBtn")
        self.m17HomeBtn = QtWidgets.QPushButton(self.m17CFrame)
        self.m17HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m17HomeBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m17HomeBtn.setObjectName("m17HomeBtn")
        self.m17SFrame = QtWidgets.QFrame(self.m17Page)
        self.m17SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m17SFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m17SFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m17SFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m17SFrame.setObjectName("m17SFrame")
        self.m17AngLabel = QtWidgets.QLabel(self.m17SFrame)
        self.m17AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m17AngLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m17AngLabel.setObjectName("m17AngLabel")
        self.m17PosLabel = QtWidgets.QLabel(self.m17SFrame)
        self.m17PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m17PosLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m17PosLabel.setObjectName("m17PosLabel")
        self.m17TorqueLabel = QtWidgets.QLabel(self.m17SFrame)
        self.m17TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m17TorqueLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m17TorqueLabel.setObjectName("m17TorqueLabel")
        self.m17TempLabel = QtWidgets.QLabel(self.m17SFrame)
        self.m17TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m17TempLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m17TempLabel.setObjectName("m17TempLabel")
        self.m17ErrLabel = QtWidgets.QLabel(self.m17SFrame)
        self.m17ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m17ErrLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m17ErrLabel.setObjectName("m17ErrLabel")
        self.m17AngDial = QtWidgets.QDial(self.m17SFrame)
        self.m17AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m17AngDial.setMinimum(-150)
        self.m17AngDial.setMaximum(150)
        self.m17AngDial.setTracking(True)
        self.m17AngDial.setWrapping(False)
        self.m17AngDial.setNotchTarget(50.0)
        self.m17AngDial.setNotchesVisible(True)
        self.m17AngDial.setObjectName("m17AngDial")
        self.m17PosDial = QtWidgets.QDial(self.m17SFrame)
        self.m17PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m17PosDial.setMinimum(0)
        self.m17PosDial.setMaximum(1023)
        self.m17PosDial.setTracking(True)
        self.m17PosDial.setWrapping(False)
        self.m17PosDial.setNotchTarget(100.0)
        self.m17PosDial.setNotchesVisible(True)
        self.m17PosDial.setObjectName("m17PosDial")
        self.m17AngNum = QtWidgets.QLabel(self.m17SFrame)
        self.m17AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m17AngNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m17AngNum.setObjectName("m17AngNum")
        self.m17PosNum = QtWidgets.QLabel(self.m17SFrame)
        self.m17PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m17PosNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m17PosNum.setObjectName("m17PosNum")
        self.m17TorqueNum = QtWidgets.QLabel(self.m17SFrame)
        self.m17TorqueNum.setGeometry(QtCore.QRect(120, 330, 61, 21))
        self.m17TorqueNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m17TorqueNum.setObjectName("m17TorqueNum")
        self.m17ErrNum = QtWidgets.QLabel(self.m17SFrame)
        self.m17ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m17ErrNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m17ErrNum.setObjectName("m17ErrNum")
        self.m17TempNum = QtWidgets.QLabel(self.m17SFrame)
        self.m17TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m17TempNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m17TempNum.setObjectName("m17TempNum")
        self.stackedWidget.addWidget(self.m17Page)
        self.m18Page = QtWidgets.QWidget()
        self.m18Page.setObjectName("m18Page")
        self.m18Label = QtWidgets.QLabel(self.m18Page)
        self.m18Label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        self.m18Label.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m18Label.setObjectName("m18Label")
        self.m18CFrame = QtWidgets.QFrame(self.m18Page)
        self.m18CFrame.setGeometry(QtCore.QRect(580, 40, 211, 501))
        self.m18CFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m18CFrame.setObjectName("m18CFrame")
        self.m18GoalTSpin = QtWidgets.QSpinBox(self.m18CFrame)
        self.m18GoalTSpin.setGeometry(QtCore.QRect(30, 40, 151, 21))
        self.m18GoalTSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m18GoalTSpin.setWrapping(False)
        self.m18GoalTSpin.setAccelerated(False)
        self.m18GoalTSpin.setObjectName("m18GoalTSpin")
        self.m18GoalTLabel = QtWidgets.QLabel(self.m18CFrame)
        self.m18GoalTLabel.setGeometry(QtCore.QRect(60, 10, 111, 21))
        self.m18GoalTLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m18GoalTLabel.setObjectName("m18GoalTLabel")
        self.m18UpdateBtn = QtWidgets.QPushButton(self.m18CFrame)
        self.m18UpdateBtn.setGeometry(QtCore.QRect(20, 290, 171, 41))
        self.m18UpdateBtn.setAutoFillBackground(False)
        self.m18UpdateBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m18UpdateBtn.setAutoDefault(False)
        self.m18UpdateBtn.setDefault(False)
        self.m18UpdateBtn.setFlat(False)
        self.m18UpdateBtn.setObjectName("m18UpdateBtn")
        self.m18AngleLabel = QtWidgets.QLabel(self.m18CFrame)
        self.m18AngleLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        self.m18AngleLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m18AngleLabel.setObjectName("m18AngleLabel")
        self.m18AngleSpin = QtWidgets.QSpinBox(self.m18CFrame)
        self.m18AngleSpin.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.m18AngleSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m18AngleSpin.setWrapping(False)
        self.m18AngleSpin.setAccelerated(False)
        self.m18AngleSpin.setMinimum(-150)
        self.m18AngleSpin.setMaximum(150)
        self.m18AngleSpin.setObjectName("m18AngleSpin")
        self.m18PositionSpin = QtWidgets.QSpinBox(self.m18CFrame)
        self.m18PositionSpin.setGeometry(QtCore.QRect(30, 190, 151, 21))
        self.m18PositionSpin.setStyleSheet("font: 63 13pt \"KacstArt\";")
        self.m18PositionSpin.setWrapping(False)
        self.m18PositionSpin.setAccelerated(False)
        self.m18PositionSpin.setMaximum(1023)
        self.m18PositionSpin.setObjectName("m18PositionSpin")
        self.m18PositionLabel = QtWidgets.QLabel(self.m18CFrame)
        self.m18PositionLabel.setGeometry(QtCore.QRect(70, 170, 81, 21))
        self.m18PositionLabel.setStyleSheet("font: 63 14pt \"KacstArt\";\n"
"border : none;")
        self.m18PositionLabel.setObjectName("m18PositionLabel")
        self.m18AngleBtn = QtWidgets.QPushButton(self.m18CFrame)
        self.m18AngleBtn.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.m18AngleBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m18AngleBtn.setObjectName("m18AngleBtn")
        self.m18PositionBtn = QtWidgets.QPushButton(self.m18CFrame)
        self.m18PositionBtn.setGeometry(QtCore.QRect(30, 220, 151, 21))
        self.m18PositionBtn.setStyleSheet("QPushButton\n"
"{font: 63 12pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m18PositionBtn.setObjectName("m18PositionBtn")
        self.m18HomeBtn = QtWidgets.QPushButton(self.m18CFrame)
        self.m18HomeBtn.setGeometry(QtCore.QRect(20, 370, 171, 61))
        self.m18HomeBtn.setStyleSheet("QPushButton\n"
"{font: 63 14pt \"KacstArt\";\n"
"border : 2px solid black;\n"
"}\n"
"QPushButton:pressed\n"
"{    \n"
"    background-color : rgb(209,209,224);\n"
"}\n"
"\n"
"        ")
        self.m18HomeBtn.setObjectName("m18HomeBtn")
        self.m18SFrame = QtWidgets.QFrame(self.m18Page)
        self.m18SFrame.setGeometry(QtCore.QRect(10, 40, 561, 501))
        self.m18SFrame.setStyleSheet("border : 1px solid rgb(113, 0, 0);\n"
"")
        self.m18SFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.m18SFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.m18SFrame.setObjectName("m18SFrame")
        self.m18AngLabel = QtWidgets.QLabel(self.m18SFrame)
        self.m18AngLabel.setGeometry(QtCore.QRect(120, 40, 61, 21))
        self.m18AngLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m18AngLabel.setObjectName("m18AngLabel")
        self.m18PosLabel = QtWidgets.QLabel(self.m18SFrame)
        self.m18PosLabel.setGeometry(QtCore.QRect(390, 40, 91, 21))
        self.m18PosLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m18PosLabel.setObjectName("m18PosLabel")
        self.m18TorqueLabel = QtWidgets.QLabel(self.m18SFrame)
        self.m18TorqueLabel.setGeometry(QtCore.QRect(80, 270, 141, 21))
        self.m18TorqueLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m18TorqueLabel.setObjectName("m18TorqueLabel")
        self.m18TempLabel = QtWidgets.QLabel(self.m18SFrame)
        self.m18TempLabel.setGeometry(QtCore.QRect(370, 270, 131, 21))
        self.m18TempLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m18TempLabel.setObjectName("m18TempLabel")
        self.m18ErrLabel = QtWidgets.QLabel(self.m18SFrame)
        self.m18ErrLabel.setGeometry(QtCore.QRect(260, 390, 61, 21))
        self.m18ErrLabel.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m18ErrLabel.setObjectName("m18ErrLabel")
        self.m18AngDial = QtWidgets.QDial(self.m18SFrame)
        self.m18AngDial.setGeometry(QtCore.QRect(100, 80, 91, 81))
        self.m18AngDial.setMinimum(-150)
        self.m18AngDial.setMaximum(150)
        self.m18AngDial.setTracking(True)
        self.m18AngDial.setWrapping(False)
        self.m18AngDial.setNotchTarget(50.0)
        self.m18AngDial.setNotchesVisible(True)
        self.m18AngDial.setObjectName("m18AngDial")
        self.m18PosDial = QtWidgets.QDial(self.m18SFrame)
        self.m18PosDial.setGeometry(QtCore.QRect(380, 80, 91, 81))
        self.m18PosDial.setMinimum(0)
        self.m18PosDial.setMaximum(1023)
        self.m18PosDial.setTracking(True)
        self.m18PosDial.setWrapping(False)
        self.m18PosDial.setNotchTarget(100.0)
        self.m18PosDial.setNotchesVisible(True)
        self.m18PosDial.setObjectName("m18PosDial")
        self.m18AngNum = QtWidgets.QLabel(self.m18SFrame)
        self.m18AngNum.setGeometry(QtCore.QRect(120, 200, 61, 21))
        self.m18AngNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m18AngNum.setObjectName("m18AngNum")
        self.m18PosNum = QtWidgets.QLabel(self.m18SFrame)
        self.m18PosNum.setGeometry(QtCore.QRect(400, 200, 61, 21))
        self.m18PosNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m18PosNum.setObjectName("m18PosNum")
        self.m18TorqueNum = QtWidgets.QLabel(self.m18SFrame)
        self.m18TorqueNum.setGeometry(QtCore.QRect(120, 320, 61, 21))
        self.m18TorqueNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m18TorqueNum.setObjectName("m18TorqueNum")
        self.m18ErrNum = QtWidgets.QLabel(self.m18SFrame)
        self.m18ErrNum.setGeometry(QtCore.QRect(260, 440, 61, 21))
        self.m18ErrNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m18ErrNum.setObjectName("m18ErrNum")
        self.m18TempNum = QtWidgets.QLabel(self.m18SFrame)
        self.m18TempNum.setGeometry(QtCore.QRect(400, 320, 61, 21))
        self.m18TempNum.setStyleSheet("font: 63 16pt \"KacstArt\";\n"
"border : none;")
        self.m18TempNum.setObjectName("m18TempNum")
        self.stackedWidget.addWidget(self.m18Page)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)

        #MyCode Start
        self.recs = []
        self.torquesOn()
        self.updateMotors()
        _thread.start_new_thread(self.updateThread, ())

        #Shifting between pages Start
        self.mGoBtn.clicked.connect(self.forward)
        mHomeBtns = [self.m1HomeBtn, self.m2HomeBtn, self.m3HomeBtn, self.m4HomeBtn,
                     self.m5HomeBtn, self.m6HomeBtn, self.m7HomeBtn, self.m8HomeBtn,
                     self.m9HomeBtn, self.m10HomeBtn, self.m11HomeBtn, self.m12HomeBtn,
                     self.m13HomeBtn, self.m14HomeBtn, self.m15HomeBtn, self.m16HomeBtn,
                     self.m17HomeBtn, self.m18HomeBtn]
        for mhomeBtn in mHomeBtns:
            mhomeBtn.clicked.connect(self.backward)
        #Shifting between Pages Finish

        #Dialing Start
        self.m1AngDial.valueChanged.connect(lambda: self.updateAngDial(1))
        self.m2AngDial.valueChanged.connect(lambda: self.updateAngDial(2))
        self.m3AngDial.valueChanged.connect(lambda: self.updateAngDial(3))
        self.m4AngDial.valueChanged.connect(lambda: self.updateAngDial(4))
        self.m5AngDial.valueChanged.connect(lambda: self.updateAngDial(5))
        self.m6AngDial.valueChanged.connect(lambda: self.updateAngDial(6))
        self.m7AngDial.valueChanged.connect(lambda: self.updateAngDial(7))
        self.m8AngDial.valueChanged.connect(lambda: self.updateAngDial(8))
        self.m9AngDial.valueChanged.connect(lambda: self.updateAngDial(9))
        self.m10AngDial.valueChanged.connect(lambda: self.updateAngDial(10))
        self.m11AngDial.valueChanged.connect(lambda: self.updateAngDial(11))
        self.m12AngDial.valueChanged.connect(lambda: self.updateAngDial(12))
        self.m13AngDial.valueChanged.connect(lambda: self.updateAngDial(13))
        self.m14AngDial.valueChanged.connect(lambda: self.updateAngDial(14))
        self.m15AngDial.valueChanged.connect(lambda: self.updateAngDial(15))
        self.m16AngDial.valueChanged.connect(lambda: self.updateAngDial(16))
        self.m17AngDial.valueChanged.connect(lambda: self.updateAngDial(17))
        self.m18AngDial.valueChanged.connect(lambda: self.updateAngDial(18))

        self.m1PosDial.valueChanged.connect(lambda: self.updatePosDial(1))
        self.m2PosDial.valueChanged.connect(lambda: self.updatePosDial(2))
        self.m3PosDial.valueChanged.connect(lambda: self.updatePosDial(3))
        self.m4PosDial.valueChanged.connect(lambda: self.updatePosDial(4))
        self.m5PosDial.valueChanged.connect(lambda: self.updatePosDial(5))
        self.m6PosDial.valueChanged.connect(lambda: self.updatePosDial(6))
        self.m7PosDial.valueChanged.connect(lambda: self.updatePosDial(7))
        self.m8PosDial.valueChanged.connect(lambda: self.updatePosDial(8))
        self.m9PosDial.valueChanged.connect(lambda: self.updatePosDial(9))
        self.m10PosDial.valueChanged.connect(lambda: self.updatePosDial(10))
        self.m11PosDial.valueChanged.connect(lambda: self.updatePosDial(11))
        self.m12PosDial.valueChanged.connect(lambda: self.updatePosDial(12))
        self.m13PosDial.valueChanged.connect(lambda: self.updatePosDial(13))
        self.m14PosDial.valueChanged.connect(lambda: self.updatePosDial(14))
        self.m15PosDial.valueChanged.connect(lambda: self.updatePosDial(15))
        self.m16PosDial.valueChanged.connect(lambda: self.updatePosDial(16))
        self.m17PosDial.valueChanged.connect(lambda: self.updatePosDial(17))
        self.m18PosDial.valueChanged.connect(lambda: self.updatePosDial(18))
        #Dialing Finished

        #Ang Start
        self.m1AngleBtn.clicked.connect(lambda: self.updateAng(1))
        self.m2AngleBtn.clicked.connect(lambda: self.updateAng(2))
        self.m3AngleBtn.clicked.connect(lambda: self.updateAng(3))
        self.m4AngleBtn.clicked.connect(lambda: self.updateAng(4))
        self.m5AngleBtn.clicked.connect(lambda: self.updateAng(5))
        self.m6AngleBtn.clicked.connect(lambda: self.updateAng(6))
        self.m7AngleBtn.clicked.connect(lambda: self.updateAng(7))
        self.m8AngleBtn.clicked.connect(lambda: self.updateAng(8))
        self.m9AngleBtn.clicked.connect(lambda: self.updateAng(9))
        self.m10AngleBtn.clicked.connect(lambda: self.updateAng(10))
        self.m11AngleBtn.clicked.connect(lambda: self.updateAng(11))
        self.m12AngleBtn.clicked.connect(lambda: self.updateAng(12))
        self.m13AngleBtn.clicked.connect(lambda: self.updateAng(13))
        self.m14AngleBtn.clicked.connect(lambda: self.updateAng(14))
        self.m15AngleBtn.clicked.connect(lambda: self.updateAng(15))
        self.m16AngleBtn.clicked.connect(lambda: self.updateAng(16))
        self.m17AngleBtn.clicked.connect(lambda: self.updateAng(17))
        self.m18AngleBtn.clicked.connect(lambda: self.updateAng(18))

        #Ang Finished

        #Pos Start
        self.m1PositionBtn.clicked.connect(lambda: self.updatePos(1))
        self.m2PositionBtn.clicked.connect(lambda: self.updatePos(2))
        self.m3PositionBtn.clicked.connect(lambda: self.updatePos(3))
        self.m4PositionBtn.clicked.connect(lambda: self.updatePos(4))
        self.m5PositionBtn.clicked.connect(lambda: self.updatePos(5))
        self.m6PositionBtn.clicked.connect(lambda: self.updatePos(6))
        self.m7PositionBtn.clicked.connect(lambda: self.updatePos(7))
        self.m8PositionBtn.clicked.connect(lambda: self.updatePos(8))
        self.m9PositionBtn.clicked.connect(lambda: self.updatePos(9))
        self.m10PositionBtn.clicked.connect(lambda: self.updatePos(10))
        self.m11PositionBtn.clicked.connect(lambda: self.updatePos(11))
        self.m12PositionBtn.clicked.connect(lambda: self.updatePos(12))
        self.m13PositionBtn.clicked.connect(lambda: self.updatePos(13))
        self.m14PositionBtn.clicked.connect(lambda: self.updatePos(14))
        self.m15PositionBtn.clicked.connect(lambda: self.updatePos(15))
        self.m16PositionBtn.clicked.connect(lambda: self.updatePos(16))
        self.m17PositionBtn.clicked.connect(lambda: self.updatePos(17))
        self.m18PositionBtn.clicked.connect(lambda: self.updatePos(18))
        #Pos Finished

        #Insert Started
        self.inRecBtn.clicked.connect(self.insertRec)
        self.saveRecBtn.clicked.connect(self.saveRec)
        self.newRecBtn.clicked.connect(self.newRec)
        #Insert Finshed

        #MyCode Finish

        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def insertRec(self):
        rec = []
        for motor in motors.motors:
            try:
                recTup = (motor.get_servo_position(), motor.get_servo_angle())
            except:
                recTup = ("None", "None")
            rec.append(recTup)
        self.recs.append(rec)
        recNum = int(self.recNumLabel.text())
        self.recNumLabel.setText(str(recNum + 1))
        print(self.recs)

    def newRec(self):
        del(self.recs[:])
        self.recNumLabel.setText('0')

    def saveRec(self):
        fileName = self.recNameInput.text()
        fileName = "Records/" + fileName + ".txt"
        file = open(fileName, 'a')
        for rec in self.recs:
            file.write(str(rec) + '\n')
        file.close()


    def updateThread(self):
        while(True):
            self.updateMotors()
            time.sleep(1)

    def torquesOn(self):
        try:
            for motor in motors.motors:
                motor.torque_on()
            print("Motors Torque on")
        except:
            print("Torque on err")

    def updateMotors(self):
        #motor 1
        try:
            self.m1Ang.setText(str(motors.motors[0].get_servo_angle()))
            self.m1Pos.setText(str(motors.motors[0].get_servo_position()))
            self.m1AngNum.setText(str(motors.motors[0].get_servo_angle()))
            self.m1PosNum.setText(str(motors.motors[0].get_servo_position()))
            self.m1AngDial.setValue(int(motors.motors[0].get_servo_angle()))
            self.m1PosDial.setValue(motors.motors[0].get_servo_position())
            self.m1TorqueNum.setText(str(motors.motors[0].get_torque_state()))
            self.m1TempNum.setText(str(motors.motors[0].get_servo_temperature()))
            self.m1ErrNum.setText(str(motors.motors[0].get_servo_status()))
        except:
            print("AN on motor 1")

        #motor2
        try:
            self.m2Ang.setText(str(motors.motors[1].get_servo_angle()))
            self.m2Pos.setText(str(motors.motors[1].get_servo_position()))
            self.m2AngNum.setText(str(motors.motors[1].get_servo_angle()))
            self.m2PosNum.setText(str(motors.motors[1].get_servo_position()))
            self.m2AngDial.setValue(int(motors.motors[1].get_servo_angle()))
            self.m2PosDial.setValue(motors.motors[1].get_servo_position())
            self.m2TorqueNum.setText(str(motors.motors[1].get_torque_state()))
            self.m2TempNum.setText(str(motors.motors[1].get_servo_temperature()))
            self.m2ErrNum.setText(str(motors.motors[1].get_servo_status()))
        except:
            print("AN on motor 2")

        #motor3
        try:
            self.m3Ang.setText(str(motors.motors[2].get_servo_angle()))
            self.m3Pos.setText(str(motors.motors[2].get_servo_position()))
            self.m3AngNum.setText(str(motors.motors[2].get_servo_angle()))
            self.m3PosNum.setText(str(motors.motors[2].get_servo_position()))
            self.m3AngDial.setValue(int(motors.motors[2].get_servo_angle()))
            self.m3PosDial.setValue(motors.motors[2].get_servo_position())
            self.m3TorqueNum.setText(str(motors.motors[2].get_torque_state()))
            self.m3TempNum.setText(str(motors.motors[2].get_servo_temperature()))
            self.m3ErrNum.setText(str(motors.motors[2].get_servo_status()))
        except:
            print("AN on motor 3")

        #motor 4
        try:
            self.m4Ang.setText(str(motors.motors[3].get_servo_angle()))
            self.m4Pos.setText(str(motors.motors[3].get_servo_position()))
            self.m4AngNum.setText(str(motors.motors[3].get_servo_angle()))
            self.m4PosNum.setText(str(motors.motors[3].get_servo_position()))
            self.m4AngDial.setValue(int(motors.motors[3].get_servo_angle()))
            self.m4PosDial.setValue(motors.motors[3].get_servo_position())
            self.m4TorqueNum.setText(str(motors.motors[3].get_torque_state()))
            self.m4TempNum.setText(str(motors.motors[3].get_servo_temperature()))
            self.m4ErrNum.setText(str(motors.motors[3].get_servo_status()))
        except:
            print("AN on motor 4")

        #motor5
        try:
            self.m5Ang.setText(str(motors.motors[4].get_servo_angle()))
            self.m5Pos.setText(str(motors.motors[4].get_servo_position()))
            self.m5AngNum.setText(str(motors.motors[4].get_servo_angle()))
            self.m5PosNum.setText(str(motors.motors[4].get_servo_position()))
            self.m5AngDial.setValue(int(motors.motors[4].get_servo_angle()))
            self.m5PosDial.setValue(motors.motors[4].get_servo_position())
            self.m5TorqueNum.setText(str(motors.motors[4].get_torque_state()))
            self.m5TempNum.setText(str(motors.motors[4].get_servo_temperature()))
            self.m5ErrNum.setText(str(motors.motors[4].get_servo_status()))
        except:
            print("AN on motor 5")

        #motor6
        try:
            self.m6Ang.setText(str(motors.motors[5].get_servo_angle()))
            self.m6Pos.setText(str(motors.motors[5].get_servo_position()))
            self.m6AngNum.setText(str(motors.motors[5].get_servo_angle()))
            self.m6PosNum.setText(str(motors.motors[5].get_servo_position()))
            self.m6AngDial.setValue(int(motors.motors[5].get_servo_angle()))
            self.m6PosDial.setValue(motors.motors[5].get_servo_position())
            self.m6TorqueNum.setText(str(motors.motors[5].get_torque_state()))
            self.m6TempNum.setText(str(motors.motors[5].get_servo_temperature()))
            self.m6ErrNum.setText(str(motors.motors[5].get_servo_status()))
        except:
            print("AN on motor 6")

        #motor 7
        try:
            self.m7Ang.setText(str(motors.motors[6].get_servo_angle()))
            self.m7Pos.setText(str(motors.motors[6].get_servo_position()))
            self.m7AngNum.setText(str(motors.motors[6].get_servo_angle()))
            self.m7PosNum.setText(str(motors.motors[6].get_servo_position()))
            self.m7AngDial.setValue(int(motors.motors[6].get_servo_angle()))
            self.m7PosDial.setValue(motors.motors[6].get_servo_position())
            self.m7TorqueNum.setText(str(motors.motors[6].get_torque_state()))
            self.m7TempNum.setText(str(motors.motors[6].get_servo_temperature()))
            self.m7ErrNum.setText(str(motors.motors[6].get_servo_status()))
        except:
            print("AN on motor 7")

        #motor8
        try:
            self.m8Ang.setText(str(motors.motors[7].get_servo_angle()))
            self.m8Pos.setText(str(motors.motors[7].get_servo_position()))
            self.m8AngNum.setText(str(motors.motors[7].get_servo_angle()))
            self.m8PosNum.setText(str(motors.motors[7].get_servo_position()))
            self.m8AngDial.setValue(int(motors.motors[7].get_servo_angle()))
            self.m8PosDial.setValue(motors.motors[7].get_servo_position())
            self.m8TorqueNum.setText(str(motors.motors[7].get_torque_state()))
            self.m8TempNum.setText(str(motors.motors[7].get_servo_temperature()))
            self.m8ErrNum.setText(str(motors.motors[7].get_servo_status()))
        except:
            print("AN on motor 8")

        #motor9
        try:
            self.m9Ang.setText(str(motors.motors[8].get_servo_angle()))
            self.m9Pos.setText(str(motors.motors[8].get_servo_position()))
            self.m9AngNum.setText(str(motors.motors[8].get_servo_angle()))
            self.m9PosNum.setText(str(motors.motors[8].get_servo_position()))
            self.m9AngDial.setValue(int(motors.motors[8].get_servo_angle()))
            self.m9PosDial.setValue(motors.motors[8].get_servo_position())
            self.m9TorqueNum.setText(str(motors.motors[8].get_torque_state()))
            self.m9TempNum.setText(str(motors.motors[8].get_servo_temperature()))
            self.m9ErrNum.setText(str(motors.motors[8].get_servo_status()))
        except:
            print("AN on motor 9")

        #motor 10
        try:
            self.m10Ang.setText(str(motors.motors[9].get_servo_angle()))
            self.m10Pos.setText(str(motors.motors[9].get_servo_position()))
            self.m10AngNum.setText(str(motors.motors[9].get_servo_angle()))
            self.m10PosNum.setText(str(motors.motors[9].get_servo_position()))
            self.m10AngDial.setValue(int(motors.motors[9].get_servo_angle()))
            self.m10PosDial.setValue(motors.motors[9].get_servo_position())
            self.m10TorqueNum.setText(str(motors.motors[9].get_torque_state()))
            self.m10TempNum.setText(str(motors.motors[9].get_servo_temperature()))
            self.m10ErrNum.setText(str(motors.motors[9].get_servo_status()))
        except:
            print("AN on motor 10")

        #motor 11
        try:
            self.m11Ang.setText(str(motors.motors[10].get_servo_angle()))
            self.m11Pos.setText(str(motors.motors[10].get_servo_position()))
            self.m11AngNum.setText(str(motors.motors[10].get_servo_angle()))
            self.m11PosNum.setText(str(motors.motors[10].get_servo_position()))
            self.m11AngDial.setValue(int(motors.motors[10].get_servo_angle()))
            self.m11PosDial.setValue(motors.motors[10].get_servo_position())
            self.m11TorqueNum.setText(str(motors.motors[10].get_torque_state()))
            self.m11TempNum.setText(str(motors.motors[10].get_servo_temperature()))
            self.m11ErrNum.setText(str(motors.motors[10].get_servo_status()))
        except:
            print("AN on motor 11")

        #motor 12
        try:
            self.m12Ang.setText(str(motors.motors[11].get_servo_angle()))
            self.m12Pos.setText(str(motors.motors[11].get_servo_position()))
            self.m12AngNum.setText(str(motors.motors[11].get_servo_angle()))
            self.m12PosNum.setText(str(motors.motors[11].get_servo_position()))
            self.m12AngDial.setValue(int(motors.motors[11].get_servo_angle()))
            self.m12PosDial.setValue(motors.motors[11].get_servo_position())
            self.m12TorqueNum.setText(str(motors.motors[11].get_torque_state()))
            self.m12TempNum.setText(str(motors.motors[11].get_servo_temperature()))
            self.m12ErrNum.setText(str(motors.motors[11].get_servo_status()))
        except:
            print("AN on motor 12")

        #motor 13
        try:
            self.m13Ang.setText(str(motors.motors[12].get_servo_angle()))
            self.m13Pos.setText(str(motors.motors[12].get_servo_position()))
            self.m13AngNum.setText(str(motors.motors[12].get_servo_angle()))
            self.m13PosNum.setText(str(motors.motors[12].get_servo_position()))
            self.m13AngDial.setValue(int(motors.motors[12].get_servo_angle()))
            self.m13PosDial.setValue(motors.motors[12].get_servo_position())
            self.m13TorqueNum.setText(str(motors.motors[12].get_torque_state()))
            self.m13TempNum.setText(str(motors.motors[12].get_servo_temperature()))
            self.m13ErrNum.setText(str(motors.motors[12].get_servo_status()))
        except:
            print("AN on motor 13")

        #motor 14
        try:
            self.m14Ang.setText(str(motors.motors[13].get_servo_angle()))
            self.m14Pos.setText(str(motors.motors[13].get_servo_position()))
            self.m14AngNum.setText(str(motors.motors[13].get_servo_angle()))
            self.m14PosNum.setText(str(motors.motors[13].get_servo_position()))
            self.m14AngDial.setValue(int(motors.motors[13].get_servo_angle()))
            self.m14PosDial.setValue(motors.motors[13].get_servo_position())
            self.m14TorqueNum.setText(str(motors.motors[13].get_torque_state()))
            self.m14TempNum.setText(str(motors.motors[13].get_servo_temperature()))
            self.m14ErrNum.setText(str(motors.motors[13].get_servo_status()))
        except:
            print("AN on motor 14")

        #motor15
        try:
            self.m15Ang.setText(str(motors.motors[14].get_servo_angle()))
            self.m15Pos.setText(str(motors.motors[14].get_servo_position()))
            self.m15AngNum.setText(str(motors.motors[14].get_servo_angle()))
            self.m15PosNum.setText(str(motors.motors[14].get_servo_position()))
            self.m15AngDial.setValue(int(motors.motors[14].get_servo_angle()))
            self.m15PosDial.setValue(motors.motors[14].get_servo_position())
            self.m15TorqueNum.setText(str(motors.motors[14].get_torque_state()))
            self.m15TempNum.setText(str(motors.motors[14].get_servo_temperature()))
            self.m15ErrNum.setText(str(motors.motors[14].get_servo_status()))
        except:
            print("AN on motor 15")

        #motor 16
        try:
            self.m16Ang.setText(str(motors.motors[15].get_servo_angle()))
            self.m16Pos.setText(str(motors.motors[15].get_servo_position()))
            self.m16AngNum.setText(str(motors.motors[15].get_servo_angle()))
            self.m16PosNum.setText(str(motors.motors[15].get_servo_position()))
            self.m16AngDial.setValue(int(motors.motors[15].get_servo_angle()))
            self.m16PosDial.setValue(motors.motors[15].get_servo_position())
            self.m16TorqueNum.setText(str(motors.motors[15].get_torque_state()))
            self.m16TempNum.setText(str(motors.motors[15].get_servo_temperature()))
            self.m16ErrNum.setText(str(motors.motors[15].get_servo_status()))
        except:
            print("AN on motor 16")

        #motor 17
        try:
            self.m17Ang.setText(str(motors.motors[16].get_servo_angle()))
            self.m17Pos.setText(str(motors.motors[16].get_servo_position()))
            self.m17AngNum.setText(str(motors.motors[16].get_servo_angle()))
            self.m17PosNum.setText(str(motors.motors[16].get_servo_position()))
            self.m17AngDial.setValue(int(motors.motors[16].get_servo_angle()))
            self.m17PosDial.setValue(motors.motors[16].get_servo_position())
            self.m17TorqueNum.setText(str(motors.motors[16].get_torque_state()))
            self.m17TempNum.setText(str(motors.motors[16].get_servo_temperature()))
            self.m17ErrNum.setText(str(motors.motors[16].get_servo_status()))
        except:
            print("AN on motor 17")

        #motor 18
        try:
            self.m18Ang.setText(str(motors.motors[17].get_servo_angle()))
            self.m18Pos.setText(str(motors.motors[17].get_servo_position()))
            self.m18AngNum.setText(str(motors.motors[17].get_servo_angle()))
            self.m18PosNum.setText(str(motors.motors[17].get_servo_position()))
            self.m18AngDial.setValue(int(motors.motors[17].get_servo_angle()))
            self.m18PosDial.setValue(motors.motors[17].get_servo_position())
            self.m18TorqueNum.setText(str(motors.motors[17].get_torque_state()))
            self.m18TempNum.setText(str(motors.motors[17].get_servo_temperature()))
            self.m18ErrNum.setText(str(motors.motors[17].get_servo_status()))
        except:
            print("AN on motor 18")

    def updateAngDial(self, mNum):
        if(mNum == 1):
            try:
                self.m1AngNum.setText(str(self.m1AngDial.value()))
                goalTime = self.m1GoalTSpin.value()
                goalAngle = self.m1AngDial.value()
                motors.motors[0].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m1")

        if(mNum == 2):
            try:
                self.m2AngNum.setText(str(self.m2AngDial.value()))
                goalTime = self.m2GoalTSpin.value()
                goalAngle = self.m2AngDial.value()
                motors.motors[1].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m2")

        if(mNum == 3):
            try:
                self.m3AngNum.setText(str(self.m3AngDial.value()))
                goalTime = self.m3GoalTSpin.value()
                goalAngle = self.m3AngDial.value()
                motors.motors[2].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m3")

        if(mNum == 4):
            try:
                self.m4AngNum.setText(str(self.m4AngDial.value()))
                goalTime = self.m4GoalTSpin.value()
                goalAngle = self.m4AngDial.value()
                motors.motors[3].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m4")

        if(mNum == 5):
            try:
                self.m5AngNum.setText(str(self.m5AngDial.value()))
                goalTime = self.m5GoalTSpin.value()
                goalAngle = self.m5AngDial.value()
                motors.motors[4].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m5")

        if(mNum == 6):
            try:
                self.m6AngNum.setText(str(self.m6AngDial.value()))
                goalTime = self.m6GoalTSpin.value()
                goalAngle = self.m6AngDial.value()
                motors.motors[5].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m6")

        if(mNum == 7):
            try:
                self.m7AngNum.setText(str(self.m7AngDial.value()))
                goalTime = self.m7GoalTSpin.value()
                goalAngle = self.m7AngDial.value()
                motors.motors[6].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m7")

        if(mNum == 8):
            try:
                self.m8AngNum.setText(str(self.m8AngDial.value()))
                goalTime = self.m8GoalTSpin.value()
                goalAngle = self.m8AngDial.value()
                motors.motors[7].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m8")

        if(mNum == 9):
            try:
                self.m9AngNum.setText(str(self.m9AngDial.value()))
                goalTime = self.m9GoalTSpin.value()
                goalAngle = self.m9AngDial.value()
                motors.motors[8].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m9")

        if(mNum == 10):
            try:
                self.m10AngNum.setText(str(self.m10AngDial.value()))
                goalTime = self.m10GoalTSpin.value()
                goalAngle = self.m10AngDial.value()
                motors.motors[9].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m10")

        if(mNum == 11):
            try:
                self.m11AngNum.setText(str(self.m11AngDial.value()))
                goalTime = self.m11GoalTSpin.value()
                goalAngle = self.m11AngDial.value()
                motors.motors[10].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m11")

        if(mNum == 12):
            try:
                self.m12AngNum.setText(str(self.m12AngDial.value()))
                goalTime = self.m12GoalTSpin.value()
                goalAngle = self.m12AngDial.value()
                motors.motors[11].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m12")

        if(mNum == 13):
            try:
                self.m13AngNum.setText(str(self.m13AngDial.value()))
                goalTime = self.m13GoalTSpin.value()
                goalAngle = self.m13AngDial.value()
                motors.motors[12].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m13")

        if(mNum == 14):
            try:
                self.m14AngNum.setText(str(self.m14AngDial.value()))
                goalTime = self.m14GoalTSpin.value()
                goalAngle = self.m14AngDial.value()
                motors.motors[13].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m14")

        if(mNum == 15):
            try:
                self.m15AngNum.setText(str(self.m15AngDial.value()))
                goalTime = self.m15GoalTSpin.value()
                goalAngle = self.m15AngDial.value()
                motors.motors[14].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m15")

        if(mNum == 16):
            try:
                self.m16AngNum.setText(str(self.m16AngDial.value()))
                goalTime = self.m16GoalTSpin.value()
                goalAngle = self.m16AngDial.value()
                motors.motors[15].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m16")

        if(mNum == 17):
            try:
                self.m17AngNum.setText(str(self.m17AngDial.value()))
                goalTime = self.m17GoalTSpin.value()
                goalAngle = self.m17AngDial.value()
                motors.motors[16].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m17")

        if(mNum == 18):
            try:
                self.m18AngNum.setText(str(self.m18AngDial.value()))
                goalTime = self.m18GoalTSpin.value()
                goalAngle = self.m18AngDial.value()
                motors.motors[17].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang Dial m18")

    def updateAng(self, mNum):
        if(mNum == 1):
            try:
                goalTime = self.m1GoalTSpin.value()
                goalAngle = self.m1AngleSpin.value()
                motors.motors[0].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m1")

        if(mNum == 2):
            try:
                goalTime = self.m2GoalTSpin.value()
                goalAngle = self.m2AngleSpin.value()
                motors.motors[1].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m2")

        if(mNum == 3):
            try:
                goalTime = self.m3GoalTSpin.value()
                goalAngle = self.m3AngleSpin.value()
                motors.motors[2].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m3")

        if(mNum == 4):
            try:
                goalTime = self.m4GoalTSpin.value()
                goalAngle = self.m4AngleSpin.value()
                motors.motors[3].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m4")

        if(mNum == 5):
            try:
                goalTime = self.m5GoalTSpin.value()
                goalAngle = self.m5AngleSpin.value()
                motors.motors[4].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m5")

        if(mNum == 6):
            try:
                goalTime = self.m6GoalTSpin.value()
                goalAngle = self.m6AngleSpin.value()
                motors.motors[5].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m6")

        if(mNum == 7):
            try:
                goalTime = self.m7GoalTSpin.value()
                goalAngle = self.m7AngleSpin.value()
                motors.motors[6].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m7")

        if(mNum == 8):
            try:
                goalTime = self.m8GoalTSpin.value()
                goalAngle = self.m8AngleSpin.value()
                motors.motors[7].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m8")

        if(mNum == 9):
            try:
                goalTime = self.m9GoalTSpin.value()
                goalAngle = self.m9AngleSpin.value()
                motors.motors[8].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m9")

        if(mNum == 10):
            try:
                goalTime = self.m10GoalTSpin.value()
                goalAngle = self.m10AngleSpin.value()
                motors.motors[9].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m10")

        if(mNum == 11):
            try:
                goalTime = self.m11GoalTSpin.value()
                goalAngle = self.m11AngleSpin.value()
                motors.motors[10].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m11")

        if(mNum == 12):
            try:
                goalTime = self.m12GoalTSpin.value()
                goalAngle = self.m12AngleSpin.value()
                motors.motors[11].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m12")

        if(mNum == 13):
            try:
                goalTime = self.m13GoalTSpin.value()
                goalAngle = self.m13AngleSpin.value()
                motors.motors[12].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m13")

        if(mNum == 14):
            try:
                goalTime = self.m14GoalTSpin.value()
                goalAngle = self.m14AngleSpin.value()
                motors.motors[13].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m14")

        if(mNum == 15):
            try:
                goalTime = self.m15GoalTSpin.value()
                goalAngle = self.m15AngleSpin.value()
                motors.motors[14].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m15")

        if(mNum == 16):
            try:
                goalTime = self.m16GoalTSpin.value()
                goalAngle = self.m16AngleSpin.value()
                motors.motors[15].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m16")

        if(mNum == 17):
            try:
                goalTime = self.m17GoalTSpin.value()
                goalAngle = self.m17AngleSpin.value()
                motors.motors[16].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m17")

        if(mNum == 18):
            try:
                goalTime = self.m18GoalTSpin.value()
                goalAngle = self.m18AngleSpin.value()
                motors.motors[17].set_servo_angle(goalAngle, goalTime, 0x04 )
            except:
                print("Update Ang m18")

    def updatePosDial(self, mNum):
        if(mNum == 1):
            try:
                self.m1PosNum.setText(str(self.m1PosDial.value()))
                goalTime = self.m1GoalTSpin.value()
                goalPos = self.m1PosDial.value()
                motors.motors[0].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m1")

        if(mNum == 2):
            try:
                self.m2PosNum.setText(str(self.m2PosDial.value()))
                goalTime = self.m2GoalTSpin.value()
                goalPos = self.m2PosDial.value()
                motors.motors[1].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m2")

        if(mNum == 3):
            try:
                self.m3PosNum.setText(str(self.m3PosDial.value()))
                goalTime = self.m3GoalTSpin.value()
                goalPos = self.m3PosDial.value()
                motors.motors[2].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m3")

        if(mNum == 4):
            try:
                self.m4PosNum.setText(str(self.m4PosDial.value()))
                goalTime = self.m4GoalTSpin.value()
                goalPos = self.m4PosDial.value()
                motors.motors[3].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m4")

        if(mNum == 5):
            try:
                self.m5PosNum.setText(str(self.m5PosDial.value()))
                goalTime = self.m5GoalTSpin.value()
                goalPos = self.m5PosDial.value()
                motors.motors[4].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m5")

        if(mNum == 6):
            try:
                self.m6PosNum.setText(str(self.m6PosDial.value()))
                goalTime = self.m6GoalTSpin.value()
                goalPos = self.m6PosDial.value()
                motors.motors[5].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m6")

        if(mNum == 7):
            try:
                self.m7PosNum.setText(str(self.m7PosDial.value()))
                goalTime = self.m7GoalTSpin.value()
                goalPos = self.m7PosDial.value()
                motors.motors[6].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m7")

        if(mNum == 8):
            try:
                self.m8PosNum.setText(str(self.m8PosDial.value()))
                goalTime = self.m8GoalTSpin.value()
                goalPos = self.m8PosDial.value()
                motors.motors[7].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m8")

        if(mNum == 9):
            try:
                self.m9PosNum.setText(str(self.m9PosDial.value()))
                goalTime = self.m9GoalTSpin.value()
                goalPos = self.m9PosDial.value()
                motors.motors[8].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m9")

        if(mNum == 10):
            try:
                self.m10PosNum.setText(str(self.m10PosDial.value()))
                goalTime = self.m10GoalTSpin.value()
                goalPos = self.m10PosDial.value()
                motors.motors[9].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m10")

        if(mNum == 11):
            try:
                self.m11PosNum.setText(str(self.m11PosDial.value()))
                goalTime = self.m11GoalTSpin.value()
                goalPos = self.m11PosDial.value()
                motors.motors[10].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m11")

        if(mNum == 12):
            try:
                self.m12PosNum.setText(str(self.m12PosDial.value()))
                goalTime = self.m12GoalTSpin.value()
                goalPos = self.m12PosDial.value()
                motors.motors[11].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m12")

        if(mNum == 13):
            try:
                self.m13PosNum.setText(str(self.m13PosDial.value()))
                goalTime = self.m13GoalTSpin.value()
                goalPos = self.m13PosDial.value()
                motors.motors[12].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m13")

        if(mNum == 14):
            try:
                self.m14PosNum.setText(str(self.m14PosDial.value()))
                goalTime = self.m14GoalTSpin.value()
                goalPos = self.m14PosDial.value()
                motors.motors[13].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m14")

        if(mNum == 15):
            try:
                self.m15PosNum.setText(str(self.m15PosDial.value()))
                goalTime = self.m15GoalTSpin.value()
                goalPos = self.m15PosDial.value()
                motors.motors[14].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m15")

        if(mNum == 16):
            try:
                self.m16PosNum.setText(str(self.m16PosDial.value()))
                goalTime = self.m16GoalTSpin.value()
                goalPos = self.m16PosDial.value()
                motors.motors[15].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m16")

        if(mNum == 17):
            try:
                self.m17PosNum.setText(str(self.m17PosDial.value()))
                goalTime = self.m17GoalTSpin.value()
                goalPosition = self.m17PosDial.value()
                motors.motors[16].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m17")

        if(mNum == 18):
            try:
                self.m18PosNum.setText(str(self.m18PosDial.value()))
                goalTime = self.m18GoalTSpin.value()
                goalPos = self.m18PosDial.value()
                motors.motors[17].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos Dial m18")

    def updatePos(self, mNum):
        if(mNum == 1):
            try:
                goalTime = self.m1GoalTSpin.value()
                goalPos = self.m1PositionSpin.value()
                motors.motors[0].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m1")

        if(mNum == 2):
            try:
                goalTime = self.m2GoalTSpin.value()
                goalPos = self.m2PositionSpin.value()
                motors.motors[1].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m2")

        if(mNum == 3):
            try:
                goalTime = self.m3GoalTSpin.value()
                goalPos = self.m3PositionSpin.value()
                motors.motors[2].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m3")

        if(mNum == 4):
            try:
                goalTime = self.m4GoalTSpin.value()
                goalPos = self.m4PositionSpin.value()
                motors.motors[3].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m4")

        if(mNum == 5):
            try:
                goalTime = self.m5GoalTSpin.value()
                goalPos = self.m5PositionSpin.value()
                motors.motors[4].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m5")

        if(mNum == 6):
            try:
                goalTime = self.m6GoalTSpin.value()
                goalPos = self.m6PositionSpin.value()
                motors.motors[5].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m6")

        if(mNum == 7):
            try:
                goalTime = self.m7GoalTSpin.value()
                goalPos = self.m7PositionSpin.value()
                motors.motors[6].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m7")

        if(mNum == 8):
            try:
                goalTime = self.m8GoalTSpin.value()
                goalPos = self.m8PositionSpin.value()
                motors.motors[7].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m8")

        if(mNum == 9):
            try:
                goalTime = self.m9GoalTSpin.value()
                goalPos = self.m9PositionSpin.value()
                motors.motors[8].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m9")

        if(mNum == 10):
            try:
                goalTime = self.m10GoalTSpin.value()
                goalPos = self.m10PositionSpin.value()
                motors.motors[9].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m10")

        if(mNum == 11):
            try:
                goalTime = self.m11GoalTSpin.value()
                goalPos = self.m11PositionSpin.value()
                motors.motors[10].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m11")

        if(mNum == 12):
            try:
                goalTime = self.m12GoalTSpin.value()
                goalPos = self.m12PositionSpin.value()
                motors.motors[11].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m12")

        if(mNum == 13):
            try:
                goalTime = self.m13GoalTSpin.value()
                goalPos = self.m13PositionSpin.value()
                motors.motors[12].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m13")

        if(mNum == 14):
            try:
                goalTime = self.m14GoalTSpin.value()
                goalPos = self.m14PositionSpin.value()
                motors.motors[13].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m14")

        if(mNum == 15):
            try:
                goalTime = self.m15GoalTSpin.value()
                goalPos = self.m15PositionSpin.value()
                motors.motors[14].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m15")

        if(mNum == 16):
            try:
                goalTime = self.m16GoalTSpin.value()
                goalPos = self.m16PositionSpin.value()
                motors.motors[15].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m16")

        if(mNum == 17):
            try:
                goalTime = self.m17GoalTSpin.value()
                goalPosition = self.m17PositionSpin.value()
                motors.motors[16].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m17")

        if(mNum == 18):
            try:
                goalTime = self.m18GoalTSpin.value()
                goalPos = self.m18PositionSpin.value()
                motors.motors[17].set_servo_position(goalPos, goalTime, 0x04 )
            except:
                print("Update Pos m18")

    def changeValDial(self):
        try:
            #self.m1PosNum.setText(str(self.m1PosDial.value()))
            self.m1PosNum.setText(str(motors.motors[0].get_model()))
        except:
            self.m1PosNum.setText("salam")

    def forward(self):
        motorSelect = str(self.mSelect.currentText()).split(' ')
        motorSelect = int(motorSelect[1])
        #motorSelect = int(motorSelect.split(' ')[1])
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + motorSelect)

    def backward(self):
        self.stackedWidget.setCurrentIndex(0)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AUT-Man"))
        self.mId.setText(_translate("MainWindow", "ID"))
        self.mAngle.setText(_translate("MainWindow", "Angle"))
        self.mPos.setText(_translate("MainWindow", "Position"))
        self.m1.setText(_translate("MainWindow", "1"))
        self.m1Ang.setText(_translate("MainWindow", "None"))
        self.m1Pos.setText(_translate("MainWindow", "None"))
        self.m10.setText(_translate("MainWindow", "10"))
        self.m10Ang.setText(_translate("MainWindow", "None"))
        self.m10Pos.setText(_translate("MainWindow", "None"))
        self.m2.setText(_translate("MainWindow", "2"))
        self.m2Ang.setText(_translate("MainWindow", "None"))
        self.label_4.setText(_translate("MainWindow", "None"))
        self.m2Pos.setText(_translate("MainWindow", "None"))
        self.m11.setText(_translate("MainWindow", "11"))
        self.m11Pos.setText(_translate("MainWindow", "None"))
        self.m11Ang.setText(_translate("MainWindow", "None"))
        self.m3Ang.setText(_translate("MainWindow", "None"))
        self.m3Pos.setText(_translate("MainWindow", "None"))
        self.label_8.setText(_translate("MainWindow", "None"))
        self.m3.setText(_translate("MainWindow", "3"))
        self.m12.setText(_translate("MainWindow", "12"))
        self.m12Pos.setText(_translate("MainWindow", "None"))
        self.m12Ang.setText(_translate("MainWindow", "None"))
        self.m4Ang.setText(_translate("MainWindow", "None"))
        self.m4Pos.setText(_translate("MainWindow", "None"))
        self.m4.setText(_translate("MainWindow", "4"))
        self.m13.setText(_translate("MainWindow", "13"))
        self.m13Pos.setText(_translate("MainWindow", "None"))
        self.m13Ang.setText(_translate("MainWindow", "None"))
        self.m5.setText(_translate("MainWindow", "5"))
        self.m5Ang.setText(_translate("MainWindow", "None"))
        self.m5Pos.setText(_translate("MainWindow", "None"))
        self.m14.setText(_translate("MainWindow", "14"))
        self.m14Pos.setText(_translate("MainWindow", "None"))
        self.m14Ang.setText(_translate("MainWindow", "None"))
        self.m6.setText(_translate("MainWindow", "6"))
        self.m6Ang.setText(_translate("MainWindow", "None"))
        self.m6Pos.setText(_translate("MainWindow", "None"))
        self.m15.setText(_translate("MainWindow", "15"))
        self.m15Pos.setText(_translate("MainWindow", "None"))
        self.m15Ang.setText(_translate("MainWindow", "None"))
        self.m7.setText(_translate("MainWindow", "7"))
        self.m7Ang.setText(_translate("MainWindow", "None"))
        self.m7Pos.setText(_translate("MainWindow", "None"))
        self.m16.setText(_translate("MainWindow", "16"))
        self.m16Pos.setText(_translate("MainWindow", "None"))
        self.m16Ang.setText(_translate("MainWindow", "None"))
        self.m8.setText(_translate("MainWindow", "8"))
        self.m8Ang.setText(_translate("MainWindow", "None"))
        self.m8Pos.setText(_translate("MainWindow", "None"))
        self.m17.setText(_translate("MainWindow", "17"))
        self.m17Pos.setText(_translate("MainWindow", "None"))
        self.m17Ang.setText(_translate("MainWindow", "None"))
        self.recSavedLabel.setText(_translate("MainWindow", "Records saved : "))
        self.recNumLabel.setText(_translate("MainWindow", "0"))
        self.mUpdateBtn.setText(_translate("MainWindow", "Update Motors"))
        self.m9.setText(_translate("MainWindow", "9"))
        self.m9Ang.setText(_translate("MainWindow", "None"))
        self.m9Pos.setText(_translate("MainWindow", "None"))
        self.m18.setText(_translate("MainWindow", "18"))
        self.m18Pos.setText(_translate("MainWindow", "None"))
        self.m18Ang.setText(_translate("MainWindow", "None"))
        self.mId_2.setText(_translate("MainWindow", "ID"))
        self.mAngle_2.setText(_translate("MainWindow", "Angle"))
        self.mPos_2.setText(_translate("MainWindow", "Position"))
        self.inRecBtn.setText(_translate("MainWindow", "Insert Record"))
        self.saveRecBtn.setText(_translate("MainWindow", "save Records"))
        self.recNameInput.setText(_translate("MainWindow", "Rec Name"))
        self.saveStatusLabel.setText(_translate("MainWindow", "Not Saved"))
        self.newRecBtn.setText(_translate("MainWindow", "New Record"))
        self.mSelect.setItemText(0, _translate("MainWindow", "Motor 1"))
        self.mSelect.setItemText(1, _translate("MainWindow", "Motor 2"))
        self.mSelect.setItemText(2, _translate("MainWindow", "Motor 3"))
        self.mSelect.setItemText(3, _translate("MainWindow", "Motor 4"))
        self.mSelect.setItemText(4, _translate("MainWindow", "Motor 5"))
        self.mSelect.setItemText(5, _translate("MainWindow", "Motor 6"))
        self.mSelect.setItemText(6, _translate("MainWindow", "Motor 7"))
        self.mSelect.setItemText(7, _translate("MainWindow", "Motor 8"))
        self.mSelect.setItemText(8, _translate("MainWindow", "Motor 9"))
        self.mSelect.setItemText(9, _translate("MainWindow", "Motor 10"))
        self.mSelect.setItemText(10, _translate("MainWindow", "Motor 11"))
        self.mSelect.setItemText(11, _translate("MainWindow", "Motor 12"))
        self.mSelect.setItemText(12, _translate("MainWindow", "Motor 13"))
        self.mSelect.setItemText(13, _translate("MainWindow", "Motor 14"))
        self.mSelect.setItemText(14, _translate("MainWindow", "Motor 15"))
        self.mSelect.setItemText(15, _translate("MainWindow", "Motor 16"))
        self.mSelect.setItemText(16, _translate("MainWindow", "Motor 17"))
        self.mSelect.setItemText(17, _translate("MainWindow", "Motor 18"))
        self.mGoBtn.setText(_translate("MainWindow", "Go"))
        self.m1Label.setText(_translate("MainWindow", "Motor 1"))
        self.m1AngLabel.setText(_translate("MainWindow", "Angle"))
        self.m1PosLabel.setText(_translate("MainWindow", "Position"))
        self.m1TorqueLabel.setText(_translate("MainWindow", "Torque Status"))
        self.m1TempLabel.setText(_translate("MainWindow", "Temprature"))
        self.m1ErrLabel.setText(_translate("MainWindow", "Error"))
        self.m1AngNum.setText(_translate("MainWindow", "None"))
        self.m1PosNum.setText(_translate("MainWindow", "None"))
        self.m1TorqueNum.setText(_translate("MainWindow", "None"))
        self.m1ErrNum.setText(_translate("MainWindow", "None"))
        self.m1TempNum.setText(_translate("MainWindow", "None"))
        self.m1GoalTLabel.setText(_translate("MainWindow", "Goal Time"))
        self.m1UpdateBtn.setText(_translate("MainWindow", "Update Motor"))
        self.m1AngleLabel.setText(_translate("MainWindow", "Angle"))
        self.m1PositionLabel.setText(_translate("MainWindow", "Position"))
        self.m1AngleBtn.setText(_translate("MainWindow", "Go Angle"))
        self.m1PositionBtn.setText(_translate("MainWindow", "Go Position"))
        self.m1HomeBtn.setText(_translate("MainWindow", "Back to Home"))
        self.m2AngLabel.setText(_translate("MainWindow", "Angle"))
        self.m2PosLabel.setText(_translate("MainWindow", "Position"))
        self.m2TorqueLabel.setText(_translate("MainWindow", "Torque Status"))
        self.m2TempLabel.setText(_translate("MainWindow", "Temprature"))
        self.m2ErrLabel.setText(_translate("MainWindow", "Error"))
        self.m2AngNum.setText(_translate("MainWindow", "None"))
        self.m2PosNum.setText(_translate("MainWindow", "None"))
        self.m2TorqueNum.setText(_translate("MainWindow", "None"))
        self.m2ErrNum.setText(_translate("MainWindow", "None"))
        self.m2TempNum.setText(_translate("MainWindow", "None"))
        self.m2GoalTLabel.setText(_translate("MainWindow", "Goal Time"))
        self.m2UpdateBtn.setText(_translate("MainWindow", "Update Motor"))
        self.m2AngleLabel.setText(_translate("MainWindow", "Angle"))
        self.m2PositionLabel.setText(_translate("MainWindow", "Position"))
        self.m2AngleBtn.setText(_translate("MainWindow", "Go Angle"))
        self.m2PositionBtn.setText(_translate("MainWindow", "Go Position"))
        self.m2HomeBtn.setText(_translate("MainWindow", "Back to Home"))
        self.m2Label.setText(_translate("MainWindow", "Motor 2"))
        self.m3AngLabel.setText(_translate("MainWindow", "Angle"))
        self.m3PosLabel.setText(_translate("MainWindow", "Position"))
        self.m3TorqueLabel.setText(_translate("MainWindow", "Torque Status"))
        self.m3TempLabel.setText(_translate("MainWindow", "Temprature"))
        self.m3ErrLabel.setText(_translate("MainWindow", "Error"))
        self.m3AngNum.setText(_translate("MainWindow", "None"))
        self.m3PosNum.setText(_translate("MainWindow", "None"))
        self.m3TorqueNum.setText(_translate("MainWindow", "None"))
        self.m3ErrNum.setText(_translate("MainWindow", "None"))
        self.m3TempNum.setText(_translate("MainWindow", "None"))
        self.m3GoalTLabel.setText(_translate("MainWindow", "Goal Time"))
        self.m3UpdateBtn.setText(_translate("MainWindow", "Update Motor"))
        self.m3AngleLabel.setText(_translate("MainWindow", "Angle"))
        self.m3PositionLabel.setText(_translate("MainWindow", "Position"))
        self.m3AngleBtn.setText(_translate("MainWindow", "Go Angle"))
        self.m3PositionBtn.setText(_translate("MainWindow", "Go Position"))
        self.m3HomeBtn.setText(_translate("MainWindow", "Back to Home"))
        self.m3Label.setText(_translate("MainWindow", "Motor 3"))
        self.m4AngLabel.setText(_translate("MainWindow", "Angle"))
        self.m4PosLabel.setText(_translate("MainWindow", "Position"))
        self.m4TorqueLabel.setText(_translate("MainWindow", "Torque Status"))
        self.m4TempLabel.setText(_translate("MainWindow", "Temprature"))
        self.m4ErrLabel.setText(_translate("MainWindow", "Error"))
        self.m4AngNum.setText(_translate("MainWindow", "None"))
        self.m4PosNum.setText(_translate("MainWindow", "None"))
        self.m4TorqueNum.setText(_translate("MainWindow", "None"))
        self.m4ErrNum.setText(_translate("MainWindow", "None"))
        self.m4TempNum.setText(_translate("MainWindow", "None"))
        self.m4GoalTLabel.setText(_translate("MainWindow", "Goal Time"))
        self.m4UpdateBtn.setText(_translate("MainWindow", "Update Motor"))
        self.m4AngleLabel.setText(_translate("MainWindow", "Angle"))
        self.m4PositionLabel.setText(_translate("MainWindow", "Position"))
        self.m4AngleBtn.setText(_translate("MainWindow", "Go Angle"))
        self.m4PositionBtn.setText(_translate("MainWindow", "Go Position"))
        self.m4HomeBtn.setText(_translate("MainWindow", "Back to Home"))
        self.m4Label.setText(_translate("MainWindow", "Motor 4"))
        self.m5AngLabel.setText(_translate("MainWindow", "Angle"))
        self.m5PosLabel.setText(_translate("MainWindow", "Position"))
        self.m5TorqueLabel.setText(_translate("MainWindow", "Torque Status"))
        self.m5TempLabel.setText(_translate("MainWindow", "Temprature"))
        self.m5ErrLabel.setText(_translate("MainWindow", "Error"))
        self.m5AngNum.setText(_translate("MainWindow", "None"))
        self.m5PosNum.setText(_translate("MainWindow", "None"))
        self.m5TorqueNum.setText(_translate("MainWindow", "None"))
        self.m5ErrNum.setText(_translate("MainWindow", "None"))
        self.m5TempNum.setText(_translate("MainWindow", "None"))
        self.m5GoalTLabel.setText(_translate("MainWindow", "Goal Time"))
        self.m5UpdateBtn.setText(_translate("MainWindow", "Update Motor"))
        self.m5AngleLabel.setText(_translate("MainWindow", "Angle"))
        self.m5PositionLabel.setText(_translate("MainWindow", "Position"))
        self.m5AngleBtn.setText(_translate("MainWindow", "Go Angle"))
        self.m5PositionBtn.setText(_translate("MainWindow", "Go Position"))
        self.m5HomeBtn.setText(_translate("MainWindow", "Back to Home"))
        self.m5Label.setText(_translate("MainWindow", "Motor 5"))
        self.m6Label.setText(_translate("MainWindow", "Motor 6"))
        self.m6GoalTLabel.setText(_translate("MainWindow", "Goal Time"))
        self.m6UpdateBtn.setText(_translate("MainWindow", "Update Motor"))
        self.m6AngleLabel.setText(_translate("MainWindow", "Angle"))
        self.m6PositionLabel.setText(_translate("MainWindow", "Position"))
        self.m6AngleBtn.setText(_translate("MainWindow", "Go Angle"))
        self.m6PositionBtn.setText(_translate("MainWindow", "Go Position"))
        self.m6HomeBtn.setText(_translate("MainWindow", "Back to Home"))
        self.m6AngLabel.setText(_translate("MainWindow", "Angle"))
        self.m6PosLabel.setText(_translate("MainWindow", "Position"))
        self.m6TorqueLabel.setText(_translate("MainWindow", "Torque Status"))
        self.m6TempLabel.setText(_translate("MainWindow", "Temprature"))
        self.m6ErrLabel.setText(_translate("MainWindow", "Error"))
        self.m6AngNum.setText(_translate("MainWindow", "None"))
        self.m6PosNum.setText(_translate("MainWindow", "None"))
        self.m6TorqueNum.setText(_translate("MainWindow", "None"))
        self.m6ErrNum.setText(_translate("MainWindow", "None"))
        self.m6TempNum.setText(_translate("MainWindow", "None"))
        self.m7Label.setText(_translate("MainWindow", "Motor 7"))
        self.m7GoalTLabel.setText(_translate("MainWindow", "Goal Time"))
        self.m7UpdateBtn.setText(_translate("MainWindow", "Update Motor"))
        self.m7AngleLabel.setText(_translate("MainWindow", "Angle"))
        self.m7PositionLabel.setText(_translate("MainWindow", "Position"))
        self.m7AngleBtn.setText(_translate("MainWindow", "Go Angle"))
        self.m7PositionBtn.setText(_translate("MainWindow", "Go Position"))
        self.m7HomeBtn.setText(_translate("MainWindow", "Back to Home"))
        self.m7AngLabel.setText(_translate("MainWindow", "Angle"))
        self.m7PosLabel.setText(_translate("MainWindow", "Position"))
        self.m7TorqueLabel.setText(_translate("MainWindow", "Torque Status"))
        self.m7TempLabel.setText(_translate("MainWindow", "Temprature"))
        self.m7ErrLabel.setText(_translate("MainWindow", "Error"))
        self.m7AngNum.setText(_translate("MainWindow", "None"))
        self.m7PosNum.setText(_translate("MainWindow", "None"))
        self.m7TorqueNum.setText(_translate("MainWindow", "None"))
        self.m7ErrNum.setText(_translate("MainWindow", "None"))
        self.m7TempNum.setText(_translate("MainWindow", "None"))
        self.m8AngLabel.setText(_translate("MainWindow", "Angle"))
        self.m8PosLabel.setText(_translate("MainWindow", "Position"))
        self.m8TorqueLabel.setText(_translate("MainWindow", "Torque Status"))
        self.m8TempLabel.setText(_translate("MainWindow", "Temprature"))
        self.m8ErrLabel.setText(_translate("MainWindow", "Error"))
        self.m8AngNum.setText(_translate("MainWindow", "None"))
        self.m8PosNum.setText(_translate("MainWindow", "None"))
        self.m8TorqueNum.setText(_translate("MainWindow", "None"))
        self.m8ErrNum.setText(_translate("MainWindow", "None"))
        self.m8TempNum.setText(_translate("MainWindow", "None"))
        self.m8Label.setText(_translate("MainWindow", "Motor 8"))
        self.m8GoalTLabel.setText(_translate("MainWindow", "Goal Time"))
        self.m8UpdateBtn.setText(_translate("MainWindow", "Update Motor"))
        self.m8AngleLabel.setText(_translate("MainWindow", "Angle"))
        self.m8PositionLabel.setText(_translate("MainWindow", "Position"))
        self.m8AngleBtn.setText(_translate("MainWindow", "Go Angle"))
        self.m8PositionBtn.setText(_translate("MainWindow", "Go Position"))
        self.m8HomeBtn.setText(_translate("MainWindow", "Back to Home"))
        self.m9Label.setText(_translate("MainWindow", "Motor 9"))
        self.m9GoalTLabel.setText(_translate("MainWindow", "Goal Time"))
        self.m9UpdateBtn.setText(_translate("MainWindow", "Update Motor"))
        self.m9AngleLabel.setText(_translate("MainWindow", "Angle"))
        self.m9PositionLabel.setText(_translate("MainWindow", "Position"))
        self.m9AngleBtn.setText(_translate("MainWindow", "Go Angle"))
        self.m9PositionBtn.setText(_translate("MainWindow", "Go Position"))
        self.m9HomeBtn.setText(_translate("MainWindow", "Back to Home"))
        self.m9AngLabel.setText(_translate("MainWindow", "Angle"))
        self.m9PosLabel.setText(_translate("MainWindow", "Position"))
        self.m9TorqueLabel.setText(_translate("MainWindow", "Torque Status"))
        self.m9TempLabel.setText(_translate("MainWindow", "Temprature"))
        self.m9ErrLabel.setText(_translate("MainWindow", "Error"))
        self.m9AngNum.setText(_translate("MainWindow", "None"))
        self.m9PosNum.setText(_translate("MainWindow", "None"))
        self.m9TorqueNum.setText(_translate("MainWindow", "None"))
        self.m9ErrNum.setText(_translate("MainWindow", "None"))
        self.m9TempNum.setText(_translate("MainWindow", "None"))
        self.m10Label.setText(_translate("MainWindow", "Motor 10"))
        self.m10GoalTLabel.setText(_translate("MainWindow", "Goal Time"))
        self.m10UpdateBtn.setText(_translate("MainWindow", "Update Motor"))
        self.m10AngleLabel.setText(_translate("MainWindow", "Angle"))
        self.m10PositionLabel.setText(_translate("MainWindow", "Position"))
        self.m10AngleBtn.setText(_translate("MainWindow", "Go Angle"))
        self.m10PositionBtn.setText(_translate("MainWindow", "Go Position"))
        self.m10HomeBtn.setText(_translate("MainWindow", "Back to Home"))
        self.m10AngLabel.setText(_translate("MainWindow", "Angle"))
        self.m10PosLabel.setText(_translate("MainWindow", "Position"))
        self.m10TorqueLabel.setText(_translate("MainWindow", "Torque Status"))
        self.m10TempLabel.setText(_translate("MainWindow", "Temprature"))
        self.m10ErrLabel.setText(_translate("MainWindow", "Error"))
        self.m10AngNum.setText(_translate("MainWindow", "None"))
        self.m10PosNum.setText(_translate("MainWindow", "None"))
        self.m10TorqueNum.setText(_translate("MainWindow", "None"))
        self.m10ErrNum.setText(_translate("MainWindow", "None"))
        self.m10TempNum.setText(_translate("MainWindow", "None"))
        self.m11Label.setText(_translate("MainWindow", "Motor 11"))
        self.m11GoalTLabel.setText(_translate("MainWindow", "Goal Time"))
        self.m11UpdateBtn.setText(_translate("MainWindow", "Update Motor"))
        self.m11AngleLabel.setText(_translate("MainWindow", "Angle"))
        self.m11PositionLabel.setText(_translate("MainWindow", "Position"))
        self.m11AngleBtn.setText(_translate("MainWindow", "Go Angle"))
        self.m11PositionBtn.setText(_translate("MainWindow", "Go Position"))
        self.m11HomeBtn.setText(_translate("MainWindow", "Back to Home"))
        self.m11AngLabel.setText(_translate("MainWindow", "Angle"))
        self.m11PosLabel.setText(_translate("MainWindow", "Position"))
        self.m11TorqueLabel.setText(_translate("MainWindow", "Torque Status"))
        self.m11TempLabel.setText(_translate("MainWindow", "Temprature"))
        self.m11ErrLabel.setText(_translate("MainWindow", "Error"))
        self.m11AngNum.setText(_translate("MainWindow", "None"))
        self.m11PosNum.setText(_translate("MainWindow", "None"))
        self.m11TorqueNum.setText(_translate("MainWindow", "None"))
        self.m11ErrNum.setText(_translate("MainWindow", "None"))
        self.m11TempNum.setText(_translate("MainWindow", "None"))
        self.m12Label.setText(_translate("MainWindow", "Motor 12"))
        self.m12GoalTLabel.setText(_translate("MainWindow", "Goal Time"))
        self.m12UpdateBtn.setText(_translate("MainWindow", "Update Motor"))
        self.m12AngleLabel.setText(_translate("MainWindow", "Angle"))
        self.m12PositionLabel.setText(_translate("MainWindow", "Position"))
        self.m12AngleBtn.setText(_translate("MainWindow", "Go Angle"))
        self.m12PositionBtn.setText(_translate("MainWindow", "Go Position"))
        self.m12HomeBtn.setText(_translate("MainWindow", "Back to Home"))
        self.m12AngLabel.setText(_translate("MainWindow", "Angle"))
        self.m12PosLabel.setText(_translate("MainWindow", "Position"))
        self.m12TorqueLabel.setText(_translate("MainWindow", "Torque Status"))
        self.m12TempLabel.setText(_translate("MainWindow", "Temprature"))
        self.m12ErrLabel.setText(_translate("MainWindow", "Error"))
        self.m12AngNum.setText(_translate("MainWindow", "None"))
        self.m12PosNum.setText(_translate("MainWindow", "None"))
        self.m12TorqueNum.setText(_translate("MainWindow", "None"))
        self.m12ErrNum.setText(_translate("MainWindow", "None"))
        self.m12TempNum.setText(_translate("MainWindow", "None"))
        self.m13Label.setText(_translate("MainWindow", "Motor 13"))
        self.m13GoalTLabel.setText(_translate("MainWindow", "Goal Time"))
        self.m13UpdateBtn.setText(_translate("MainWindow", "Update Motor"))
        self.m13AngleLabel.setText(_translate("MainWindow", "Angle"))
        self.m13PositionLabel.setText(_translate("MainWindow", "Position"))
        self.m13AngleBtn.setText(_translate("MainWindow", "Go Angle"))
        self.m13PositionBtn.setText(_translate("MainWindow", "Go Position"))
        self.m13HomeBtn.setText(_translate("MainWindow", "Back to Home"))
        self.m13AngLabel.setText(_translate("MainWindow", "Angle"))
        self.m13PosLabel.setText(_translate("MainWindow", "Position"))
        self.m13TorqueLabel.setText(_translate("MainWindow", "Torque Status"))
        self.m13TempLabel.setText(_translate("MainWindow", "Temprature"))
        self.m13ErrLabel.setText(_translate("MainWindow", "Error"))
        self.m13AngNum.setText(_translate("MainWindow", "None"))
        self.m13PosNum.setText(_translate("MainWindow", "None"))
        self.m13TorqueNum.setText(_translate("MainWindow", "None"))
        self.m13ErrNum.setText(_translate("MainWindow", "None"))
        self.m13TempNum.setText(_translate("MainWindow", "None"))
        self.m14Label.setText(_translate("MainWindow", "Motor 14"))
        self.m14GoalTLabel.setText(_translate("MainWindow", "Goal Time"))
        self.m14UpdateBtn.setText(_translate("MainWindow", "Update Motor"))
        self.m14AngleLabel.setText(_translate("MainWindow", "Angle"))
        self.m14PositionLabel.setText(_translate("MainWindow", "Position"))
        self.m14AngleBtn.setText(_translate("MainWindow", "Go Angle"))
        self.m14PositionBtn.setText(_translate("MainWindow", "Go Position"))
        self.m14HomeBtn.setText(_translate("MainWindow", "Back to Home"))
        self.m14AngLabel.setText(_translate("MainWindow", "Angle"))
        self.m14PosLabel.setText(_translate("MainWindow", "Position"))
        self.m14TorqueLabel.setText(_translate("MainWindow", "Torque Status"))
        self.m14TempLabel.setText(_translate("MainWindow", "Temprature"))
        self.m14ErrLabel.setText(_translate("MainWindow", "Error"))
        self.m14AngNum.setText(_translate("MainWindow", "None"))
        self.m14PosNum.setText(_translate("MainWindow", "None"))
        self.m14TorqueNum.setText(_translate("MainWindow", "None"))
        self.m14ErrNum.setText(_translate("MainWindow", "None"))
        self.m14TempNum.setText(_translate("MainWindow", "None"))
        self.m15Label.setText(_translate("MainWindow", "Motor 15"))
        self.m15GoalTLabel.setText(_translate("MainWindow", "Goal Time"))
        self.m15UpdateBtn.setText(_translate("MainWindow", "Update Motor"))
        self.m15AngleLabel.setText(_translate("MainWindow", "Angle"))
        self.m15PositionLabel.setText(_translate("MainWindow", "Position"))
        self.m15AngleBtn.setText(_translate("MainWindow", "Go Angle"))
        self.m15PositionBtn.setText(_translate("MainWindow", "Go Position"))
        self.m15HomeBtn.setText(_translate("MainWindow", "Back to Home"))
        self.m15AngLabel.setText(_translate("MainWindow", "Angle"))
        self.m15PosLabel.setText(_translate("MainWindow", "Position"))
        self.m15TorqueLabel.setText(_translate("MainWindow", "Torque Status"))
        self.m15TempLabel.setText(_translate("MainWindow", "Temprature"))
        self.m15ErrLabel.setText(_translate("MainWindow", "Error"))
        self.m15AngNum.setText(_translate("MainWindow", "None"))
        self.m15PosNum.setText(_translate("MainWindow", "None"))
        self.m15TorqueNum.setText(_translate("MainWindow", "None"))
        self.m15ErrNum.setText(_translate("MainWindow", "None"))
        self.m15TempNum.setText(_translate("MainWindow", "None"))
        self.m16Label.setText(_translate("MainWindow", "Motor 16"))
        self.m16GoalTLabel.setText(_translate("MainWindow", "Goal Time"))
        self.m16UpdateBtn.setText(_translate("MainWindow", "Update Motor"))
        self.m16AngleLabel.setText(_translate("MainWindow", "Angle"))
        self.m16PositionLabel.setText(_translate("MainWindow", "Position"))
        self.m16AngleBtn.setText(_translate("MainWindow", "Go Angle"))
        self.m16PositionBtn.setText(_translate("MainWindow", "Go Position"))
        self.m16HomeBtn.setText(_translate("MainWindow", "Back to Home"))
        self.m16AngLabel.setText(_translate("MainWindow", "Angle"))
        self.m16PosLabel.setText(_translate("MainWindow", "Position"))
        self.m16TorqueLabel.setText(_translate("MainWindow", "Torque Status"))
        self.m16TempLabel.setText(_translate("MainWindow", "Temprature"))
        self.m16ErrLabel.setText(_translate("MainWindow", "Error"))
        self.m16AngNum.setText(_translate("MainWindow", "None"))
        self.m16PosNum.setText(_translate("MainWindow", "None"))
        self.m16TorqueNum.setText(_translate("MainWindow", "None"))
        self.m16ErrNum.setText(_translate("MainWindow", "None"))
        self.m16TempNum.setText(_translate("MainWindow", "None"))
        self.m17Label.setText(_translate("MainWindow", "Motor 17"))
        self.m17GoalTLabel.setText(_translate("MainWindow", "Goal Time"))
        self.m17UpdateBtn.setText(_translate("MainWindow", "Update Motor"))
        self.m17AngleLabel.setText(_translate("MainWindow", "Angle"))
        self.m17PositionLabel.setText(_translate("MainWindow", "Position"))
        self.m17AngleBtn.setText(_translate("MainWindow", "Go Angle"))
        self.m17PositionBtn.setText(_translate("MainWindow", "Go Position"))
        self.m17HomeBtn.setText(_translate("MainWindow", "Back to Home"))
        self.m17AngLabel.setText(_translate("MainWindow", "Angle"))
        self.m17PosLabel.setText(_translate("MainWindow", "Position"))
        self.m17TorqueLabel.setText(_translate("MainWindow", "Torque Status"))
        self.m17TempLabel.setText(_translate("MainWindow", "Temprature"))
        self.m17ErrLabel.setText(_translate("MainWindow", "Error"))
        self.m17AngNum.setText(_translate("MainWindow", "None"))
        self.m17PosNum.setText(_translate("MainWindow", "None"))
        self.m17TorqueNum.setText(_translate("MainWindow", "None"))
        self.m17ErrNum.setText(_translate("MainWindow", "None"))
        self.m17TempNum.setText(_translate("MainWindow", "None"))
        self.m18Label.setText(_translate("MainWindow", "Motor 18"))
        self.m18GoalTLabel.setText(_translate("MainWindow", "Goal Time"))
        self.m18UpdateBtn.setText(_translate("MainWindow", "Update Motor"))
        self.m18AngleLabel.setText(_translate("MainWindow", "Angle"))
        self.m18PositionLabel.setText(_translate("MainWindow", "Position"))
        self.m18AngleBtn.setText(_translate("MainWindow", "Go Angle"))
        self.m18PositionBtn.setText(_translate("MainWindow", "Go Position"))
        self.m18HomeBtn.setText(_translate("MainWindow", "Back to Home"))
        self.m18AngLabel.setText(_translate("MainWindow", "Angle"))
        self.m18PosLabel.setText(_translate("MainWindow", "Position"))
        self.m18TorqueLabel.setText(_translate("MainWindow", "Torque Status"))
        self.m18TempLabel.setText(_translate("MainWindow", "Temprature"))
        self.m18ErrLabel.setText(_translate("MainWindow", "Error"))
        self.m18AngNum.setText(_translate("MainWindow", "None"))
        self.m18PosNum.setText(_translate("MainWindow", "None"))
        self.m18TorqueNum.setText(_translate("MainWindow", "None"))
        self.m18ErrNum.setText(_translate("MainWindow", "None"))
        self.m18TempNum.setText(_translate("MainWindow", "None"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

