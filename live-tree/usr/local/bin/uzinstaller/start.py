# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'startHuzzvZ.ui'
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
        MainWindow.resize(807, 453)
        MainWindow.setMinimumSize(QSize(807, 453))
        MainWindow.setMaximumSize(QSize(807, 453))
        icon = QIcon()
        icon.addFile(u"/usr/local/bin/uzinstaller/2705.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 130, 181, 181))
        self.label.setPixmap(QPixmap(u"/usr/local/bin/uzinstaller/2705.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(290, 130, 271, 31))
        font = QFont()
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(290, 170, 461, 141))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_7.setFont(font1)
        self.label_7.setText(u"\u0442\u044b \u0437\u043d\u0430\u043b? \u043d\u0435\u0442, \u0442\u044b \u043d\u0435 \u0437\u043d\u0430\u043b. **Uzbek Linux** \u044d\u0442\u043e \u043f\u0440\u043e\u0441\u0442\u043e \u0442\u043e\u043f\u043e\u0432\u0430\u044f \u0437\u0430\u043c\u0435\u043d\u0430 **haram** windoze! \u044f \u043d\u0430\u0432\u0430\u0439\u0431\u043a\u043e\u0434\u0438\u043b \u0442\u0435\u0431\u0435 **29.9%** \u0441\u0438\u0441\u0442\u0435\u043c\u044b \u0447\u0435\u0440\u0435\u0437 UzbekGPT, \u0438 \u0434\u0430, \u044d\u0442\u043e \u043c\u0435\u043d\u044c\u0448\u0435 \u0447\u0435\u043c \u0443 \u043c\u0438\u043a\u0440\u043e\u0441\u043b\u043e\u043f\u043e\u0432 **\u043d\u0430 0,1%**! \u0442\u044b \u0433\u043e\u0442\u043e\u0432 \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u043b\u0443\u0447\u0448\u0443\u044e \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u043e\u043d\u043d\u0443\u044e \u0441\u0438\u0441\u0442\u0435\u043c\u0443 \u0432 2026 \u0432\u0435\u043a\u0435?\u2620\ufe0f\u261d\ufe0f")
        self.label_7.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_7.setWordWrap(True)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(690, 400, 88, 34))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430 Uzbek Linux", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip(QCoreApplication.translate("MainWindow", u"\u0438\u0432\u0430", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u043f\u0440\u0438\u0432\u0435\u0442, \u043a\u0430\u043a \u0434\u0435\u043b\u0430\u2705", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043b\u0435\u0435", None))
    # retranslateUi

