# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kai/project/hotel-management/src/ui/ui_customers_scene.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.container = QtWidgets.QWidget(self.centralwidget)
        self.container.setGeometry(QtCore.QRect(0, 0, 791, 551))
        self.container.setObjectName("container")
        self.containerQwidget = QtWidgets.QHBoxLayout(self.container)
        self.containerQwidget.setContentsMargins(0, 0, 0, 0)
        self.containerQwidget.setObjectName("containerQwidget")
        self.list_customers = QtWidgets.QTableWidget(self.container)
        self.list_customers.setObjectName("list_customers")
        self.list_customers.setColumnCount(0)
        self.list_customers.setRowCount(0)
        self.containerQwidget.addWidget(self.list_customers)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.add_customer_btn = QtWidgets.QPushButton(self.container)
        self.add_customer_btn.setObjectName("add_customer_btn")
        self.verticalLayout.addWidget(self.add_customer_btn)
        self.edit_customer_btn = QtWidgets.QPushButton(self.container)
        self.edit_customer_btn.setObjectName("edit_customer_btn")
        self.verticalLayout.addWidget(self.edit_customer_btn)
        self.remove_customer_btn = QtWidgets.QPushButton(self.container)
        self.remove_customer_btn.setObjectName("remove_customer_btn")
        self.verticalLayout.addWidget(self.remove_customer_btn)
        self.exit_btn = QtWidgets.QPushButton(self.container)
        self.exit_btn.setObjectName("exit_btn")
        self.verticalLayout.addWidget(self.exit_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.containerQwidget.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_customer_btn.setText(_translate("MainWindow", "ADD"))
        self.edit_customer_btn.setText(_translate("MainWindow", "EDIT"))
        self.remove_customer_btn.setText(_translate("MainWindow", "REMOVE"))
        self.exit_btn.setText(_translate("MainWindow", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())