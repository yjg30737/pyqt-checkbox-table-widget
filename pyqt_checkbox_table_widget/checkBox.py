from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QCheckBox


class CheckBox(QCheckBox):
    checkedSignal = pyqtSignal(int, Qt.CheckState)

    def __init__(self, r_idx, flag):
        super().__init__()
        self.__r_idx = r_idx
        self.setChecked(flag)
        self.stateChanged.connect(self.__sendCheckedSignal)

    def __sendCheckedSignal(self, flag):
        self.checkedSignal.emit(self.__r_idx, flag)
