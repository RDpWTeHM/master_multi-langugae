# baidu.py
"""
"""

import sys
import hashlib
import random

import urllib
import requests
from requests.exceptions import ConnectionError
# from requests.exceptions import ConnectTimeout

import json


# configuration #####################
import conf.apiauth
CONF = conf.apiauth.baiduauth


def gen_rest_url(q, fromlang, tolang):
    api_path = '/api/trans/vip/translate'

    salt = random.randint(32768, 65536)
    plain_sign = CONF.app_id + q + str(salt) + CONF.key

    m1 = hashlib.md5()
    m1.update(plain_sign.encode('utf-8'))  # check develop document.
    encode_hex_sign = m1.hexdigest()

    return "http://api.fanyi.baidu.com" + api_path + \
        '?appid=' + CONF.app_id + \
        '&q=' + urllib.parse.quote(q) + \
        '&from=' + fromlang + '&to=' + tolang + \
        '&salt=' + str(salt) + '&sign=' + encode_hex_sign


def fanyi(word):
    url = gen_rest_url(word, 'en', 'zh')
    try:
        r = requests.get(url, timeout=3)
        r.raise_for_status()
        r.encoding = r.apparent_encoding

    except ConnectionError:
        raise
    except Exception:
        raise
    else:
        return json.loads(r.text)


def enwrite(hans):
    url = gen_rest_url(hans, 'zh', 'en')
    try:
        r = requests.get(url, timeout=3)
        r.raise_for_status()
        r.encoding = r.apparent_encoding

    except ConnectionError:
        raise
    except Exception:
        raise
    else:
        return json.loads(r.text)
