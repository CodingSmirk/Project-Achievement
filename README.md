# Project-Achievement

***

## ① PUF 기반 보안을 지원하는 다중 드론 임무 가변형 FANET 통신모듈 개발
### 1. 프로젝트 개요
- 종류 : 민군과제
- 기간 : 2021년 3월 ~ 2025년 7월 (약 4년 5개월)
- 역할(기여도) : 주 개발자(90%)

### 2. 사용 기술
- C
- Riverbed Modeler(구 Opnet Network Simulator)
- MATLAB

### 3. Riverbed Modeler 설계
<kbd>
  <img src="https://github.com/CodingSmirk/Project-Achievement/blob/b7610d152b660cee0c16ac19801fefff983cbe9d/Image/Riverbed%20Modeler%20Modeling.png"/>
</kbd>

### 4. 담당 역할
- Riverbed 네트워크 시뮬레이터(구 OPNET) 기반 SLS(NLS) 시뮬레이터 상세 설계 및 제작
- 임무 가변형 다중 드론 FANET 통신 프로토콜 스택의 성능 검증 및 분석을 위한 Riverbed 네트워크 시뮬레이터(구 OPNET) LLS/SLS(NLS) 통합 시뮬레이터 제작
- Riverbed 네트워크 시뮬레이터(구 OPNET) 기반 LLS/SLS(NLS) 통합 시뮬레이터 안정화
- MATLAB 기반 충돌 방지를 위한 간단한 편대 비행 알고리즘 개발 및 검증

### 5. 프로젝트 결과물
- 상세 코드는 프로젝트 보안 특성에 따라 생략하며, 시스템의 기본 통신 구조와 로직은 첨부된 Riverbed Modeler 설계도로 확인 가능

### 6. 결과물 예시
<kbd>
  <img src="https://github.com/CodingSmirk/Project-Achievement/blob/0d727f694f6ce106e7e57591849bd062bbfd21d8/Image/Riverbed%20Modeler%201.png"/>
</kbd>
<kbd>
  <img src="https://github.com/CodingSmirk/Project-Achievement/blob/0d727f694f6ce106e7e57591849bd062bbfd21d8/Image/Riverbed%20Modeler%202.png"/>
</kbd>
<kbd>
  <img src="https://github.com/CodingSmirk/Project-Achievement/blob/0d727f694f6ce106e7e57591849bd062bbfd21d8/Image/Riverbed%20Modeler%203.png"/>
</kbd>
<kbd>
  <img src="https://github.com/CodingSmirk/Project-Achievement/blob/0d727f694f6ce106e7e57591849bd062bbfd21d8/Image/MATLAB.png"/>
</kbd>

***

## ② 악조건에서의 5G-NR 기반 V2X 서비스 통신성능 검증 모듈
### 1. 프로젝트 개요
- 종류 : 연구실 용역 과제
- 기간 : 2023년 2월 ~ 2024년 2월 (약 1년 1개월)
- 역할(기여도) : 주 개발자(40%)

### 2. 사용 기술
- Python
- Socket (데이터 전송)
- Numpy (영상 데이터 Slicing & Joining)
- OpenCV (영상 데이터 수집 및 시각화)
- Matplotlib (성능 시각화(그래프))
- PyQt5 (성능 검증용 소프트웨어 GUI화)

### 3. 성능 검증용 소프트웨어 구조
<kbd>
  <img src="https://github.com/CodingSmirk/Project-Achievement/blob/96ed5809669b234d8a8fae7e61dbf487b149624b/Image/SW%20Structure.png"/>
</kbd>

### 4. 담당 역할
- 5G-NR 기반 V2X 통신 장비 간 데이터 통신 프로토콜 구현 및 검증
- 통신 장비 성능(Packer Delivery Rate, Throughput) 검증 알고리즘 구현 및 검증
- 영상 데이터 전송 기능 구현 및 검증
- Log 표시 및 저장 기능 개발
- 성능 검증용 소프트웨어 GUI화
- 로그 데이터를 활용한 도로 상황의 직관적인 GUI 시각화

### 5. 프로젝트 결과물(5G-NR V2X Communication System Performance Verification Software 폴더)
- packet_header_struct.py # 5G-NR 기반 통신 장비용 패킷 헤더 구조체 정의
- select_window.py # 송수신(Sender/Receiver) 역할 선택 인터페이스
- sender_window.py # 송신자용 모니터링 GUI 및 데이터 전송,처리 백엔드 모듈
- receiver_window.py # 수신자용 모니터링 GUI 및 데이터 전송, 처리 백엔드 모듈
- GPS_log_visualization.py # 위치 데이터(GPS) 기반 통신 성능 맵핑 및 시각화 .html 산출 모듈
- resource 폴더 내 파일들 # GUI 구성을 위한 시각적 에셋 및 네비게이션 리소스

### 6. 결과물 예시
<kbd>
  <img src="https://github.com/CodingSmirk/Project-Achievement/blob/d0dc052516b384eab7e10056e4a5077f318686ef/Image/Software%20%26%20Hardware.png"/>
</kbd>
<kbd>
  <img src="https://github.com/CodingSmirk/Project-Achievement/blob/5159343cb1a141e1baa918768215fc7ce3af7068/Image/GPS_log_visualization_result.png"/>
</kbd>
