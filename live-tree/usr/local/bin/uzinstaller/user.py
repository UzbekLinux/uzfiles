# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerabttYg.ui'
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
from PyQt6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(831, 619)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(240, 40, 341, 31))
        font = QFont()
        font.setFamilies([u"Sans Serif"])
        font.setPointSize(16)
        self.label.setFont(font)
        self.UserNameEdit = QLineEdit(self.centralwidget)
        self.UserNameEdit.setObjectName(u"UserNameEdit")
        self.UserNameEdit.setGeometry(QRect(30, 120, 281, 27))
        font1 = QFont()
        font1.setFamilies([u"Sans Serif"])
        self.UserNameEdit.setFont(font1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(330, 120, 471, 31))
        font2 = QFont()
        font2.setFamilies([u"Sans Serif"])
        font2.setPointSize(14)
        font2.setItalic(True)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(330, 160, 471, 31))
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_3.setWordWrap(True)
        self.HostNameEdit = QLineEdit(self.centralwidget)
        self.HostNameEdit.setObjectName(u"HostNameEdit")
        self.HostNameEdit.setGeometry(QRect(30, 160, 281, 27))
        self.HostNameEdit.setFont(font1)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(30, 200, 771, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(330, 230, 471, 31))
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_4.setWordWrap(True)
        self.UserPassWordEdit = QLineEdit(self.centralwidget)
        self.UserPassWordEdit.setObjectName(u"UserPassWordEdit")
        self.UserPassWordEdit.setGeometry(QRect(30, 230, 281, 27))
        self.UserPassWordEdit.setFont(font1)
        self.UserPassWordEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(330, 270, 471, 31))
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_5.setWordWrap(True)
        self.RootPassWordEdit = QLineEdit(self.centralwidget)
        self.RootPassWordEdit.setObjectName(u"RootPassWordEdit")
        self.RootPassWordEdit.setGeometry(QRect(30, 270, 281, 27))
        self.RootPassWordEdit.setFont(font1)
        self.RootPassWordEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 340, 771, 151))
        font3 = QFont()
        font3.setFamilies([u"Sans Serif"])
        font3.setPointSize(13)
        font3.setItalic(True)
        self.label_6.setFont(font3)
        self.label_6.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_6.setWordWrap(True)
        self.pushButton_next = QPushButton(self.centralwidget)
        self.pushButton_next.setObjectName(u"pushButton_next")
        self.pushButton_next.setGeometry(QRect(180, 540, 481, 27))
        self.pushButton_next.setFont(font1)
        icon = QIcon()
        icon.addFile(u"/usr/local/bin/uzinstaller/2705.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_next.setIcon(icon)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(30, 310, 771, 16))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u043a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u044f \u0441\u043e\u0431\u0438\u0440\u0430\u0435\u043c\u044b\u0445 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.UserNameEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0438\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"- \u0438\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f (\u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440: uzbek)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"- \u0438\u043c\u044f \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u0430 (\u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440: uzbek-pc)", None))
        self.HostNameEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0438\u043c\u044f \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u0430", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"- \u043f\u0430\u0440\u043e\u043b\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.UserPassWordEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u043f\u0430\u0440\u043e\u043b\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"- \u043f\u0430\u0440\u043e\u043b\u044c \u0441\u0443\u043f\u0435\u0440\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.RootPassWordEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u043f\u0430\u0440\u043e\u043b\u044c \u0441\u0443\u043f\u0435\u0440\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u043f\u043e \u043d\u0430\u0436\u0430\u0442\u0438\u044e \u043a\u043d\u043e\u043f\u043a\u0438 \"\u0443\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c\" \u043d\u0430\u0447\u043d\u0451\u0442\u0441\u044f \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430 **Uzbek Linux 2026.2**. \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0435 \u0432\u0430\u043c\u0438 \u0440\u0430\u0437\u0434\u0435\u043b\u044b/\u0434\u0438\u0441\u043a **\u0431\u0443\u0434\u0443\u0442 \u043e\u0442\u0444\u043e\u0440\u043c\u0430\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u044b** \u0438 \u0434\u0430\u043d\u043d\u044b\u0435 \u043d\u0430 \u043d\u0438\u0445 \u043f\u0440\u043e\u043f\u0430\u0434\u0443\u0442 (\u043d\u0435\u043e\u0436\u0438\u0434\u0430\u043d\u043d\u043e,\u0434\u0430?). \u043d\u0435 \u0432\u044b\u043a\u043b\u044e\u0447\u0430\u0439\u0442\u0435 \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440 \u0438 \u043d\u0435 \u0437\u0430\u043a\u0440\u044b\u0432\u0430\u0439\u0442\u0435 \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043e\u0447"
                        "\u043d\u043e\u0435 \u0441\u0440\u0435\u0434\u0441\u0442\u0432\u043e \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u043e\u043d\u043d\u043e\u0439 \u0441\u0438\u0441\u0442\u0435\u043c\u044b Uzbek Linux \u0432\u0435\u0440\u0441\u0438\u0438 2026.2 \u043d\u0430 \u0431\u0430\u0437\u0435 GNU/Linux.", None))
        self.pushButton_next.setText(QCoreApplication.translate("MainWindow", u"\u0443\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
    # retranslateUi

