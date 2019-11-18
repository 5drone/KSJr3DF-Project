# 윈도우 이미지 자동화 도구 Code #


import os
from os import path
import sys
# import urllib.request
import requests
from tqdm import tqdm
import subprocess
import hashlib

# URL 저장 경로 지정
W7_url_1 = "http://207.148.109.78/W7.part1.exe"
W7_url_2 = "http://207.148.109.78/W7.part2.rar"
WS12_url_1 = "http://207.148.109.78/WS12.part1.exe"
WS12_url_2 = "http://207.148.109.78/WS12.part2.rar"

# 저장할 파일이름
save_file_path = path.expandvars(r'%APPDATA%\5drone')
savename_W7_url_1 = path.expandvars(r'%APPDATA%\5drone\W7.part1.exe')
savename_W7_url_2 = path.expandvars(r'%APPDATA%\5drone\W7.part2.rar')
savename_WS12_url_1 = path.expandvars(r'%APPDATA%\5drone\WS12.part1.exe')
savename_WS12_url_2 = path.expandvars(r'%APPDATA%\5drone\WS12.part2.rar')

# VM Image가 저장될 환경 변수 경로
ovf_source_W7 = path.expandvars(r'%appdata%\5drone\5drone_Win7x64.ovf')
mf_source_W7 = path.expandvars(r'%APPDATA%\5drone\5drone_Win7x64.mf')
vmdk_source_W7 = path.expandvars(r'%APPDATA%\5drone\5drone_Win7x64-disk1.vmdk')
appdata_W7 = path.expandvars(r'%appdata%\5drone\5drone_Win7x64\5drone_Win7x64.vmx')
ovf_source_WS12 = path.expandvars(r'%appdata%\5drone\5drone_WinServer2012.ovf')
mf_source_WS12 = path.expandvars(r'%APPDATA%\5drone\5drone_WinServer2012.mf')
vmdk_source_WS12 = path.expandvars(r'%APPDATA%\5drone\5drone_WinServer2012-disk1.vmdk')
appdata_WS12 = path.expandvars(r'%appdata%\5drone\5drone_WinServer2012\5drone_WinServer2012.vmx')


# ovftool
ovftool = path.expandvars(r'%ProgramFiles(x86)%\VMware\VMware Workstation\OVFTool\ovftool.exe') 

# vmrun
vmrun = path.expandvars(r'%ProgramFiles(x86)%\VMware\VMware Workstation\vmrun.exe')

# 서버에 업로드 된 이미지 압축 파일 HASH
HASH_W7_url_1 = "A10C2D32CE04A06B1ACC5D9339E0941FC1922E7F"
HASH_W7_url_2 = "3A5D90469E56D11815F35030BD4FF0D7B4C4BFE3"
HASH_WS12_url_1 = "6B73E9AB8AB4332E6B52671E56D3D15D47BFED98"
HASH_WS12_url_2 = "0EE3AB19D48B798358B006C8001126E20853F36E"

# 인자로 받기
def receive_argu(string):
    # 경로 확인 후 존재하지 않으면 생성
    if not(os.path.isdir(save_file_path)):
            os.makedirs(os.path.join(save_file_path))
    # 인자 확인 후 다운로드 진행
    if (string == 1):
        print("Detecting Windows Images that already exists ...")
        if(os.path.isfile(appdata_W7) == False):
            print("Download Windows 7 Images from server")
            download_WIN7()
            os.system(savename_W7_url_1)
            subprocess.call([ovftool,'-tt=vmx',ovf_source_W7,save_file_path])
        print("Windows 7 Images Detected. Starting....")
        subprocess.run([vmrun,'-T','ws','start',appdata_W7])
        Delete_Temp_Files_W7()
    elif (string == 2):
        print("Detecting Windows Server Images that already exists ...")
        if(os.path.isfile(appdata_WS12) == False):
            print("Download Windows Server Images from server")
            download_WINSERVER2012()
            os.system(savename_WS12_url_1)
            subprocess.call([ovftool,'-tt=vmx',ovf_source_WS12,save_file_path])
        print("Windows Server 2012 Images Detected. Starting....")
        subprocess.run([vmrun,'-T','ws','start',appdata_WS12])
        Delete_Temp_Files_WS12()
    else:
        print("Invalid Argument !!!")

# 임시파일 삭제
def Delete_Temp_Files_W7():
    print("Temp Files Deleting ...")
    if os.path.isfile(savename_W7_url_1):
        os.remove(savename_W7_url_1)
    if os.path.isfile(savename_W7_url_2):
        os.remove(savename_W7_url_2)
    if os.path.isfile(mf_source_W7):
        os.remove(mf_source_W7)
    if os.path.isfile(ovf_source_W7):
        os.remove(ovf_source_W7)
    if os.path.isfile(vmdk_source_W7):
        os.remove(vmdk_source_W7)
    print("Temp Files Deleted.")

