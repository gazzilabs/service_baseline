import json
from os.path import exists, abspath

"""
외부에서 CONF_DATA 만 가져가면 설정 정보를 사용할 수 있다.
"""
CONF_DATA = None
CONF_PATH = abspath('./config/config.json')

class ServiceConfig:
    def __init__(self):
        """
        설정 정보를 담고있는 json (이하, config json) 존재를 확인하고, 필요한 변수를 생성한다.
        - conf_data       : config json 전체 구조 파싱 dict
        - rabbitmq_url    : rabbitmq 접근 url
        - addr_ip         : rabbitmq 접근 ip
        - service_name    : celery 에서 사용할 서비스 이름
        - queue_name      : 작업 할당 받을 queue 이름 (실행 전 반드시 rabbitmq에 설정 되어있어야한다.)
        """
        self.conf_json = self._get_config_data(CONF_PATH)

        self.rabbitmq_url = 'amqp://%s:%s@%s:%d%s'%(self.conf_json['rabbitmq']['id'],
                                                    self.conf_json['rabbitmq']['pw'],
                                                    self.conf_json['rabbitmq']['ip'],
                                                    self.conf_json['rabbitmq']['port'],
                                                    self.conf_json['rabbitmq']['vhost'])
        self.addr_ip = self.conf_json['rabbitmq']['ip']
        self.service_name = self.conf_json['service']['name']
        self.queue_name = self.conf_json['service']['queue']
        self.celery_queue_name = 'celery_%s'%self.queue_name
    
    def _get_config_data(self, conf_path:str):
        """
        config file이 있는지 확인하고, config data 를 전달
        """
        assert exists(conf_path), f'config file({conf_path}) does not exist.'
        with open(conf_path, 'r', encoding='utf-8') as conf_file:
            buf = conf_file.read()

        config_data = json.loads(buf)
        self._check_config_structure(config_data)

        return config_data

    def _check_config_structure(self,conf_data:dict):
        """
        설정 정보를 확인한다.
        """
        assert 'rabbitmq' in conf_data, 'config data [rabbitmq] does not exist'
        # 예외처리 추가 예정

CONF_DATA = ServiceConfig()