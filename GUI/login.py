# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\sec\PycharmProjects\KSJr3DF-Project\GUI\ui_dir\Login1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        self.setupUi(Dialog)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 280)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\sec\\PycharmProjects\\KSJr3DF-Project\\GUI\\ui_dir\\../icon/dron.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.Image2_Label = QtWidgets.QLabel(Dialog)
        self.Image2_Label.setGeometry(QtCore.QRect(20, 110, 38, 38))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Image2_Label.sizePolicy().hasHeightForWidth())
        self.Image2_Label.setSizePolicy(sizePolicy)
        self.Image2_Label.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.Image2_Label.setText("")
        self.Image2_Label.setPixmap(QtGui.QPixmap("C:\\Users\\sec\\PycharmProjects\\KSJr3DF-Project\\GUI\\ui_dir\\../icon/user2.png"))
        self.Image2_Label.setScaledContents(True)
        self.Image2_Label.setObjectName("Image2_Label")
        self.PW_editText = QtWidgets.QTextEdit(Dialog)
        self.PW_editText.setGeometry(QtCore.QRect(58, 160, 210, 38))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PW_editText.sizePolicy().hasHeightForWidth())
        self.PW_editText.setSizePolicy(sizePolicy)
        self.PW_editText.setObjectName("PW_editText")
        self.Signup_Label = QtWidgets.QLabel(Dialog)
        self.Signup_Label.setGeometry(QtCore.QRect(118, 240, 64, 15))
        self.Signup_Label.setObjectName("Signup_Label")
        self.Auto_login_checkBox = QtWidgets.QCheckBox(Dialog)
        self.Auto_login_checkBox.setGeometry(QtCore.QRect(58, 210, 111, 19))
        self.Auto_login_checkBox.setObjectName("Auto_login_checkBox")
        self.ID_editText = QtWidgets.QTextEdit(Dialog)
        self.ID_editText.setGeometry(QtCore.QRect(58, 110, 210, 38))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ID_editText.sizePolicy().hasHeightForWidth())
        self.ID_editText.setSizePolicy(sizePolicy)
        self.ID_editText.setObjectName("ID_editText")
        self.Login_pushButton = QtWidgets.QPushButton(Dialog)
        self.Login_pushButton.setGeometry(QtCore.QRect(278, 110, 105, 90))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Login_pushButton.sizePolicy().hasHeightForWidth())
        self.Login_pushButton.setSizePolicy(sizePolicy)
        self.Login_pushButton.setIconSize(QtCore.QSize(20, 20))
        self.Login_pushButton.setObjectName("Login_pushButton")
        self.Image3_Label = QtWidgets.QLabel(Dialog)
        self.Image3_Label.setGeometry(QtCore.QRect(20, 160, 38, 38))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Image3_Label.sizePolicy().hasHeightForWidth())
        self.Image3_Label.setSizePolicy(sizePolicy)
        self.Image3_Label.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.Image3_Label.setText("")
        self.Image3_Label.setPixmap(QtGui.QPixmap("C:\\Users\\sec\\PycharmProjects\\KSJr3DF-Project\\GUI\\ui_dir\\../icon/key3.png"))
        self.Image3_Label.setScaledContents(True)
        self.Image3_Label.setObjectName("Image3_Label")
        self.NonMember_Login_Label = QtWidgets.QLabel(Dialog)
        self.NonMember_Login_Label.setGeometry(QtCore.QRect(208, 240, 101, 16))
        self.NonMember_Login_Label.setObjectName("NonMember_Login_Label")
        self.Image1_Label = QtWidgets.QLabel(Dialog)
        self.Image1_Label.setGeometry(QtCore.QRect(138, 5, 101, 101))
        self.Image1_Label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Image1_Label.setStyleSheet("")
        self.Image1_Label.setText("")
        self.Image1_Label.setPixmap(QtGui.QPixmap("C:\\Users\\sec\\PycharmProjects\\KSJr3DF-Project\\GUI\\ui_dir\\../icon/user1.png"))
        self.Image1_Label.setScaledContents(True)
        self.Image1_Label.setObjectName("Image1_Label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "General 5ho"))
        self.Signup_Label.setText(_translate("Dialog", "회원가입"))
        self.Auto_login_checkBox.setText(_translate("Dialog", "자동 로그인"))
        self.Login_pushButton.setText(_translate("Dialog", "로그인"))
        self.NonMember_Login_Label.setText(_translate("Dialog", "비회원 로그인"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    Dialog.show()
    sys.exit(app.exec_())
