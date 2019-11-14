from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
import GUI.ui_form_code.mainwindow
import GUI.DialogSet

# UI 코드와 논리 코드 구분
# UI 코드 -> ui_form_code 밑에 저장
# MainWindow 테스트 및 구현 부분


# MainWInow
class MyWindow(QMainWindow, GUI.ui_form_code.mainwindow.Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.Menu1_pushButton.clicked.connect(self.menu1OnClicked)                     # Menu1_pushButton과 menu1OnClicked함수 연결
        self.Menu2_pushButton.clicked.connect(self.menu2OnClicked)                     # Menu2_pushbutton과 menu2OnClicked함수 연결
        self.Menu3_pushButton.clicked.connect(self.menu3OnClicked)                     # Menu3_pushbutton과 menu3OnClicked함수 연결
        self.Menu4_pushButton.clicked.connect(self.menu4OnClicked)                     # Menu4_pushbutton과 menu4OnClicked함수 연결
        self.Menu5_pushButton.clicked.connect(self.menu5OnClicked)                     # Menu5_pushbutton과 menu5OnClicked함수 연결
        self.Active_pushButton.clicked.connect(self.activeOnClicked)                   # Active_pushButton과 activeOnClicked함수 연결


    # menu1버튼 이벤트
    def menu1OnClicked(self):
        dialog1 = GUI.DialogSet.DlgMenu1Evt(self)
        dialog1.exec_()

    # menu2버튼 이벤트
    def menu2OnClicked(self):
        dialog2 = GUI.DialogSet.DlgMenu2Evt(self)
        dialog2.exec_()

    # menu3버튼 이벤트
    def menu3OnClicked(self):
        dialog3 = GUI.DialogSet.DlgMenu3Evt(self)
        dialog3.exec_()

    # menu4버튼 이벤트
    def menu4OnClicked(self):
        dialog4 = GUI.DialogSet.DlgMenu4Evt(self)
        dialog4.exec_()

    # menu5버튼 이벤트
    def menu5OnClicked(self):
        QtWidgets.QMessageBox.about(None, "menu5", "menu5")

    # Active버튼 이벤트
    def activeOnClicked(self):
        QtWidgets.QMessageBox.about(None, "Active", "Active")


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MyWindow()
    main.show()
    app.exec_()


if __name__ == "__main__":
    main()