# pyqt-checkbox-table-widget
PyQt's QTableWidget which has checkbox as first header item

## Requirements
PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-checkbox-table-widget`

## Method Overview
Many methods is changed/overriden because of the fact that check box being used in first column.
* `setHorizontalHeaderLabels(labels: typing.Iterable[str])` - Sets horizontal header label except for first column (for check box), automatically set the count of the columns based on labels
* `clearContents(start_r_idx=0)` - Remove all contents including check box from start_r_idx
* `setDefaultValueOfCheckBox(flag: bool)` - Self-explanatory.
* `stretchEveryColumnExceptForCheckBox()` - Apply self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) except for first column, which is for check box.
* `setRowCount(rows: int)`
* `insertRow(rows: int)`
* `toggleState(state)` - Toggle every single checkbox. State should be Qt.CheckState. You can see how to use this feature in Code Example 2 below.
* `getCheckedRows()` - Return the list of indexes of row which are checked.
* `getUncheckedRows()`
* `setCheckedAt(idx: int, f: bool)` - If f is True, the check box at idx is checked. f is False, the check box at idx is unchecked.
* `removeCheckedRows()`
* `removeUncheckedRows()`

## Example
Code Example 1
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

Code Example 2
```python
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMainWindow, QCheckBox, QVBoxLayout, QWidget
from pyqt_checkbox_table_widget.checkBoxTableWidget import CheckBoxTableWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        allChkBox = QCheckBox('Check all')
        tableWidget = CheckBoxTableWidget()
        tableWidget.setRowCount(10)
        tableWidget.stretchEveryColumnExceptForCheckBox() # stretch every section of tablewidget except for check box section
        for i in range(tableWidget.rowCount()):
            item = QTableWidgetItem()
            item.setTextAlignment(Qt.AlignCenter) # align
            item.setText(str(i)*50) # text sample
            tableWidget.setItem(i, 1, item)
        allChkBox.stateChanged.connect(tableWidget.toggleState) # if allChkBox is checked, tablewidget checkboxes will also be checked 

        lay = QVBoxLayout()
        lay.addWidget(allChkBox)
        lay.addWidget(tableWidget)

        mainWidget = QWidget()
        mainWidget.setLayout(lay)

        self.setCentralWidget(mainWidget)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
```

Result

https://user-images.githubusercontent.com/55078043/144937804-958af370-5069-4fe9-870d-ace9838eb483.mp4

## Similar package
<a href="https://github.com/yjg30737/pyqt-checkbox-list-widget.git">pyqt-checkbox-list-widget</a>

