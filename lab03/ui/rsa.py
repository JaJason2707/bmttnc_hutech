# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/rsa.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1016, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 30, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 71, 16))
        self.label_2.setObjectName("label_2")
        self.txtplaintext = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txtplaintext.setGeometry(QtCore.QRect(90, 120, 341, 101))
        self.txtplaintext.setObjectName("txtplaintext")
        self.txtcptext = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txtcptext.setGeometry(QtCore.QRect(90, 280, 341, 101))
        self.txtcptext.setObjectName("txtcptext")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 280, 71, 16))
        self.label_3.setObjectName("label_3")
        self.txtinfomation = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txtinfomation.setGeometry(QtCore.QRect(570, 120, 341, 101))
        self.txtinfomation.setObjectName("txtinfomation")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(490, 120, 71, 16))
        self.label_4.setObjectName("label_4")
        self.txtsign = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txtsign.setGeometry(QtCore.QRect(580, 280, 341, 101))
        self.txtsign.setObjectName("txtsign")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(500, 280, 71, 16))
        self.label_5.setObjectName("label_5")
        self.btnen = QtWidgets.QPushButton(self.centralwidget)
        self.btnen.setGeometry(QtCore.QRect(90, 420, 93, 28))
        self.btnen.setObjectName("btnen")
        self.btnde = QtWidgets.QPushButton(self.centralwidget)
        self.btnde.setGeometry(QtCore.QRect(330, 420, 93, 28))
        self.btnde.setObjectName("btnde")
        self.btninfo = QtWidgets.QPushButton(self.centralwidget)
        self.btninfo.setGeometry(QtCore.QRect(570, 420, 93, 28))
        self.btninfo.setObjectName("btninfo")
        self.btnsign = QtWidgets.QPushButton(self.centralwidget)
        self.btnsign.setGeometry(QtCore.QRect(810, 420, 93, 28))
        self.btnsign.setObjectName("btnsign")
        self.btngenerate = QtWidgets.QPushButton(self.centralwidget)
        self.btngenerate.setGeometry(QtCore.QRect(480, 30, 93, 28))
        self.btngenerate.setObjectName("btngenerate")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1016, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "RSA CIPHER"))
        self.label_2.setText(_translate("MainWindow", "Plain Text"))
        self.label_3.setText(_translate("MainWindow", "Cipher Text"))
        self.label_4.setText(_translate("MainWindow", "Infomation"))
        self.label_5.setText(_translate("MainWindow", "SIgnature"))
        self.btnen.setText(_translate("MainWindow", "encrypt"))
        self.btnde.setText(_translate("MainWindow", "decrypt"))
        self.btninfo.setText(_translate("MainWindow", "information"))
        self.btnsign.setText(_translate("MainWindow", "signature"))
        self.btngenerate.setText(_translate("MainWindow", "generate keys"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
