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
![5드론_시스템구성도](https://user-images.githubusercontent.com/49422777/69651242-1ffbaf80-10b3-11ea-8438-0401d642b9a2.jpg)

# 3. Tech/Framework
     * Installation bundle : VMWare, TightVNC, Silent Intall Builder, NSIS   
     * Server : Vultr, Cent OS   
     * DB : Maria DB  
     * GUI : python PyQt  
     * Docker : Docker Toolbox  
     * Docker Image : Kali Linux, Ubuntu, Bee, CentOS, metasploit, VyOS   
     
# 4. Contributors
* 김종우, 민준영, 윤영기, 이영진, 최민철
