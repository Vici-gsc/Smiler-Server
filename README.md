# Smiler-Server
”사회적 상호작용 장애 치료”를 위한 표정 연습 애플리케이션 

## Getting started

1. Install python 3.7+ and FastAPI
2. Clone this repository.

```
git clone https://github.com/Vici-gsc/Smiler-Server.git
```

3. Run FastAPI Server

```
python3 -m uvicorn main:app --reload
```

## How to Test
We wrote test code to verify that it works well against the server API. Here's how to run the test code.  

1. Run FastAPI Server  
2. Open another terminal and move to tests/ directory  
3. Install required python package using requirements.txt
3. Run test_main.py  
```
pytest test_main.py
```