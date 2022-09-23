# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *



class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(559, 559)
        icon = QIcon()
        icon.addFile(u"images/logo_pmp.ico", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(90, 210, 421, 331))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.userInput = QLineEdit(self.frame)
        self.userInput.setObjectName(u"userInput")
        self.userInput.setGeometry(QRect(120, 60, 181, 31))
        self.userInput.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color:#fff;\n"
"background-color: rgba(0, 0, 0, 150);\n"
"border-radius:3.5px;\n"
"padding:8px;")
        self.passwdInput = QLineEdit(self.frame)
        self.passwdInput.setObjectName(u"passwdInput")
        self.passwdInput.setGeometry(QRect(120, 130, 181, 31))
        self.passwdInput.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color:#fff;\n"
"background-color: rgba(0, 0, 0, 150);\n"
"border-radius:3.5px;\n"
"padding:8px;")
        self.passwdInput.setEchoMode(QLineEdit.Password)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(170, 200, 75, 51))
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
        self.pushButton.setFlat(False)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 30, 271, 141))
        self.label_3.setPixmap(QPixmap(u"images/logo_pmp.png"))
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(-11, -1, 651, 581))
        self.frame_2.setStyleSheet(u"background-image: url(images/wallpaper_pmp.jpg);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.raise_()
        self.frame.raise_()
        self.label_3.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"PMP-Farm\u00e1cias", None))
        self.userInput.setPlaceholderText(QCoreApplication.translate("Form", u"Usu\u00e1rio:", None))
        self.passwdInput.setPlaceholderText(QCoreApplication.translate("Form", u"Senha:", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"ENTRAR", None))
        self.label_3.setText("")
    # retranslateUi

