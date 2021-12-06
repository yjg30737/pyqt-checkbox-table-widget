import typing

from PyQt5.QtWidgets import QHeaderView, QTableWidget, QWidget, QGridLayout
from PyQt5.QtCore import Qt, pyqtSignal

from pyqt_checkbox_table_widget.checkBox import CheckBox


class CheckBoxTableWidget(QTableWidget):
    checkedSignal = pyqtSignal(int, Qt.CheckState)

    def __init__(self, parent=None):
        self._default_check_flag = False
        super().__init__()
        self.__initUi()

    def __initUi(self):
        # Least column count (one for checkbox, one for another)
        self.setColumnCount(2)

    def setHorizontalHeaderLabels(self, labels: typing.Iterable[str]) -> None:
        lst = [_ for _ in labels if _]
        lst.insert(0, '') # 0 index vacant for checkbox
        super().set_horizontal_header(lst)
        self.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)

    def clearContents(self, start_r_idx=0):
        for i in range(start_r_idx, self.rowCount()):
            for j in range(1, self.columnCount()):
                self.takeItem(i, j)

    def setDefaultValueOfCheckBox(self, flag: bool):
        self._default_check_flag = flag

    def stretchEveryColumnExceptForCheckBox(self):
        if self.horizontalHeader():
            self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
            self.setColumnWidth(0, 10)

    def setRowCount(self, rows: int) -> None:
        super().setRowCount(rows)
        for row in range(0, rows):
            self.__setCheckBox(row)

    def __setCheckBox(self, r_idx):
        chkBox = CheckBox(r_idx, self._default_check_flag)
        chkBox.checkedSignal.connect(self.__sendCheckedSignal)

        lay = QGridLayout()
        lay.addWidget(chkBox)

        widget = QWidget()
        widget.setLayout(lay)

        self.setCellWidget(r_idx, 0, widget)

        if self._default_check_flag:
            self.checkedSignal.emit(r_idx, Qt.Checked)
        self.resizeColumnToContents(0)

    def __sendCheckedSignal(self, r_idx, flag: Qt.CheckState):
        self.checkedSignal.emit(r_idx, flag)

    def toggleState(self, state):
        for i in range(self.rowCount()):
            item = super().cellWidget(i, 0)
            if item.checkState() != state:
                item.setCheckState(state)

    def getCheckedRows(self):
        return self.__getCheckedStateOfRows(Qt.Checked)

    def getUncheckedRows(self):
        return self.__getCheckedStateOfRows(Qt.Unchecked)

    def __getCheckedStateOfRows(self, flag: Qt.CheckState):
        flag_lst = []
        for i in range(self.rowCount()):
            item = super().cellWidget(i, 0)
            if item.checkState() == flag:
                flag_lst.append(i)

        return flag_lst

    def removeCheckedRows(self):
        self.__removeCertainCheckedStateRows(Qt.Checked)

    def removeUncheckedRows(self):
        self.__removeCertainCheckedStateRows(Qt.Unchecked)

    def __removeCertainCheckedStateRows(self, flag):
        flag_lst = self.__getCheckedStateOfRows(flag)
        flag_lst = reversed(flag_lst)
        for i in flag_lst:
            self.removeRow(i)
