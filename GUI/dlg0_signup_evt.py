# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\sec\PycharmProjects\KSJr3DF-Project\GUI\ui_dir\Dlg0_Signup_Evt.ui'
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
        Dialog.resize(300, 110)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\sec\\PycharmProjects\\KSJr3DF-Project\\GUI\\ui_dir\\../icon/dron.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setStyleSheet("background-color: rgb(51, 160, 255);")
        self.pushButton.setAutoDefault(True)
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)

        self.pushButton.clicked.connect(self.pushOnClicked)  # pushButton과 pushOnClicked함수 연결
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "General 5ho"))
        self.label.setText(_translate("Dialog", "인증완료!"))
        self.pushButton.setText(_translate("Dialog", "OK"))

    # pushButton Event처리
    def pushOnClicked(self):
        QtWidgets.QMessageBox.about(None, "하위", "ㅇㄹ어ㅏㄹ머ㅣ")
        Dialog.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    Dialog.show()
    sys.exit(app.exec_())
