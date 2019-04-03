# -*- coding: utf-8 -*-
import requests
from plugin.util import urlhandler
from lib.core.settings import HEADERS, TIMEOUT, VERIFY, RETRY_CNT
from data.info_dict import GIT_KEYWORD

requests.packages.urllib3.disable_warnings()

def poc(url):
    testurl = urlhandler(url)
    payload = testurl + ".git/config"

    try_cnt = 0
    while True:
        try:
            r = requests.get(payload, headers=HEADERS, timeout=TIMEOUT,
                             verify=VERIFY)
            if GIT_KEYWORD in r.content:
                return '[Git_Leak] %s' % payload
            break
        except Exception:
            if try_cnt >= RETRY_CNT:
                return '[RequestErr-Git_Leak] %s' % payload
