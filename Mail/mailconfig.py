import smtplib
from email.mime.text import MIMEText
import secrets

class MailController:
    def __init__(self, email):
        self.email=email
        self.session = smtplib.SMTP('smtp.gmail.com', 587) # 세션 생성
        self.session = smtplib.SMTP('smtp.gmail.com', 587)
        self.session.starttls()
        self.session.login('slrcoding1234@gmail.com', 'asvbtdarotqcqmmq')
        self.key = secrets.token_hex(3)

    def sendmail(self):
        msg = MIMEText('인증번호 : %s'%self.key)
        msg['Subject'] = '제목 : 본인 인증입니다.'
        self.session.sendmail("slrcoding1234@gmail.com", self.email, msg.as_string())
        self.session.quit()


if __name__=="__main__":

    test = MailController("tmxk4197@naver.com")
    test.sendmail()



