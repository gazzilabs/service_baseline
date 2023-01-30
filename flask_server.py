'''
flask server
'''
from flask import Flask, request
from pika import BlockingConnection,ConnectionParameters,BasicProperties

import json

from utils.management_config import CONF_DATA

app = Flask(__name__)

# 라우팅 경로 설정 및 요청이 올 때 실행할 함수 작성
@app.route('/Test/MQ',methods=["POST"])
def mq_publish_test(): # 
    post_json = json.loads(request.get_data())
    conn = BlockingConnection(ConnectionParameters(CONF_DATA.addr_ip, blocked_connection_timeout=120, connection_attempts=5))
    try:
        ch = conn.channel()
        ch.basic_publish(   
                            exchange='amq.topic', 
                            routing_key=CONF_DATA.service_name, 
                            body=request.get_data(post_json), 
                            properties=(BasicProperties(content_type='application/json', delivery_mode=2))
                        )
    except Exception as e:
        print(f'ERR :: {e}')
    finally:
        conn.close()
    return 'done'

# 해당 포트로 서버 구동
app.run(host="0.0.0.0",port=31000) # port 변경 필요