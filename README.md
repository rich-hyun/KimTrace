# 🛡️ KimTrace Project

## 🎯 프로젝트 개요

**KimTrace**는 AI 모델이 추론한 결과의 신뢰성을 확보하기 위해,  
결과 해시값을 생성하고 이를 **블록체인에 저장**해 투명하고 검증 가능한 시스템을 구축하는 프로젝트입니다.

---

## 🧠 핵심 아이디어

- AI 모델 결과 → 해시 처리  
- 해시 → 스마트컨트랙트를 통해 블록체인(Sepolia Testnet)에 저장  
- 이후 사용자 또는 개발자가 해당 결과를 조회하고 검증 가능  



## 🏗️ 기술 아키텍처


[ User ]  
   ↓  
[ FastAPI 서버 ]  
   ↓  
[ 해시 처리 (SHA256 등) ]  
   ↓  
[ Web3.py → 스마트컨트랙트 ]  
   ↓  
[ Sepolia Testnet (Ethereum 기반 블록체인) ]  

<br>


## 📅 프로젝트 진행 일지

### ✅ 1주차: 문제 정의 및 구조 설계
- AI 결과의 신뢰성 부족 문제를 정의
- Modelchain, Aletheia 등 유사 프로젝트 분석
- `AI 결과 → 해시 생성 → 블록체인 기록` 흐름 구상

### ✅ 2주차: 기술 아키텍처 구성
- FastAPI 서버 구성 및 역할 분담
- Sepolia Testnet 사용 결정
- Web3.py와 연결 계획 수립

### ✅ 3주차: Remix에서 스마트컨트랙트 배포
- Solidity 기반 스마트컨트랙트 작성 및 Remix IDE에서 배포
- `storeHash(string memory)` 함수 구현
- Etherscan을 통해 실제 트랜잭션 기록 확인

### ✅ 4주차: FastAPI 서버 개발
- VSCode + 가상환경 구성
- `main.py`, `hash_router.py` 파일 작성
- Swagger UI로 API 테스트 환경 완성

---


## ✅ 주요 기능 (6/13 기준)

### 1. SHA256 해시 생성 API (`/hash`)
- 사용자가 입력한 데이터를 SHA256 해시로 변환하여 반환

### 2. 블록체인 전송 API (`/send`)
- 해시값을 스마트컨트랙트에 기록하고 트랜잭션 해시 반환

### 3. 트랜잭션 조회 API (`/tx/{index}`)
- 인덱스를 통해 스마트컨트랙트에 저장된 트랜잭션 해시와 Etherscan URL 조회

---

## 🧪 실험 결과

Swagger UI를 통해 다음 흐름으로 실험:
1. `/hash`로 해시 생성
2. `/send`로 스마트컨트랙트에 저장
3. `/tx/0`, `/tx/1` 등으로 트랜잭션 해시 확인  
✅ 실제로 Sepolia Etherscan 링크가 열리는 것까지 확인 완료

---

## 🔜 향후 계획

- `/count` API 고도화 및 예외 처리 추가  
- Swagger 문서 분류 정비 (tags/summary) 완료  
- 프론트엔드 연결 또는 Etherscan 결과 뷰어 시각화 준비  
- Github Actions 또는 Testnet 연동 자동화 탐색

---

## 🔧 사용 기술 스택

- Python 3.10  
- FastAPI  
- Web3.py  
- MetaMask + Infura (Sepolia)  
- Solidity + Remix IDE  
- Swagger UI (자동 문서화)

---

📌 현재까지 모든 기능은 Sepolia 테스트넷 상에서 실시간 검증 완료되었습니다.

## 🙌 개발자

- 👤 Jaehyun Kim (김재현)  
- 🎓 Konkuk Univ. / Virginia Tech (Spring 2025 Exchange)  
- 🌐 Blockchain & AI Researcher  
