# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\sec\PycharmProjects\KSJr3DF-Project\GUI\ui_dir\SignUp.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 350)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\sec\\PycharmProjects\\KSJr3DF-Project\\GUI\\ui_dir\\../icon/dron.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 85, 251))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ID_Label = QtWidgets.QLabel(self.layoutWidget)
        self.ID_Label.setObjectName("ID_Label")
        self.verticalLayout_2.addWidget(self.ID_Label)
        self.PW_Label = QtWidgets.QLabel(self.layoutWidget)
        self.PW_Label.setObjectName("PW_Label")
        self.verticalLayout_2.addWidget(self.PW_Label)
        self.PW_Check_Label = QtWidgets.QLabel(self.layoutWidget)
        self.PW_Check_Label.setObjectName("PW_Check_Label")
        self.verticalLayout_2.addWidget(self.PW_Check_Label)
        self.Email_Label = QtWidgets.QLabel(self.layoutWidget)
        self.Email_Label.setObjectName("Email_Label")
        self.verticalLayout_2.addWidget(self.Email_Label)
        self.Check_Num_Label = QtWidgets.QLabel(self.layoutWidget)
        self.Check_Num_Label.setObjectName("Check_Num_Label")
        self.verticalLayout_2.addWidget(self.Check_Num_Label)
        self.Signup_pushButton = QtWidgets.QPushButton(Dialog)
        self.Signup_pushButton.setGeometry(QtCore.QRect(130, 280, 120, 40))
        self.Signup_pushButton.setObjectName("Signup_pushButton")
        self.Check_Num_pusthButton = QtWidgets.QPushButton(Dialog)
        self.Check_Num_pusthButton.setGeometry(QtCore.QRect(285, 230, 110, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Check_Num_pusthButton.sizePolicy().hasHeightForWidth())
        self.Check_Num_pusthButton.setSizePolicy(sizePolicy)
        self.Check_Num_pusthButton.setObjectName("Check_Num_pusthButton")
        self.Check_Num_trans_pushButton = QtWidgets.QPushButton(Dialog)
        self.Check_Num_trans_pushButton.setGeometry(QtCore.QRect(285, 180, 110, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Check_Num_trans_pushButton.sizePolicy().hasHeightForWidth())
        self.Check_Num_trans_pushButton.setSizePolicy(sizePolicy)
        self.Check_Num_trans_pushButton.setObjectName("Check_Num_trans_pushButton")
        self.ID_editText = QtWidgets.QLineEdit(Dialog)
        self.ID_editText.setGeometry(QtCore.QRect(100, 30, 180, 40))
        self.ID_editText.setObjectName("ID_editText")
        self.PW_editText = QtWidgets.QLineEdit(Dialog)
        self.PW_editText.setGeometry(QtCore.QRect(100, 80, 180, 40))
        self.PW_editText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PW_editText.setObjectName("PW_editText")
        self.PW_Check_editText = QtWidgets.QLineEdit(Dialog)
        self.PW_Check_editText.setGeometry(QtCore.QRect(100, 130, 180, 40))
        self.PW_Check_editText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PW_Check_editText.setObjectName("PW_Check_editText")
        self.Email_editText = QtWidgets.QLineEdit(Dialog)
        self.Email_editText.setGeometry(QtCore.QRect(100, 180, 180, 40))
        self.Email_editText.setObjectName("Email_editText")
        self.Check_Num_editText = QtWidgets.QLineEdit(Dialog)
        self.Check_Num_editText.setGeometry(QtCore.QRect(100, 230, 180, 40))
        self.Check_Num_editText.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Check_Num_editText.setObjectName("Check_Num_editText")

        self.retranslateUi(Dialog)
        self.Check_Num_pusthButton.clicked.connect(Dialog.open)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "General 5ho"))
        self.ID_Label.setText(_translate("Dialog", "ID           :"))
        self.PW_Label.setText(_translate("Dialog", "P/W        :"))
        self.PW_Check_Label.setText(_translate("Dialog", "P/W 확인 :"))
        self.Email_Label.setText(_translate("Dialog", "이메일     :"))
        self.Check_Num_Label.setText(_translate("Dialog", "인증번호  :"))
        self.Signup_pushButton.setText(_translate("Dialog", "회원가입"))
        self.Check_Num_pusthButton.setText(_translate("Dialog", "인증하기"))
        self.Check_Num_trans_pushButton.setText(_translate("Dialog", "인증번호 전송"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
