# pyqt-checkbox-table-widget
PyQt's QTableWidget which has checkbox as first header item\

## Requirements
PyQt5 >= 5.8

## Setup
``` pip3 install git+https://github.com/yjg30737/pyqt-checkbox-table-widget.git --upgrade```

## Example
Code Example
```python
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
```

Result

![image](https://user-images.githubusercontent.com/55078043/144935820-2acc561c-1c8d-4e39-9d22-5a3da32a47f0.png)

