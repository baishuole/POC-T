# -*- coding: utf-8 -*-
import requests
from lib.core.settings import HEADERS, TIMEOUT, VERIFY
from data.info_dict import PHPMYADMIN_KEYWORD, PHPMYADMIN_DICT
from plugin.util import urlhandler, siteIndexTest

requests.packages.urllib3.disable_warnings()


def poc(url):
    testurl = urlhandler(url)
    if not siteIndexTest(testurl):
        return  # '[SiteRequestErr-phpMyAdmin] %s' % testurl

    result = []

    for d in PHPMYADMIN_DICT:
        payload = testurl + d
        try:
            r = requests.get(payload, headers=HEADERS, timeout=TIMEOUT,
                             verify=VERIFY)
            if r.status_code == 200 and PHPMYADMIN_KEYWORD in r.content:
                    result.append('[phpMyAdmin] %s' % payload)
        except Exception:
            pass

    if result:
        return result