# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/ui/os.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_os(object):
    def setupUi(self, os):
        os.setObjectName("os")
        os.resize(800, 500)
        os.setStyleSheet("background-color: #333333;\n"
"color: white;\n"
"")
        self.label = QtWidgets.QLabel(os)
        self.label.setGeometry(QtCore.QRect(0, 40, 800, 61))
        font = QtGui.QFont()
        font.setFamily("UD Digi Kyokasho NP-B")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("font-size: 46px;a=")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_6 = QtWidgets.QPushButton(os)
        self.pushButton_6.setGeometry(QtCore.QRect(40, 170, 341, 51))
        font = QtGui.QFont()
        font.setFamily("UD Digi Kyokasho NK-B")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("font-size: 18px;\n"
"background-color: white;\n"
"color: #222222;\n"
"border: 3px solid #555555;\n"
"border-radius: 10px")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_8 = QtWidgets.QPushButton(os)
        self.pushButton_8.setGeometry(QtCore.QRect(40, 230, 341, 51))
        font = QtGui.QFont()
        font.setFamily("UD Digi Kyokasho NK-B")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("font-size: 18px;\n"
"background-color: white;\n"
"color: #222222;\n"
"border: 3px solid #555555;\n"
"border-radius: 10px")
        self.pushButton_8.setObjectName("pushButton_8")
        self.textEdit_2 = QtWidgets.QTextEdit(os)
        self.textEdit_2.setEnabled(False)
        self.textEdit_2.setGeometry(QtCore.QRect(40, 380, 721, 41))
        font = QtGui.QFont()
        font.setFamily("UD Digi Kyokasho NK-B")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setAutoFillBackground(False)
        self.textEdit_2.setStyleSheet("font-size: 17px;\n"
"outline: none;\n"
"border-radius: 10px;\n"
"background-color: #fff;\n"
"color: black;\n"
"padding: 5px 9px;s")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_3 = QtWidgets.QLabel(os)
        self.label_3.setGeometry(QtCore.QRect(40, 350, 721, 21))
        font = QtGui.QFont()
        font.setFamily("UD Digi Kyokasho NK-B")
        font.setPointSize(-1)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font-size: 22px;\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton_12 = QtWidgets.QPushButton(os)
        self.pushButton_12.setGeometry(QtCore.QRect(410, 170, 341, 51))
        font = QtGui.QFont()
        font.setFamily("UD Digi Kyokasho NK-B")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("font-size: 18px;\n"
"background-color: white;\n"
"color: #222222;\n"
"border: 3px solid #555555;\n"
"border-radius: 10px;")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(os)
        self.pushButton_13.setGeometry(QtCore.QRect(410, 230, 341, 51))
        font = QtGui.QFont()
        font.setFamily("UD Digi Kyokasho NK-B")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("font-size: 18px;\n"
"background-color: white;\n"
"color: #222222;\n"
"border: 3px solid #555555;\n"
"border-radius: 10px;")
        self.pushButton_13.setObjectName("pushButton_13")

        self.retranslateUi(os)
        QtCore.QMetaObject.connectSlotsByName(os)

    def retranslateUi(self, os):
        _translate = QtCore.QCoreApplication.translate
        os.setWindowTitle(_translate("os", "Form"))
        self.label.setText(_translate("os", "Migoto/OS"))
        self.pushButton_6.setText(_translate("os", "Name of the operating system"))
        self.pushButton_8.setText(_translate("os", "Current process’s user id."))
        self.textEdit_2.setHtml(_translate("os", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'UD Digi Kyokasho NK-B\'; font-size:17px; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("os", "Output"))
        self.pushButton_12.setText(_translate("os", "Home directory"))
        self.pushButton_13.setText(_translate("os", "???"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    os = QtWidgets.QWidget()
    ui = Ui_os()
    ui.setupUi(os)
    os.show()
    sys.exit(app.exec_())