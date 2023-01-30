import json
from pika import BlockingConnection, ConnectionParameters

from utils.management_config import CONF_DATA
from set_worker import test_module_1

def on_message(channel, method_frame, header_frame, body):
    """
    - Message Queue 에서 작업 할당 받았을 때, 실행 코드.
    - body 에 전달 받을 데이터 존재
    """
    json_body = json.loads(body)            # Body(content type : application/json) 파싱
    print(json_body)
    test_module_1.apply_async(queue=CONF_DATA.celery_queue_name,args=(json_body,)) # Celery(-> worker) 실행
    channel.basic_ack(delivery_tag=method_frame.delivery_tag) # Ack 전달


if __name__ == '__main__':
    connection = BlockingConnection(ConnectionParameters(host=CONF_DATA.addr_ip))
    channel = connection.channel()
    channel.basic_consume(queue=CONF_DATA.queue_name, on_message_callback=on_message)
    print('start')
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()

    connection.close()