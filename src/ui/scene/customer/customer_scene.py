from PyQt5 import QtWidgets, QtCore

from ui.ui_customer_scene import Ui_CustomerScene


class CustomerScene(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CustomerScene()
        self.ui.setupUi(self)
        # layout = QtWidgets.QVBoxLayout(self)
        # label = QtWidgets.QLabel("Guest Scene")
        # label.setAlignment(QtCore.Qt.AlignCenter)
        # layout.addWidget(label)
