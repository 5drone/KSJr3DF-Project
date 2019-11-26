# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\sec\PycharmProjects\KSJr3DF-Project\GUI\ui_dir\Topology.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(950, 750)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\sec\\PycharmProjects\\KSJr3DF-Project\\GUI\\ui_dir\\../icon/dron.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.Right_frame = QtWidgets.QFrame(Dialog)
        self.Right_frame.setGeometry(QtCore.QRect(730, 20, 210, 710))
        self.Right_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Right_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Right_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Right_frame.setObjectName("Right_frame")
        self.Finish_pushButton = QtWidgets.QPushButton(self.Right_frame)
        self.Finish_pushButton.setGeometry(QtCore.QRect(10, 670, 190, 30))
        self.Finish_pushButton.setStyleSheet("background-color: rgb(51, 160, 255);\n"
"color: rgb(255, 255, 255);")
        self.Finish_pushButton.setObjectName("Finish_pushButton")
        self.Toolbox_scrollArea = QtWidgets.QScrollArea(self.Right_frame)
        self.Toolbox_scrollArea.setGeometry(QtCore.QRect(10, 465, 190, 150))
        self.Toolbox_scrollArea.setStyleSheet("background-color: rgb(209, 212, 205);")
        self.Toolbox_scrollArea.setWidgetResizable(True)
        self.Toolbox_scrollArea.setObjectName("Toolbox_scrollArea")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 188, 148))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.Toolbox_scrollArea.setWidget(self.scrollAreaWidgetContents_4)
        self.First_scrollArea = QtWidgets.QScrollArea(self.Right_frame)
        self.First_scrollArea.setGeometry(QtCore.QRect(10, 30, 190, 100))
        self.First_scrollArea.setStyleSheet("background-color: rgb(209, 212, 205);")
        self.First_scrollArea.setWidgetResizable(True)
        self.First_scrollArea.setObjectName("First_scrollArea")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 188, 98))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.First_scrollArea.setWidget(self.scrollAreaWidgetContents_6)
        self.line_4 = QtWidgets.QFrame(self.Right_frame)
        self.line_4.setGeometry(QtCore.QRect(10, 140, 190, 3))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.First_Label = QtWidgets.QLabel(self.Right_frame)
        self.First_Label.setGeometry(QtCore.QRect(10, 10, 190, 25))
        self.First_Label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.First_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.First_Label.setObjectName("First_Label")
        self.Second_Label = QtWidgets.QLabel(self.Right_frame)
        self.Second_Label.setGeometry(QtCore.QRect(10, 150, 190, 25))
        self.Second_Label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Second_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Second_Label.setObjectName("Second_Label")
        self.Third_Label = QtWidgets.QLabel(self.Right_frame)
        self.Third_Label.setGeometry(QtCore.QRect(10, 295, 190, 25))
        self.Third_Label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Third_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Third_Label.setObjectName("Third_Label")
        self.Second_scrollArea = QtWidgets.QScrollArea(self.Right_frame)
        self.Second_scrollArea.setGeometry(QtCore.QRect(10, 175, 190, 100))
        self.Second_scrollArea.setStyleSheet("background-color: rgb(209, 212, 205);")
        self.Second_scrollArea.setWidgetResizable(True)
        self.Second_scrollArea.setObjectName("Second_scrollArea")
        self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 188, 98))
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        self.Second_scrollArea.setWidget(self.scrollAreaWidgetContents_7)
        self.Third_scrollArea = QtWidgets.QScrollArea(self.Right_frame)
        self.Third_scrollArea.setGeometry(QtCore.QRect(10, 320, 190, 100))
        self.Third_scrollArea.setStyleSheet("background-color: rgb(209, 212, 205);")
        self.Third_scrollArea.setWidgetResizable(True)
        self.Third_scrollArea.setObjectName("Third_scrollArea")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 188, 98))
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.Third_scrollArea.setWidget(self.scrollAreaWidgetContents_8)
        self.line_5 = QtWidgets.QFrame(self.Right_frame)
        self.line_5.setGeometry(QtCore.QRect(10, 285, 190, 3))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.Toolbox_Label = QtWidgets.QLabel(self.Right_frame)
        self.Toolbox_Label.setGeometry(QtCore.QRect(10, 440, 190, 25))
        self.Toolbox_Label.setStyleSheet("background-color: rgb(51, 160, 255);\n"
"color: rgb(255, 255, 255);")
        self.Toolbox_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Toolbox_Label.setObjectName("Toolbox_Label")
        self.line_6 = QtWidgets.QFrame(self.Right_frame)
        self.line_6.setGeometry(QtCore.QRect(10, 430, 190, 3))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(10, 20, 710, 710))
        self.graphicsView.setObjectName("graphicsView")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "General 5ho"))
        self.Finish_pushButton.setText(_translate("Dialog", "완료"))
        self.First_Label.setToolTip(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.First_Label.setWhatsThis(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.First_Label.setText(_translate("Dialog", "1"))
        self.Second_Label.setToolTip(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.Second_Label.setWhatsThis(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.Second_Label.setText(_translate("Dialog", "2"))
        self.Third_Label.setToolTip(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.Third_Label.setWhatsThis(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.Third_Label.setText(_translate("Dialog", "3"))
        self.Toolbox_Label.setText(_translate("Dialog", "도구상자"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
