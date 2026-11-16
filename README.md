# 캡스톤디자인 눈맞춤

## 📌 프로젝트 개요
### 시각장애인을 위한 실시간 카메라 분석 및 음성 안내 앱
시각장애인 사용자가 대화 상대의 표정과 주변 상황을 파악하기 어려운 문제를 해결하기 위해, 스마트폰 카메라로 촬영한 영상을 서버에서 분석하고 그 결과를 음성으로 안내하는 Flutter 기반 모바일 앱을 구현하였습니다.<br>
대화 상대의 나이대, 성별, 표정(행복, 놀람, 무표정, 혐오, 분노, 슬픔) 정보를 실시간 음성 피드백으로 제공하여 사회적 상호작용을 돕고, 화면 낭독과 음성 안내 중심의 접근성 UI를 설계하였습니다.<br>
주요 기능은 대화 모드, 이동 모드, 실시간 음성 안내, 보호자 모드의 접근성 설정(진동, 명도, 버튼 크기, 폰트), FAQ 등이 있습니다.
<hr>

## 👨🏻‍💻 팀 구성 및 역할 분담
#### 정원준: Front-end


## 🛠️ 기술 스택
#### Mobile

<img src="https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white"/> <img src="https://img.shields.io/badge/Dart-0175C2?style=for-the-badge&logo=dart&logoColor=white"/> <img src="https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white"/> <img src="https://img.shields.io/badge/iOS-000000?style=for-the-badge&logo=apple&logoColor=white"/><br>


#### Communication

<img src="https://img.shields.io/badge/WebSocket-010101?style=for-the-badge&logo=socketdotio&logoColor=white"/> <img src="https://img.shields.io/badge/REST_API-005571?style=for-the-badge&logoColor=white"/><br>


#### Accessibility

<img src="https://img.shields.io/badge/Flutter_TTS-02569B?style=for-the-badge&logo=flutter&logoColor=white"/> <img src="https://img.shields.io/badge/Semantics-02569B?style=for-the-badge&logo=flutter&logoColor=white"/><br>

<hr>

## Event Flow Diagram
![Event Flow Diagram]([이미지 URL])

## ERD Diagram
![ERD]([이미지 URL])


<hr>

## 🖥️ 주요 기능

### 로딩 화면 <br>

![로딩 화면]([이미지 URL])<br>
- 앱 실행 시 "눈맞춤" 로고 화면 표시
- 3초 후 메인 화면으로 자동 전환
<br>

### 대화 모드 <br>

![대화 모드 화면]([이미지 URL])<br>
- 대화 상대의 표정 확인을 위한 카메라 촬영 시작 및 종료 기능
- 촬영 프레임을 JPEG로 변환 및 압축 후 WebSocket으로 서버 전송
- 3초 주기로 분석 결과를 받아 나이대, 성별, 표정 정보 음성 안내
- 촬영 중 표시 및 분석 결과 텍스트 화면 출력
<br>

### 이동 모드 <br>

![이동 모드 화면]([이미지 URL])<br>
- 안전한 이동을 위한 카메라 촬영 시작 및 종료 기능
- 이동 모드 전용 API를 통한 분석 결과 수신
- 분석 결과의 음성 안내 및 화면 출력
<br>

### 음성 안내 및 접근성 <br>

![음성 안내 화면]([이미지 URL])<br>
- 모든 버튼과 화면 요소의 Semantics 라벨을 통한 화면 낭독 지원
- 버튼 탭 시 기능 설명 음성 안내
- 카메라 화면 탭 시 안내 음성 재생
- 사용자 모드와 보호자 모드 전환 버튼
<br>

### 보호자 모드 <br>

![보호자 모드 화면]([이미지 URL])<br>
- 진동 설정 ON/OFF 기능
- 명도 설정을 통한 밝은 모드와 어두운 모드 전환 기능
- 버튼 크기 늘이기 및 줄이기 기능
- 폰트 크기 설정 기능
- 설정값 저장 및 사용자 화면 반영
<br>

![폰트 설정 화면]([이미지 URL])<br>
- 기본, 선명체, 고딕체 등 7종 폰트 선택 기능
- 폰트별 샘플 미리보기
- 선택한 폰트 음성 안내
<br>

### FAQ <br>

![FAQ 화면]([이미지 URL])<br>
- 앱 기능, 작동 방식, 인식 가능한 표정 등 자주 묻는 질문 확인
- 질문 탭 시 질문과 답변 음성 안내
- 문의 메일 보내기 버튼
<br>
