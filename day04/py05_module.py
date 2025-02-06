# py05_module.py

# 외부 모듈을 사용하기 위한 방법
# 내 컴퓨터에 없는 모듈을 가져와서 사용하려면 
# pip : 파이썬에서 제공하는 Package Installer of Python
# 터미널 > pip install requests
# https://pypi.org => 외부패키지 찾고 싶을 때 또는 설치할 패키지 검색에 유용한 사이트!!!!!

import requests # 인터넷상에 있는 외부폴더를 다운받아서 가져오겠다.

print('외부 패키지 사용')

# 웹 브라우저가 아닌 파이썬 상에서 웹사이트 접속 
res = requests.get('https://www.google.com') # website URL

print(res.status_code) #200(ok) -> 웹사이트 접속 가능 
print(res.content)

f = open('./day04/index.html', encoding='utf-8', mode='w')

f.write(str(res.content, 'utf-8')) # 받아온 구글을 문자열로 파일에 받아와서 똑같이 index.html 파일 만들어서 적어라
f.close()

print('파일생성')

#---------------------
class Sample:
    pass


import py02_car as c

#*** __main__ 프로그램이 시작하는 진입점(entry point) 지칭
# C언어등의 static void main() 동일한 역할
# 폴더 안에 py파일 중 실행되는 파이썬 파일이 __main__(진입점)이 되고 
# 나머지는 모듈이 된다

if __name__ == '__main__' :
    sam = Sample()
    # print(sam) # 출력값 => <__main__.Sample object at 0x00000148E8847110>
    # print(__name__) # 출력값 => __main__
    car = c.Car()
    print(car)