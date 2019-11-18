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

        # Works Space 목록 레이아웃 설정
        self.scrolllayout1 = QFormLayout()
        self.scrollwidget1 = QWidget()
        self.scrollwidget1.setLayout(self.scrolllayout1)
        self.WS_scrollArea.setWidget(self.scrollwidget1)

        # Snapshot 목록 레이아웃 설정
        self.scrolllayout2 = QFormLayout()
        self.scrollwidget2 = QWidget()
        self.scrollwidget2.setLayout(self.scrolllayout2)
        self.Snapshot_scrollArea.setWidget(self.scrollwidget2)

        self.Menu1_pushButton.clicked.connect(self.menu1OnClicked)                     # Menu1_pushButton과 menu1OnClicked함수 연결
        self.Menu2_pushButton.clicked.connect(self.menu2OnClicked)                     # Menu2_pushbutton과 menu2OnClicked함수 연결
        self.Menu3_pushButton.clicked.connect(self.menu3OnClicked)                     # Menu3_pushbutton과 menu3OnClicked함수 연결
        self.Menu4_pushButton.clicked.connect(self.menu4OnClicked)                     # Menu4_pushbutton과 menu4OnClicked함수 연결
        self.Menu5_pushButton.clicked.connect(self.menu5OnClicked)                     # Menu5_pushbutton과 menu5OnClicked함수 연결
        self.Active_pushButton.clicked.connect(self.activeOnClicked)                   # Active_pushButton과 activeOnClicked함수 연결

        # Login Dialog 부터 시작
        self.dialog = GUI.DialogSet.DlgLogin(self)
        self.dialog.exec_()


    # menu1버튼 이벤트
    def menu1OnClicked(self):
        # DlgMenu1Evt클래스 시작
        dialog1 = GUI.DialogSet.DlgMenu1Evt(self)
        dialog1.exec_()

        # WorkSpace 목록 버튼 scrolllayout1에 추가
        self.ws_name_list = QPushButton()
        self.ws_name_list.setText(str(dialog1.ws_name))
        self.ws_name_list.clicked.connect(self.wsClcikCheck)
        self.scrolllayout1.addRow(self.ws_name_list)

    # menu2버튼 이벤트
    def menu2OnClicked(self):
        # DlgMenu2Evt클래스 시작
        dialog2 = GUI.DialogSet.DlgMenu2Evt(self)
        dialog2.exec_()

        # 선택된 워크스페이스 목록 삭제
        if self.ws_name_list.isChecked() == True and dialog2.result == 1:
            self.ws_name_list.deleteLater()

    # menu3버튼 이벤트
    def menu3OnClicked(self):
        # DlgMenu3Evt클래스 시작
        dialog3 = GUI.DialogSet.DlgMenu3Evt(self)
        dialog3.exec_()

        """
        # 선택된 스냅샷 목록 삭제
        if self.sn_name_list.isChecked() == True and dialog3.result == 1:
            self.sn_name_list.deleteLater()
        """

    # menu4버튼 이벤트
    def menu4OnClicked(self):
        # DlgMenu4Evt클래스 시작
        dialog4 = GUI.DialogSet.DlgMenu4Evt(self)
        dialog4.exec_()


    # menu5버튼 이벤트
    def menu5OnClicked(self):
        QtWidgets.QMessageBox.about(None, "active", "active")

    # Active버튼 이벤트
    def activeOnClicked(self):
        QtWidgets.QMessageBox.about(None, "Active", "Active")

    # WorkSpace Click Check 함수
    def wsClcikCheck(self):
        self.ws_name_list.setCheckable(True)

    # Snapshot Click Check 함수
    def snClcikCheck(self):
        self.sn_name_list.setCheckable(True)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MyWindow()

    # Login Dialog 우측 상단 닫기 버튼 클릭 시 예외처리
    if main.dialog.result == 1:
        main.show()
        app.exec_()


if __name__ == "__main__":
    main()