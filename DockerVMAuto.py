# Docker / VM 자동화 도구 Code #


import os
from os import path
import sys
import subprocess

# Docker Toolbox 경로
dockertbx = path.expandvars(r'%ProgramFiles%\Docker Toolbox')

# RealVNC Viewer 경로
rVNCviewer = path.expandvars(r'%ProgramFiles%\RealVNC\VNC Viewer\vncviewer.exe')

# 윈도우 이미지 자동화 도구 경로
WinVMAuto = "%SETUPPATH%/WinVMAuto.exe"

# docker container running on background
dockerrun = "docker run -itd"

# 인자로 받기
def receive_argu(string):
    # 인자 확인 후 다운로드 진행
    if (string == 1):
        print("Running Kali Linux on Docker ...")
        subprocess.call([dockerrun,'-p','50000:5900','-p','50001:5901','5drone/kali:latest'])
        subprocess.call([rVNCviewer,'192.168.99.100:1','-listen 50001'])
    elif (string == 2):
        print("Running Ubuntu on Docker ...")
        subprocess.call([dockerrun,'-p','50002:5900','-p','50003:5901','5drone/ubuntu:latest'])
        subprocess.call([rVNCviewer,'192.168.99.100:1','-listen 50003'])
    elif (string == 3):
        print("Running Securityonion on Docker ...")
        subprocess.call([dockerrun,'-p','50004:5900','-p','50005:5901','5drone/onion:latest'])
        subprocess.call([rVNCviewer,'192.168.99.100:1','-listen 50005'])
    elif (string == 4):
        print("Running VyOS on Docker ...")
        subprocess.call([dockerrun,'-p','50006:5900','-p','50007:5901','5drone/vyos:latest'])
        # subprocess.call([rVNCviewer,'192.168.99.100:1','-listen 50007'])
    elif (string == 5):
        print("Running Metasploitable on Docker ...")
        subprocess.call([dockerrun,'-p','50008:5900','-p','50009:5901','5drone/meta:latest'])
        # subprocess.call([rVNCviewer,'192.168.99.100:1','-listen 50009'])
    elif (string == 6):
        print("Running CentOS on Docker ...")
        subprocess.call([dockerrun,'-p','50010:5900','-p','50011:5901','5drone/centos:latest'])
        subprocess.call([rVNCviewer,'192.168.99.100:1','-listen 50011'])
    elif (string == 7):
        print("Running bWASP on Docker ...")
        subprocess.call([dockerrun,'-p','50012:5900','-p','50013:5901','5drone/bee:latest'])
        subprocess.call([rVNCviewer,'192.168.99.100:1','-listen 50013'])
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
    if(os.path.isfile(dockertbx) == False):
        print("Docker not Installed. Please Reinstall Docker.")
        exit(0)
    print("Docker Detected")

    print("Detecting RealVNC Viewer ...")
    if(os.path.isfile(rVNCviewer) == False):
        print("RealVNC Viewer not Installed. Please Reinstall RealVNC Viewer.")
        exit(0)
    print("RealVNC Viewer Detected")
    
    receive_argu(int(sys.argv[1]))