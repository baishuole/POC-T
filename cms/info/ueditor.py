#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from plugin.util import urlhandler, siteIndexTest
from lib.core.settings import HEADERS, TIMEOUT, VERIFY
from data.info_dict import UEDITOR_DICT, UEDITOR_KEYWORD

requests.packages.urllib3.disable_warnings()


def poc(url):
    testurl = urlhandler(url)

    if not siteIndexTest(testurl):
        return '[SiteRequestErr-UEditor] %s' % testurl

    result = []

    for path in UEDITOR_DICT:
        try:
            payload = testurl + path.strip()
            r = requests.get(payload, headers=HEADERS, timeout=TIMEOUT, verify=VERIFY)
            if r.status_code == 200 and UEDITOR_KEYWORD in r.content:
                    result.append("[UEditor] " + r.url)
        except Exception,e:
            pass

    if result:
        return result
    else:
        return False


if __name__ == '__main__':
    print poc('http://www.******.cn')