# K-Shield Project

# 1. 프로젝트 개요
##	1.1 프로젝트 명 및 기간
	▷ 프로젝트 명: 도커를 활용한 보안교육 모델 구축
	▷ 프로젝트 기간: 2019.10.08 ~ 2019.11.26 (8주)

##	1.2 프로젝트 배경
	 기존의 네트워크 망을 구성하여 실습하는 보안교육은 가상 머신 기술을 이용하였습니다. 실습 망 환경 전체를 실제적으로 구성하는 것은 상당한 제약이 존
	재하였고, 범용성이 뛰어난 가상 머신 기술은 이러한 제약을 해결하는데 적합합니다. 하지만 구조적인 한계로 속도가 느리고 효율적인 관리를 위해 서버에 
	가상 머신을 탑재할 경우 여러 사용자가 동시 접속할 경우 과부하의 가능성이 존재하는 단점을 가지고 있습니다. 컨테이너 기반의 오픈소스 가상화 플랫폼인 
	도커를 활용하여 이러한 시스템 가상 머신의 단점을 해결할 수 있습니다. 먼저 전체 하드웨어를 소프트웨어적으로 구현하는 구조가 아니기 때문에 시스템에 
	비교적 적은 부담을 주며 가상 머신보다 적은 자원을 사용하기에 개인 PC에 가상 네트워크 망을 구성할 수 있습니다. 따라서 도커를 활용하여 기존의 가상 
	머신으로 구축한 실습망을 성능 및 비용 측면에서 개선할 수 있습니다.

##	1.3 프로젝트 목표
	* GUI를 통해 사용자가 원하는 환경 구성 편의성 제공 
	* 설정한 환경의 토폴로지 프리뷰 제공
	* 설정한 환경들을 자동화하여 구축하는 스크립트 제작
	* 도커를 이용해 사용자 스스로 PC에 교육망 구축함으로써 기존의 망 구축보다 비용 및 성능면에서 높은 효율을 보일 것 

# 2. 시스템 구성도
# 3. Tech/Framework
# 4. How to use?
# 5. Contributors
* 김종우, 민준영, 윤영기, 이영진, 최민철
# 6. 도커 이미지 생성

* qemu 설치

