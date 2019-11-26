
# Docker / VM 자동화 도구 Code #


import os
from os import path
import sys
import subprocess
import time

# Docker Toolbox 경로
dockertbx = path.expandvars(r'%ProgramFiles%\Docker Toolbox')

# TightVNC Viewer 경로
tVNCviewer = path.expandvars(r'%ProgramFiles(x86)%\TightVNC\tvnviewer.exe')

# 윈도우 이미지 자동화 도구 경로
#WinVMAuto = "WinVMAuto.exe"

# 인자로 받기

def receive_argu(string, int):
    # 인자 확인 후 다운로드 진행
    if (string == 'A'):
        string = 'net_group_A'
    elif (string == 'B'):
        string = 'net_group_B'
    elif (string == 'C'):
        string = 'net_group_C'
    elif (string == 'D'):
        string = 'net_group_D'

    if (int == 1):
        print("Running Kali Linux on Docker ...")
        subprocess.call(['docker','run','-itd','--name','kalivnc','-p','50001:5901','--net',string,'5drone/dockerhub:kali','/bin/bash'])
        subprocess.call(['docker','exec','kalivnc','vnc4server'])
        subprocess.run([tVNCviewer,'192.168.99.100::50001','-password=5drone'])
    elif (int == 2):
        print("Running Ubuntu on Docker ...")
        subprocess.call(['docker','run','-itd','--name','ubuntuvnc','-p','50002:5901','--net',string,'5drone/dockerhub:ubuntu','/bin/bash'])
        subprocess.call(['docker','exec','ubuntuvnc','vnc4server'])
        subprocess.run([tVNCviewer,'192.168.99.100::50002','-password=5drone'])
    elif (int == 3):
        print("Running Securityonion on Docker ...")
        subprocess.call(['docker','run','-itd','--name','onionvnc','-p','50003:5901','--net',string,'5drone/dockerhub:onion','/bin/bash'])
        subprocess.call(['docker','exec','onionvnc','vnc4server'])
        subprocess.run([tVNCviewer,'192.168.99.100::50003','-password=5drone'])
    elif (int == 4):
        print("Running VyOS on Docker ...")
        subprocess.call(['docker','run','-itd','--name','vyosvnc','-p','50004:5901','--net',string,'5drone/dockerhub:vyos','/bin/bash'])
        subprocess.call(['docker','exec','vyosvnc','vnc4server'])
        subprocess.run([tVNCviewer,'192.168.99.100::50004','-password=5drone'])
    elif (int == 5):
        print("Running Metasploitable on Docker ...")
        subprocess.call(['docker','run','-itd','--name','metavnc','-p','50005:5901','--net',string,'5drone/dockerhub:meta','/bin/bash'])
        subprocess.call(['docker','exec','metavnc','vnc4server'])
        subprocess.run([tVNCviewer,'192.168.99.100::50005','-password=5drone'])
    elif (int == 6):
        print("Running CentOS on Docker ...")
        subprocess.call(['docker','run','-itd','--name','centosvnc','-p','50006:5901','--net',string,'5drone/dockerhub:centos','/bin/bash'])
        subprocess.call(['docker','exec','centosvnc','vnc4server'])
        subprocess.run([tVNCviewer,'192.168.99.100::50006','-password=5drone'])
    elif (int == 7):
        print("Running bWASP on Docker ...")
        subprocess.call(['docker','run','-itd','--name','beevnc','-p','50007:5901','--net',string,'5drone/dockerhub:bee','/bin/bash'])
        subprocess.call(['docker','exec','beevnc','vnc4server'])
        subprocess.run([tVNCviewer,'192.168.99.100::50007','-password=5drone'])
    else:
        print("Invalid Argument !!!")


# main
if __name__ == '__main__':
    print("======== Docker / VM Launcher ========")

    print("Detecting Docker ...")
    #print(dockertbx)
    if(os.path.isdir(dockertbx) == False):
        print("Docker not Installed. Please Reinstall Docker.")
        exit(0)
    print("Docker Detected")

    print("Detecting TightVNC Viewer ...")
    #print(tVNCviewer)
    if(os.path.isfile(tVNCviewer) == False):
        print("TightVNC Viewer not Installed. Please Reinstall TightVNC Viewer.")
        exit(0)
    print("TightVNC Viewer Detected")
    
    subprocess.call(['docker','network','create','--driver','bridge','net_group_A'])
    subprocess.call(['docker','network','create','--driver','bridge','net_group_B'])
    subprocess.call(['docker','network','create','--driver','bridge','net_group_C'])
    subprocess.call(['docker','network','create','--driver','bridge','net_group_D'])

    receive_argu(str(sys.argv[1]), int(sys.argv[2]))