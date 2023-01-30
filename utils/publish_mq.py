import json
from pika import BlockingConnection,ConnectionParameters,BasicProperties

from utils.management_config import CONF_DATA
from urllib import parse

def send_post_status(callback_url:str, send_data:dict):
    connection = BlockingConnection(ConnectionParameters(host=CONF_DATA.addr_ip, blocked_connection_timeout=120, connection_attempts=5))
    if callback_url.find('http://') == -1:
        callback_url = 'http://'+ callback_url

    send_json = {'method':'POST', 'callback_url':callback_url, 'data':send_data}
    try:
        channel = connection.channel()
        channel.basic_publish(exchange='amq.topic', routing_key='SendRequest', body=json.dumps(send_json,indent="\t", ensure_ascii = False), properties=(BasicProperties(content_type='application/json', delivery_mode=2)))
    finally:
        connection.close()