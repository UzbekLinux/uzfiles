# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerAKJbSu.ui'
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
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(831, 619)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 40, 681, 31))
        font = QFont()
        font.setFamilies([u"Sans Serif"])
        font.setPointSize(16)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 110, 371, 21))
        font1 = QFont()
        font1.setFamilies([u"Serif"])
        font1.setPointSize(16)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 140, 371, 101))
        font2 = QFont()
        font2.setFamilies([u"Sans Serif"])
        font2.setPointSize(12)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(430, 140, 371, 101))
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_4.setWordWrap(True)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(430, 110, 371, 21))
        self.label_5.setFont(font1)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(430, 240, 371, 21))
        self.label_6.setFont(font1)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 270, 371, 101))
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_7.setWordWrap(True)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 240, 371, 21))
        self.label_8.setFont(font1)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(430, 270, 371, 101))
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_9.setWordWrap(True)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(430, 400, 371, 101))
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_10.setWordWrap(True)
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(430, 370, 371, 21))
        self.label_11.setFont(font1)
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(30, 400, 371, 101))
        self.label_12.setFont(font2)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_12.setWordWrap(True)
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(30, 370, 371, 21))
        self.label_13.setFont(font1)
        self.pushButton_next = QPushButton(self.centralwidget)
        self.pushButton_next.setObjectName(u"pushButton_next")
        self.pushButton_next.setGeometry(QRect(180, 540, 481, 27))
        font3 = QFont()
        font3.setFamilies([u"Sans Serif"])
        self.pushButton_next.setFont(font3)
        icon = QIcon()
        icon.addFile(u"/usr/local/bin/uzinstaller/2705.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_next.setIcon(icon)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u043f\u0435\u0440\u0435\u0434 \u0442\u0435\u043c \u043a\u0430\u043a \u043d\u0430\u0447\u0430\u0442\u044c, \u043f\u0440\u043e\u0447\u0438\u0442\u0430\u0439\u0442\u0435 \u043f\u043e\u0447\u0435\u043c\u0443 Uzbek Linux \u0441\u0442\u043e\u0438\u0442 \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u044c \u0438 \u0441\u0442\u0430\u0431\u0438\u043b\u044c\u043d\u043e\u0441\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u043d\u0430\u0448 \u0434\u0438\u0441\u0442\u0440\u0438\u0431\u0443\u0442\u0438\u0432 \u043e\u0447\u0435\u043d\u044c \u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u044b\u0439, \u0431\u044b\u0441\u0442\u0440\u044b\u0439 \u0438 \u0441\u0442\u0430\u0431\u0438\u043b\u044c\u043d\u044b\u0439. \u0443 \u043d\u0430\u0441 \u043d\u0435\u0442 beta-\u0432\u0435\u0442\u043e\u043a \u0432 \u043d\u0430\u0448\u0435\u0439 \u0441\u0438\u0441\u0442\u0435\u043c\u0435 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0439. \u043f\u043e\u044d\u0442\u043e\u043c\u0443, \u0432\u044b \u0431\u0443\u0434\u0435\u0442\u0435 \u043f\u043e\u043b\u0443\u0447\u0430\u0442\u044c \u0442\u043e\u043b\u044c\u043a\u043e \u0441\u0430\u043c\u044b\u0435 \u0441\u0430\u043c\u044b\u0435 \u0441\u0432\u0435\u0436\u0438\u0435 \u0432\u0435\u0440\u0441\u0438\u0438 \u043d\u0430\u0448\u0435\u0433\u043e \u041f\u041e.", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"ZDE \u0438 \u043d\u0430\u0448\u0438 \u0444\u0438\u0440\u043c\u0435\u043d\u043d\u044b\u0435 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b \u043f\u0440\u0438\u0434\u0430\u0434\u0443\u0442 \u0431\u043e\u0433\u0430\u0442\u044b\u0439 \u0438 \u0443\u0437\u0431\u0435\u043a\u0441\u043a\u0438\u0439 \u0441\u0442\u0438\u043b\u044c \u0432\u0430\u0448\u0435\u043c\u0443 \u041f\u041a. \u043c\u044b \u0442\u0430\u043a\u0436\u0435 \u043f\u0440\u0435\u0434\u043e\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u043c 3 \u0431\u0435\u0441\u043f\u043b\u0430\u0442\u043d\u044b\u0445 \u043d\u0435\u0441\u043a\u0443\u0447\u043d\u044b\u0445 \u043e\u0431\u043e\u0435\u0432 \u0440\u0430\u0431\u043e\u0447\u0435\u0433\u043e \u0441\u0442\u043e\u043b\u0430 \u0432 \u043d\u0430\u0448\u0435\u0439 \u041e\u0421.", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0441\u0442\u0438\u043b\u044c\u043d\u044b\u0439 \u0438 \u043c\u043e\u0434\u043d\u044b\u0439", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0431\u043e\u043b\u044c\u0448\u0430\u044f \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430\u0446\u0438\u044f \u0438 \u0441\u043e\u043e\u0431\u0449\u0435\u0441\u0442\u0432\u043e", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u043c\u044b \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0430\u043b\u0438 \u043d\u043e\u0432\u044b\u0439 \u0441\u043b\u043e\u0439 \u0441\u043e\u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u0438 \u043c\u0435\u0436\u0434\u0443 Uzbek Linux \u0438 Arch Linux. \u043f\u043e\u044d\u0442\u043e\u043c\u0443 \u0432\u044b \u0441\u043c\u043e\u0436\u0435\u0442\u0435 \u0441\u0442\u0430\u0432\u0438\u0442\u044c \u043f\u0430\u043a\u0435\u0442\u044b \u0434\u043b\u044f Arch Linux \u043a\u0430\u043a \u043e\u0431\u044b\u0447\u043d\u043e. \u043c\u044b \u043d\u0435 \u0433\u0430\u0440\u0430\u043d\u0442\u0438\u0440\u0443\u0435\u043c \u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u044c Arch-\u043f\u0430\u043a\u0435\u0442\u043e\u0432.", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"100% \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0430 AUR \u0438 pacman", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u043c\u044b \u043f\u0440\u0435\u0434\u043e\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u043c \u0432\u0430\u043c \u0441\u0430\u043c\u0443\u044e \u043b\u0443\u0447\u0448\u0443\u044e \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430\u0446\u0438\u044e \u043d\u0430 \u0441\u0430\u0439\u0442\u0435. \u0442\u0430\u043c \u0432\u044b \u043d\u0430\u0439\u0434\u0435\u0442\u0435 \u0432\u0441\u0435 \u0432\u043e\u043f\u0440\u043e\u0441\u044b \u043c\u0438\u0440\u0430 Uzbek Linux. \u043d\u0430\u0448\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u0441\u0442\u0432\u043e \u0435\u0441\u0442\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u043e \u0432 \u0447\u0430\u0442\u0435 \u0445\u0443\u043a\u0440\u0435\u0441,\u0433\u0434\u0435 \u0432\u0430\u0441 \u043f\u043e\u0448\u043b\u044e\u0442 \u043d\u0430\u0445\u0443\u0439", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0432 \u043e\u0442\u043b\u0438\u0447\u0438\u0438 \u043e\u0442 ShefOS, \u043c\u044b \u0434\u0430\u0451\u043c \u043b\u0451\u0433\u043a\u043e\u0441\u0442\u044c \u0438 \u0443\u0434\u043e\u0431\u0441\u0442\u0432\u043e. \u043d\u0430\u0448 \u0434\u0438\u0441\u0442\u0440\u0438\u0431\u0443\u0442\u0438\u0432 \u043d\u0430\u043f\u0438\u0441\u0430\u043d \u043f\u043e\u043b\u043d\u043e\u0441\u0442\u044c\u044e \u0441 \u043d\u0443\u043b\u044f. \u0430 pacman \u044d\u0442\u043e \u043f\u0440\u043e\u0441\u0442\u043e \u043d\u0435\u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430. \u0443 \u043d\u0430\u0441 \u0445\u0430\u043b\u044f\u043b\u044c SPM (shit package manager).", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u043d\u0430\u0448 \u0434\u0438\u0441\u0442\u0440\u0438\u0431\u0443\u0442\u0438\u0432 \u0432\u0435\u0441\u0438\u0442 \u043c\u0435\u043d\u044c\u0448\u0435 320\u043a\u0433", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u043c\u044b \u043d\u0435 \u043c\u0438\u043a\u0440\u043e\u043f\u0435\u043d\u0438\u0441. \u043d\u0430\u0448\u0430 \u043a\u043e\u043c\u0430\u043d\u0434\u0430 \u0432\u0430\u0439\u0431\u043a\u043e\u0434\u0438\u0442 29.9% \u0441\u0438\u0441\u0442\u0435\u043c\u044b. Uzbek Linux \u0438\u043c\u0435\u0435\u0442 \u0432\u0430\u0439\u0431\u043a\u043e\u0434\u0430 \u043c\u0435\u043d\u044c\u0448\u0435 \u043d\u0430 0.1% \u0447\u0435\u043c \u0432 \u0441\u0432\u0438\u043d\u0434\u043e\u0432\u0441. \u043c\u044b \u043a\u043e\u0434\u0438\u043c \u0447\u0435\u0440\u0435\u0437 UzbekGPT, \u0430 \u043f\u043b\u043e\u0432\u0410\u0418 \u0434\u0430\u0451\u0442 \u043d\u0430\u043c \u043c\u043e\u0442\u0438\u0432\u0430\u0446\u0438\u044e.", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"29.9% \u0432\u0430\u0439\u0431\u043a\u043e\u0434\u0430", None))
        self.pushButton_next.setText(QCoreApplication.translate("MainWindow", u"\u043f\u0440\u0438\u0441\u0442\u0443\u043f\u0438\u0442\u044c \u043a \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0435", None))
    # retranslateUi

