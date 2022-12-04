from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from auth import Ui_MainWindow
from lk import Ui_LKwindow
import numpy as np


import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

#Функция всплывающего оповещения
def message(text):
    msg = QMessageBox()
    msg.setWindowTitle("Оповещение")
    msg.setText(text)
    msg.exec()

#Функция шифрования
def Encrypt(word):
    a = np.array(
        [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " "]])
    b = np.array(
        [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " "]])

    l = len(word)
    lenFlag = 0
    for i in range(5):
        for j in range(6):
            if lenFlag < l:
                a[i, j] = word[lenFlag]
                lenFlag += 1

    # смена строк
    b[0], b[1], b[2], b[3], b[4] = a[2], a[3], a[0], a[4], a[1]

    # смена столбцов
    a[:, 0], a[:, 1], a[:, 2], a[:, 3], a[:, 4], a[:, 5] = b[:, 1], b[:, 3], b[:, 5], b[:, 0], b[:, 2], b[:, 4]

    word = ""
    for i in range(5):
        for j in range(6):
            word += a[i,j]
    return word

#Функция дешифрования
def Decipher(word):
    a = np.array(
        [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " "]])
    b = np.array(
        [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " "]])

    l = len(word)
    lenFlag = 0
    for i in range(5):
        for j in range(6):
            if lenFlag < l:
                a[i, j] = word[lenFlag]
                lenFlag = lenFlag + 1

    #смена строк
    b[2], b[3], b[0], b[4], b[1] = a[0], a[1], a[2], a[3], a[4]

    #смена столбцов
    a[:, 1], a[:, 3], a[:, 5], a[:, 0], a[:, 2], a[:, 4] = b[:, 0], b[:, 1], b[:, 2], b[:, 3], b[:, 4], b[:, 5]

    word = ""
    for i in range(5):
        for j in range(6):
            word += a[i, j]
    return word

#Функции считывания логина и пароля
def log():
    log = ui.plainTextEditLog.toPlainText()
    return log
def pas():
    pas = ui.plainTextEditPass.toPlainText()
    return pas

#Функция отчистки полей логина и пароля
def clear():
    ui.plainTextEditLog.setPlainText("")
    ui.plainTextEditPass.setPlainText("")

#Функция авторизации + работа личного кабинета
def click_auth():
    with open('credentials.txt', 'r') as f:
        flag = 0
        credentials = log() + pas()
        for row in f:
            if row == Encrypt(credentials) + "\n":
                flag = 1
                break
    clear()
    if flag == 1:
        global LKwindow
        LKwindow = QtWidgets.QMainWindow()
        ui = Ui_LKwindow()
        ui.setupUi(LKwindow)
        MainWindow.close()
        LKwindow.show()

        def toMain():
            MainWindow.show()
            LKwindow.close()
        def textEnc():
            text = ui.plainTextEdit.toPlainText()
            if len(text) > 30:
                message("Превышен лимит символов")
            else:
                with open("encryptedText.txt", "w") as k:
                    k.write(Encrypt(text))
                message("Шифровка записана в файл encryptedText.txt")
        def textBack():
            encryptedText = ui.plainTextEdit_2.toPlainText()
            if len(encryptedText) > 30:
                message("Превышен лимит символов")
            else:
                encryptedText = Decipher(encryptedText)
                encryptedText = encryptedText.strip()
                mes = "Расшифровка: \n" + encryptedText
                message(mes + "\nРасшифровка перезаписана в decipherText.txt")
                with open("decipherText.txt", "w") as k:
                    k.write(mes)


        ui.pushButtonMain.clicked.connect(toMain)
        ui.pushButtonEncrypt.clicked.connect(textEnc)
        ui.pushButtonDecipher.clicked.connect(textBack)
    else:
        message("Неверный логин или пароль, попробуте еще раз")

#Функция регистрации
def click_reg():
    with open('login.txt', 'r') as f:
        for row in f:
            flag = 0
            if (Encrypt(log()) + "\n") == row:
                message("Такой логин уже существует")
                flag = 1
                break
        if flag == 0:
            checkLog = len(log())
            checkPas = len(pas())
            if checkLog < 16 and checkLog > 4 and checkPas < 16 and checkPas > 4:
                space = " "
                if space in log() or space in pas():
                    message("Недопустимый символ в логине или пароле: Пробел")
                else:
                    with open('login.txt', 'a') as f:
                        f.write(Encrypt(log()) + "\n")
                    with open('credentials.txt', 'a') as d:
                        credentials = log() + pas()
                        d.write(Encrypt(credentials) + '\n')
                    clear()
            else:
                message("Некорректные логин или пароль, попробуйте еще раз")

ui.pushButtonRegistration.clicked.connect(click_reg)
ui.pushButtonLogin.clicked.connect(click_auth)

sys.exit(app.exec())

