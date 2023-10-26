# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/ui/textops.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TextOperations(object):
    def setupUi(self, TextOperations):
        TextOperations.setObjectName("TextOperations")
        TextOperations.resize(800, 500)
        TextOperations.setStyleSheet("background-color: #333333;\n"
"color: white;\n"
"")
        self.header = QtWidgets.QLabel(TextOperations)
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
        self.btn_compile = QtWidgets.QPushButton(TextOperations)
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
        self.label_input = QtWidgets.QLabel(TextOperations)
        self.label_input.setGeometry(QtCore.QRect(420, 130, 341, 21))
        font = QtGui.QFont()
        font.setFamily("UD Digi Kyokasho NK-B")
        font.setPointSize(-1)
        self.label_input.setFont(font)
        self.label_input.setStyleSheet("font-size: 22px;\n"
"")
        self.label_input.setAlignment(QtCore.Qt.AlignCenter)
        self.label_input.setObjectName("label_input")
        self.label_output = QtWidgets.QLabel(TextOperations)
        self.label_output.setGeometry(QtCore.QRect(420, 300, 341, 21))
        font = QtGui.QFont()
        font.setFamily("UD Digi Kyokasho NK-B")
        font.setPointSize(-1)
        self.label_output.setFont(font)
        self.label_output.setStyleSheet("font-size: 22px;\n"
"")
        self.label_output.setAlignment(QtCore.Qt.AlignCenter)
        self.label_output.setObjectName("label_output")
        self.btn_change_order = QtWidgets.QPushButton(TextOperations)
        self.btn_change_order.setGeometry(QtCore.QRect(50, 210, 341, 51))
        font = QtGui.QFont()
        font.setFamily("UD Digi Kyokasho NK-B")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btn_change_order.setFont(font)
        self.btn_change_order.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_change_order.setStyleSheet("font-size: 18px;\n"
"background-color: white;\n"
"color: #222222;\n"
"border: 3px solid #555555;\n"
"border-radius: 10px")
        self.btn_change_order.setObjectName("btn_change_order")
        self.btn_length_str = QtWidgets.QPushButton(TextOperations)
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
        self.btn_reverse_str = QtWidgets.QPushButton(TextOperations)
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
        self.btn_remove_symbol = QtWidgets.QPushButton(TextOperations)
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
        self.btn_makoto_camel = QtWidgets.QPushButton(TextOperations)
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
        self.output = QtWidgets.QTextBrowser(TextOperations)
        self.output.setGeometry(QtCore.QRect(420, 330, 341, 101))
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
        self.input = QtWidgets.QLineEdit(TextOperations)
        self.input.setGeometry(QtCore.QRect(420, 170, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.input.setFont(font)
        self.input.setStyleSheet("background: white;\n"
"color: black;\n"
"outline: none;\n"
"border-radius: 10px;\n"
"padding: 5px 9px;")
        self.input.setText("")
        self.input.setObjectName("input")

        self.retranslateUi(TextOperations)
        QtCore.QMetaObject.connectSlotsByName(TextOperations)

    def retranslateUi(self, TextOperations):
        _translate = QtCore.QCoreApplication.translate
        TextOperations.setWindowTitle(_translate("TextOperations", "Makoto/TextOperations"))
        self.header.setText(_translate("TextOperations", "Migoto/TextOperations"))
        self.btn_compile.setText(_translate("TextOperations", "Compile"))
        self.label_input.setText(_translate("TextOperations", "Input"))
        self.label_output.setText(_translate("TextOperations", "Output"))
        self.btn_change_order.setText(_translate("TextOperations", "Change symbol order"))
        self.btn_length_str.setText(_translate("TextOperations", "Calculate length of the string"))
        self.btn_reverse_str.setText(_translate("TextOperations", "Reverse string"))
        self.btn_remove_symbol.setText(_translate("TextOperations", "Remove random Symbol"))
        self.btn_makoto_camel.setText(_translate("TextOperations", "True CamelCase"))
        self.output.setHtml(_translate("TextOperations", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; -qt-user-state:131073;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TextOperations = QtWidgets.QWidget()
    ui = Ui_TextOperations()
    ui.setupUi(TextOperations)
    TextOperations.show()
    sys.exit(app.exec_())
