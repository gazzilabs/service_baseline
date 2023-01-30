## celery -A set_worker worker --loglevel=info --autoscale=10,3     -> 리눅스
## celery -A set_worker worker --loglevel=info --pool=solo          -> 윈도우
import json
from celery import Celery
from kombu import Queue
from time import sleep

from utils.management_config import CONF_DATA

from work_func import work

app = Celery(CONF_DATA.service_name, broker=CONF_DATA.rabbitmq_url)
app.conf.task_queues = (Queue(CONF_DATA.celery_queue_name),)

# 작업할당이 들어왔을 때 문자열 출력 -> 5초 딜레이 -> 종료 문자열 출력 하는 예제입니다.
@app.task(bind=True)
def test_module_1(self, str_body):
    '''
    str_body : body(json) = dict 구조
    '''
    
    # 동작 예시. 이곳에 바로 코드를 작성하거나 함수로 묶어 동작하게 하여도 됩니다.
    # 함수로 묶어 동작하도록 하면 디버깅이 편합니다.
    print(f'start')
    work(str_body)
    sleep(3)
    print('done')