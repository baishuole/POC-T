# -*- coding: utf-8 -*-
import requests
from urlparse import urlparse
from plugin.util import urlhandler, siteIndexTest, rar_size
from lib.core.settings import HEADERS, TIMEOUT, VERIFY, ALLOW_REDIRECTS, STREAM
from data.info_dict import BAKFILE_DICT, BakFileSuffixFormat

requests.packages.urllib3.disable_warnings()

def poc(url):
    testurl = urlhandler(url)
    if not siteIndexTest(testurl):
        return '[SiteRequestErr-bakfile] %s' % testurl
    return audit(testurl)


def audit(url):
    parse = urlparse(url)
    url_netloc = parse.netloc
    url = urlhandler(url)
    host_keys = url_netloc.split('.')

    wwwlen = len(host_keys)
    topdomainnopoint = ''

    if wwwlen > 2:
        for i in range(1, wwwlen):
            topdomainnopoint += host_keys[i]
    else:
        for i in range(wwwlen):
            topdomainnopoint += host_keys[i]

    try:
        realdomain = url_netloc
        domainnopoint = realdomain.replace('.', '')
        topdomain = realdomain.split('.', 1)[-1]
        hosthead = host_keys[0]
        domaincenter = host_keys[1]
        domainunderline = realdomain.replace('.', '_')
        topdomainunderline = topdomain.replace('.', '_')

        domainDic = [realdomain, domainnopoint, topdomainnopoint, topdomain,
                     hosthead, domaincenter, domainunderline,
                     topdomainunderline]

    except:
        return u"[BAKFILE] DomainHandlerError"

    listFile = []
    for i in BAKFILE_DICT:
        listFile.append(i)


    for s in BakFileSuffixFormat:
        for d in domainDic:
            if d + s not in listFile:
                listFile.append(d + s)

    warning_list = []
    for payload in listFile:
        vul_url = url + payload

        try:
            r = requests.get(vul_url, headers=HEADERS, timeout=TIMEOUT,
                             allow_redirects=ALLOW_REDIRECTS, stream=STREAM,
                             verify=VERIFY)

            contentType = r.headers["Content-Type"]

            if r.status_code == 200 and "Content-Type" in r.headers \
                    and 'text/html' not in contentType \
                    and 'image/' not in contentType:
                rarsize = int(r.headers.get('Content-Length'))
                rarsize = rar_size(rarsize)
                if rarsize == '0K':
                    pass
                else:
                    warning_list.append("[BAKFILE] %s Size:%s %s" % (
                        vul_url, rarsize, contentType))
        except Exception:
            pass

    if len(warning_list) < 10:
        return warning_list
