from PyQt5.QtWidgets import QApplication, QTableWidgetItem
from pyqt_checkbox_table_widget.checkBoxTableWidget import CheckBoxTableWidget

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    widget = CheckBoxTableWidget()
    widget.setRowCount(3)
    widget.setItem(0, 1, QTableWidgetItem('abc')) # Remember column argument should be at least 1 (if it is zero, item will cover the checkbox cell)
    widget.show()
    app.exec_()