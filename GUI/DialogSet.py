from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
import GUI.ui_form_code.dlg0_signup_evt, GUI.ui_form_code.dlg1_menu1_evt
import GUI.ui_form_code.dlg2_menu2_evt, GUI.ui_form_code.dlg3_menu3_evt
import GUI.ui_form_code.dlg4_menu4_evt, GUI.ui_form_code.login
import GUI.ui_form_code.signup, GUI.ui_form_code.topology
import GUI.MainWindow
import DB.dbconfig
import Mail.mailconfig

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

        self.ws_name=None

        self.Cancel_pushButton.clicked.connect(self.cancelOnClicked)            # Cancel_pushButton과 cancelOnClicked함수 연결
        self.Next_pushButton.clicked.connect(self.nextOnClicked)                # Next_pushButton과 nextOnClicked함수 연결
        self.one_to_two_pushButton.clicked.connect(self.oneTotwoOnClicekd)      # one_to_two_pushButton과 oneTotwoOnClicekd함수 연결
        self.two_to_three_pushButton.clicked.connect(self.twoTothreeOnClicekd)  # two_to_three_pushButton과 oneTotwoOnClicekd함수 연결

    # 취소 버튼 클릭 이벤트
    def cancelOnClicked(self):
        self.close()

    # 다음 버튼 클릭 이벤트
    def nextOnClicked(self):
        self.ws_name = self.WS_Name_editText.text()
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

        self.Login_pushButton.clicked.connect(self.loginpushOnClicked)                  # Login_pushButton과 loginpushOnClicked함수 연결
        self.Signup_pushButton.clicked.connect(self.signuppushOnClicked)                # Signup_pushButton signuppushOnClicked함수 연결
        self.NonMember_Login_pushButton.clicked.connect(self.NonMemeberpushOnClicked)   # NonMember_Login_pushButton NonMemeberpushOnClicked함수 연결

    # Login버튼 이벤트
    def loginpushOnClicked(self):
        login = [self.ID_editText.text(), self.PW_editText.text()]
        mysql_controller = DB.dbconfig.DBController()

        result = mysql_controller.selectSQL_login(login)
        if result == False:
            QtWidgets.QMessageBox.about(None, "로그인 실패", "로그인 실패다~ 이 ~ 개 쉐이야")
        elif login[0] == result[0][0] and login[1] == result[0][1]:
            self.result=1
            self.close()
            return self.result
        else:
            QtWidgets.QMessageBox.about(None, "로그인 실패", "로그인 실패다~ 이 ~ 개 쉐이야")

    # SignUp버튼 이벤트
    def signuppushOnClicked(self):
        signup_dialog = DlgSignup(self)
        signup_dialog.exec_()
        self.result=1
        return self.result

    # NonMember Login버튼 이벤트
    def NonMemeberpushOnClicked(self):
        self.result=1
        self.close()
        return self.result


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
        self.flag = [1,0,0,0]           # [인증번호 검증, 중복 아이디 검증, 비밀번호 재확인 검증, 공란 검증]

        self.Check_Num_pusthButton.clicked.connect(self.checkNumOnClicked)         # Check_Num_pusthButton버튼과 checkNumOnClicked함수 연결
        self.Check_Num_trans_pushButton.clicked.connect(self.checkTransOnClicked)  # Check_Num_trans_pushButton버튼과 checkTransOnClicked함수 연결
        self.Signup_pushButton.clicked.connect(self.signupOnClicked)               # Signup_pushButton버튼과 signupOnClicked함수 연결

    # 인증번호 검증 (false -> flag : 1)
    def checkNumOnClicked(self):
        if self.Check_Num_editText.text() == self.gmail.key:
            self.flag.insert(0,0)
            check_dialog = DlgSignupEvt(self)
            check_dialog.exec_()
        else:
            self.flag.insert(0,1)
            QtWidgets.QMessageBox.about(None, "인증 실패", "인증 실패")

    # 중복 아이디 검증 (false -> flag : 2)
    def checkID(self):
        login = [self.ID_editText.text()]
        mysql_controller = DB.dbconfig.DBController()

        if mysql_controller.selectSQL_login(login):
            self.flag.insert(1,2)
        else:
            self.flag.insert(1,0)


    # 비밀번호 재확인 검증 (false -> flag : 3)
    def checkPW(self):
        if self.PW_editText.text() != self.PW_Check_editText.text():
            self.flag.insert(2,3)
        else:
            self.flag.insert(2,0)

    # 공란 검증 (false -> flag : 4)
    def checkBlank(self):
        if not self.ID_editText.text() or not self.PW_Check_editText.text() or \
                not self.PW_editText.text() or not self.Check_Num_editText.text() or not self.Email_editText.text():
            self.flag.insert(3,4)
        else:
            self.flag.insert(3,0)

    def checkTransOnClicked(self):
        self.gmail = Mail.mailconfig.MailController(self.Email_editText.text())
        self.gmail.sendmail()
        QtWidgets.QMessageBox.about(None, "인증번호 전송", "인증번호 전송완료")

    def signupOnClicked(self):
        self.checkID()
        self.checkPW()
        self.checkBlank()
        if self.flag[0] == 1:
            QtWidgets.QMessageBox.about(None, "#1", "인증번호가 유효하지 않습니다")
        elif self.flag[1] == 2:
            QtWidgets.QMessageBox.about(None, "#2", "중복되는 아이디가 있습니다")
        elif self.flag[2] == 3:
            QtWidgets.QMessageBox.about(None, "#3", "비밀번호를 다시 확인해주세요")
        elif self.flag[3] == 4:
            QtWidgets.QMessageBox.about(None, "#4", "작성하지 못한 부분이 있습니다")
        else :
            mysql_controller = DB.dbconfig.DBController()
            if mysql_controller.insertSQL_login([self.ID_editText.text(), self.PW_editText.text(), self.Email_editText.text()]):
                QtWidgets.QMessageBox.about(None, "회원가입", "회원가입 성공")
            else:
                QtWidgets.QMessageBox.about(None, "회원가입", "회원가입 실패")
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


# Dialog 테스트 함수
def main():
    app = QtWidgets.QApplication(sys.argv)

    # 다이얼로그 선택
    #Dialog = DlgSignupEvt()
    #Dialog = DlgMenu1Evt()
    #Dialog = DlgMenu2Evt()
    #Dialog = DlgMenu3Evt()
    #Dialog = DlgMenu4Evt()

    Dialog = DlgLogin()
    #Dialog = DlgSignup()
    #Dialog = DlgTopology()
    Dialog.show()
    app.exec_()
    print(Dialog.result)


if __name__ == "__main__":
    main()
