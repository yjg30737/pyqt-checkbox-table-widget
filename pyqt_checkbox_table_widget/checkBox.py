from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QCheckBox, QWidget, QGridLayout


class CheckBox(QWidget):
    checkedSignal = pyqtSignal(int, Qt.CheckState)

    def __init__(self, r_idx, flag):
        super().__init__()
        self.__r_idx = r_idx
        self.__initUi(flag)

    def __initUi(self, flag):
        chkBox = QCheckBox()
        chkBox.setChecked(flag)
        chkBox.stateChanged.connect(self.__sendCheckedSignal)

        lay = QGridLayout()
        lay.addWidget(chkBox)

        self.setLayout(lay)

    def __sendCheckedSignal(self, flag):
        self.checkedSignal.emit(self.__r_idx, flag)
