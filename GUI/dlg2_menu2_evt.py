# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\sec\PycharmProjects\KSJr3DF-Project\GUI\ui_dir\Dlg2_Menu2_Evt.ui'
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
        Dialog.resize(350, 140)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\sec\\PycharmProjects\\KSJr3DF-Project\\GUI\\ui_dir\\../icon/dron.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.buttonBox.accepted.connect(self.removeOnCliecked)                  # buttonBox.accepted버튼과 removeOnCliecked함수 연결
        self.buttonBox.rejected.connect(Dialog.reject)                          # buttonBox.rejected버튼과 Dialog.accept 연결(바로 창 꺼짐)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "General 5ho"))
        self.label.setText(_translate("Dialog", "정말 선택한 워크스페이스를 삭제하시겠습니까?"))

    # 삭제 버튼 이벤트
    def removeOnCliecked(self):
        QtWidgets.QMessageBox.about(None, "워크스페이스삭제", "워크스페이스 삭제 가즈아~~")
        Dialog.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    Dialog.show()
    sys.exit(app.exec_())
