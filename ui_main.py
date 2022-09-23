# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(893, 855)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"images/logo_pmp.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(210, 220, 431, 331))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.inputPathFrom = QLineEdit(self.frame)
        self.inputPathFrom.setObjectName(u"inputPathFrom")
        self.inputPathFrom.setGeometry(QRect(190, 150, 201, 41))
        self.inputPathFrom.setStyleSheet(u"QLineEdit{\n"
                                         "	font: 12pt \"MS Shell Dlg 2\";\n"
                                         "	background-color: rgba(0, 0, 0, 150);\n"
                                         "	border-radius:4px;\n"
                                         "	color:#fff;\n"
                                         "	padding-left:10px;\n"
                                         "}")
        self.inputPathFrom.setFrame(False)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 160, 171, 20))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 220, 141, 20))
        self.inputPathTo = QLineEdit(self.frame)
        self.inputPathTo.setObjectName(u"inputPathTo")
        self.inputPathTo.setGeometry(QRect(190, 210, 201, 41))
        self.inputPathTo.setStyleSheet(u"QLineEdit{\n"
                                       "	font: 12pt \"MS Shell Dlg 2\";\n"
                                       "	background-color: rgba(0, 0, 0, 150);\n"
                                       "	border-radius:4px;\n"
                                       "	color:#fff;\n"
                                       " 	padding-left:10px;\n"
                                       "}")
        self.inputPathTo.setFrame(False)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(70, 30, 281, 38))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton_2 = QRadioButton(self.frame_4)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.radioButton_2.setAcceptDrops(False)
        self.radioButton_2.setChecked(True)

        self.horizontalLayout.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.frame_4)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.radioButton_3)

        self.radioButton = QRadioButton(self.frame_4)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.radioButton)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 270, 121, 51))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
                                      "	border-radius:3.5px;\n"
                                      "	background-color:green;\n"
                                      "	color:white;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "	\n"
                                      "	background-color:rgb(0,200,0);\n"
                                      "	color:black;\n"
                                      "}")
        self.inputLoja = QLineEdit(self.frame)
        self.inputLoja.setObjectName(u"inputLoja")
        self.inputLoja.setEnabled(True)
        self.inputLoja.setGeometry(QRect(70, 90, 131, 41))
        self.inputLoja.setStyleSheet(u"QLineEdit{\n"
                                     "	font: 12pt \"MS Shell Dlg 2\";\n"
                                     "	background-color: rgba(0, 0, 0, 150);\n"
                                     "	border-radius:4px;\n"
                                     "	color:#fff;\n"
                                     "	padding-left:10px;\n"
                                     "}")
        self.inputLoja.setFrame(False)
        self.inputIp = QLineEdit(self.frame)
        self.inputIp.setObjectName(u"inputIp")
        self.inputIp.setEnabled(True)
        self.inputIp.setGeometry(QRect(220, 90, 131, 41))
        self.inputIp.setStyleSheet(u"QLineEdit{\n"
                                   "	font: 12pt \"MS Shell Dlg 2\";\n"
                                   "	background-color: rgba(0, 0, 0, 150);\n"
                                   "	border-radius:4px;\n"
                                   "	color:#fff;\n"
                                   "	padding-left:10px;\n"
                                   "}")
        self.inputIp.setFrame(False)
        self.terminal = QTextEdit(self.centralwidget)
        self.terminal.setObjectName(u"terminal")
        self.terminal.setGeometry(QRect(150, 560, 581, 231))
        self.terminal.setStyleSheet(u"QTextEdit{\n"
                                    "	color: rgb(255, 255, 255);\n"
                                    "	font: 12pt \"MS Shell Dlg 2\";\n"
                                    "	background-color: rgba(0, 0, 0, 150);\n"
                                    "	border-radius:4px;\n"
                                    "	padding-left:4px;\n"
                                    "\n"
                                    "}")
        self.terminal.setFrameShape(QFrame.NoFrame)
        self.terminal.setFrameShadow(QFrame.Raised)
        self.terminal.setReadOnly(True)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(260, 20, 321, 191))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 40, 271, 141))
        self.label_3.setPixmap(QPixmap(u"images/logo_pmp.png"))
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(-10, -10, 931, 871))
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMaximumSize(QSize(931, 871))
        self.frame_3.setAcceptDrops(False)
        self.frame_3.setStyleSheet(u"background-image: url(images/wallpaper_pmp.jpg);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_3.raise_()
        self.frame.raise_()
        self.terminal.raise_()
        self.frame_2.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.inputPathFrom.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/arq ou c:\\arq ", None))
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"<html><head/><body><p><span style=\" font-size:12pt;\">Caminho do arquivo:</span></p></body></html>",
                                                      None))
        self.label_2.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p><span style=\" font-size:12pt;\">Caminho destino:</span></p></body></html>",
                                                        None))
        self.inputPathTo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/destino", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Caixa", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Balc\u00e3o", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Toda rede", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.inputLoja.setPlaceholderText(QCoreApplication.translate("MainWindow", u"LOJA", None))
        self.inputIp.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Final do IP", None))
        self.label_3.setText("")
    # retranslateUi