def Delete_Temp_Files_WS12():
    print("Temp Files Deleting ...")
    if os.path.isfile(savename_WS12_url_1):
        os.remove(savename_WS12_url_1)
    if os.path.isfile(savename_WS12_url_2):
        os.remove(savename_WS12_url_2)
    if os.path.isfile(mf_source_WS12):
        os.remove(mf_source_WS12)
    if os.path.isfile(ovf_source_WS12):
        os.remove(ovf_source_WS12)
    if os.path.isfile(vmdk_source_WS12):
        os.remove(vmdk_source_WS12)
    print("Temp Files Deleted.")

# 다운로드 함수
def download_file(url):
    if (url == W7_url_1):
        local_filename = savename_W7_url_1
    elif (url == W7_url_2):
        local_filename = savename_W7_url_2
    elif (url == WS12_url_1):
        local_filename = savename_WS12_url_1
    elif (url == WS12_url_2):
        local_filename = savename_WS12_url_2
    else:
        print("Invalid Argument !!!")

    r = requests.get(url, stream=True)
    r.raise_for_status()
    total_size = int(r.headers.get('content-length',0))
    t = tqdm(total=total_size, unit='iB', unit_scale=True)
    with open(local_filename, 'wb') as f:
        for data in r.iter_content(chunk_size=8192):
            t.update(len(data))
            f.write(data)
    t.close()
    r.close()
    f.close()
    return

# 이미지 원본과의 HASH값 비교
def hash_compare(download_file_hash):
    if (download_file_hash == savename_W7_url_1):
        print("Windows 7 VM Image 1/2 Hash Checking...")
        download_file_hash = hash_for_largefile(savename_W7_url_1)
        if (download_file_hash != HASH_W7_url_1.lower()):
            print("Hash does not match. Redownloading...")
            download_file(W7_url_1)
        print("Hash Matched! [1/2]")

    if (download_file_hash == savename_W7_url_2):
        print("Windows 7 VM Image 2/2 Hash Checking...")
        download_file_hash = hash_for_largefile(savename_W7_url_2)
        if (download_file_hash != HASH_W7_url_2.lower()):
            print("Hash does not match. Redownloading...")
            download_file(W7_url_2)
        print("Hash Matched! [2/2]")
    
    if (download_file_hash == savename_WS12_url_1):
        print("Windows Server 2012 VM 1/2 Image Hash Checking...")
        download_file_hash = hash_for_largefile(savename_WS12_url_1)
        if (download_file_hash != HASH_WS12_url_1.lower()):
            print("Hash does not match. Redownloading...")
            download_file(WS12_url_1)
        print("Hash Matched! [1/2]")
    
    if (download_file_hash == savename_WS12_url_2):
        print("Windows Server 2012 VM 2/2 Image Hash Checking...")
        download_file_hash = hash_for_largefile(savename_WS12_url_2)
        if (download_file_hash != HASH_WS12_url_2.lower()):
            print("Hash does not match. Redownloading...")
            download_file(WS12_url_2)
        print("Hash Matched! [2/2]")

# Buffer를 이용하여 큰 파일 해싱 수행(SHA-1)
def hash_for_largefile(filepath, blocksize=8192):
    sha_1 = hashlib.sha1()
    try:
        f = open(filepath, "rb")
    except IOError as e:
        print("File open error !", e)
        return
    while True:
        buf = f.read(blocksize)
        if not buf:
            break
        sha_1.update(buf)
    f.close()
    return sha_1.hexdigest()

# 인자별 다운로드
def download_WIN7():
    download_file(W7_url_1)
    hash_compare(savename_W7_url_1)
    print("=========== Windows 7 VM Image Download Complete 1/2 ===========")
    download_file(W7_url_2)
    hash_compare(savename_W7_url_2)
    print("=========== Windows 7 VM Image Download Complete 2/2 ===========")

def download_WINSERVER2012():
    download_file(WS12_url_1)
    hash_compare(savename_WS12_url_1)
    print("=========== Windows Server 2012 VM Image Download Complete 1/2 ===========")
    download_file(WS12_url_2)
    hash_compare(savename_WS12_url_2)
    print("=========== Windows Server 2012 VM Image Download Complete 2/2 ===========")

# main
if __name__ == '__main__':
    print("======== Windows VM Auto Launcher ========")

    print("Detecting OVFTool ...")
    if(os.path.isfile(ovftool) == False):
        print("OVFTool not Installed. Please Reinstall VMWare Workstation.")
        exit(0)
    print("OVFTool Detected")

    print("Detecting VMRun ...")
    if(os.path.isfile(vmrun) == False):
        print("VMRun not Installed. Please Reinstall VMWare Workstation.")
        exit(0)
    print("VMRun Detected")
    
    receive_argu(int(sys.argv[1]))
