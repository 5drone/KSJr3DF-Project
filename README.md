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

*우분투에 도커 설치하기(참고사이트 : https://kururu.tistory.com/87)

![4](https://user-images.githubusercontent.com/49422777/71220835-6f797800-230d-11ea-95aa-1d0d4aa34cca.JPG)

![5](https://user-images.githubusercontent.com/49422777/71220841-72746880-230d-11ea-9a7c-2c3bd9e94537.JPG)

![6](https://user-images.githubusercontent.com/49422777/71220845-7607ef80-230d-11ea-8101-3ee313216843.JPG)

![7](https://user-images.githubusercontent.com/49422777/71220850-799b7680-230d-11ea-841c-82c0f3bb4095.JPG)

![8](https://user-images.githubusercontent.com/49422777/71220856-7ef8c100-230d-11ea-9780-7769f38f1a8b.JPG)

![9](https://user-images.githubusercontent.com/49422777/71220862-828c4800-230d-11ea-8526-57fee7e2bef5.JPG)

![10](https://user-images.githubusercontent.com/49422777/71220867-861fcf00-230d-11ea-8515-c18541609489.JPG)

![11](https://user-images.githubusercontent.com/49422777/71220869-891abf80-230d-11ea-8c88-5994685289f4.JPG)

![12](https://user-images.githubusercontent.com/49422777/71220875-8ddf7380-230d-11ea-9f9d-20bef5c39062.JPG)

*vmdk파일을 도커 이미지로 변환 
(참고사이트 : https://blog.inslash.com/how-to-convert-vmdk-to-a-docker-image-be939745ed8a
             https://medium.com/@roberto.fernandez.perez/create-docker-base-image-for-legacy-linux-system-3f5f77acd740 )

![13](https://user-images.githubusercontent.com/49422777/71221638-b4eb7480-2310-11ea-9f98-3bdad829f5b3.JPG)

![14](https://user-images.githubusercontent.com/49422777/71221644-b9179200-2310-11ea-92d8-3489390c3715.JPG)

![15](https://user-images.githubusercontent.com/49422777/71221647-bc128280-2310-11ea-910a-aab6613a4d13.JPG)

![16](https://user-images.githubusercontent.com/49422777/71221649-be74dc80-2310-11ea-918a-db4049057761.JPG)

![01-1](https://user-images.githubusercontent.com/49422777/71223212-8cff0f80-2316-11ea-93b7-775c3e0ec289.JPG)

![02-1](https://user-images.githubusercontent.com/49422777/71223218-8ffa0000-2316-11ea-8a20-ad287f592602.JPG)

![05-1](https://user-images.githubusercontent.com/49422777/71223219-925c5a00-2316-11ea-89bb-48bdae5f8b5e.JPG)

![20](https://user-images.githubusercontent.com/49422777/71244478-f2bebc00-2355-11ea-9ed7-25b8970c2df7.JPG)

![06](https://user-images.githubusercontent.com/49422777/71223222-94261d80-2316-11ea-848f-915140053ba3.JPG)

![23](https://user-images.githubusercontent.com/49422777/71245727-b04aae80-2358-11ea-870a-886868c9794a.JPG)

![24](https://user-images.githubusercontent.com/49422777/71245743-b6d92600-2358-11ea-909c-f6776da4962e.JPG)
