#!/usr/bin/python3
#-*- coding: utf-8 -*-
# HTTP 헤더 규격
print("content-type:text/html; charset=UTF-8\n")
print()

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
files = os.listdir('data')
listStr = ''
for item in files:
    listStr = listStr + '<li><a href="hello.py?id={name}">{name}</a></li>'.format(name=item)

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r', encoding="utf-8").read()
else:
    pageId = 'Welcome'
    description = 'Hello, web'
print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="hello.py">WEB</a></h1>
  <ol>
    {listStr}
  </ol>
  <a href="create.py">create</a>
  <form action="process_create.py" method="post">
      <p><input type="text" name="title" placeholder="title"></p>
      <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
      <p><input type="submit"></p>
  </form>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=listStr))
