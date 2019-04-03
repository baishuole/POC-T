# -*- coding: utf-8 -*-
import requests
from lib.core.settings import HEADERS, TIMEOUT, VERIFY
from data.info_dict import JQUERY_DICT, JQUERY_KEYWORD
from plugin.util import urlhandler, siteIndexTest

requests.packages.urllib3.disable_warnings()


def poc(url):
    testurl = urlhandler(url)
    if not siteIndexTest(testurl):
        return  # '[SiteRequestErr-Jquery] %s' % testurl

    result = []

    for path in JQUERY_DICT:
        try:
            payload = testurl + path.strip()
            r = requests.get(payload, headers=HEADERS, timeout=TIMEOUT,
                             verify=VERIFY)
            if r.status_code == 200 and JQUERY_KEYWORD in r.content:
                    result.append("[jQuery] " + payload)
        except Exception,e:
            pass

    if result:
        return result



