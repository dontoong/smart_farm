# 환영합니다
전남인재평생교육원에서 주최한 2022 대학생 무한도전 프로젝트에서 최우수상을 수여받았습니다.<br/><br/>
스마트팜 모니터링 시스템 프로젝트 중 임배디드 프로그램 개발을 담당하였습니다.<br/><br/>
팀명 : 브로그래머's<br/><br/>
# 사업 목표
## 최종 목표
- 기업과 연계하여 스마트팜 모니터링 시스템을 개발함으로서 실질적인 기업의 개발 프로세스를 경험하고 이를 이용하여 직접 스마트팜의 제어 및 모니터링 제품을 개발<br/>
- OneM2M과 같은 IoT 국제표준을 이용한 산업에서 사용 가능한 시스템 개발을 통해 즉시 직무 수행이 가능한 기술의 습득<br/>
## 세부목표
- IoT표준을 따르는 소규모 스마트팜 시뮬레이터 제작
- 센서데이터 처리용 미들웨어 제작
- 원격 모니터링 및 제어 인터페이스 (WEB/APP) 개발
- 기업 스마트팜 실증시설을 이용한 시스템 실증

# 개발과제
## IoT 표준을 따르는 소규모 스마트팜 시뮬레이터 제작
### 실증을 위한 기업 소유의 데이터 수집 장치 기 확보
### 실증 전 사전에 개발과정에 필요한 소규모 시뮬레이터 제작
### 소규모 시뮬레이터 제작 -시스템 구축 과정에서 활용
(실증 환경과 같은 센서노드 구성) - 연계 기업과 협의를 통해 적용<br/>
   
