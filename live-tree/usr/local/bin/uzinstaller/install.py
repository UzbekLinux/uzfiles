# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerrkUESV.ui'
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
from PyQt6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(831, 619)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 40, 291, 31))
        font = QFont()
        font.setFamilies([u"Sans Serif"])
        font.setPointSize(16)
        self.label.setFont(font)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 110, 771, 21))
        font1 = QFont()
        font1.setFamilies([u"Sans Serif"])
        font1.setPointSize(13)
        font1.setItalic(True)
        self.label_6.setFont(font1)
        self.label_6.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_6.setWordWrap(True)
        self.pushButton_next = QPushButton(self.centralwidget)
        self.pushButton_next.setObjectName(u"pushButton_next")
        self.pushButton_next.setGeometry(QRect(180, 540, 231, 27))
        font2 = QFont()
        font2.setFamilies([u"Sans Serif"])
        self.pushButton_next.setFont(font2)
        icon = QIcon()
        icon.addFile(u"/usr/local/bin/uzinstaller/2705.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_next.setIcon(icon)
        self.pushButton_reboot = QPushButton(self.centralwidget)
        self.pushButton_reboot.setObjectName(u"pushButton_reboot")
        self.pushButton_reboot.setGeometry(QRect(420, 540, 241, 27))
        self.pushButton_reboot.setFont(font2)
        self.pushButton_reboot.setIcon(icon)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 30, 181, 51))
        self.label_2.setPixmap(QPixmap(u"/usr/local/bin/uzinstaller/uzbek_logo.png"))
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(620, 30, 181, 51))
        self.label_3.setPixmap(QPixmap(u"/usr/local/bin/uzinstaller/uzbek_logo.png"))
        self.label_3.setScaledContents(True)
        self.terminalView = QTextEdit(self.centralwidget)
        self.terminalView.setObjectName(u"terminalView")
        self.terminalView.setGeometry(QRect(30, 140, 771, 381))
        font3 = QFont()
        font3.setFamilies([u"Monospace"])
        font3.setPointSize(10)
        self.terminalView.setFont(font3)
        self.terminalView.setAutoFillBackground(False)
        self.terminalView.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430 Uzbek Linux 2026.2", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0434\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c \u0432 Uzbek Linux 2026.2! \u043e\u0436\u0438\u0434\u0430\u0439\u0442\u0435 \u043f\u043e\u043a\u0430 \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430 \u0437\u0430\u043a\u043e\u043d\u0447\u0438\u0442\u0441\u044f.", None))
        self.pushButton_next.setText(QCoreApplication.translate("MainWindow", u"\u0432\u044b\u0439\u0442\u0438 \u0438\u0437 \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u0449\u0438\u043a\u0430", None))
        self.pushButton_reboot.setText(QCoreApplication.translate("MainWindow", u"\u043f\u0435\u0440\u0435\u0437\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440", None))
        self.label_2.setText("")
        self.label_3.setText("")
    # retranslateUi

