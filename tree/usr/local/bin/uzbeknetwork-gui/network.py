# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerGJsvns.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(627, 507)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 581, 21))
        font = QFont()
        font.setFamilies([u"Sans Serif"])
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setText(u"Uzbek\u041d\u0435\u0442\u0432\u043e\u0440\u043a")
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(20, 50, 581, 23))
        font1 = QFont()
        font1.setFamilies([u"Sans Serif"])
        self.radioButton.setFont(font1)
        self.radioButton.setText(u"\u043f\u0440\u043e\u0432\u043e\u0434 \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0438!")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 80, 581, 35))
        self.comboBox.setFont(font1)
        self.comboBox.setCurrentText(u"")
        self.comboBox.setPlaceholderText(u"\u0432\u044b\u0431\u0435\u0440\u0438 \u043f\u0440\u043e\u0432\u043e\u0434 \u0438\u043d\u0442\u0435\u0440\u0444\u0435\u0439\u0441 Da.")
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(20, 120, 581, 23))
        self.radioButton_2.setFont(font1)
        self.radioButton_2.setText(u"\u0431\u0435\u0437 \u043f\u0440\u043e\u0432\u043e\u0434\u0430 \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0438")
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(20, 150, 581, 35))
        self.comboBox_2.setFont(font1)
        self.comboBox_2.setCurrentText(u"")
        self.comboBox_2.setPlaceholderText(u"\u0432\u044b\u0431\u0435\u0440\u0438 \u0431\u0435\u0441\u043f\u0440\u043e\u0432\u043e\u0434 \u0438\u043d\u0442\u0435\u0440\u0444\u0435\u0439\u0441 Da.")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(170, 230, 431, 35))
        self.lineEdit.setFont(font1)
        self.lineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 238, 151, 21))
        font2 = QFont()
        font2.setFamilies([u"Sans Serif"])
        font2.setPointSize(12)
        self.label_2.setFont(font2)
        self.label_2.setText(u"\u043f\u0430\u0440\u043e\u043b\u044c")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(18, 450, 581, 38))
        self.pushButton.setFont(font1)
        self.pushButton.setText(u"\u043f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c \u0438 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(20, 190, 581, 35))
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lineEdit_2.setPlaceholderText(u"\u0438\u043c\u044f ssid")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi

