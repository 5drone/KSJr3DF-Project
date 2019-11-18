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

        self.text =1
        self.scrolllayotu = QFormLayout()
        self.scrollwidget = QWidget()
        self.scrollwidget.setLayout(self.scrolllayotu)
        self.WS_scrollArea.setWidget(self.scrollwidget)

        self.scrolllayout2 = QFormLayout()
        self.scrollwidget1 = QWidget()
        self.scrollwidget1.setLayout(self.scrolllayout2)
        self.Snapshot_scrollArea.setWidget(self.scrollwidget1)

        self.Menu1_pushButton.clicked.connect(self.menu1OnClicked)                     # Menu1_pushButton과 menu1OnClicked함수 연결
        self.Menu2_pushButton.clicked.connect(self.menu2OnClicked)                     # Menu2_pushbutton과 menu2OnClicked함수 연결
        self.Menu3_pushButton.clicked.connect(self.menu3OnClicked)                     # Menu3_pushbutton과 menu3OnClicked함수 연결
        self.Menu4_pushButton.clicked.connect(self.menu4OnClicked)                     # Menu4_pushbutton과 menu4OnClicked함수 연결
        self.Menu5_pushButton.clicked.connect(self.menu5OnClicked)                     # Menu5_pushbutton과 menu5OnClicked함수 연결
        self.Active_pushButton.clicked.connect(self.activeOnClicked)                   # Active_pushButton과 activeOnClicked함수 연결

        self.dialog = GUI.DialogSet.DlgLogin(self)
        self.dialog.exec_()


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
        self.l2 = QPushButton()
        self.l2.setText(str(self.text))
        self.l2.clicked.connect(self.dummyEvent)
        self.text+=1
        self.scrolllayout2.addRow(self.l2)
        """"
        dialog4 = GUI.DialogSet.DlgMenu4Evt(self)
        dialog4.exec_()
        """
    # dummy event
    def dummyEvent(self):
        self.l2.setCheckable(True)


    # menu5버튼 이벤트
    def menu5OnClicked(self):
        if self.l2.isChecked() == True:
            self.l2.deleteLater()
            QtWidgets.QMessageBox.about(None, "dumy", "good")
        else:
            QtWidgets.QMessageBox.about(None, "dumy", "nop")
        """
        #self.WS_scrollArea.setWidgetResizable(False)
        l1 = QLabel()
        l1.setText(str(self.text))
        self.text+=1
        self.scrolllayotu.addRow(l1)
        """
        #QtWidgets.QMessageBox.about(None, "menu5", "menu5")

    # Active버튼 이벤트
    def activeOnClicked(self):
        QtWidgets.QMessageBox.about(None, "Active", "Active")


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MyWindow()
    if main.dialog.result == 1:
        main.show()
        app.exec_()


if __name__ == "__main__":
    main()