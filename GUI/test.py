# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dlg3.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import dlg1, dlg2, dlg3, dlg4, login, mainwindow, topology, signup


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    Dialog1 = QtWidgets.QDialog()
    Dialog2 = QtWidgets.QDialog()
    Dialog3 = QtWidgets.QDialog()
    Dialog4 = QtWidgets.QDialog()

    ui1 = dlg1.Ui_Dialog()
    ui2 = dlg2.Ui_Dialog()
    ui3 = dlg3.Ui_Dialog()
    ui4 = dlg4.Ui_Dialog()

    ui1.setupUi(Dialog1)
    ui2.setupUi(Dialog2)
    ui3.setupUi(Dialog3)
    ui4.setupUi(Dialog4)

    Dialog1.show()
    Dialog2.show()
    Dialog3.show()
    Dialog4.show()

    sys.exit(app.exec_())


