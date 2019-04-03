# -*- coding: utf-8 -*-
import requests
from plugin.util import urlhandler
from lib.core.settings import HEADERS, TIMEOUT, VERIFY, RETRY_CNT
from data.info_dict import SVN_KEYWORD

requests.packages.urllib3.disable_warnings()

def poc(url):
    testurl = urlhandler(url)
    payload = testurl + ".svn/entries"

    try_cnt = 0
    while True:
        try:
            r = requests.get(payload, headers=HEADERS, timeout=TIMEOUT,
                             verify=VERIFY)
            if SVN_KEYWORD in r.content:
                return '[Svn_Leak] %s' % payload
            break
        except Exception, e:
            try_cnt += 1
            if try_cnt >= RETRY_CNT:
                return  # '[RequestErr-Svn_Leak] %s' % payload
