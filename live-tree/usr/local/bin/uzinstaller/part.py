# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'partuPYpuN.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QWidget)

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
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(20, 90, 471, 22))
        font1 = QFont()
        font1.setPointSize(11)
        self.radioButton.setFont(font1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 70, 711, 18))
        font2 = QFont()
        font2.setPointSize(12)
        self.label_3.setFont(font2)
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(20, 110, 471, 22))
        self.radioButton_2.setFont(font1)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 140, 321, 21))
        self.label_4.setMaximumSize(QSize(1000, 1000))
        self.label_4.setFont(font2)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 160, 761, 32))
        self.comboBox.setCurrentText(u"")
        self.comboBox.setPlaceholderText(u"\u0432\u044b\u0431\u0435\u0440\u0438 \u0434\u0438\u0441\u043a \u044d\u0442\u043e \u0442\u0438\u043f\u0430 /dev/sda \u0438\u043b\u0438 \u043f\u043e\u0434\u043e\u0431\u043d\u043e\u0435 Da.")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 210, 471, 18))
        self.label_5.setFont(font2)
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(20, 230, 761, 32))
        self.comboBox_2.setCurrentText(u"")
        self.comboBox_2.setPlaceholderText(u"\u0432\u044b\u0431\u0435\u0440\u0438 \u0440\u0430\u0437\u0434\u0435\u043b Da.")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 270, 471, 18))
        self.label_6.setFont(font2)
        self.comboBox_3 = QComboBox(self.centralwidget)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(20, 290, 761, 32))
        self.comboBox_3.setCurrentText(u"")
        self.comboBox_3.setPlaceholderText(u"\u0432\u044b\u0431\u0435\u0440\u0438 \u0440\u0430\u0437\u0434\u0435\u043b Da.")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(690, 400, 88, 34))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(587, 400, 101, 34))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 410, 561, 18))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setItalic(True)
        self.label_7.setFont(font3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430 Uzbek Linux", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"What doesn't kill you makes you stronger \u2705 ", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0440\u0430\u0437\u043c\u0435\u0442\u043a\u0430 UzbekPartitions\u2122", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0432\u044b\u0431\u0435\u0440\u0438 \u0441\u0443\u043a\u0430 \u043a\u0430\u043a \u043c\u044b \u0442\u0435\u0431\u0435 \u0434\u0438\u0441\u043a \u043d\u0430\u0441\u0438\u043b\u043e\u0432\u0430\u0442\u044c \u0431\u0443\u0434\u0435\u0442 \u0443\u0437\u0431\u0435\u043a\u043e\u043c\u2705\u2705", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0440\u0443\u0447\u043d\u0430\u044f haram \u0440\u0430\u0437\u043c\u0435\u0442\u043a\u0430\u274c\u274c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"UzbekPartitions\u2122 \u0434\u0438\u0441\u043a \u043a\u0443\u0434\u0430 \u0441\u0442\u0430\u0432\u0438\u0442\u044c \u0441\u0443\u043a\u0430:", None))
#if QT_CONFIG(tooltip)
        self.comboBox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0440\u0430\u0437\u0434\u0435\u043b \u0434\u043b\u044f root (\u0440\u0443\u0447\u043d\u0430\u044f \u0440\u0430\u0437\u043c\u0435\u0442\u043a\u0430):", None))
#if QT_CONFIG(tooltip)
        self.comboBox_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0440\u0430\u0437\u0434\u0435\u043b \u0434\u043b\u044f efi (\u0440\u0443\u0447\u043d\u0430\u044f \u0440\u0430\u0437\u043c\u0435\u0442\u043a\u0430):", None))
#if QT_CONFIG(tooltip)
        self.comboBox_3.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043b\u0435\u0435", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"GayParted", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u043d\u0435 \u0437\u043d\u0430\u0435\u0448\u044c \u043a\u0430\u043a\u043e\u0439 \u0438\u043c\u0435\u043d\u043d\u043e \u0440\u0430\u0437\u0434\u0435\u043b \u0432\u044b\u0431\u0440\u0430\u0442\u044c? \u043e\u0442\u043a\u0440\u043e\u0439 GayParted >>>", None))
    # retranslateUi

