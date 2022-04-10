# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mp3Gui2.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(564, 578)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 470, 181, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: ;\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 0px;\n"
"    border-color: beige;\n"
"    font: 20px;\n"
"    min-width: 3em;\n"
"    padding: 1px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 520, 551, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(255, 23, 38)")
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 400, 501, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textEdit_2.setFont(font)
        self.textEdit_2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.textEdit_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.textEdit_2.setLineWidth(3)
        self.textEdit_2.setMidLineWidth(0)
        self.textEdit_2.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 350, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 450, 141, 20))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 350, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgb(85, 255, 0)")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-20, -10, 611, 281))
        self.frame.setStyleSheet("image:url(:/logov4/logov4.png)")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(30, 290, 501, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textEdit_3.setFont(font)
        self.textEdit_3.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.textEdit_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.textEdit_3.setLineWidth(3)
        self.textEdit_3.setMidLineWidth(0)
        self.textEdit_3.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 240, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.frame.raise_()
        self.label_3.raise_()
        self.textEdit_2.raise_()
        self.label_4.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.label_5.raise_()
        self.textEdit_3.raise_()
        self.label_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Faiz Fauzi Youtube Playlist Downloader"))
        self.pushButton.setText(_translate("MainWindow", "Download"))
        self.label_3.setText(_translate("MainWindow", "Status"))
        self.label_4.setText(_translate("MainWindow", "Youtube Playlist Link:"))
        self.label.setText(_translate("MainWindow", "Designed by Faiz Fauzi"))
        self.label_6.setText(_translate("MainWindow", "Folder saved to # leave blank if want to use /root"))

import utube

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

