# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\sec\PycharmProjects\KSJr3DF-Project\GUI\ui_dir\Dlg1_Menu1_Evt.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 350)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\sec\\PycharmProjects\\KSJr3DF-Project\\GUI\\ui_dir\\../icon/dron.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.Sub_pusthButton = QtWidgets.QPushButton(Dialog)
        self.Sub_pusthButton.setGeometry(QtCore.QRect(540, 130, 20, 20))
        self.Sub_pusthButton.setObjectName("Sub_pusthButton")
        self.List_scrollArea3 = QtWidgets.QScrollArea(Dialog)
        self.List_scrollArea3.setGeometry(QtCore.QRect(370, 120, 150, 150))
        self.List_scrollArea3.setWidgetResizable(True)
        self.List_scrollArea3.setObjectName("List_scrollArea3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 148, 148))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.List_scrollArea3.setWidget(self.scrollAreaWidgetContents_3)
        self.List_scrollArea1 = QtWidgets.QScrollArea(Dialog)
        self.List_scrollArea1.setGeometry(QtCore.QRect(10, 120, 150, 150))
        self.List_scrollArea1.setWidgetResizable(True)
        self.List_scrollArea1.setObjectName("List_scrollArea1")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 148, 148))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.List_scrollArea1.setWidget(self.scrollAreaWidgetContents)
        self.Next_pushButton = QtWidgets.QPushButton(Dialog)
        self.Next_pushButton.setGeometry(QtCore.QRect(360, 290, 100, 40))
        self.Next_pushButton.setStyleSheet("background-color: rgb(51, 160, 255);")
        self.Next_pushButton.setObjectName("Next_pushButton")
        self.two_to_three_pushButton = QtWidgets.QPushButton(Dialog)
        self.two_to_three_pushButton.setGeometry(QtCore.QRect(340, 120, 31, 151))
        self.two_to_three_pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\sec\\PycharmProjects\\KSJr3DF-Project\\GUI\\ui_dir\\../icon/arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.two_to_three_pushButton.setIcon(icon1)
        self.two_to_three_pushButton.setObjectName("two_to_three_pushButton")
        self.WS_Name_editText = QtWidgets.QTextEdit(Dialog)
        self.WS_Name_editText.setGeometry(QtCore.QRect(60, 30, 150, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WS_Name_editText.sizePolicy().hasHeightForWidth())
        self.WS_Name_editText.setSizePolicy(sizePolicy)
        self.WS_Name_editText.setObjectName("WS_Name_editText")
        self.Group_List_spinBox1 = QtWidgets.QSpinBox(Dialog)
        self.Group_List_spinBox1.setGeometry(QtCore.QRect(190, 80, 150, 30))
        self.Group_List_spinBox1.setObjectName("Group_List_spinBox1")
        self.Group_List_editText = QtWidgets.QTextEdit(Dialog)
        self.Group_List_editText.setGeometry(QtCore.QRect(10, 80, 150, 30))
        self.Group_List_editText.setObjectName("Group_List_editText")
        self.one_to_two_pushButton = QtWidgets.QPushButton(Dialog)
        self.one_to_two_pushButton.setGeometry(QtCore.QRect(160, 120, 31, 151))
        self.one_to_two_pushButton.setText("")
        self.one_to_two_pushButton.setIcon(icon1)
        self.one_to_two_pushButton.setObjectName("one_to_two_pushButton")
        self.List_scrollArea2 = QtWidgets.QScrollArea(Dialog)
        self.List_scrollArea2.setGeometry(QtCore.QRect(190, 120, 150, 150))
        self.List_scrollArea2.setWidgetResizable(True)
        self.List_scrollArea2.setObjectName("List_scrollArea2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 148, 148))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.List_scrollArea2.setWidget(self.scrollAreaWidgetContents_2)
        self.WS_Name_Label = QtWidgets.QLabel(Dialog)
        self.WS_Name_Label.setGeometry(QtCore.QRect(20, 35, 41, 16))
        self.WS_Name_Label.setObjectName("WS_Name_Label")
        self.Group_List_spinBox2 = QtWidgets.QSpinBox(Dialog)
        self.Group_List_spinBox2.setGeometry(QtCore.QRect(370, 80, 150, 30))
        self.Group_List_spinBox2.setObjectName("Group_List_spinBox2")
        self.Add_pushButton = QtWidgets.QPushButton(Dialog)
        self.Add_pushButton.setGeometry(QtCore.QRect(520, 130, 20, 20))
        self.Add_pushButton.setObjectName("Add_pushButton")
        self.Cancel_pushButton = QtWidgets.QPushButton(Dialog)
        self.Cancel_pushButton.setGeometry(QtCore.QRect(470, 290, 100, 40))
        self.Cancel_pushButton.setStyleSheet("background-color: rgb(51, 160, 255);")
        self.Cancel_pushButton.setObjectName("Cancel_pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "General 5ho"))
        self.Sub_pusthButton.setText(_translate("Dialog", "-"))
        self.Next_pushButton.setText(_translate("Dialog", "다음"))
        self.WS_Name_Label.setText(_translate("Dialog", "이름"))
        self.Add_pushButton.setText(_translate("Dialog", "+"))
        self.Cancel_pushButton.setText(_translate("Dialog", "취소"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
