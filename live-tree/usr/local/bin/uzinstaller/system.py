# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerioUdMI.ui'
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
from PyQt6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(831, 619)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 40, 591, 31))
        font = QFont()
        font.setFamilies([u"Sans Serif"])
        font.setPointSize(16)
        self.label.setFont(font)
        self.auto_RadioButton = QRadioButton(self.centralwidget)
        self.auto_RadioButton.setObjectName(u"auto_RadioButton")
        self.auto_RadioButton.setGeometry(QRect(30, 110, 361, 24))
        font1 = QFont()
        font1.setFamilies([u"Sans Serif"])
        font1.setPointSize(12)
        self.auto_RadioButton.setFont(font1)
        self.manual_RadioButton = QRadioButton(self.centralwidget)
        self.manual_RadioButton.setObjectName(u"manual_RadioButton")
        self.manual_RadioButton.setGeometry(QRect(410, 110, 391, 24))
        self.manual_RadioButton.setFont(font1)
        self.Auto_Disk_comboBox = QComboBox(self.centralwidget)
        self.Auto_Disk_comboBox.setObjectName(u"Auto_Disk_comboBox")
        self.Auto_Disk_comboBox.setGeometry(QRect(30, 190, 361, 27))
        font2 = QFont()
        font2.setFamilies([u"Sans Serif"])
        self.Auto_Disk_comboBox.setFont(font2)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 140, 361, 41))
        font3 = QFont()
        font3.setFamilies([u"Sans Serif"])
        font3.setPointSize(12)
        font3.setItalic(True)
        self.label_2.setFont(font3)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_2.setWordWrap(True)
        self.manual_root_ComboBox = QComboBox(self.centralwidget)
        self.manual_root_ComboBox.setObjectName(u"manual_root_ComboBox")
        self.manual_root_ComboBox.setGeometry(QRect(410, 190, 361, 27))
        self.manual_root_ComboBox.setFont(font2)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(410, 140, 361, 41))
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_3.setWordWrap(True)
        self.manual_boot_comboBox = QComboBox(self.centralwidget)
        self.manual_boot_comboBox.setObjectName(u"manual_boot_comboBox")
        self.manual_boot_comboBox.setGeometry(QRect(410, 220, 361, 27))
        self.manual_boot_comboBox.setFont(font2)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(30, 270, 771, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.bootloader_comboBox = QComboBox(self.centralwidget)
        self.bootloader_comboBox.setObjectName(u"bootloader_comboBox")
        self.bootloader_comboBox.setGeometry(QRect(30, 340, 741, 27))
        self.bootloader_comboBox.setFont(font2)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 290, 771, 41))
        self.label_4.setFont(font3)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_4.setWordWrap(True)
        self.displayManager_comboBox = QComboBox(self.centralwidget)
        self.displayManager_comboBox.setObjectName(u"displayManager_comboBox")
        self.displayManager_comboBox.setGeometry(QRect(30, 370, 741, 27))
        self.displayManager_comboBox.setFont(font2)
        self.pushButton_next = QPushButton(self.centralwidget)
        self.pushButton_next.setObjectName(u"pushButton_next")
        self.pushButton_next.setGeometry(QRect(180, 540, 161, 27))
        self.pushButton_next.setFont(font2)
        icon = QIcon()
        icon.addFile(u"/usr/local/bin/uzinstaller/2705.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_next.setIcon(icon)
        self.pushButton_next_2 = QPushButton(self.centralwidget)
        self.pushButton_next_2.setObjectName(u"pushButton_next_2")
        self.pushButton_next_2.setGeometry(QRect(350, 540, 311, 27))
        self.pushButton_next_2.setFont(font2)
        self.pushButton_next_2.setIcon(icon)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0440\u0430\u0437\u0434\u0435\u043b\u044b \u0438 \u0431\u0430\u0437\u043e\u0432\u0430\u044f \u043a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u044f \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0438 Uzbek Linux 2026.2", None))
        self.auto_RadioButton.setText(QCoreApplication.translate("MainWindow", u"\u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0440\u0430\u0437\u043c\u0435\u0442\u043a\u0430", None))
        self.manual_RadioButton.setText(QCoreApplication.translate("MainWindow", u"\u0440\u0443\u0447\u043d\u0430\u044f \u0440\u0430\u0437\u043c\u0435\u0442\u043a\u0430", None))
        self.Auto_Disk_comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0432\u044b\u0431\u0435\u0440\u0438 \u0437\u0434\u0435\u0441\u044c \u0441\u0432\u043e\u0439 \u0434\u0438\u0441\u043a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u043d\u0430\u0448\u0430 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0432\u0441\u0451 \u0441\u0434\u0435\u043b\u0430\u0435\u0442 \u0437\u0430 \u0432\u0430\u0441 \u0438 \u0440\u0430\u0437\u043c\u0435\u0442\u0438\u0442 \u0434\u0438\u0441\u043a \u043a\u0430\u043a \u043d\u0430\u0434\u043e", None))
        self.manual_root_ComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0432\u044b\u0431\u0435\u0440\u0438 \u0437\u0434\u0435\u0441\u044c \u0440\u0443\u0442 \u0440\u0430\u0437\u0434\u0435\u043b", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0432\u044b \u0441\u0430\u043c\u0438 \u0432\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u0437\u0430\u0433\u0440\u0443\u0437\u043e\u0447\u043d\u044b\u0439 \u0440\u0430\u0437\u0434\u0435\u043b \u0438 \u0440\u0430\u0437\u0434\u0435\u043b \u043a\u0443\u0434\u0430 \u0431\u0443\u0434\u0435\u0442 \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d\u0430 \u0441\u0438\u0441\u0442\u0435\u043c\u0430", None))
        self.manual_boot_comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0432\u044b\u0431\u0435\u0440\u0438 \u0437\u0434\u0435\u0441\u044c \u0437\u0430\u0433\u0440\u0443\u0437\u043e\u0447\u043d\u044b\u0439 \u0440\u0430\u0437\u0434\u0435\u043b", None))
        self.bootloader_comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0437\u0434\u0435\u0441\u044c \u043d\u0443\u0436\u043d\u043e \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u0437\u0430\u0433\u0440\u0443\u0437\u0447\u0438\u043a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0442\u0443\u0442 \u0432\u0430\u043c \u043d\u0443\u0436\u043d\u043e \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u0432\u0430\u0448 \u0437\u0430\u0433\u0440\u0443\u0437\u0447\u0438\u043a \u0438 \u0434\u0438\u0441\u043f\u043b\u0435\u0439\u043d\u044b\u0439 \u043c\u0435\u043d\u0435\u0434\u0436\u0435\u0440. \u0443\u0437\u0431\u0435\u043a\u0438 \u0440\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u044e\u0442 sddm \u0438 grub. \u0432\u044b\u0431\u043e\u0440 \u043c\u043e\u0436\u0435\u0442 \u0431\u044b\u0442\u044c \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d \u0435\u0441\u043b\u0438 \u0432\u0430\u0448 \u043f\u043a \u043d\u0435 \u0442\u0430\u043a\u043e\u0439 \u043a\u0440\u0443\u0442\u043e\u0439.", None))
        self.displayManager_comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0437\u0434\u0435\u0441\u044c \u043d\u0443\u0436\u043d\u043e \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u0434\u0438\u0441\u043f\u043b\u0435\u0439\u043d\u044b\u0439 \u043c\u0435\u043d\u0435\u0434\u0436\u0435\u0440", None))
        self.pushButton_next.setText(QCoreApplication.translate("MainWindow", u"\u0434\u0430\u043b\u0435\u0435", None))
        self.pushButton_next_2.setText(QCoreApplication.translate("MainWindow", u"\u043e\u0442\u043a\u0440\u044b\u0442\u044c GayParted", None))
    # retranslateUi

