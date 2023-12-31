# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/ui/calendar.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calendar(object):
    def setupUi(self, Calendar):
        Calendar.setObjectName("Calendar")
        Calendar.resize(800, 500)
        Calendar.setStyleSheet("background-color: #333333;\n"
"color: white;\n"
"")
        self.header = QtWidgets.QLabel(Calendar)
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
        self.label_oncopy = QtWidgets.QLabel(Calendar)
        self.label_oncopy.setEnabled(True)
        self.label_oncopy.setGeometry(QtCore.QRect(650, 400, 111, 20))
        font = QtGui.QFont()
        font.setFamily("UD Digi Kyokasho NK-B")
        font.setPointSize(-1)
        self.label_oncopy.setFont(font)
        self.label_oncopy.setStyleSheet("font-size: 18px;\n"
"")
        self.label_oncopy.setText("")
        self.label_oncopy.setAlignment(QtCore.Qt.AlignCenter)
        self.label_oncopy.setObjectName("label_oncopy")
        self.calendarWidget = QtWidgets.QCalendarWidget(Calendar)
        self.calendarWidget.setGeometry(QtCore.QRect(70, 120, 661, 301))
        self.calendarWidget.setStyleSheet("color: black;\n"
"background-color: white;")
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.btn_save_data = QtWidgets.QPushButton(Calendar)
        self.btn_save_data.setGeometry(QtCore.QRect(70, 450, 661, 41))
        font = QtGui.QFont()
        font.setFamily("UD Digi Kyokasho NK-B")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btn_save_data.setFont(font)
        self.btn_save_data.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_save_data.setStyleSheet("font-size: 18px;\n"
"background-color: #4629f2;\n"
"color: white;\n"
"border: 3px solid #555555;\n"
"border-radius: 10px")
        self.btn_save_data.setObjectName("btn_save_data")

        self.retranslateUi(Calendar)
        QtCore.QMetaObject.connectSlotsByName(Calendar)

    def retranslateUi(self, Calendar):
        _translate = QtCore.QCoreApplication.translate
        Calendar.setWindowTitle(_translate("Calendar", "Migoto/Calendar"))
        self.header.setText(_translate("Calendar", "Migoto/Calendar"))
        self.btn_save_data.setText(_translate("Calendar", "Save data in .txt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calendar = QtWidgets.QWidget()
    ui = Ui_Calendar()
    ui.setupUi(Calendar)
    Calendar.show()
    sys.exit(app.exec_())
