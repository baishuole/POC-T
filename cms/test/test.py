# -*- coding: utf-8 -*-
import requests
import re
import urlparse
import chardet
from plugin.util import urlhandler
from socket import gethostbyname
from lib.core.settings import HEADERS, TIMEOUT, VERIFY, RETRY_CNT, STREAM

requests.packages.urllib3.disable_warnings()

def poc(url):
    testurl = urlhandler(url)
    payload = testurl
    nodomain = urlparse.urlparse(payload).netloc
    ip_list = ''
    try:
        ip_list = gethostbyname(str(nodomain.strip()))
    except:
        pass

    try_cnt = 0
    while True:
        try:
            r = requests.get(payload, headers=HEADERS, timeout=TIMEOUT, verify=VERIFY,stream=STREAM)
            codesty = chardet.detect(r.content)
            repcontent = r.content.decode(codesty['encoding'])
            # print repcontent[:900]
            ok_status_code = [200,403,404,500,502]
            r_status_code = r.status_code
            if r_status_code is not '':
                if repcontent:
                    # header_list = []
                    # header_server = r.headers.get('Server')
                    # header_XPoweredBy = r.headers.get('X-Powered-By')
                    # if header_XPoweredBy is not None: header_list.append(header_XPoweredBy)
                    # if header_server is not None: header_list.append(header_server)
                    status_lst = []
                    url_title = re.search('<title>(.*)</title>', repcontent, re.I|re.S)

                    if url_title:
                        url_title = url_title.group(1).strip()[:30]

                    if not r.history:
                        status_lst.append(r_status_code)
                        # loginfo = "{:<20}  {:<10}  {:<26}  {:<20}  {}".format(ip_list, status_lst, url, url_title, header_list)
                        loginfo = "{:<20}  {:<10}  {:<26}  {}".format(ip_list, status_lst, url, url_title)
                    else:
                        for code in r.history:
                            status_lst.append(code.status_code)
                        status_lst.append(r.status_code)
                        # loginfo = "{:<20}  {:<10}  {:<26}  {:<20}  {}".format(ip_list, status_lst, url, url_title, header_list)
                        loginfo = "{:<20}  {:<10}  {:<26}  {}".format(ip_list, status_lst, url, url_title)
                    return loginfo
            else:
                print '{} {}'.fromat(payload, r_status_code)
            break
        except Exception, e:
            # print e
            try_cnt += 1
            if try_cnt >= RETRY_CNT:
                return