![image](https://github.com/dontoong/smart_farm/assets/106039761/34625770-790c-49df-b1bc-d3cab5e6789b)

그림 [센서 노드 H/W 블록도] 예시

<br/><br/>

표 [센서 노드 설계 고려요소]

![image](https://github.com/dontoong/smart_farm/assets/106039761/cc573442-8fe3-47e4-89cd-ebe473fc3391)

## 센서 데이터 처리용 미들웨어 제작
### IoT 표준기술 (oneM2M) - 온실의 센싱 데이터 처리 및 전송을 위한 oneM2M Gateway Platform- 온실의 데이터 수집 및 관리를 위한 oneM2M Server Platform

![image](https://github.com/dontoong/smart_farm/assets/106039761/64cdca2d-7f54-43a9-9990-d47dde891423)

그림 [oneM2M 표준 규격]

<br/><br/>

### 미들웨어 구조
- 센서에서 수집된 데이터를 안정적으로 관리하고 오류데이터 및 센서의 오작동 검출<br/>
- 다량의 센싱 데이터를 안정적으로 처리할 수 있도록 최적화 알고리즘 선택<br/>
- 데이터베이스를 연동하여 센서에서 수집한 데이터를 저장하고 통합시스템과 연동<br/>
- MachBase 사용<br/>

![image](https://github.com/dontoong/smart_farm/assets/106039761/070a70ee-d394-4fdf-b777-02faada7ddc7)

그림 [미들웨어 구조]

<br/><br/>

### IoT 표준 oneM2M 기반 Gateway Platform 구축
- 시스템 설정 관리, 장애 관리, 로그 관리, Open API 사용 이력 관리기능 제작<br/>
- HTTP, CoAP, MQTT 프로토콜을 지원하며 서비스 계층 Core Protocol과의 Binding 기능<br/>
- 디바이스/어플리케이션/사용자 등록 요청 시 공통 플랫폼에서 인증키를 생성/발급/관리 기능<br/>
- HTTP, CoAP, MQTT 간 프로토콜 변환(Conversion) 기능 구축<br/>
- RFC7252의 CoAP-HTTP Proxy를 만족하는 CoAP과 HTTP간의 프로토콜 변환기<br/>
- 경량 프로토콜(CoAP, MQTT 등)과 비경량 프로토콜(HTTP, SOAP 등) 간의 통신을 위한 Proxy 구조 설계 구성요소 식별<br/>
- CoAP/MQTT 간 프로토콜 변환 기능<br/>
- MQTT-HTTP 간 프로토콜 변환을 위한 요구사항 도출/구조 설계 및 프로토콜 변환 기능<br/>

![image](https://github.com/dontoong/smart_farm/assets/106039761/4973bace-5826-4ed7-92a0-dd892187eba6)

그림 [Gateway 구성도]

<br/><br/>

### IoT 표준 oneM2M 기반 Server Platform 구축
- IoT 국제 표준인 oneM2M을 분석하여 디바이스로부터 전송되는 데이터를  수집할 수 있도록 제작<br/>
- 관리되는 모든 리소스는 RESTful API로 접근할 수 있도록 제작<br/>
- URI 형태를 준수<br/>
- Resource 맵핑 URI식별자 구성<br/>

![image](https://github.com/dontoong/smart_farm/assets/106039761/895562d3-835e-492d-a112-585a543f47e8)

그림 [Server 구성도]

<br/><br/>

## 원격 모니터링 및 제어 WEB/APP 개발
### 환경정보를 모니터링하고 적정 수치범위 초과시 원격제어 할 수 있는 시스템 개발
### 제어 대상 장비를 통합제어기를 통해 웹에서 시스템으로 제어하도록 구성
- 제어장비 적정수치 설정 및 변경관리<br/>
- 제어장비 운영정보 및 센서데이터 통합 조회<br/>

![image](https://github.com/dontoong/smart_farm/assets/106039761/bfda4fe4-a5e4-4247-a5a1-30308370a8de)

그림 [시스템 구성도]

<br/><br/>

- 천창, 스크린 : open/close 제어<br/>

![image](https://github.com/dontoong/smart_farm/assets/106039761/140d18aa-185b-4ae2-862d-158cadaae19b)

그림 [천창, 스크린 예시]

<br/><br/>

- 팬 : 공기순환 보조 제어<br/>

![image](https://github.com/dontoong/smart_farm/assets/106039761/51ab56cd-ceac-4d90-af3d-5fd2675f8615)

그림 [팬 예시]

<br/><br/>

- 스프링쿨러 : 습도조절 스프링쿨러 on/off<br/>

![image](https://github.com/dontoong/smart_farm/assets/106039761/1a3736f3-4515-46bd-ae13-95cc6483f8f2)

그림 [스프링쿨러 예시]

<br/><br/>

### 온실 통합제어기 간 RS485기반 Modbus 인터페이스 제작
       - 유리온실의 센서노드 및 구동기 노드, 온실 통합제어기 간 표준화된 방식의 프로토콜을 사용하여 서로 다른 장치 간 상호 연동이 가능하도록 제작<br/>
       - 반밀폐형 유리온실을 구성하는 각 구성 요소나 장치는 ID를 통해 식별되기 때문에 RS485 Modbus 방식으로 데이터 송수신을 위해서 address 사용<br/>

![image](https://github.com/dontoong/smart_farm/assets/106039761/1f14d6a5-031e-4dc0-b3fb-8189d72ed98c)

그림 [Modbus 인터페이스]

<br/><br/>

- 상호연동을 위해 기존에 사용하던 ID와 RS485 Modbus address간 매핑<br/>

<br/><br/>

표 [상호간 매핑 방법]

![image](https://github.com/dontoong/smart_farm/assets/106039761/108b2c41-0331-4869-8c8e-393b20b48362)

### 유리온실 통합관제시스템 구축
- 유리온실 설비 제어기능<br/>
- 유리온실 통계정보 조회<br/>
- 유리온실 데이터 관리기능 제작<br/>
- 각 센서 값에 대한 일별 평균치, 최고치, 최저치, 합을 계산<br/>

<br/><br/>

표 [모니터링 및 제어 항목]

![image](https://github.com/dontoong/smart_farm/assets/106039761/ca0db0ec-534c-46c1-b2aa-af1dfda89392)

<br/><br/>

### 유리온실 통합 관제시스템 UI 제작(WEB/APP)

![image](https://github.com/dontoong/smart_farm/assets/106039761/8df93d52-3967-43e5-b5f1-d74c550acc3e)

그림 [유리온실 통합관제시스템 화면 예시]

## 기업 스마트팜을 이용한 시스템 실증
### 연계 기업의 실증지를 방문하여 대규모의 스마트팜 환경에서 미리 구축한 개발환경을 이용하여 시스템이 실제로 데이터를 받아서 잘 작동하는지 확인
<br/><br/>
# 나의 개발 담당 [임베디드 프로그램 개발]
## 개발 환경
![image](https://github.com/dontoong/smart_farm/assets/106039761/10485a04-633e-4400-ba94-afd6cae231fa)

## 인터페이스 설계 및 구조
![image](https://github.com/dontoong/smart_farm/assets/106039761/96ce987c-13f3-470c-bf47-b36a06286a1f)

## UI 메인 화면(스마트팜 [일반] 화면)
![image](https://github.com/dontoong/smart_farm/assets/106039761/55bd0da6-cd59-475c-ae5b-e07f483c5689)

## 스마트팜 [제어] 화면
![image](https://github.com/dontoong/smart_farm/assets/106039761/1a6b6baf-8984-403f-821b-d11da0787d34)

## 스마트팜 [센서] 화면
![image](https://github.com/dontoong/smart_farm/assets/106039761/84a29c76-97b8-4db9-9caf-bf0c5f1fc8c1)

### 센서 모니터링 화면
![image](https://github.com/dontoong/smart_farm/assets/106039761/a00e26f9-ecae-4b5c-bacb-087811ba654a)


# 팀원들의 개발

## 게이트웨이 개발(프로젝트의 서버 구조)
![image](https://github.com/dontoong/smart_farm/assets/106039761/7e69a84f-95a1-475e-992d-bb982dcdf20d)

## 미들웨어 개발
![image](https://github.com/dontoong/smart_farm/assets/106039761/9cf48542-5f36-4836-8a2e-80b8b3f4b2a8)

## 애플리케이션 개발
![image](https://github.com/dontoong/smart_farm/assets/106039761/64f284f1-193d-4b49-b7cc-02ef9154c249)

## 웹 페이지 개발
![image](https://github.com/dontoong/smart_farm/assets/106039761/5b15319a-673d-4ef7-b65d-b9be06d92136)
![image](https://github.com/dontoong/smart_farm/assets/106039761/8d5a3122-60c8-4e19-a69d-22c218bbd84e)

# 프로젝트 실증
![image](https://github.com/dontoong/smart_farm/assets/106039761/130ff9ac-5080-4c3f-a653-a5ec91b35a38)
