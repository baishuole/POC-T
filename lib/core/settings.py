#!/usr/bin/env python
# -*- coding: utf-8 -*-
# project = https://github.com/Xyntax/POC-T
# author = i@cdxy.me


import os
import subprocess

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}
TIMEOUT = 15
VERIFY = False
STREAM = True
ALLOW_REDIRECTS = True
RETRY_CNT = 2  # 0,1,2 失败尝试最多3次
DELAY = 0  # 延时

VERSION = '2.0.5'
PROJECT = "POC-T"
AUTHOR = 'cdxy'
MAIL = 'i@cdxy.me'
PLATFORM = os.name
LICENSE = 'GPLv2'
IS_WIN = subprocess.mswindows

# essential methods/functions in custom scripts/PoC (such as function poc())
ESSENTIAL_MODULE_METHODS = ['poc']
# Encoding used for Unicode data
UNICODE_ENCODING = "utf-8"
# String representation for NULL value
NULL = "NULL"
# Format used for representing invalid unicode characters
INVALID_UNICODE_CHAR_FORMAT = r"\x%02x"

ISSUES_PAGE = "https://github.com/Xyntax/POC-T/issues"
GIT_REPOSITORY = "git://github.com/Xyntax/POC-T.git"
GIT_PAGE = "https://github.com/Xyntax/POC-T"

BANNER = """\033[01;34m
                                             \033[01;31m__/\033[01;34m
    ____     ____     _____           ______\033[01;33m/ \033[01;31m__/\033[01;34m
   / __ \   / __ \   / ___/   ____   /__  __/\033[01;33m_/\033[01;34m
  / /_/ /  / /_/ /  / /___   /___/     / /
 / /___/   \____/   \____/            / /
/_/                                  /_/
    \033[01;37m{\033[01;m Version %s by %s mail:%s \033[01;37m}\033[0m
\n""" % (VERSION, AUTHOR, MAIL)
