# Form implementation generated from reading ui file 'lk.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox


class Ui_LKwindow(object):
    def setupUi(self, LKwindow):
        LKwindow.setObjectName("LKwindow")
        LKwindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(LKwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(35, 85, 265, 45))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(440, 90, 291, 21))
        self.label_2.setObjectName("label_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 130, 301, 121))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setPlaceholderText("Максимальная длина 30 символов \nШифровка перезаписывается в файл encryptedText.txt \nПробелы в шифре значимые")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(420, 130, 291, 121))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_2.setPlaceholderText("Максимальная длина 30 символов\nПробелы в шифре значимые\nРасшифровка перезаписывается в файл decipherText.txt")
        self.pushButtonEncrypt = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonEncrypt.setGeometry(QtCore.QRect(100, 260, 131, 31))
        self.pushButtonEncrypt.setObjectName("pushButtonEncrypt")
        self.pushButtonDecipher = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDecipher.setGeometry(QtCore.QRect(500, 260, 141, 31))
        self.pushButtonDecipher.setObjectName("pushButtonDecipher")
        self.pushButtonMain = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonMain.setGeometry(QtCore.QRect(590, 490, 191, 61))
        self.pushButtonMain.setObjectName("pushButtonMain")
        LKwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LKwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        LKwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LKwindow)
        self.statusbar.setObjectName("statusbar")
        LKwindow.setStatusBar(self.statusbar)

        self.retranslateUi(LKwindow)
        QtCore.QMetaObject.connectSlotsByName(LKwindow)

    def retranslateUi(self, LKwindow):
        _translate = QtCore.QCoreApplication.translate
        LKwindow.setWindowTitle(_translate("LKwindow", "Личный кабинет"))
        self.label.setText(_translate("LKwindow", "Введите текст, который вы хотите зашифровать"))
        self.label_2.setText(_translate("LKwindow", "Введите текст, который вы хотите расшифровать"))
        self.pushButtonEncrypt.setText(_translate("LKwindow", "Зашифровать"))
        self.pushButtonDecipher.setText(_translate("LKwindow", "Расшифровать текст"))
        self.pushButtonMain.setText(_translate("LKwindow", "Вернуться на главный экран"))
