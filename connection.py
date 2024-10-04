import sys
from PyQt5 import QtWidgets, uic, QtGui
from Class import *  # Ensure that Class.py file exists in the same directory
ui_file = "binary_tree.ui"

# No need for duplicate import of uic
# No need for duplicate import of QDialog from QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi(ui_file, self)
        self.pushButton.clicked.connect(self.get_numbers)

    def get_numbers(self):
        numbers = self.lineEdit.text().split()
        numbers_m = [int(num) for num in numbers if num.strip().isdigit()]  # Using list comprehension to filter and convert to integers
        print(numbers_m)

        if len(numbers_m) == len(numbers):  # Checking if all input elements are valid numbers
            t = Tree()
            for number in numbers_m:
                t.append(Node(number))
            result = t.show_wide_tree(t.root)
            self.label_8.setText(result)
        else:
            error_message = "В вашей записи обнаружены символы вместо чисел. Пожалуйста, исправьте!"
            self.error_dialog = ErrorDialog(error_message)
            self.error_dialog.exec_()

class ErrorDialog(QtWidgets.QDialog):  # Using QtWidgets.QDialog here
    def __init__(self, message, parent=None):
        super(ErrorDialog, self).__init__(parent)
        uic.loadUi("error_mes_tree.ui", self)
        self.show()
        self.label_2.setText(message)
        self.pushButton.setText('Ок')
        self.pushButton.clicked.connect(self.close_app)

    def close_app(self):
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
