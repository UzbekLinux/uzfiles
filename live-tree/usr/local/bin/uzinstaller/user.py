# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'userlmWjnO.ui'
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
from PyQt6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(807, 453)
        MainWindow.setMinimumSize(QSize(807, 453))
        MainWindow.setMaximumSize(QSize(807, 453))
        icon = QIcon()
        icon.addFile(u"2705.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 70, 711, 18))
        font = QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 201, 51))
        self.label.setPixmap(QPixmap(u"uzbek_logo.png"))
        self.label.setScaledContents(True)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(690, 400, 88, 34))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(310, 10, 481, 51))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setItalic(True)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(180, 190, 601, 32))
        self.lineEdit.setInputMask(u"")
        self.lineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(180, 90, 601, 32))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 90, 161, 31))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setItalic(True)
        self.label_4.setFont(font2)
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(180, 130, 601, 32))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 130, 161, 31))
        self.label_5.setFont(font2)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 170, 711, 18))
        self.label_6.setFont(font)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 190, 161, 31))
        self.label_7.setFont(font2)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 230, 161, 31))
        self.label_8.setFont(font2)
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(180, 230, 601, 32))
        self.lineEdit_4.setInputMask(u"")
        self.lineEdit_4.setEchoMode(QLineEdit.EchoMode.Password)
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(20, 401, 661, 31))
        self.checkBox.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430 Uzbek Linux", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0441\u0443\u043a\u0430 \u0442\u0435\u043f\u0435\u0440\u044c \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u0443\u0437\u0431\u0435\u043a\u0430\u2705", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043b\u0435\u0435", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"What doesn't kill you makes you stronger \u2705 ", None))
        self.lineEdit.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0445\u0430\u043b\u044f\u043b\u044c \u0445\u043e\u0441\u0442\u043d\u0435\u0439\u043c\u2705", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0442\u0432\u043e\u0439 halal \u044e\u0437\u0435\u0440\u043d\u044d\u0439\u043c", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0441\u0443\u043a\u0430 \u0442\u0435\u043f\u0435\u0440\u044c \u043f\u0430\u0440\u043e\u043b\u044c \u0443\u0437\u0431\u0435\u043a\u0430\u2705", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"halal \u044e\u0437\u0435\u0440 \u043f\u0430\u0441\u0441\u0432\u043e\u0440\u0434", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"halal \u0440\u0443\u0442 \u043f\u0430\u0441\u0441\u0432\u043e\u0440\u0434", None))
        self.lineEdit_4.setText("")
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u0441\u043b\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u043e \u0432\u0430\u0441 \u0432 t.me/uzbeklinux \u043f\u043e\u0441\u043b\u0435 \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 \u043d\u0430\u0448\u0435\u0433\u043e \u0440\u0435\u0432\u043e\u043b\u044e\u0446\u0438\u044f\u2705", None))
    # retranslateUi

