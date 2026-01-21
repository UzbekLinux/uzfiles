# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'overviewkhLvYQ.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

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
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 201, 51))
        self.label.setPixmap(QPixmap(u"uzbek_logo.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(310, 10, 481, 51))
        font = QFont()
        font.setPointSize(14)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 70, 711, 21))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_3.setFont(font1)
        self.label_3.setTextFormat(Qt.TextFormat.MarkdownText)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(690, 400, 88, 34))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 100, 371, 31))
        font2 = QFont()
        font2.setPointSize(16)
        self.label_4.setFont(font2)
        self.label_4.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 140, 371, 91))
        self.label_5.setFont(font1)
        self.label_5.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_5.setWordWrap(True)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(410, 100, 371, 31))
        self.label_6.setFont(font2)
        self.label_6.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(410, 140, 371, 91))
        self.label_7.setFont(font1)
        self.label_7.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_7.setWordWrap(True)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(410, 240, 371, 31))
        self.label_8.setFont(font2)
        self.label_8.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(410, 280, 371, 91))
        self.label_9.setFont(font1)
        self.label_9.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_9.setWordWrap(True)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 240, 371, 31))
        self.label_10.setFont(font2)
        self.label_10.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 280, 371, 91))
        self.label_11.setFont(font1)
        self.label_11.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_11.setWordWrap(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430 Uzbek Linux", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"What doesn't kill you makes you stronger \u2705 ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u043f\u0440\u0438\u0432\u0435\u0442 Da.\u2705 \u044d\u0442\u043e **\u0423\u0437\u0431\u0435\u043a \u041b\u0438\u043d\u0443\u043a\u0441** \u0432\u043a\u0440\u0430\u0442\u0446\u0435:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043b\u0435\u0435", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"**\u0445\u0430\u0439\u043f\u043e\u0432\u044b\u0439 ZDE**", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0437\u0434\u0435\u0441\u044c \u0432\u0441\u0442\u0440\u043e\u0435\u043d \u0445\u0430\u0439\u043f\u043e\u0432\u044b\u0439 **ZDE** \u043e\u0442 **ZSoftware** \u043f\u043e\u0442\u043e\u043c\u0443 \u0447\u0442\u043e \u043e\u043d halal \u0438 \u043a\u0440\u0443\u0442\u043e\u0439 Da. \u043e\u043d \u0442\u0430\u043a\u0436\u0435 \u0432\u0435\u0440\u0438\u0444\u0438\u0446\u0438\u0440\u043e\u0432\u0430\u043d Uzbek\u2122 (\u0442.e, \u0435\u0441\u0442\u044c \u0432 uzbek-apps)\u261d\ufe0f\u261d\ufe0f", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"**\u043b\u0443\u0447\u0448\u0438\u0439 \u043e\u0431\u043d\u043e\u0432\u043b\u044f\u0442\u043e\u0440 \u0441\u0438\u0441\u0442\u0435\u043c\u0430**", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u044f \u0441\u0434\u0435\u043b\u0430\u043b \u0441\u0443\u043f\u0435\u0440\u0441\u043a\u0438\u0439 **uzupdate** \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u043e\u0431\u043d\u043e\u0432\u0438\u0442 \u0432\u0430\u0448 Uzbek Linux \u043d\u0430 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u044e\u044e \u0432\u0435\u0440\u0441\u0438\u044e \u0431\u0435\u0437 \u043f\u0440\u043e\u0431\u043b\u0435\u043c \u043f\u0440\u0438\u043c\u0435\u0440\u043d\u043e **\u0437\u0430 0.1 \u0441\u0435\u043a\u0443\u043d\u0434\u0443**\u2705", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"**halalfetch, uzinstall \u0438 \u0442.\u0434.**", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u043c\u044b (Uzbek\u2122, EblanSoft, ZSoftware) \u043f\u0435\u0440\u0435\u043f\u0438\u0441\u044b\u0432\u0430\u0435\u043c \u0432\u0441\u0435 \u043f\u043e\u043f\u0443\u043b\u044f\u0440\u043d\u044b\u0435 haram \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b. \u0447\u0442\u043e\u0431\u044b \u0437\u0430\u0449\u0438\u0442\u0438\u0442\u044c \u044e\u0437\u0435\u0440\u043e\u0432 \u0438 \u043f\u0440\u0435\u0434\u043e\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u043d\u0430\u0448\u0438 halal \u0430\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u044b.", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"**shit package manager**", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u044d\u0442\u043e \u0440\u0435\u0430\u043b\u044c\u043d\u043e \u043a\u0440\u0443\u0442\u043e\u0439 \u043f\u0430\u043a\u0435\u0442\u043d\u044b\u0439 \u043c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u043e\u0442 \u0437\u0435\u043d\u0443\u0441\u0443\u0441 \u0438 \u043e\u043d \u043d\u0430 100% halal \u0438 \u0435\u0441\u0442\u044c \u0432 \u0440\u0435\u043f\u043e **uzbek-apps**. \u0442\u0430\u043c \u0435\u0441\u0442\u044c \u043e\u0447\u0435\u043d\u044c \u043c\u043d\u043e\u0433\u043e \u043f\u0440\u043e\u0433 \u043e\u0442 EblanSoft.", None))
    # retranslateUi

