# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import ui.res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(797, 519)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_20 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.tabWidget.setStyleSheet(u"QTabWidget::pane {\n"
"    border: 1px solid #999;  \n"
"    top: -1px; /* Space between tab bar and frame */  \n"
"}  \n"
"\n"
"QTabBar::tab {  \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   \n"
"                                      stop:0 #999999, stop:1 #000000);  \n"
"    border: 1px solid #c4c4c3;  \n"
"    border-bottom-color: #c2c7cb; /* Same as pane color */  \n"
"    border-top-left-radius: 5px;  \n"
"    border-top-right-radius: 5px;  \n"
"    min-width: 80px;\n"
"	min-height: 20px;\n"
"    padding: 10px;\n"
"	font: 12pt;\n"
"	font-weight: bold;\n"
"	color: white;\n"
"}  \n"
"\n"
"QTabBar::tab:selected {  \n"
"    background-color: #707070;  \n"
"    border-color: #8f8f91;  \n"
"    border-bottom-color: #e0e0e0; /* Same as pane color */  \n"
"}  \n"
"\n"
"QTabBar::tab:!selected {  \n"
"    margin-top: 2px; /* Make non-selected tabs look recessed */  \n"
"}  \n"
"\n"
"QTabBar::tab:hover {  \n"
"    background: #83878a;  \n"
"    border-color: #999;  \n"
"}")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.rfid_tab = QWidget()
        self.rfid_tab.setObjectName(u"rfid_tab")
        self.verticalLayout = QVBoxLayout(self.rfid_tab)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_45 = QWidget(self.rfid_tab)
        self.widget_45.setObjectName(u"widget_45")
        self.widget_45.setAutoFillBackground(False)
        self.widget_45.setStyleSheet(u"QWidget {\n"
"	background-image: url(:/img/back_image1.jpg);\n"
"}")
        self.verticalLayout_30 = QVBoxLayout(self.widget_45)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.widget_45)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        font = QFont()
        font.setPointSize(8)
        font.setBold(False)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.tableWidget.rowCount() < 6):
            self.tableWidget.setRowCount(6)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFlags(Qt.NoItemFlags);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(0, 4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem14)
        self.tableWidget.setObjectName(u"tableWidget")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        self.tableWidget.setFont(font1)
        self.tableWidget.setStyleSheet(u"QTableWidget {  \n"
"  	 background-color: rgba(40, 40, 40, 180); \n"
"    gridline-color: #d1d1d1;  \n"
"    font: 14pt;\n"
"}  \n"
"QHeaderView::section {  \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   \n"
"                                      stop:0 #777777, stop:1 #000000);\n"
"    color: white;  \n"
"    padding: 5px;\n"
"	font: 16pt bold;\n"
"    border: 1px solid #555;  \n"
"}  \n"
"QTableWidget::item {\n"
"	background-color: rgba(40, 40, 40, 150);  \n"
"	color: white;\n"
"    border: 1px solid #202020;\n"
" 	padding: 5px  \n"
"}  \n"
"/*QTableWidget::item:selected {  \n"
"    background-color: #336699;  \n"
"     \n"
"} */")
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget.setTextElideMode(Qt.ElideLeft)
        self.tableWidget.setRowCount(6)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(60)

        self.verticalLayout_30.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.widget_45)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.rfid_tab)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"font-size: 10pt;")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"background-color: orange; \n"
"padding: 5px;\n"
"border: 1px solid black;")

        self.verticalLayout_2.addWidget(self.label)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.last_rfid_read = QLabel(self.widget)
        self.last_rfid_read.setObjectName(u"last_rfid_read")
        self.last_rfid_read.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid black;")

        self.gridLayout_2.addWidget(self.last_rfid_read, 1, 1, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid black;")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.rfid_connection_status = QLabel(self.widget)
        self.rfid_connection_status.setObjectName(u"rfid_connection_status")
        self.rfid_connection_status.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid black;")

        self.gridLayout_2.addWidget(self.rfid_connection_status, 0, 1, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid black;")

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid black;")

        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)

        self.last_rfid_time = QLabel(self.widget)
        self.last_rfid_time.setObjectName(u"last_rfid_time")
        self.last_rfid_time.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid black;")

        self.gridLayout_2.addWidget(self.last_rfid_time, 2, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.rfid_tab)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"font-size: 10pt;")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"background-color: orange; \n"
