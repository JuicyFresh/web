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
def fileList():
    files = os.listdir('data')
    listStr = ''
    for item in files:
        listStr = listStr + '<li><a href="hello.py?id={name}">{name}</a></li>'.format(name=item)
    return listStr

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r', encoding="utf-8").read()
    description = description.replace('<', '&lt;')
    description = description.replace('>', '&gt;')
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
    delete_action = '''
        <form action='process_delete.py' method='post'>
            <input type='hidden' name='pageId' value='{}'>
            <input type='submit' value='delete'>

        </form>
    '''.format(pageId)
else:
    pageId = 'Welcome'
    description = 'Hello, web'
    update_link = ''
    delete_action = ''
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
  {update_link}
  {delete_action}
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=fileList(), update_link=update_link,delete_action = delete_action))