![2](https://user-images.githubusercontent.com/49422777/71220709-df3b3300-230c-11ea-95ee-3e55b7344c7d.JPG)


* guestfish 설치

![3](https://user-images.githubusercontent.com/49422777/71220830-6c7e8780-230d-11ea-9797-eec553257131.JPG)


* 우분투에 도커 설치하기(참고사이트 : https://kururu.tistory.com/87)

![4](https://user-images.githubusercontent.com/49422777/71220835-6f797800-230d-11ea-95aa-1d0d4aa34cca.JPG)


![5](https://user-images.githubusercontent.com/49422777/71220841-72746880-230d-11ea-9a7c-2c3bd9e94537.JPG)


![6](https://user-images.githubusercontent.com/49422777/71220845-7607ef80-230d-11ea-8101-3ee313216843.JPG)


![7](https://user-images.githubusercontent.com/49422777/71220850-799b7680-230d-11ea-841c-82c0f3bb4095.JPG)


![8](https://user-images.githubusercontent.com/49422777/71220856-7ef8c100-230d-11ea-9780-7769f38f1a8b.JPG)


![9](https://user-images.githubusercontent.com/49422777/71220862-828c4800-230d-11ea-8526-57fee7e2bef5.JPG)


![10](https://user-images.githubusercontent.com/49422777/71220867-861fcf00-230d-11ea-8515-c18541609489.JPG)

* docker 테스트를 위해 hello-world 이미지를 이용해 컨테이너 run
![12](https://user-images.githubusercontent.com/49422777/71220875-8ddf7380-230d-11ea-9f9d-20bef5c39062.JPG)


* vmdk파일을 도커 이미지로 변환 
(참고사이트 : 
https://blog.inslash.com/how-to-convert-vmdk-to-a-docker-image-be939745ed8a

https://medium.com/@roberto.fernandez.perez/create-docker-base-image-for-legacy-linux-system-3f5f77acd740 )

* 이미지로 만들 vmdk파일을 리눅스에 저장
![13](https://user-images.githubusercontent.com/49422777/71221638-b4eb7480-2310-11ea-9f98-3bdad829f5b3.JPG)


* qemu를 이용해 vmdk파일을 변환

qemu-img convert -f [포맷] -O [변경후 포맷] [사용할 파일] [이름 지정]
![14](https://user-images.githubusercontent.com/49422777/71221644-b9179200-2310-11ea-92d8-3489390c3715.JPG)


* guestfish를 이용해 가상이미지에서 운영체제가 설치된 파티션 추출

guestfish -a [가상이미지 이름] --ro
![15](https://user-images.githubusercontent.com/49422777/71221647-bc128280-2310-11ea-910a-aab6613a4d13.JPG)


run 실행 후 이미지에서 파티션 목록 출력

list-filesystems

![16](https://user-images.githubusercontent.com/49422777/71221649-be74dc80-2310-11ea-918a-db4049057761.JPG)


* 메인파티션을 / 에 마운트
mount [메인파티션 경로] /
* 마운트 된 파티션으로 tar 형식 파일 만들기(시간 오래 걸림)
tar-out / [파일이름 지정]

![01-1](https://user-images.githubusercontent.com/49422777/71223212-8cff0f80-2316-11ea-93b7-775c3e0ec289.JPG)


* 완료 후 exit로 guestfish 종료

![02-1](https://user-images.githubusercontent.com/49422777/71223218-8ffa0000-2316-11ea-8a20-ad287f592602.JPG)


* 도커를 이용해 tar파일을 도커이미지파일로 변환

docker import [tar파일] [도커이미지 이름]

도커이미지의 이름은 [계정명]/[운영체제이름]:[버전태그]로 지정

확인하기 위해 저장되어 있는 도커이미지 파일 확인

docker images

![05-1](https://user-images.githubusercontent.com/49422777/71223219-925c5a00-2316-11ea-89bb-48bdae5f8b5e.JPG)


* 도커허브에 도커이미지를 올리기 위해 로그인

docker login - 도커허브 id와 password 입력

![20](https://user-images.githubusercontent.com/49422777/71244478-f2bebc00-2355-11ea-9ed7-25b8970c2df7.JPG)


* 도커허브에 도커 이미지 저장하기

docker push [도커이미지이름]
![06](https://user-images.githubusercontent.com/49422777/71223222-94261d80-2316-11ea-848f-915140053ba3.JPG)


* 도커허브에 올린 도커이미지파일 저장

docker pull [저장할 도커이미지파일 이름]
![23](https://user-images.githubusercontent.com/49422777/71245727-b04aae80-2358-11ea-870a-886868c9794a.JPG)


* 도커이미지 이용해 컨테이너 생성

docker run -it -p[호스트쪽 포트번호:컨테이너쪽 포트번호] [컨테이너 생성에 사용할 도커이미지파일 이름]

-p 옵션으로 외부에서 컨테이너에 접속시 포트번호가 필요하므로 컨테이너 생성시 포트번호 지정

vnc는 5901 포트부터 시작하므로 컨테이너 쪽은 5901, 5902 포트 지정, 호스트 쪽은 임의 포트번호 지정

![24](https://user-images.githubusercontent.com/49422777/71245743-b6d92600-2358-11ea-909c-f6776da4962e.JPG)

* 컨테이너에 접속 후 vnc사용을 위해 vnc4server 설치

(참고사이트 : https://web-programming-info.tistory.com/26
	      https://idchowto.com/?p=46149 )

apt-get install vnc4server

![25](https://user-images.githubusercontent.com/49422777/71270748-b1e69780-2395-11ea-8179-6b4eb79e5c05.JPG)


* vnc4server를 실행해 접속 시 사용할 패스워드 설정

![26](https://user-images.githubusercontent.com/49422777/71270739-ab582000-2395-11ea-87c8-1f61f37f2b33.JPG)


* vnc를 종료시키고 설정을 위해 ~/.vnc로 이동 후 xstartup 파일 편집

vnc4server -kill :1

cd ~/.vnc

vi xstartup

![27](https://user-images.githubusercontent.com/49422777/71270775-c2970d80-2395-11ea-8ba7-6c2e39fceb4e.JPG)


# -------------------------------------------------------------------------------------------------------------------------

## (여기서부터는 수정 필요)

* xstartup파일 수정 및 저장
![28](https://user-images.githubusercontent.com/49422777/71270814-d6db0a80-2395-11ea-89bb-ce16c7ae824d.JPG)



![29](https://user-images.githubusercontent.com/49422777/71270842-e0647280-2395-11ea-86de-0a43b61b5cd2.JPG)


* vnc사용 위해 vnc실행

![31](https://user-images.githubusercontent.com/49422777/71270851-e78b8080-2395-11ea-83db-21652977f659.JPG)


* 컨테이너 생성시 호스트의 10000번 포트는 컨테이너의 5901, 호스트의 10001번 포트는 컨테이너의 5902
포트로 연결되게 설정하였음

* 현재 호스트에서 도커 컨테이너로 접근 시 192.168.99.100 ip로 접근해야 함

* 현재 vnc 실행 시 1번 디스플레이가 시작됨 -> vnc는 5901부터 시작하므로 10000번포트를 이용해 접속

![30](https://user-images.githubusercontent.com/49422777/71270855-ea867100-2395-11ea-9029-f3d60b3691b3.JPG)


* 호스트에서 vnc뷰어 프로그램(사진은 크롬 확장프로그램중 VNC Viewer for google chrome)을 실행
* 접속하고자 하는 컨테이너의 ip와 포트번호 지정 후 연결

![32](https://user-images.githubusercontent.com/49422777/71277931-89609c80-2399-11ea-8743-3a845d24dfca.JPG)


![33](https://user-images.githubusercontent.com/49422777/71277934-8bc2f680-2399-11ea-8144-17c65043d901.JPG)


* vnc4server 설치시 지정했던 패스워드 입력

![34](https://user-images.githubusercontent.com/49422777/71277940-8e255080-2399-11ea-9a39-68ddc3e02842.JPG)


* vnc로 접속된 모습

![35](https://user-images.githubusercontent.com/49422777/71277946-91204100-2399-11ea-8c28-eeba648ebe12.JPG)
