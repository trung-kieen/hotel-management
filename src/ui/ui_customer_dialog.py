# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kai/project/hotel-management/src/ui/ui_customer_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 250, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 361, 221))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.firstNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.firstNameLabel)
        self.firstname = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.firstname.setObjectName("firstname")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.firstname)
        self.lastNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.lastNameLabel.setObjectName("lastNameLabel")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lastNameLabel)
        self.lastname = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lastname.setObjectName("lastname")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lastname)
        self.addressLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.addressLabel.setObjectName("addressLabel")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.addressLabel)
        self.address = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.address.setObjectName("address")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.address)
        self.birthLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.birthLabel.setObjectName("birthLabel")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.birthLabel)
        self.birth = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.birth.setObjectName("birth")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.birth)
        self.genderLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.genderLabel.setObjectName("genderLabel")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.genderLabel)
        self.gender = QtWidgets.QComboBox(self.formLayoutWidget)
        self.gender.setObjectName("gender")
        self.gender.addItem("")
        self.gender.addItem("")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.gender)
        self.phoneLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.phoneLabel.setObjectName("phoneLabel")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.phoneLabel)
        self.phone = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.phone.setObjectName("phone")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.phone)
        self.emailLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.emailLabel.setObjectName("emailLabel")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.emailLabel)
        self.email = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.email.setObjectName("email")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.email)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.firstNameLabel.setText(_translate("Dialog", "First Name"))
        self.lastNameLabel.setText(_translate("Dialog", "Last Name"))
        self.addressLabel.setText(_translate("Dialog", "Address"))
        self.birthLabel.setText(_translate("Dialog", "Birth"))
        self.genderLabel.setText(_translate("Dialog", "Gender"))
        self.gender.setItemText(0, _translate("Dialog", "Male"))
        self.gender.setItemText(1, _translate("Dialog", "Female"))
        self.phoneLabel.setText(_translate("Dialog", "Phone"))
        self.emailLabel.setText(_translate("Dialog", "Email"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
