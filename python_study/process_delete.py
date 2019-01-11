#!/usr/bin/python3
#-*- coding: utf-8 -*-
# # HTTP 헤더 규격 (이제 이 밑으로는 html이야.)
# print("content-type:text/html; charset=UTF-8\n")
# print()

#아래는 브라우저에서 한글을 표기하기 위한 코드
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# cgitb는 CGI 프로그래밍시 디버깅을 위한 모듈로, cgitb.enable()
# 할 경우 런타임 에러를 웹브라우저로 전송한다
# cgitb.enable() 하지 않은 상태로 실행 중 오류가 발생한 경우
# 웹서버는 클라이언트에게 HTTP 응답코드 500을 전송한다
import cgi
import cgitb
cgitb.enable()


import os
form = cgi.FieldStorage()
title = form["pageId"].value

os.remove('data/'+title)

# HTTP 헤더 규격 (저 페이지로 이동해!, Redirection)
print("Location: hello.py")
print()