"padding: 5px;\n"
"border: 1px solid black;")

        self.verticalLayout_3.addWidget(self.label_8)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.last_gps_read = QLabel(self.widget_2)
        self.last_gps_read.setObjectName(u"last_gps_read")
        self.last_gps_read.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid black;")

        self.gridLayout_3.addWidget(self.last_gps_read, 1, 1, 1, 1)

        self.label_10 = QLabel(self.widget_2)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid black;")

        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)

        self.gps_connection_status = QLabel(self.widget_2)
        self.gps_connection_status.setObjectName(u"gps_connection_status")
        self.gps_connection_status.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid black;")

        self.gridLayout_3.addWidget(self.gps_connection_status, 0, 1, 1, 1)

        self.label_12 = QLabel(self.widget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid black;")

        self.gridLayout_3.addWidget(self.label_12, 1, 0, 1, 1)

        self.label_13 = QLabel(self.widget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid black;")

        self.gridLayout_3.addWidget(self.label_13, 2, 0, 1, 1)

        self.last_gps_time = QLabel(self.widget_2)
        self.last_gps_time.setObjectName(u"last_gps_time")
        self.last_gps_time.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid black;")

        self.gridLayout_3.addWidget(self.last_gps_time, 2, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_3)


        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.tabWidget.addTab(self.rfid_tab, "")
        self.setting_tab = QWidget()
        self.setting_tab.setObjectName(u"setting_tab")
        self.setting_tab.setStyleSheet(u"#setting_tab{\n"
"	background-image: url(:/img/back_image.jpg);\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.setting_tab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.setting_tab)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"#widget_3{\n"
"	background-color: rgba(40, 40, 40, 220);\n"
"}")
        self.gridLayout_4 = QGridLayout(self.widget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(50, -1, 50, -1)
        self.groupBox_2 = QGroupBox(self.widget_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font2)
        self.groupBox_2.setStyleSheet(u"QGroupBox::title {  \n"
"    color: white;  /* Change 'blue' to any color you want */  \n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(20, -1, 20, 15)
        self.widget_8 = QWidget(self.groupBox_2)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy2)
        self.verticalLayout_13 = QVBoxLayout(self.widget_8)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(9, 0, 9, 0)
        self.checkBox = QCheckBox(self.widget_8)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font2)
        self.checkBox.setStyleSheet(u"QCheckBox{\n"
"	color: white; \n"
"}")

        self.verticalLayout_13.addWidget(self.checkBox)


        self.verticalLayout_9.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.groupBox_2)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy2.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy2)
        self.verticalLayout_12 = QVBoxLayout(self.widget_9)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 50, 0)
        self.groupBox_3 = QGroupBox(self.widget_9)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy2.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy2)
        self.groupBox_3.setStyleSheet(u"QGroupBox {  \n"
"    border: 0px;\n"
"}  ")
        self.horizontalLayout_12 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.radioButton = QRadioButton(self.groupBox_3)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setFont(font2)
        self.radioButton.setStyleSheet(u"QRadioButton{\n"
"	color: white; \n"
"}")
        self.radioButton.setChecked(True)

        self.horizontalLayout_12.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox_3)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font2)
        self.radioButton_2.setStyleSheet(u"QRadioButton{\n"
"	color: white; \n"
"}")

        self.horizontalLayout_12.addWidget(self.radioButton_2)


        self.verticalLayout_12.addWidget(self.groupBox_3)


        self.verticalLayout_9.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.groupBox_2)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy3)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_11 = QWidget(self.widget_10)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_10 = QVBoxLayout(self.widget_11)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.label_31 = QLabel(self.widget_11)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font2)
        self.label_31.setStyleSheet(u"QLabel {  \n"
"    color: white;  /* Change 'blue' to your preferred color */  \n"
"}  ")

        self.verticalLayout_10.addWidget(self.label_31)

        self.label_32 = QLabel(self.widget_11)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font2)
        self.label_32.setStyleSheet(u"QLabel {  \n"
"    color: white;  /* Change 'blue' to your preferred color */  \n"
"}  ")

        self.verticalLayout_10.addWidget(self.label_32)

        self.label_33 = QLabel(self.widget_11)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font2)
        self.label_33.setStyleSheet(u"QLabel {  \n"
"    color: white;  /* Change 'blue' to your preferred color */  \n"
"}  ")

        self.verticalLayout_10.addWidget(self.label_33)

        self.label_34 = QLabel(self.widget_11)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font2)
        self.label_34.setStyleSheet(u"QLabel {  \n"
"    color: white;  /* Change 'blue' to your preferred color */  \n"
"}  ")

        self.verticalLayout_10.addWidget(self.label_34)

        self.label_35 = QLabel(self.widget_11)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font2)
        self.label_35.setStyleSheet(u"QLabel {  \n"
"    color: white;  /* Change 'blue' to your preferred color */  \n"
"}  ")

        self.verticalLayout_10.addWidget(self.label_35)

        self.label_36 = QLabel(self.widget_11)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font2)
        self.label_36.setStyleSheet(u"QLabel {  \n"
"    color: white;  /* Change 'blue' to your preferred color */  \n"
"}  ")

        self.verticalLayout_10.addWidget(self.label_36)

        self.label_37 = QLabel(self.widget_11)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font2)
        self.label_37.setStyleSheet(u"QLabel {  \n"
"    color: white;  /* Change 'blue' to your preferred color */  \n"
"}  ")

        self.verticalLayout_10.addWidget(self.label_37)


        self.horizontalLayout_2.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.widget_10)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy4)
        self.widget_12.setStyleSheet(u"QLineEdit {  \n"
"    border: 2px solid gray;  \n"
"    border-radius: 10px;  \n"
"    padding: 2 8 2 8 px;  \n"
"    background: white;  \n"
"    selection-background-color: darkgray;  \n"
"} ")
        self.verticalLayout_11 = QVBoxLayout(self.widget_12)
        self.verticalLayout_11.setSpacing(8)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.edit_gps_noti = QLineEdit(self.widget_12)
        self.edit_gps_noti.setObjectName(u"edit_gps_noti")
        self.edit_gps_noti.setFont(font2)

        self.verticalLayout_11.addWidget(self.edit_gps_noti)

        self.edit_gps_hand = QLineEdit(self.widget_12)
        self.edit_gps_hand.setObjectName(u"edit_gps_hand")
        self.edit_gps_hand.setFont(font2)

        self.verticalLayout_11.addWidget(self.edit_gps_hand)

        self.edit_gps_port = QLineEdit(self.widget_12)
        self.edit_gps_port.setObjectName(u"edit_gps_port")
        self.edit_gps_port.setFont(font2)

        self.verticalLayout_11.addWidget(self.edit_gps_port)

        self.edit_gps_dbits = QLineEdit(self.widget_12)
        self.edit_gps_dbits.setObjectName(u"edit_gps_dbits")
        self.edit_gps_dbits.setFont(font2)

        self.verticalLayout_11.addWidget(self.edit_gps_dbits)

        self.edit_gps_sbits = QLineEdit(self.widget_12)
        self.edit_gps_sbits.setObjectName(u"edit_gps_sbits")
        self.edit_gps_sbits.setFont(font2)

        self.verticalLayout_11.addWidget(self.edit_gps_sbits)

        self.edit_gps_parity = QLineEdit(self.widget_12)
        self.edit_gps_parity.setObjectName(u"edit_gps_parity")
        self.edit_gps_parity.setFont(font2)

        self.verticalLayout_11.addWidget(self.edit_gps_parity)

        self.edit_gps_baud = QLineEdit(self.widget_12)
        self.edit_gps_baud.setObjectName(u"edit_gps_baud")
        self.edit_gps_baud.setFont(font2)

        self.verticalLayout_11.addWidget(self.edit_gps_baud)


        self.horizontalLayout_2.addWidget(self.widget_12)


        self.verticalLayout_9.addWidget(self.widget_10)


        self.gridLayout_4.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.groupBox = QGroupBox(self.widget_3)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy4.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy4)
        self.groupBox.setFont(font2)
        self.groupBox.setStyleSheet(u"QGroupBox::title {  \n"
"    color: white;  /* Change 'blue' to any color you want */  \n"
"}\n"
"\n"
"")
        self.horizontalLayout_11 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(20, -1, 20, -1)
        self.widget_37 = QWidget(self.groupBox)
        self.widget_37.setObjectName(u"widget_37")
        sizePolicy3.setHeightForWidth(self.widget_37.sizePolicy().hasHeightForWidth())
        self.widget_37.setSizePolicy(sizePolicy3)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_37)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.widget_37)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy1.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy1)
        self.verticalLayout_7 = QVBoxLayout(self.widget_7)
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_15 = QLabel(self.widget_7)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)
        self.label_15.setStyleSheet(u"QLabel {  \n"
"    color: white;  /* Change 'blue' to your preferred color */  \n"
"}  ")

        self.verticalLayout_7.addWidget(self.label_15)

        self.label_24 = QLabel(self.widget_7)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font2)
        self.label_24.setStyleSheet(u"QLabel {  \n"
"    color: white;  /* Change 'blue' to your preferred color */  \n"
"}  ")

        self.verticalLayout_7.addWidget(self.label_24)

        self.label_25 = QLabel(self.widget_7)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font2)
        self.label_25.setStyleSheet(u"QLabel {  \n"
"    color: white;  /* Change 'blue' to your preferred color */  \n"
"}  ")

        self.verticalLayout_7.addWidget(self.label_25)

        self.label_26 = QLabel(self.widget_7)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font2)
        self.label_26.setStyleSheet(u"QLabel {  \n"
"    color: white;  /* Change 'blue' to your preferred color */  \n"
"}  ")

        self.verticalLayout_7.addWidget(self.label_26)

        self.label_27 = QLabel(self.widget_7)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font2)
        self.label_27.setStyleSheet(u"QLabel {  \n"
"    color: white;  /* Change 'blue' to your preferred color */  \n"
"}  ")

        self.verticalLayout_7.addWidget(self.label_27)

        self.label_28 = QLabel(self.widget_7)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font2)
        self.label_28.setStyleSheet(u"QLabel {  \n"
"    color: white;  /* Change 'blue' to your preferred color */  \n"
"}  ")

        self.verticalLayout_7.addWidget(self.label_28)

        self.label_29 = QLabel(self.widget_7)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font2)
        self.label_29.setStyleSheet(u"QLabel {  \n"
"    color: white;  /* Change 'blue' to your preferred color */  \n"
"}  ")

        self.verticalLayout_7.addWidget(self.label_29)

        self.label_30 = QLabel(self.widget_7)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font2)
        self.label_30.setStyleSheet(u"QLabel {  \n"
"    color: white;  /* Change 'blue' to your preferred color */  \n"
"}  ")

        self.verticalLayout_7.addWidget(self.label_30)


        self.horizontalLayout_4.addWidget(self.widget_7)

        self.widget_6 = QWidget(self.widget_37)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy3.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy3)
        self.widget_6.setStyleSheet(u"QLineEdit {  \n"
"    border: 2px solid gray;  \n"
"    border-radius: 10px;  \n"
"    padding: 2 8 2 8 px;  \n"
"    background: white;  \n"
"    selection-background-color: darkgray;  \n"
"}  ")
        self.verticalLayout_8 = QVBoxLayout(self.widget_6)
        self.verticalLayout_8.setSpacing(8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.edit_rfid_noti = QLineEdit(self.widget_6)
        self.edit_rfid_noti.setObjectName(u"edit_rfid_noti")
        self.edit_rfid_noti.setFont(font2)

        self.verticalLayout_8.addWidget(self.edit_rfid_noti)

        self.edit_rfid_host = QLineEdit(self.widget_6)
        self.edit_rfid_host.setObjectName(u"edit_rfid_host")
        self.edit_rfid_host.setFont(font2)

        self.verticalLayout_8.addWidget(self.edit_rfid_host)

        self.edit_rfid_ras1 = QLineEdit(self.widget_6)
        self.edit_rfid_ras1.setObjectName(u"edit_rfid_ras1")
        self.edit_rfid_ras1.setFont(font2)

        self.verticalLayout_8.addWidget(self.edit_rfid_ras1)

        self.edit_rfid_ras2 = QLineEdit(self.widget_6)
        self.edit_rfid_ras2.setObjectName(u"edit_rfid_ras2")
        self.edit_rfid_ras2.setFont(font2)

        self.verticalLayout_8.addWidget(self.edit_rfid_ras2)

        self.edit_rfid_las1 = QLineEdit(self.widget_6)
        self.edit_rfid_las1.setObjectName(u"edit_rfid_las1")
        self.edit_rfid_las1.setFont(font2)

        self.verticalLayout_8.addWidget(self.edit_rfid_las1)

        self.edit_rfid_las2 = QLineEdit(self.widget_6)
        self.edit_rfid_las2.setObjectName(u"edit_rfid_las2")
        self.edit_rfid_las2.setFont(font2)

        self.verticalLayout_8.addWidget(self.edit_rfid_las2)

        self.edit_rfid_ra1 = QLineEdit(self.widget_6)
        self.edit_rfid_ra1.setObjectName(u"edit_rfid_ra1")
        self.edit_rfid_ra1.setFont(font2)

        self.verticalLayout_8.addWidget(self.edit_rfid_ra1)

        self.edit_rfid_ra2 = QLineEdit(self.widget_6)
        self.edit_rfid_ra2.setObjectName(u"edit_rfid_ra2")
        self.edit_rfid_ra2.setFont(font2)

        self.verticalLayout_8.addWidget(self.edit_rfid_ra2)


        self.horizontalLayout_4.addWidget(self.widget_6)


        self.horizontalLayout_11.addWidget(self.widget_37)


        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)

        self.widget_20 = QWidget(self.widget_3)
        self.widget_20.setObjectName(u"widget_20")
        sizePolicy4.setHeightForWidth(self.widget_20.sizePolicy().hasHeightForWidth())
        self.widget_20.setSizePolicy(sizePolicy4)
        self.verticalLayout_16 = QVBoxLayout(self.widget_20)
        self.verticalLayout_16.setSpacing(10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.checkBox_4 = QCheckBox(self.widget_20)
        self.checkBox_4.setObjectName(u"checkBox_4")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        self.checkBox_4.setFont(font3)
        self.checkBox_4.setStyleSheet(u"QCheckBox{\n"
"	color:white;\n"
"}")

        self.verticalLayout_16.addWidget(self.checkBox_4)

        self.widget_21 = QWidget(self.widget_20)
        self.widget_21.setObjectName(u"widget_21")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.widget_24 = QWidget(self.widget_21)
        self.widget_24.setObjectName(u"widget_24")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_24)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(10, 0, 10, 0)
        self.widget_22 = QWidget(self.widget_24)
        self.widget_22.setObjectName(u"widget_22")
        sizePolicy1.setHeightForWidth(self.widget_22.sizePolicy().hasHeightForWidth())
        self.widget_22.setSizePolicy(sizePolicy1)
        self.verticalLayout_17 = QVBoxLayout(self.widget_22)
        self.verticalLayout_17.setSpacing(20)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_42 = QLabel(self.widget_22)
        self.label_42.setObjectName(u"label_42")
        sizePolicy3.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy3)
        self.label_42.setFont(font3)
        self.label_42.setStyleSheet(u"QLabel {  \n"
"    color: white;  /* Change 'blue' to your preferred color */  \n"
"}  ")

        self.verticalLayout_17.addWidget(self.label_42)

        self.label_43 = QLabel(self.widget_22)
        self.label_43.setObjectName(u"label_43")
        sizePolicy3.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy3)
        self.label_43.setFont(font3)
        self.label_43.setStyleSheet(u"QLabel {  \n"
"    color: white;  /* Change 'blue' to your preferred color */  \n"
"}  ")

        self.verticalLayout_17.addWidget(self.label_43)


        self.horizontalLayout_19.addWidget(self.widget_22)

        self.widget_23 = QWidget(self.widget_24)
        self.widget_23.setObjectName(u"widget_23")
        self.verticalLayout_19 = QVBoxLayout(self.widget_23)
        self.verticalLayout_19.setSpacing(20)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.setting_start_tag = QLineEdit(self.widget_23)
        self.setting_start_tag.setObjectName(u"setting_start_tag")
        self.setting_start_tag.setFont(font3)
        self.setting_start_tag.setStyleSheet(u"QLineEdit {  \n"
"    border: 2px solid gray;  \n"
"    border-radius: 10px;  \n"
"    padding: 0 8px;  \n"
"    background: white;  \n"
"    selection-background-color: darkgray;  \n"
"}  ")

        self.verticalLayout_19.addWidget(self.setting_start_tag)

        self.setting_end_tag = QLineEdit(self.widget_23)
        self.setting_end_tag.setObjectName(u"setting_end_tag")
        self.setting_end_tag.setFont(font3)
        self.setting_end_tag.setStyleSheet(u"QLineEdit {  \n"
"    border: 2px solid gray;  \n"
"    border-radius: 10px;  \n"
"    padding: 0 8px;  \n"
"    background: white;  \n"
"    selection-background-color: darkgray;  \n"
"}  ")

        self.verticalLayout_19.addWidget(self.setting_end_tag)


        self.horizontalLayout_19.addWidget(self.widget_23)


        self.horizontalLayout_18.addWidget(self.widget_24)

        self.widget_25 = QWidget(self.widget_21)
        self.widget_25.setObjectName(u"widget_25")
        self.verticalLayout_18 = QVBoxLayout(self.widget_25)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.setting_save_btn = QPushButton(self.widget_25)
        self.setting_save_btn.setObjectName(u"setting_save_btn")
        self.setting_save_btn.setFont(font2)
        self.setting_save_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setting_save_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   \n"
