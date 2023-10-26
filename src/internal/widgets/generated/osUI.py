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
        self.header = QtWidgets.QLabel(os)
        self.header.setGeometry(QtCore.QRect(0, 40, 800, 61))
        font = QtGui.QFont()
        font.setFamily("UD Digi Kyokasho NP-B")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.header.setFont(font)
        self.header.setStyleSheet("font-size: 46px;a=")
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")
        self.btn_osname = QtWidgets.QPushButton(os)
        self.btn_osname.setGeometry(QtCore.QRect(40, 170, 341, 51))
        font = QtGui.QFont()
        font.setFamily("UD Digi Kyokasho NK-B")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btn_osname.setFont(font)
        self.btn_osname.setStyleSheet("font-size: 18px;\n"
"background-color: white;\n"
"color: #222222;\n"
"border: 3px solid #555555;\n"
"border-radius: 10px")
        self.btn_osname.setObjectName("btn_osname")
        self.btn_pid = QtWidgets.QPushButton(os)
        self.btn_pid.setGeometry(QtCore.QRect(40, 230, 341, 51))
        font = QtGui.QFont()
        font.setFamily("UD Digi Kyokasho NK-B")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btn_pid.setFont(font)
        self.btn_pid.setStyleSheet("font-size: 18px;\n"
"background-color: white;\n"
"color: #222222;\n"
"border: 3px solid #555555;\n"
"border-radius: 10px")
        self.btn_pid.setObjectName("btn_pid")
        self.label_output = QtWidgets.QLabel(os)
        self.label_output.setGeometry(QtCore.QRect(40, 400, 721, 21))
        font = QtGui.QFont()
        font.setFamily("UD Digi Kyokasho NK-B")
        font.setPointSize(-1)
        self.label_output.setFont(font)
        self.label_output.setStyleSheet("font-size: 22px;\n"
"")
        self.label_output.setAlignment(QtCore.Qt.AlignCenter)
        self.label_output.setObjectName("label_output")
        self.btn_home = QtWidgets.QPushButton(os)
        self.btn_home.setGeometry(QtCore.QRect(410, 170, 341, 51))
        font = QtGui.QFont()
        font.setFamily("UD Digi Kyokasho NK-B")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btn_home.setFont(font)
        self.btn_home.setStyleSheet("font-size: 18px;\n"
"background-color: white;\n"
"color: #222222;\n"
"border: 3px solid #555555;\n"
"border-radius: 10px;")
        self.btn_home.setObjectName("btn_home")
        self.btn_user = QtWidgets.QPushButton(os)
        self.btn_user.setGeometry(QtCore.QRect(410, 230, 341, 51))
        font = QtGui.QFont()
        font.setFamily("UD Digi Kyokasho NK-B")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btn_user.setFont(font)
        self.btn_user.setStyleSheet("font-size: 18px;\n"
"background-color: white;\n"
"color: #222222;\n"
"border: 3px solid #555555;\n"
"border-radius: 10px;")
        self.btn_user.setObjectName("btn_user")
        self.output = QtWidgets.QTextBrowser(os)
        self.output.setGeometry(QtCore.QRect(40, 430, 731, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.output.setFont(font)
        self.output.setStyleSheet("background: white;\n"
"color: black;\n"
"outline: none;\n"
"border-radius: 10px;\n"
"padding: 5px 9px;")
        self.output.setObjectName("output")

        self.retranslateUi(os)
        QtCore.QMetaObject.connectSlotsByName(os)

    def retranslateUi(self, os):
        _translate = QtCore.QCoreApplication.translate
        os.setWindowTitle(_translate("os", "Migoto/OS"))
        self.header.setText(_translate("os", "Migoto/OS"))
        self.btn_osname.setText(_translate("os", "Name of the operating system"))
        self.btn_pid.setText(_translate("os", "Current process’s user id."))
        self.label_output.setText(_translate("os", "Output"))
        self.btn_home.setText(_translate("os", "Home directory"))
        self.btn_user.setText(_translate("os", "Current user login"))
        self.output.setHtml(_translate("os", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; -qt-user-state:131073;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    os = QtWidgets.QWidget()
    ui = Ui_os()
    ui.setupUi(os)
    os.show()
    sys.exit(app.exec_())
