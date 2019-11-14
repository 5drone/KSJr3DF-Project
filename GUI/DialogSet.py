from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
import GUI.ui_form_code.dlg0_signup_evt, GUI.ui_form_code.dlg1_menu1_evt
import GUI.ui_form_code.dlg2_menu2_evt, GUI.ui_form_code.dlg3_menu3_evt
import GUI.ui_form_code.dlg4_menu4_evt, GUI.ui_form_code.login
import GUI.ui_form_code.signup, GUI.ui_form_code.topology
import GUI.MainWindow

# UI 코드와 논리 코드 구분
# UI 코드 -> ui_form_code 밑에 저장
# 모든 Dialog 테스트 및 구현 부분


# 회원가입 인증완료 Dialog
class DlgSignupEvt(QDialog, GUI.ui_form_code.dlg0_signup_evt.Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.close)


# MainWinodw Menu1 클릭 Dialog
class DlgMenu1Evt(QDialog, GUI.ui_form_code.dlg1_menu1_evt.Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.Cancel_pushButton.clicked.connect(self.cancelOnClicked)            # Cancel_pushButton과 cancelOnClicked함수 연결
        self.Next_pushButton.clicked.connect(self.nextOnClicked)                # Next_pushButton과 nextOnClicked함수 연결
        self.one_to_two_pushButton.clicked.connect(self.oneTotwoOnClicekd)      # one_to_two_pushButton과 oneTotwoOnClicekd함수 연결
        self.two_to_three_pushButton.clicked.connect(self.twoTothreeOnClicekd)  # two_to_three_pushButton과 oneTotwoOnClicekd함수 연결

    # 취소 버튼 클릭 이벤트
    def cancelOnClicked(self):
        self.close()

    # 다음 버튼 클릭 이벤트
    def nextOnClicked(self):
        self.close()
        topology_dialog = DlgTopology()
        topology_dialog.exec_()

    # 1 to 2 버튼 클릭 이벤트
    def oneTotwoOnClicekd(self):
        QtWidgets.QMessageBox.about(None, "1to2", "1to2")

    # 2 to 3 버튼 클릭 이벤트
    def twoTothreeOnClicekd(self):
        QtWidgets.QMessageBox.about(None, "2to3", "2to3")


# MainWinodw Menu2 클릭 Dialog
class DlgMenu2Evt(QDialog, GUI.ui_form_code.dlg2_menu2_evt.Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.buttonBox.accepted.connect(self.removeOnCliecked)  # buttonBox.accepted버튼과 removeOnCliecked함수 연결
        self.buttonBox.rejected.connect(self.close)             # buttonBox.rejected버튼과 Dialog.accept 연결(바로 창 꺼짐)

    # 삭제 버튼 이벤트
    def removeOnCliecked(self):
        QtWidgets.QMessageBox.about(None, "워크스페이스삭제", "워크스페이스 삭제 가즈아~~")
        self.close()


# MainWinodw Menu3 클릭 Dialog
class DlgMenu3Evt(QDialog, GUI.ui_form_code.dlg3_menu3_evt.Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.buttonBox.accepted.connect(self.removeOnCliecked)  # buttonBox.accepted버튼과 removeOnCliecked함수 연결
        self.buttonBox.rejected.connect(self.close)             # buttonBox.rejected버튼과 Dialog.accept 연결(바로 창 꺼짐)

    # 삭제 버튼 이벤트
    def removeOnCliecked(self):
        QtWidgets.QMessageBox.about(None, "스냅샷 삭제", "스냅샷 삭제 가즈아~~")
        self.close()


# MainWinodw Menu4 클릭 Dialog
class DlgMenu4Evt(QDialog, GUI.ui_form_code.dlg4_menu4_evt.Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.buttonBox.rejected.connect(self.close)
        self.buttonBox.accepted.connect(self.removeOnCliecked)

    # 삭제 버튼 이벤트
    def removeOnCliecked(self):
        QtWidgets.QMessageBox.about(None, "스냅샷 초기화", "스냅샷 초기화 가즈아~~")
        self.close()

# Login Input Form Dialog
class DlgLogin(QDialog, GUI.ui_form_code.login.Ui_Dialog):

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.default = "default"
        self.id = "하위?"
        self.passwod = "오호"

        self.Login_pushButton.clicked.connect(self.loginpushOnClicked)      # Login_pushButton과 loginpushOnClicked함수 연결
        self.Signup_pushButton.clicked.connect(self.signuppushOnClicked)    # Signup_pushButton signuppushOnClicked함수 연결
        self.NonMember_Login_pushButton.clicked.connect(self.NonMemeberpushOnClicked)    # NonMember_Login_pushButton NonMemeberpushOnClicked함수 연결

    # login버튼 이벤트
    def loginpushOnClicked(self):
        if self.ID_editText.text()==self.default and self.PW_editText.text() == self.default:
            QtWidgets.QMessageBox.about(None, "로그인 성공",
            "아이디:" + self.ID_editText.text() + "\n패스워드:" + self.PW_editText.text())
            self.close()
            mainwindow = GUI.MainWindow.MyWindow(self)
            mainwindow.show()
        else :
            QtWidgets.QMessageBox.about(None, "로그인 실패", "로그인 실패다~ 이 ~ 개 쉐이야")


    # SignUp버튼 이벤트
    def signuppushOnClicked(self):
        signup_dialog = DlgSignup(self)
        signup_dialog.exec_()

    # NonMember Login버튼 이벤트
    def NonMemeberpushOnClicked(self):
        self.close()
        mainwindow = GUI.MainWindow.MyWindow(self)
        mainwindow.show()


# Signup Input Form Dialog
class DlgSignup(QDialog, GUI.ui_form_code.signup.Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.id = None
        self.password = None
        self.checkpassword = None
        self.email = None
        self.checknum = None

        self.Check_Num_pusthButton.clicked.connect(self.checkNumOnClicked)         # Check_Num_pusthButton버튼과 checkNumOnClicked함수 연결
        self.Check_Num_trans_pushButton.clicked.connect(self.checkTransOnClicked)  # Check_Num_trans_pushButton버튼과 checkTransOnClicked함수 연결
        self.Signup_pushButton.clicked.connect(self.signupOnClicked)               # Signup_pushButton버튼과 signupOnClicked함수 연결

    def checkNumOnClicked(self):
        check_dialog = DlgSignupEvt(self)
        check_dialog.exec_()

    def checkTransOnClicked(self):
        QtWidgets.QMessageBox.about(None, "인증번호 전송", self.Check_Num_Label.text())

    def signupOnClicked(self):
        QtWidgets.QMessageBox.about(None, "회원가입 성공", "회원가입 성공")
        self.close()


# Topology Input Form Dialog
class DlgTopology(QDialog, GUI.ui_form_code.topology.Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.Finish_pushButton.clicked.connect(self.finishOnClicked)            # Finish_pushButton과 finishOnClicked함수 연결

    # 완료 버튼 이벤트
    def finishOnClicked(self):
        QtWidgets.QMessageBox.about(None, "설정완료","설정완료")
        self.close()
        mainwinodw = GUI.MainWindow.MyWindow(self)
        mainwinodw.show()


# Dialog 테스트 함수
def main():
    app = QtWidgets.QApplication(sys.argv)

    # 다이얼로그 선택
    #Dialog = DlgSignupEvt()
    #Dialog = DlgMenu1Evt()
    #Dialog = DlgMenu2Evt()
    #Dialog = DlgMenu3Evt()
    #Dialog = DlgMenu4Evt()

    #Dialog = DlgLogin()
    #Dialog = DlgSignup()
    Dialog = DlgTopology()
    Dialog.show()
    app.exec_()


if __name__ == "__main__":
    main()