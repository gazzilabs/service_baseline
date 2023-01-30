- 작성 : 정소현 (@AI응용기술연구팀)
------
1) 가상환경 사용을 권장합니다.
``` bash
python -m venv venv

# 가상환경 실행
# --- win
.\venv\Scripts\activate
# --- ubuntu
source ./venv/bin/activate
```
2) 패키지 설치
``` bash
pip install -r requirements.txt
```
or
``` bash
pip install pika celery flask
```
------------------------
1) config/config.json 수정
    ``` json
    {
        "rabbitmq":{ 
            ... # 접근 정보 문의 : 정소현 (@AI응용기술연구팀)
        },
        "service":{
            "name":"test_service", # Service Name
            "queue":"test_service" # Queue Name
        }
    }
    ```
2) MQ 추가
    1) RabbitMQ 점근 정보 : 정소현 (@AI응용기술연구팀) 문의
    2) Queues > Add a new queue > Queue Name 입력
    3) Add queue
    4) 해당 queue 선택
    5) Bindings > Add binding to this queue
        > From exhange : amq.topic
        > Routing key : 해당 queue 이름
    6) Bind
3) 코드 실행
``` bash
# Flask Server
python flask_server.py

# MQ 
python run_module.py

# Celery 실행
# --- win
celery -A set_worker worker --loglevel=info --pool=solo
# --- ubuntu (ubuntu 환경 권장)
celery -A set_worker worker --loglevel=info --autoscale=10,3
```
4) URL
http://127.0.0.1:31000
POST)
```json
{"test":"json"}
```