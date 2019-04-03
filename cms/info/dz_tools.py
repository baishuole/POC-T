# -*- coding: utf-8 -*-
import requests
from plugin.util import urlhandler, siteIndexTest
from lib.core.settings import HEADERS, TIMEOUT, VERIFY
from data.info_dict import DZ_TOOLS_DICT, DZ_TOOLS_KEYWORD

requests.packages.urllib3.disable_warnings()


def poc(url):
    testurl = urlhandler(url)
    if not siteIndexTest(testurl):
        return '[SiteRequestErr-Dz_tools] %s' % testurl

    result = []

    for v in DZ_TOOLS_DICT:
        payload = testurl + v
        try:
            r = requests.get(payload, headers=HEADERS, timeout=TIMEOUT,
                             verify=VERIFY)
            if r.status_code == 200 and DZ_TOOLS_KEYWORD in r.content:
                result.append('[dz_tools] %s' % payload)
        except Exception:
            pass

    if result:
        return result