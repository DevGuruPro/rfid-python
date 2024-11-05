# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QVBoxLayout, QWidget)
import ui.res_rc

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(568, 537)
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(100, 100, 100, 100)
        self.loginwidget = QWidget(self.centralwidget)
        self.loginwidget.setObjectName(u"loginwidget")
        self.loginwidget.setStyleSheet(u"#loginwidget{\n"
"	background-color: rgba(128, 128, 128, 200);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.loginwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.loginwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout_4.addWidget(self.label)

        self.user_edit = QLineEdit(self.widget_2)
        self.user_edit.setObjectName(u"user_edit")
        font1 = QFont()
        font1.setPointSize(18)
        self.user_edit.setFont(font1)
        self.user_edit.setStyleSheet(u"QLineEdit {  \n"
"    border: 2px solid gray;  \n"
"    border-radius: 10px;  \n"
"    padding: 0 8px;  \n"
"    background: white;  \n"
"    selection-background-color: darkgray;  \n"
"}  ")

        self.verticalLayout_4.addWidget(self.user_edit)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.loginwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_5.addWidget(self.label_2)

        self.pass_edit = QLineEdit(self.widget_3)
        self.pass_edit.setObjectName(u"pass_edit")
        self.pass_edit.setFont(font1)
        self.pass_edit.setStyleSheet(u"QLineEdit {  \n"
"    border: 2px solid gray;  \n"
"    border-radius: 10px;  \n"
"    padding: 0 8px;  \n"
"    background: white;  \n"
"    selection-background-color: darkgray;  \n"
"}  ")
        self.pass_edit.setEchoMode(QLineEdit.Password)

        self.verticalLayout_5.addWidget(self.pass_edit)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.loginwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(100, -1, 100, -1)
        self.loginBtn = QPushButton(self.widget_4)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setFont(font)
        self.loginBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.loginBtn.setStyleSheet(u"QPushButton {  \n"
"    border: 2px solid white;  \n"
"    border-radius: 10px;  \n"
"    min-width: 80px;\n"
"	min-height: 30px;  \n"
"} \n"
"\n"
"QPushButton:hover {  \n"
"    background-color: #a0a0a0; /* Slightly different green on hover */  \n"
"}  \n"
"\n"
"QPushButton:pressed {  \n"
"    background-color: #909090; /* Darker green when pressed */  \n"
"}  ")
        icon = QIcon()
        icon.addFile(u":/img/delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.loginBtn.setIcon(icon)

        self.horizontalLayout.addWidget(self.loginBtn)


        self.verticalLayout.addWidget(self.widget_4)

        self.groupBox = QGroupBox(self.loginwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"QGroupBox {  \n"
"    border: 0px;\n"
"}  ")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(50, -1, 50, -1)
        self.radio_dev = QRadioButton(self.groupBox)
        self.radio_dev.setObjectName(u"radio_dev")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio_dev.sizePolicy().hasHeightForWidth())
        self.radio_dev.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(14)
        self.radio_dev.setFont(font2)
        self.radio_dev.setChecked(True)

        self.horizontalLayout_2.addWidget(self.radio_dev)

        self.radio_uat = QRadioButton(self.groupBox)
        self.radio_uat.setObjectName(u"radio_uat")
        sizePolicy.setHeightForWidth(self.radio_uat.sizePolicy().hasHeightForWidth())
        self.radio_uat.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(False)
        self.radio_uat.setFont(font3)

        self.horizontalLayout_2.addWidget(self.radio_uat)

        self.radio_prod = QRadioButton(self.groupBox)
        self.radio_prod.setObjectName(u"radio_prod")
        sizePolicy.setHeightForWidth(self.radio_prod.sizePolicy().hasHeightForWidth())
        self.radio_prod.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setPointSize(15)
        self.radio_prod.setFont(font4)

        self.horizontalLayout_2.addWidget(self.radio_prod)


        self.verticalLayout.addWidget(self.groupBox)


        self.verticalLayout_2.addWidget(self.loginwidget)

        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("LoginWindow", u"User Name", None))
        self.label_2.setText(QCoreApplication.translate("LoginWindow", u"Password", None))
        self.loginBtn.setText(QCoreApplication.translate("LoginWindow", u"Login", None))
        self.groupBox.setTitle("")
        self.radio_dev.setText(QCoreApplication.translate("LoginWindow", u"Dev", None))
        self.radio_uat.setText(QCoreApplication.translate("LoginWindow", u"Uat", None))
        self.radio_prod.setText(QCoreApplication.translate("LoginWindow", u"Prod", None))
    # retranslateUi

