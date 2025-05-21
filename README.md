# KimTrace
A blockchain-integrated MLOps project to ensure trust and integrity in AI training and inference processes. Developed during LG Business School’s MLOps field training.


# KimTrace: 블록체인 기반 AI 신뢰성 검증 플랫폼

## 📌 프로젝트 개요
AI 모델의 학습/추론 과정을 블록체인에 기록하여 신뢰성과 투명성을 확보하는 시스템입니다.

## 🧠 해결하고자 하는 문제
- AI의 판단 과정을 검증할 수 없다
- 학습/추론 이력이 위변조될 수 있다

## 💡 핵심 기능
- 데이터 및 결과 해시 생성 및 블록체인 저장
- 모델 학습 로그 검증
- 결과 추론 무결성 검증

## 🏗️ 기술 스택
- Python, MLflow, Docker, IPFS, Solidity, FastAPI

## 📜 프로젝트 진행 일정
- 1주차: 문제 정의 및 아이디어 정리
- 2주차: 시스템 구조 설계 …

## 📎 관련 링크
- 📘 블로그 연재: [네이버 블로그 시리즈 보기] https://blog.naver.com/passiontom/223873516803


📦 개발 환경 설정
이 프로젝트는 Python 기반 FastAPI + MLflow + Solidity Smart Contract + IPFS 구조로 구성되어 있으며, 다음과 같은 개발 환경에서 동작합니다.

✅ 시스템 요구사항
Python 3.10 이상

Ganache 또는 Sepolia 테스트넷

npm / Node.js (IPFS 및 Solidity 도구용)

Git (버전 관리용)


🧪 개발 환경 세팅
# 1. Python 가상환경 생성
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 2. 의존성 설치
pip install -r requirements.txt
⚠️ requirements.txt에는 FastAPI, scikit-learn, MLflow, web3, IPFS client 등이 포함되어 있습니다.

🚀 로컬 실행 방법
# FastAPI 서버 실행
uvicorn app.main:app --reload

# MLflow UI 실행 (기록 확인용)
mlflow ui
FastAPI: http://127.0.0.1:8000

MLflow UI: http://127.0.0.1:5000

🔗 블록체인 환경 설정
# Ganache CLI 실행 (로컬 테스트넷)
ganache
Solidity 스마트 컨트랙트는 /blockchain/contract.sol에 작성되어 있으며, web3.py를 통해 연동됩니다.

📂 프로젝트 디렉토리 구조 (요약)
KimTrace/
├── app/              # FastAPI 서버
├── model/            # ML 모델 학습/추론
├── blockchain/       # 스마트컨트랙트
├── ui/               # Streamlit or Flask UI
├── mlflow/           # 실험 관리 설정
├── .github/workflows # CI/CD 설정
├── requirements.txt
└── README.md

