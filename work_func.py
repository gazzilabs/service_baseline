from utils.request_api import request_post_json

# 함수로 동작 예시입니다.
def work(body_data:dict):
    print(f'func work : {body_data}')
    
    # post send 예시
    # request_post_json('http://127.0.0.1:11011', body_data)
    return

# 아래와 같이 바로 디버깅할 수 있어 편합니다.
# body_sample = {'id':'gazzi', 'item':['1', '2', '3']}
# work(body_sample)