"                                      stop:0 #222222, stop:1 #aaaaaa);\n"
"    border: 2px solid white;  \n"
"    border-radius: 10px;  \n"
"    min-width: 80px;\n"
"	min-height: 30px;\n"
"	color: white;\n"
"} \n"
"\n"
"QPushButton:hover {  \n"
"    background-color: #a0a0a0; /* Slightly different green on hover */  \n"
"}  \n"
"\n"
"QPushButton:pressed {  \n"
"    background-color: #909090; /* Darker green when pressed */  \n"
"}  ")

        self.verticalLayout_18.addWidget(self.setting_save_btn)


        self.horizontalLayout_18.addWidget(self.widget_25)


        self.verticalLayout_16.addWidget(self.widget_21)


        self.gridLayout_4.addWidget(self.widget_20, 1, 1, 1, 1)

        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_6 = QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_16 = QWidget(self.widget_4)
        self.widget_16.setObjectName(u"widget_16")
        self.verticalLayout_15 = QVBoxLayout(self.widget_16)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.checkBox_3 = QCheckBox(self.widget_16)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setFont(font3)
        self.checkBox_3.setStyleSheet(u"QCheckBox{\n"
"	color:white;\n"
"}")

        self.verticalLayout_15.addWidget(self.checkBox_3)

        self.widget_17 = QWidget(self.widget_16)
        self.widget_17.setObjectName(u"widget_17")
        sizePolicy3.setHeightForWidth(self.widget_17.sizePolicy().hasHeightForWidth())
        self.widget_17.setSizePolicy(sizePolicy3)
        self.horizontalLayout_15 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(10, 0, 10, 0)
        self.widget_18 = QWidget(self.widget_17)
        self.widget_18.setObjectName(u"widget_18")
        sizePolicy2.setHeightForWidth(self.widget_18.sizePolicy().hasHeightForWidth())
        self.widget_18.setSizePolicy(sizePolicy2)
        self.horizontalLayout_16 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_40 = QLabel(self.widget_18)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font3)
        self.label_40.setStyleSheet(u"QLabel {  \n"
"    color: white;  /* Change 'blue' to your preferred color */  \n"
"}  ")

        self.horizontalLayout_16.addWidget(self.label_40)

        self.setting_min_speed = QLineEdit(self.widget_18)
        self.setting_min_speed.setObjectName(u"setting_min_speed")
        self.setting_min_speed.setFont(font3)
        self.setting_min_speed.setStyleSheet(u"QLineEdit {  \n"
"    border: 2px solid gray;  \n"
"    border-radius: 10px;  \n"
"    padding: 0 8px;  \n"
"    background: white;  \n"
"    selection-background-color: darkgray;  \n"
"}  ")

        self.horizontalLayout_16.addWidget(self.setting_min_speed)


        self.horizontalLayout_15.addWidget(self.widget_18)

        self.widget_19 = QWidget(self.widget_17)
        self.widget_19.setObjectName(u"widget_19")
        sizePolicy2.setHeightForWidth(self.widget_19.sizePolicy().hasHeightForWidth())
        self.widget_19.setSizePolicy(sizePolicy2)
        self.horizontalLayout_17 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_41 = QLabel(self.widget_19)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font3)
        self.label_41.setStyleSheet(u"QLabel {  \n"
"    color: white;  /* Change 'blue' to your preferred color */  \n"
"}  ")

        self.horizontalLayout_17.addWidget(self.label_41)

        self.setting_max_speed = QLineEdit(self.widget_19)
        self.setting_max_speed.setObjectName(u"setting_max_speed")
        self.setting_max_speed.setFont(font3)
        self.setting_max_speed.setStyleSheet(u"QLineEdit {  \n"
"    border: 2px solid gray;  \n"
"    border-radius: 10px;  \n"
"    padding: 0 8px;  \n"
"    background: white;  \n"
"    selection-background-color: darkgray;  \n"
"}  ")

        self.horizontalLayout_17.addWidget(self.setting_max_speed)


        self.horizontalLayout_15.addWidget(self.widget_19)


        self.verticalLayout_15.addWidget(self.widget_17)


        self.verticalLayout_6.addWidget(self.widget_16)

        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_14 = QVBoxLayout(self.widget_5)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.checkBox_2 = QCheckBox(self.widget_5)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font3)
        self.checkBox_2.setStyleSheet(u"QCheckBox{\n"
"	color:white;\n"
"}")

        self.verticalLayout_14.addWidget(self.checkBox_2)

        self.widget_14 = QWidget(self.widget_5)
        self.widget_14.setObjectName(u"widget_14")
        sizePolicy3.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy3)
        self.horizontalLayout_13 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(10, 0, 10, 0)
        self.widget_13 = QWidget(self.widget_14)
        self.widget_13.setObjectName(u"widget_13")
        sizePolicy2.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy2)
        self.horizontalLayout = QHBoxLayout(self.widget_13)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_38 = QLabel(self.widget_13)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font3)
        self.label_38.setStyleSheet(u"QLabel {  \n"
"    color: white;  /* Change 'blue' to your preferred color */  \n"
"}  ")

        self.horizontalLayout.addWidget(self.label_38)

        self.setting_min_rssi = QLineEdit(self.widget_13)
        self.setting_min_rssi.setObjectName(u"setting_min_rssi")
        self.setting_min_rssi.setFont(font3)
        self.setting_min_rssi.setStyleSheet(u"QLineEdit {  \n"
"    border: 2px solid gray;  \n"
"    border-radius: 10px;  \n"
"    padding: 0 8px;  \n"
"    background: white;  \n"
"    selection-background-color: darkgray;  \n"
"}  ")

        self.horizontalLayout.addWidget(self.setting_min_rssi)


        self.horizontalLayout_13.addWidget(self.widget_13)

        self.widget_15 = QWidget(self.widget_14)
        self.widget_15.setObjectName(u"widget_15")
        sizePolicy2.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy2)
        self.horizontalLayout_14 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_39 = QLabel(self.widget_15)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font3)
        self.label_39.setStyleSheet(u"QLabel {  \n"
"    color: white;  /* Change 'blue' to your preferred color */  \n"
"}  ")

        self.horizontalLayout_14.addWidget(self.label_39)

        self.setting_max_rssi = QLineEdit(self.widget_15)
        self.setting_max_rssi.setObjectName(u"setting_max_rssi")
        self.setting_max_rssi.setFont(font3)
        self.setting_max_rssi.setStyleSheet(u"QLineEdit {  \n"
"    border: 2px solid gray;  \n"
"    border-radius: 10px;  \n"
"    padding: 0 8px;  \n"
"    background: white;  \n"
"    selection-background-color: darkgray;  \n"
"}  ")

        self.horizontalLayout_14.addWidget(self.setting_max_rssi)


        self.horizontalLayout_13.addWidget(self.widget_15)


        self.verticalLayout_14.addWidget(self.widget_14)


        self.verticalLayout_6.addWidget(self.widget_5)


        self.gridLayout_4.addWidget(self.widget_4, 1, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.widget_3)

        self.tabWidget.addTab(self.setting_tab, "")
        self.api_tab = QWidget()
        self.api_tab.setObjectName(u"api_tab")
        self.api_tab.setStyleSheet(u"#api_tab{\n"
"	background-image: url(:/img/back_image.jpg);\n"
"}")
        self.verticalLayout_21 = QVBoxLayout(self.api_tab)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.widget_27 = QWidget(self.api_tab)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setStyleSheet(u"#widget_27{\n"
"	background-color: rgba(40, 40, 40, 220);  \n"
"}\n"
"\n"
"QLineEdit {  \n"
"    border: 2px solid gray;  \n"
"    border-radius: 10px;  \n"
"    padding: 1 8 1 8 px;  \n"
"    background: white;  \n"
"    selection-background-color: darkgray;  \n"
"	font-size: 8pt;\n"
"	font-weight: bold;\n"
"} ")
        self.verticalLayout_4 = QVBoxLayout(self.widget_27)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(20, 10, 20, 10)
        self.widget_35 = QWidget(self.widget_27)
        self.widget_35.setObjectName(u"widget_35")
        self.widget_35.setFont(font2)
        self.horizontalLayout_29 = QHBoxLayout(self.widget_35)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(20, 0, 20, 0)
        self.label_48 = QLabel(self.widget_35)
        self.label_48.setObjectName(u"label_48")
        sizePolicy2.setHeightForWidth(self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy2)
        self.label_48.setFont(font)
        self.label_48.setStyleSheet(u"QWidget{\n"
"	color: white;\n"
"}")
        self.label_48.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_48)


        self.verticalLayout_4.addWidget(self.widget_35)

        self.widget_26 = QWidget(self.widget_27)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setFont(font2)
        self.widget_26.setStyleSheet(u"QWidget{\n"
"	color: white;\n"
"}")
        self.verticalLayout_27 = QVBoxLayout(self.widget_26)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(50, 0, 50, 0)
        self.line_2 = QFrame(self.widget_26)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_27.addWidget(self.line_2)

        self.groupBox_5 = QGroupBox(self.widget_26)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setStyleSheet(u"QGroupBox {  \n"
"    border: 0px;\n"
"}  ")
        self.horizontalLayout_28 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.radio_api_default = QRadioButton(self.groupBox_5)
        self.radio_api_default.setObjectName(u"radio_api_default")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.radio_api_default.sizePolicy().hasHeightForWidth())
        self.radio_api_default.setSizePolicy(sizePolicy5)
        self.radio_api_default.setFont(font2)
        self.radio_api_default.setChecked(True)

        self.horizontalLayout_28.addWidget(self.radio_api_default)

        self.radio_api_custom = QRadioButton(self.groupBox_5)
        self.radio_api_custom.setObjectName(u"radio_api_custom")
        sizePolicy5.setHeightForWidth(self.radio_api_custom.sizePolicy().hasHeightForWidth())
        self.radio_api_custom.setSizePolicy(sizePolicy5)
        self.radio_api_custom.setFont(font2)

        self.horizontalLayout_28.addWidget(self.radio_api_custom)

        self.radio_api_both = QRadioButton(self.groupBox_5)
        self.radio_api_both.setObjectName(u"radio_api_both")
        sizePolicy5.setHeightForWidth(self.radio_api_both.sizePolicy().hasHeightForWidth())
        self.radio_api_both.setSizePolicy(sizePolicy5)
        self.radio_api_both.setFont(font2)

        self.horizontalLayout_28.addWidget(self.radio_api_both)


        self.verticalLayout_27.addWidget(self.groupBox_5)

        self.line = QFrame(self.widget_26)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_27.addWidget(self.line)


        self.verticalLayout_4.addWidget(self.widget_26)

        self.widget_29 = QWidget(self.widget_27)
        self.widget_29.setObjectName(u"widget_29")
        self.widget_29.setFont(font2)
        self.horizontalLayout_22 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_44 = QLabel(self.widget_29)
        self.label_44.setObjectName(u"label_44")
        sizePolicy2.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy2)
        self.label_44.setFont(font2)
        self.label_44.setStyleSheet(u"QWidget{\n"
"	color: white;\n"
"}")
        self.label_44.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_44)


        self.verticalLayout_4.addWidget(self.widget_29)

        self.widget_28 = QWidget(self.widget_27)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setFont(font2)
        self.widget_28.setStyleSheet(u"QWidget{\n"
"	color: white;\n"
"}")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(200, 0, 200, 0)
        self.groupBox_4 = QGroupBox(self.widget_28)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy2.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy2)
        self.groupBox_4.setStyleSheet(u"QGroupBox {  \n"
"    border: 0px;\n"
"}  ")
        self.horizontalLayout_27 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_27.setSpacing(50)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.radio_login_basic = QRadioButton(self.groupBox_4)
        self.radio_login_basic.setObjectName(u"radio_login_basic")
        sizePolicy5.setHeightForWidth(self.radio_login_basic.sizePolicy().hasHeightForWidth())
        self.radio_login_basic.setSizePolicy(sizePolicy5)
        self.radio_login_basic.setFont(font2)
        self.radio_login_basic.setChecked(True)

        self.horizontalLayout_27.addWidget(self.radio_login_basic)

        self.radio_login_token = QRadioButton(self.groupBox_4)
        self.radio_login_token.setObjectName(u"radio_login_token")
        sizePolicy5.setHeightForWidth(self.radio_login_token.sizePolicy().hasHeightForWidth())
        self.radio_login_token.setSizePolicy(sizePolicy5)
        self.radio_login_token.setFont(font2)

        self.horizontalLayout_27.addWidget(self.radio_login_token)


        self.horizontalLayout_21.addWidget(self.groupBox_4)


        self.verticalLayout_4.addWidget(self.widget_28)

        self.widget_30 = QWidget(self.widget_27)
        self.widget_30.setObjectName(u"widget_30")
        self.horizontalLayout_26 = QHBoxLayout(self.widget_30)
        self.horizontalLayout_26.setSpacing(20)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(20, 10, 20, 10)
        self.widget_31 = QWidget(self.widget_30)
        self.widget_31.setObjectName(u"widget_31")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_31)
        self.horizontalLayout_23.setSpacing(10)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_45 = QLabel(self.widget_31)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font2)
        self.label_45.setStyleSheet(u"color: white;")
        self.label_45.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_45)

        self.edit_username = QLineEdit(self.widget_31)
        self.edit_username.setObjectName(u"edit_username")
        font4 = QFont()
        font4.setPointSize(8)
        font4.setBold(True)
        self.edit_username.setFont(font4)

        self.horizontalLayout_23.addWidget(self.edit_username)


        self.horizontalLayout_26.addWidget(self.widget_31)

        self.widget_32 = QWidget(self.widget_30)
        self.widget_32.setObjectName(u"widget_32")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_32)
        self.horizontalLayout_24.setSpacing(10)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_46 = QLabel(self.widget_32)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font2)
        self.label_46.setStyleSheet(u"color: white;")
        self.label_46.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_46)

        self.edit_password = QLineEdit(self.widget_32)
        self.edit_password.setObjectName(u"edit_password")
        self.edit_password.setFont(font4)
        self.edit_password.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_24.addWidget(self.edit_password)


        self.horizontalLayout_26.addWidget(self.widget_32)

        self.widget_33 = QWidget(self.widget_30)
        self.widget_33.setObjectName(u"widget_33")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_33)
        self.horizontalLayout_25.setSpacing(10)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_47 = QLabel(self.widget_33)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font2)
        self.label_47.setStyleSheet(u"color: white;")
        self.label_47.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.label_47)

        self.edit_url = QLineEdit(self.widget_33)
        self.edit_url.setObjectName(u"edit_url")
        self.edit_url.setMinimumSize(QSize(200, 0))
        self.edit_url.setFont(font4)

        self.horizontalLayout_25.addWidget(self.edit_url)


        self.horizontalLayout_26.addWidget(self.widget_33)


        self.verticalLayout_4.addWidget(self.widget_30)

        self.widget_34 = QWidget(self.widget_27)
        self.widget_34.setObjectName(u"widget_34")
        self.widget_34.setFont(font2)
        self.horizontalLayout_33 = QHBoxLayout(self.widget_34)
        self.horizontalLayout_33.setSpacing(20)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.groupBox_6 = QGroupBox(self.widget_34)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setFont(font2)
        self.groupBox_6.setStyleSheet(u"#groupBox_6{\n"
"	color: white;\n"
"	border: 2px solid white;\n"
"}")
        self.horizontalLayout_34 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.widget_38 = QWidget(self.groupBox_6)
        self.widget_38.setObjectName(u"widget_38")
        self.verticalLayout_22 = QVBoxLayout(self.widget_38)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_51 = QLabel(self.widget_38)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font2)
        self.label_51.setStyleSheet(u"QLabel {  \n"
"    color: white;  /* Change 'blue' to your preferred color */  \n"
"}  ")

        self.verticalLayout_22.addWidget(self.label_51)

        self.label_52 = QLabel(self.widget_38)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font2)
        self.label_52.setStyleSheet(u"QLabel {  \n"
"    color: white;  /* Change 'blue' to your preferred color */  \n"
"}  ")

        self.verticalLayout_22.addWidget(self.label_52)

        self.label_53 = QLabel(self.widget_38)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font2)
        self.label_53.setStyleSheet(u"QLabel {  \n"
"    color: white;  /* Change 'blue' to your preferred color */  \n"
"}  ")

        self.verticalLayout_22.addWidget(self.label_53)

        self.label_54 = QLabel(self.widget_38)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font2)
        self.label_54.setStyleSheet(u"QLabel {  \n"
"    color: white;  /* Change 'blue' to your preferred color */  \n"
"}  ")

        self.verticalLayout_22.addWidget(self.label_54)

        self.label_55 = QLabel(self.widget_38)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font2)
        self.label_55.setStyleSheet(u"QLabel {  \n"
"    color: white;  /* Change 'blue' to your preferred color */  \n"
"}  ")

        self.verticalLayout_22.addWidget(self.label_55)

        self.label_56 = QLabel(self.widget_38)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font2)
        self.label_56.setStyleSheet(u"QLabel {  \n"
"    color: white;  /* Change 'blue' to your preferred color */  \n"
"}  ")

        self.verticalLayout_22.addWidget(self.label_56)


        self.horizontalLayout_34.addWidget(self.widget_38)

        self.widget_39 = QWidget(self.groupBox_6)
        self.widget_39.setObjectName(u"widget_39")
        self.verticalLayout_23 = QVBoxLayout(self.widget_39)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.edit_api_tag = QLineEdit(self.widget_39)
        self.edit_api_tag.setObjectName(u"edit_api_tag")
        self.edit_api_tag.setFont(font4)

        self.verticalLayout_23.addWidget(self.edit_api_tag)

        self.edit_api_ant = QLineEdit(self.widget_39)
        self.edit_api_ant.setObjectName(u"edit_api_ant")
        self.edit_api_ant.setFont(font4)

        self.verticalLayout_23.addWidget(self.edit_api_ant)

        self.edit_api_lat = QLineEdit(self.widget_39)
        self.edit_api_lat.setObjectName(u"edit_api_lat")
        self.edit_api_lat.setFont(font4)

        self.verticalLayout_23.addWidget(self.edit_api_lat)

        self.edit_api_lng = QLineEdit(self.widget_39)
        self.edit_api_lng.setObjectName(u"edit_api_lng")
        self.edit_api_lng.setFont(font4)

        self.verticalLayout_23.addWidget(self.edit_api_lng)

        self.edit_api_heading = QLineEdit(self.widget_39)
        self.edit_api_heading.setObjectName(u"edit_api_heading")
        self.edit_api_heading.setFont(font4)

        self.verticalLayout_23.addWidget(self.edit_api_heading)

        self.edit_api_speed = QLineEdit(self.widget_39)
        self.edit_api_speed.setObjectName(u"edit_api_speed")
        self.edit_api_speed.setFont(font4)

        self.verticalLayout_23.addWidget(self.edit_api_speed)


        self.horizontalLayout_34.addWidget(self.widget_39)


        self.horizontalLayout_33.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.widget_34)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setFont(font2)
        self.groupBox_7.setStyleSheet(u"#groupBox_7{\n"
"	color: white;\n"
"	border: 2px solid white;\n"
"}")
        self.verticalLayout_28 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(-1, 20, -1, -1)
        self.widget_43 = QWidget(self.groupBox_7)
        self.widget_43.setObjectName(u"widget_43")
        self.horizontalLayout_36 = QHBoxLayout(self.widget_43)
        self.horizontalLayout_36.setSpacing(20)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.label_59 = QLabel(self.widget_43)
        self.label_59.setObjectName(u"label_59")
        sizePolicy2.setHeightForWidth(self.label_59.sizePolicy().hasHeightForWidth())
        self.label_59.setSizePolicy(sizePolicy2)
        self.label_59.setFont(font2)
        self.label_59.setStyleSheet(u"QLabel {  \n"
"    color: white;  /* Change 'blue' to your preferred color */  \n"
"}  ")

        self.horizontalLayout_36.addWidget(self.label_59)

        self.edit_api_rssi = QLineEdit(self.widget_43)
        self.edit_api_rssi.setObjectName(u"edit_api_rssi")
        self.edit_api_rssi.setFont(font4)

        self.horizontalLayout_36.addWidget(self.edit_api_rssi)


        self.verticalLayout_28.addWidget(self.widget_43)

        self.widget_44 = QWidget(self.groupBox_7)
        self.widget_44.setObjectName(u"widget_44")
        self.verticalLayout_29 = QVBoxLayout(self.widget_44)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_60 = QLabel(self.widget_44)
        self.label_60.setObjectName(u"label_60")
        sizePolicy2.setHeightForWidth(self.label_60.sizePolicy().hasHeightForWidth())
        self.label_60.setSizePolicy(sizePolicy2)
        self.label_60.setPixmap(QPixmap(u":/img/api_json_request.png"))
        self.label_60.setScaledContents(True)

        self.verticalLayout_29.addWidget(self.label_60)


        self.verticalLayout_28.addWidget(self.widget_44)

        self.widget_42 = QWidget(self.groupBox_7)
        self.widget_42.setObjectName(u"widget_42")
        self.horizontalLayout_35 = QHBoxLayout(self.widget_42)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.widget_40 = QWidget(self.widget_42)
        self.widget_40.setObjectName(u"widget_40")
        self.verticalLayout_24 = QVBoxLayout(self.widget_40)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_57 = QLabel(self.widget_40)
        self.label_57.setObjectName(u"label_57")
        sizePolicy2.setHeightForWidth(self.label_57.sizePolicy().hasHeightForWidth())
        self.label_57.setSizePolicy(sizePolicy2)
        self.label_57.setFont(font2)
        self.label_57.setStyleSheet(u"QLabel {  \n"
"    color: white;  /* Change 'blue' to your preferred color */  \n"
"}  ")

        self.verticalLayout_24.addWidget(self.label_57)

        self.edit_api_heading_3 = QLineEdit(self.widget_40)
        self.edit_api_heading_3.setObjectName(u"edit_api_heading_3")
        self.edit_api_heading_3.setFont(font4)

        self.verticalLayout_24.addWidget(self.edit_api_heading_3)

        self.edit_api_heading_2 = QLineEdit(self.widget_40)
        self.edit_api_heading_2.setObjectName(u"edit_api_heading_2")
        self.edit_api_heading_2.setFont(font4)

        self.verticalLayout_24.addWidget(self.edit_api_heading_2)

        self.edit_api_heading_4 = QLineEdit(self.widget_40)
        self.edit_api_heading_4.setObjectName(u"edit_api_heading_4")
        self.edit_api_heading_4.setFont(font4)

        self.verticalLayout_24.addWidget(self.edit_api_heading_4)

        self.edit_api_lng_2 = QLineEdit(self.widget_40)
        self.edit_api_lng_2.setObjectName(u"edit_api_lng_2")
        self.edit_api_lng_2.setFont(font4)

        self.verticalLayout_24.addWidget(self.edit_api_lng_2)


        self.horizontalLayout_35.addWidget(self.widget_40)

        self.widget_41 = QWidget(self.widget_42)
        self.widget_41.setObjectName(u"widget_41")
        self.verticalLayout_25 = QVBoxLayout(self.widget_41)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_63 = QLabel(self.widget_41)
        self.label_63.setObjectName(u"label_63")
        sizePolicy2.setHeightForWidth(self.label_63.sizePolicy().hasHeightForWidth())
        self.label_63.setSizePolicy(sizePolicy2)
        self.label_63.setFont(font2)
        self.label_63.setStyleSheet(u"QLabel {  \n"
"    color: white;  /* Change 'blue' to your preferred color */  \n"
"}  ")

        self.verticalLayout_25.addWidget(self.label_63)

        self.edit_api_heading_5 = QLineEdit(self.widget_41)
        self.edit_api_heading_5.setObjectName(u"edit_api_heading_5")
        self.edit_api_heading_5.setFont(font4)

        self.verticalLayout_25.addWidget(self.edit_api_heading_5)

        self.edit_api_ant_2 = QLineEdit(self.widget_41)
        self.edit_api_ant_2.setObjectName(u"edit_api_ant_2")
        self.edit_api_ant_2.setFont(font4)

        self.verticalLayout_25.addWidget(self.edit_api_ant_2)

        self.edit_api_lat_2 = QLineEdit(self.widget_41)
        self.edit_api_lat_2.setObjectName(u"edit_api_lat_2")
        self.edit_api_lat_2.setFont(font4)

        self.verticalLayout_25.addWidget(self.edit_api_lat_2)

        self.edit_api_speed_2 = QLineEdit(self.widget_41)
        self.edit_api_speed_2.setObjectName(u"edit_api_speed_2")
        self.edit_api_speed_2.setFont(font4)

        self.verticalLayout_25.addWidget(self.edit_api_speed_2)


        self.horizontalLayout_35.addWidget(self.widget_41)


        self.verticalLayout_28.addWidget(self.widget_42)


        self.horizontalLayout_33.addWidget(self.groupBox_7)


        self.verticalLayout_4.addWidget(self.widget_34)

        self.widget_36 = QWidget(self.widget_27)
        self.widget_36.setObjectName(u"widget_36")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_36)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.widget_36)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(100, 16777215))
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,   \n"
"                                      stop:0 #222222, stop:1 #aaaaaa);\n"
"    border: 2px solid white;  \n"
"    border-radius: 10px;  \n"
"    min-width: 80px;\n"
"	min-height: 30px;\n"
"	color: white;\n"
"} \n"
"\n"
"QPushButton:hover {  \n"
"    background-color: #a0a0a0; /* Slightly different green on hover */  \n"
"}  \n"
"\n"
"QPushButton:pressed {  \n"
"    background-color: #909090; /* Darker green when pressed */  \n"
"}  ")

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.verticalLayout_4.addWidget(self.widget_36)


        self.verticalLayout_21.addWidget(self.widget_27)

        self.tabWidget.addTab(self.api_tab, "")

        self.verticalLayout_20.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"RFID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Antenna", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"RSSI", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Location", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Last Updated", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"5", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("MainWindow", u"RFID Health Status", None))
        self.last_rfid_read.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"RFID Connection Status", None))
        self.rfid_connection_status.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Last RFID Tag Read", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Last RFID Read Time", None))
        self.last_rfid_time.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"GPS Health Status", None))
        self.last_gps_read.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"GPS Connection Status", None))
        self.gps_connection_status.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Last GPS Read", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Last GPS Read Time", None))
        self.last_gps_time.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rfid_tab), QCoreApplication.translate("MainWindow", u"RFID", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"GPS", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Enable GPS", None))
        self.groupBox_3.setTitle("")
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"GPS", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Internet GPS", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Notify GPS", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"GPS HandShake", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"GPS Port", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"GPS DataBits", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"GPS StopBits", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"GPS Parity", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"GPS BaudRate", None))
        self.edit_gps_noti.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"RFID", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Notify RFID", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"RFID Host", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"RFID RSA1", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"RFID RSA2", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"RFID LSA1", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"RFID LSA2", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"RFID RA1", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"RFID RA2", None))
        self.edit_rfid_noti.setText(QCoreApplication.translate("MainWindow", u"-1", None))
        self.edit_rfid_host.setText(QCoreApplication.translate("MainWindow", u"169.254.10.1", None))
        self.edit_rfid_ras1.setText("")
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Enable Tag Range Limit", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Start Tag Value", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"End Tag Value", None))
        self.setting_save_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Enable Speed Limit", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Min Speed", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Max Speed", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Enable RSSI Limit", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Min RSSI", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Max RSSI", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.setting_tab), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Set up the third party API integration below if you want to get the scan tags data using your API. Provide the API URL, login credentials, JSON data\n"
"tag mapping with available data points. Use custom fields for any data points not available; you can hard-code item", None))
        self.groupBox_5.setTitle("")
        self.radio_api_default.setText(QCoreApplication.translate("MainWindow", u"Default API", None))
        self.radio_api_custom.setText(QCoreApplication.translate("MainWindow", u"Customer API", None))
        self.radio_api_both.setText(QCoreApplication.translate("MainWindow", u"Both", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Login Type", None))
        self.groupBox_4.setTitle("")
        self.radio_login_basic.setText(QCoreApplication.translate("MainWindow", u"Basic", None))
        self.radio_login_token.setText(QCoreApplication.translate("MainWindow", u"Token", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"UserName", None))
        self.edit_username.setText("")
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Login Url", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Default", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Tag", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Ant", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"lat", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"lng", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"heading", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"speed", None))
        self.edit_api_tag.setText("")
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Client", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"rssi", None))
        self.edit_api_rssi.setText("")
        self.label_60.setText("")
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Custom Tag", None))
        self.edit_api_heading_3.setText("")
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Custom Value", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.api_tab), QCoreApplication.translate("MainWindow", u"API Integration", None))
    # retranslateUi

