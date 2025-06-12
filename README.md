# 🛡️ KimTrace Project

## 🎯 프로젝트 개요

**KimTrace**는 AI 모델이 추론한 결과의 신뢰성을 확보하기 위해,  
결과 해시값을 생성하고 이를 **블록체인에 저장**해 투명하고 검증 가능한 시스템을 구축하는 프로젝트입니다.

---

## 🧠 핵심 아이디어

- AI 모델 결과 → 해시 처리  
- 해시 → 스마트컨트랙트를 통해 블록체인(Sepolia Testnet)에 저장  
- 이후 사용자 또는 개발자가 해당 결과를 조회하고 검증 가능  

---

## 🏗️ 기술 아키텍처

```plaintext
[ User ]
   ↓
[ FastAPI 서버 ]
   ↓
[ 해시 처리 (SHA256 등) ]
   ↓
[ Web3.py → 스마트컨트랙트 ]
   ↓
[ Sepolia Testnet (Ethereum 기반 블록체인) ]

---

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

## 🧪 6월 12일 기준 테스트 결과

- `/send` API를 2회 호출해 서로 다른 해시값 전송  
- `/count` API 결과: `"count": 2` 정상 반환  
- `/get/0`, `/get/1` API로 저장된 해시값 정확히 조회됨

---

## 📌 다음 목표

- `exists` API로 중복 해시 여부 확인 기능 추가
- `msg.sender`, timestamp 저장 추가 (Solidity 개선)
- 프론트엔드 연동 (React, Next.js 등) 고려

---

## 🙌 개발자

- 👤 Jaehyun Kim (김재현)  
- 🎓 Konkuk Univ. / Virginia Tech (Spring 2025 Exchange)  
- 🌐 Blockchain & AI Researcher  
