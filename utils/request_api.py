import requests
import json

def request_get_fully_url(url):
    '''
    http://url?key=value&key2=value2
    url = 'http://url?key=value&key2=value2'
    '''
    response = requests.get(url)
    return response.status_code

def request_get_prams(url, param):
    '''
    http://url?key=value&key2=value2
    url = http://url
    param = {'key':'value', 'key2':'value2'}  ## dictionary
    or
    param = ((key, value), (key2, value2))    ## tuple
    '''
    response = requests.get(url=url, params=param)
    return response.status_code

def request_post_json(url, json_temp):
    '''
    url = http://url
    json_temp = {'key':'value', 'key2':['value2', 'value3']}
    '''
    headers = {'Content-Type':'application/json; charset=utf-8'}
    response = requests.post(url, data = json.dumps(json_temp), headers= headers)
    return response.status_code