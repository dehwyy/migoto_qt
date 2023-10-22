# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/ui/textops.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Translation(object):
    def setupUi(self, Translation):
        Translation.setObjectName("Translation")
        Translation.resize(800, 500)
        Translation.setStyleSheet("background-color: #333333;\n"
"color: white;\n"
"")
        self.header = QtWidgets.QLabel(Translation)
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
        self.btn_compile = QtWidgets.QPushButton(Translation)
        self.btn_compile.setGeometry(QtCore.QRect(420, 230, 341, 41))
        font = QtGui.QFont()
        font.setFamily("UD Digi Kyokasho NK-B")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btn_compile.setFont(font)
        self.btn_compile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_compile.setStyleSheet("font-size: 18px;\n"
"background-color: #4629f2;\n"
"color: white;\n"
"border: 3px solid #555555;\n"
"border-radius: 10px")
        self.btn_compile.setObjectName("btn_compile")
        self.output = QtWidgets.QTextEdit(Translation)
        self.output.setEnabled(False)
        self.output.setGeometry(QtCore.QRect(420, 330, 341, 101))
        font = QtGui.QFont()
        font.setFamily("UD Digi Kyokasho NK-B")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.output.setFont(font)
        self.output.setAutoFillBackground(False)
        self.output.setStyleSheet("font-size: 17px;\n"
"outline: none;\n"
"border-radius: 10px;\n"
"background-color: #fff;\n"
"color: black;\n"
"padding: 5px 9px;s")
        self.output.setObjectName("output")
        self.label_input = QtWidgets.QLabel(Translation)
        self.label_input.setGeometry(QtCore.QRect(420, 130, 341, 21))
        font = QtGui.QFont()
        font.setFamily("UD Digi Kyokasho NK-B")
        font.setPointSize(-1)
        self.label_input.setFont(font)
        self.label_input.setStyleSheet("font-size: 22px;\n"
"")
        self.label_input.setAlignment(QtCore.Qt.AlignCenter)
        self.label_input.setObjectName("label_input")
        self.label_output = QtWidgets.QLabel(Translation)
        self.label_output.setGeometry(QtCore.QRect(420, 300, 341, 21))
        font = QtGui.QFont()
        font.setFamily("UD Digi Kyokasho NK-B")
        font.setPointSize(-1)
        self.label_output.setFont(font)
        self.label_output.setStyleSheet("font-size: 22px;\n"
"")
        self.label_output.setAlignment(QtCore.Qt.AlignCenter)
        self.label_output.setObjectName("label_output")
        self.input = QtWidgets.QLineEdit(Translation)
        self.input.setEnabled(True)
        self.input.setGeometry(QtCore.QRect(420, 170, 341, 41))
        font = QtGui.QFont()
        font.setFamily("UD Digi Kyokasho NK-B")
        font.setPointSize(10)
        self.input.setFont(font)
        self.input.setStyleSheet("background: white;\n"
"color: black;\n"
"outline: none;\n"
"border-radius: 10px;\n"
"padding: 5px 9px;")
        self.input.setObjectName("input")
        self.btn_random_str = QtWidgets.QPushButton(Translation)
        self.btn_random_str.setGeometry(QtCore.QRect(50, 210, 341, 51))
        font = QtGui.QFont()
        font.setFamily("UD Digi Kyokasho NK-B")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btn_random_str.setFont(font)
        self.btn_random_str.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_random_str.setStyleSheet("font-size: 18px;\n"
"background-color: white;\n"
"color: #222222;\n"
"border: 3px solid #555555;\n"
"border-radius: 10px")
        self.btn_random_str.setObjectName("btn_random_str")
        self.btn_length_str = QtWidgets.QPushButton(Translation)
        self.btn_length_str.setGeometry(QtCore.QRect(50, 270, 341, 51))
        font = QtGui.QFont()
        font.setFamily("UD Digi Kyokasho NK-B")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btn_length_str.setFont(font)
        self.btn_length_str.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_length_str.setStyleSheet("font-size: 18px;\n"
"background-color: white;\n"
"color: #222222;\n"
"border: 3px solid #555555;\n"
"border-radius: 10px")
        self.btn_length_str.setObjectName("btn_length_str")
        self.btn_reverse_str = QtWidgets.QPushButton(Translation)
        self.btn_reverse_str.setGeometry(QtCore.QRect(50, 330, 341, 51))
        font = QtGui.QFont()
        font.setFamily("UD Digi Kyokasho NK-B")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btn_reverse_str.setFont(font)
        self.btn_reverse_str.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_reverse_str.setStyleSheet("font-size: 18px;\n"
"background-color: white;\n"
"color: #222222;\n"
"border: 3px solid #555555;\n"
"border-radius: 10px")
        self.btn_reverse_str.setObjectName("btn_reverse_str")
        self.btn_remove_symbol = QtWidgets.QPushButton(Translation)
        self.btn_remove_symbol.setGeometry(QtCore.QRect(50, 150, 341, 51))
        font = QtGui.QFont()
        font.setFamily("UD Digi Kyokasho NK-B")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btn_remove_symbol.setFont(font)
        self.btn_remove_symbol.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_remove_symbol.setStyleSheet("font-size: 18px;\n"
"background-color: white;\n"
"color: #222222;\n"
"border: 3px solid #555555;\n"
"border-radius: 10px")
        self.btn_remove_symbol.setObjectName("btn_remove_symbol")
        self.btn_makoto_camel = QtWidgets.QPushButton(Translation)
        self.btn_makoto_camel.setGeometry(QtCore.QRect(50, 390, 341, 51))
        font = QtGui.QFont()
        font.setFamily("UD Digi Kyokasho NK-B")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btn_makoto_camel.setFont(font)
        self.btn_makoto_camel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_makoto_camel.setStyleSheet("font-size: 18px;\n"
"background-color: white;\n"
"color: #222222;\n"
"border: 3px solid #555555;\n"
"border-radius: 10px")
        self.btn_makoto_camel.setObjectName("btn_makoto_camel")
        self.btn_back = QtWidgets.QPushButton(Translation)
        self.btn_back.setGeometry(QtCore.QRect(590, 450, 191, 41))
        font = QtGui.QFont()
        font.setFamily("UD Digi Kyokasho NK-B")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btn_back.setFont(font)
        self.btn_back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_back.setStyleSheet("font-size: 18px;\n"
"background-color: #ff00d2;\n"
"color: white;\n"
"border: 3px solid #555555;\n"
"border-radius: 10px")
        self.btn_back.setObjectName("btn_back")

        self.retranslateUi(Translation)
        QtCore.QMetaObject.connectSlotsByName(Translation)

    def retranslateUi(self, Translation):
        _translate = QtCore.QCoreApplication.translate
        Translation.setWindowTitle(_translate("Translation", "Makoto/Translation"))
        self.header.setText(_translate("Translation", "Migoto/TextOperations"))
        self.btn_compile.setText(_translate("Translation", "Compile"))
        self.output.setHtml(_translate("Translation", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'UD Digi Kyokasho NK-B\'; font-size:17px; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_input.setText(_translate("Translation", "Input"))
        self.label_output.setText(_translate("Translation", "Output"))
        self.btn_random_str.setText(_translate("Translation", "Generate random string"))
        self.btn_length_str.setText(_translate("Translation", "Calculate length of the string"))
        self.btn_reverse_str.setText(_translate("Translation", "Reverse string"))
        self.btn_remove_symbol.setText(_translate("Translation", "Remove Symbol from string"))
        self.btn_makoto_camel.setText(_translate("Translation", "True CamelCase"))
        self.btn_back.setText(_translate("Translation", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Translation = QtWidgets.QWidget()
    ui = Ui_Translation()
    ui.setupUi(Translation)
    Translation.show()
    sys.exit(app.exec_())
