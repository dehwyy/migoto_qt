import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from internal.widgets.generated.calendarUI import Ui_Calendar
from config import DEFAULT_QMESSAGE_SIZE
from config import DEFAULT_WINDOW_SIZE


class Calendar(QWidget,  Ui_Calendar):
    def __init__(self):
        super().__init__()
        # App initt
        self.init_ui()

        self.setupUi(self)

        self.btn_save_data.clicked.connect(self.save)

    def init_ui(self):
        self.setWindowIcon(QIcon('assets/icon.png'))
        self.setFixedSize(*DEFAULT_WINDOW_SIZE)

    def save(self):
        filePath, ok_pressed = QFileDialog.getSaveFileName(
            self, "Сохранить картинку", "", "Текст (*.txt);")

        if ok_pressed:
            with open(filePath, "w") as f:
                date_to_write_v1 = \
                    self.calendarWidget.selectedDate().toString('dd.MM.yyyy')
                date_to_write_v2 = \
                    self.calendarWidget.selectedDate().toString('yyyy-MM-dd')
                f.write(str(date_to_write_v1))
                f.write("\t" + str(date_to_write_v2))

                success_box = QMessageBox(self)
                success_box.setFixedSize(*DEFAULT_QMESSAGE_SIZE)
                success_box.show()
                success_box.setIcon(QMessageBox.Information)
                success_box.setText("Success!")
                success_box.setInformativeText(f"Date was saved!")
                success_box.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    t = Calendar()
    t.show()

    sys.exit(app.exec())
