# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kai/project/hotel-management/src/ui/ui_home_scene.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HomeScene(object):
    def setupUi(self, HomeScene):
        HomeScene.setObjectName("HomeScene")
        HomeScene.resize(800, 600)
        self.label = QtWidgets.QLabel(HomeScene)
        self.label.setGeometry(QtCore.QRect(190, 180, 261, 51))
        self.label.setObjectName("label")

        self.retranslateUi(HomeScene)
        QtCore.QMetaObject.connectSlotsByName(HomeScene)

    def retranslateUi(self, HomeScene):
        _translate = QtCore.QCoreApplication.translate
        HomeScene.setWindowTitle(_translate("HomeScene", "Hotel"))
        self.label.setText(_translate("HomeScene", "This is home scene load from separate file ui"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HomeScene = QtWidgets.QWidget()
    ui = Ui_HomeScene()
    ui.setupUi(HomeScene)
    HomeScene.show()
    sys.exit(app.exec_())
