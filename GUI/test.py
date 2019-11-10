# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dlg3.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import GUI.dlg0_signup_evt, GUI.dlg1_menu1_evt, GUI.dlg2_menu2_evt, GUI.dlg3_menu3_evt, GUI.dlg4_menu4_evt
import GUI.login, GUI.signup, GUI.mainwindow, GUI.topology

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    Dialog0 = QtWidgets.QDialog()
    Dialog1 = QtWidgets.QDialog()
    Dialog2 = QtWidgets.QDialog()
    Dialog3 = QtWidgets.QDialog()
    Dialog4 = QtWidgets.QDialog()
    Login = QtWidgets.QDialog()
    SignUp = QtWidgets.QDialog()
    MainWindow = QtWidgets.QMainWindow()
    Topology = QtWidgets.QDialog()

    ui0 = GUI.dlg0_signup_evt.Ui_Dialog()
    ui1 = GUI.dlg1_menu1_evt.Ui_Dialog()
    ui2 = GUI.dlg2_menu2_evt.Ui_Dialog()
    ui3 = GUI.dlg3_menu3_evt.Ui_Dialog()
    ui4 = GUI.dlg4_menu4_evt.Ui_Dialog()
    login_ui = GUI.login.Ui_Dialog()
    signup_ui = GUI.signup.Ui_Dialog()
    mainwindow_ui = GUI.mainwindow.Ui_MainWindow()
    topology_ui = GUI.topology.Ui_Dialog()

    # Dialog 창 띄우기
    #Dialog0.show()
    #Dialog1.show()
    #Dialog2.show()
    #Dialog3.show()
    #Dialog4.show()

    # MainWindow 창 띄우기
    Login.show()
    SignUp.show()
    #MainWindow.show()
    Topology.show()

    sys.exit(app.exec_())

