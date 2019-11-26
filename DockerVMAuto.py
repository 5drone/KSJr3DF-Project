# Docker / VM 자동화 도구 Code #


import os
from os import path
import sys
import subprocess
import time

# Docker Toolbox 경로
dockertbx = path.expandvars(r'%ProgramFiles%\Docker Toolbox')

# TightVNC Viewer 경로
tVNCviewer = path.expandvars(r'%ProgramFiles%\TightVNC\tvnviewer.exe')

# 윈도우 이미지 자동화 도구 경로
WinVMAuto = "%SETUPPATH%/WinVMAuto.exe"

# 인자로 받기
def receive_argu(string):
    # 인자 확인 후 다운로드 진행
    if (string == 1):
        print("Running Kali Linux on Docker ...")
        subprocess.call(['docker','run','-itd','--name','kalivnc','-p','50001:5901','5drone/dockerhub:kali','/bin/bash'])
        subprocess.call(['docker','exec','kalivnc','vnc4server'])
        subprocess.run([tVNCviewer,'192.168.99.100::50001','-password=5drone'])
    elif (string == 2):
        print("Running Ubuntu on Docker ...")
        subprocess.call(['docker','run','-itd','--name','ubuntuvnc','-p','50002:5901','5drone/dockerhub:ubuntu','/bin/bash'])
        subprocess.call(['docker','exec','ubuntuvnc','vnc4server'])
        subprocess.run([tVNCviewer,'192.168.99.100::50002','-password=5drone'])
    elif (string == 3):
        print("Running Securityonion on Docker ...")
        subprocess.call(['docker','run','-itd','--name','onionvnc','-p','50003:5901','5drone/dockerhub:onion','/bin/bash'])
        subprocess.call(['docker','exec','onionvnc','vnc4server'])
        subprocess.run([tVNCviewer,'192.168.99.100::50003','-password=5drone'])
    elif (string == 4):
        print("Running VyOS on Docker ...")
        subprocess.call(['docker','run','-itd','--name','vyosvnc','-p','50004:5901','5drone/dockerhub:vyos','/bin/bash'])
        subprocess.call(['docker','exec','vyosvnc','vnc4server'])
        subprocess.run([tVNCviewer,'192.168.99.100::50004','-password=5drone'])
    elif (string == 5):
        print("Running Metasploitable on Docker ...")
        subprocess.call(['docker','run','-itd','--name','metavnc','-p','50005:5901','5drone/dockerhub:meta','/bin/bash'])
        subprocess.call(['docker','exec','metavnc','vnc4server'])
        subprocess.run([tVNCviewer,'192.168.99.100::50005','-password=5drone'])
    elif (string == 6):
        print("Running CentOS on Docker ...")
        subprocess.call(['docker','run','-itd','--name','centosvnc','-p','50006:5901','5drone/dockerhub:centos','/bin/bash'])
        subprocess.call(['docker','exec','centosvnc','vnc4server'])
        subprocess.run([tVNCviewer,'192.168.99.100::50006','-password=5drone'])
    elif (string == 7):
        print("Running bWASP on Docker ...")
        subprocess.call(['docker','run','-itd','--name','beevnc','-p','50007:5901','5drone/dockerhub:bee','/bin/bash'])
        subprocess.call(['docker','exec','beevnc','vnc4server'])
        subprocess.run([tVNCviewer,'192.168.99.100::50007','-password=5drone'])
    elif (string == 8):
        print("Running Windows 7 on VMWare ...")
        subprocess.call([WinVMAuto,'1'])
    elif (string == 9):
        print("Running Windows Server 2012 on VMWare ...")
        subprocess.call([WinVMAuto,'2'])
    else:
        print("Invalid Argument !!!")

# main
if __name__ == '__main__':
    print("======== Docker / VM Launcher ========")

    print("Detecting Docker ...")
    print(dockertbx)
    if(os.path.isdir(dockertbx) == False):
        print("Docker not Installed. Please Reinstall Docker.")
        exit(0)
    print("Docker Detected")

    print("Detecting TightVNC Viewer ...")
    print(tVNCviewer)
    if(os.path.isfile(tVNCviewer) == False):
        print("TightVNC Viewer not Installed. Please Reinstall TightVNC Viewer.")
        exit(0)
    print("TightVNC Viewer Detected")
    
    receive_argu(int(sys.argv[1]))