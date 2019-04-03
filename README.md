# POC-T: *Pentest Over Concurrent Toolkit* 

## Referer
- [http://www.freebuf.com/sectool/176562.html](http://www.freebuf.com/sectool/176562.html)
- [https://www.t00ls.net/thread-48738-1-1.html](https://www.t00ls.net/thread-48738-1-1.html)

## 使用
- `python POC-T.py --batch -iF 1.txt` 使用fuzz脚本
- `python POC-T.py -eT -t 20 -s xx -iF 1w.txt`
- `python POC-T.py -eT -t 10 --cms dedecms -iF url.txt`

## 插件
- waf 检测waf 并返回没有waf的url
- craw 爬取链接中的相关地址
- vulscan 检测sql注入漏洞
- portscan 端口扫描，检测弱口令服务
- findsub 查找子域名

## 请遵守法律
本程序含有一定的破坏性，请遵守当地法律后使用。不可用于非法用途！

- 2018-11-28 在 [https://github.com/boy-hack/POC-T](https://github.com/boy-hack/POC-T) 的基础上增加一个--cms的功能

## cms目录下创建cms名称的文件夹，然后再该cms目录下自己写poc


```
cms目录结构
cms
├── dedecms
│   ├── dede.py
│   ├── dede_reinstall.py
│   ├── dede_short.py
│   └── __init__.py
├── ecshop
│   ├── ecshop-getshell.py
│   └── __init__.py
├── info
│   └── __init__.py
├── __init__.py
├── metinfo
│   ├── __init__.py
│   ├── metinfo-504-sqli.py
│   └── metinfo.py
├── phpcms
│   ├── __init__.py
│   ├── phpcms9.6.0-sqli.py
│   ├── phpcms_database.py
├── phpcms2008
│   ├── __init__.py
│   └── phpcms2008.py
├── qibo
│   ├── __init__.py
│   ├── qibo_admin.py
│   ├── qibo_download.py
│   └── qibo.py
├── redis
│   ├── __init__.py
│   └── redis-unauth.py
├── s-cms
│   ├── __init__.py
│   └── s-cms3.0sqli.py
├── ueditor
│   ├── __init__.py
│   └── ueditor.py
└── zzcms
    ├── __init__.py
    └── zzcms_getshell.py

11 directories, 33 files

```
