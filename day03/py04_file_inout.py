# 파일 입출력

# 파일 오픈,읽고,쓰고, 닫음
# 파일 경로 : 파일이 컴퓨터상에 들어있는 위치
# 경로의 구분자가 \ , / 다 사용가능 
# mode : 읽기(r), 쓰기(w), 추가(a),...
# encoding : 한글 쓰려면(euc-kr, cp949),  국제어(utf-8)
# . : 현재 사용자의 위치
# .. : 자신의 부모폴더 위치


#상대경로 - 경로를 특수문자로 생략하는 법
# ------시작-------
# f = open('./test.txt', mode='w', encoding='UTF-8')
# f.write('파일 쓰기 시작하기~!')
# f.close()
# print('******파일쓰기 완료했습니다******') 
# IOT-Python-2025에 만들어짐
# ------끝-------


# 부모폴더에 test3이 생김
# ------시작-------
# f = open('../test3.txt', mode='w', encoding='UTF-8')
# f.write('파일 쓰기 시작하기~!')
# f.close()
# print('******파일쓰기 완료했습니다******') 
# day03 파일 안에 만들어짐
# ------끝-------

# \를 문자열에 표현하고 싶으면 \\ 사용
# 절대경로 - 드라이브부터 모든 경로를 다 작성하는 법
# ------시작-------
# f = open('C:\\Source\\iot-python-2025\\day03\\test4.txt', mode='w', encoding='UTF-8')
# f.write('파일 쓰기 시작하기~!')
# f.close()
# print('******파일쓰기 완료했습니다******') 
#day03 파일 안에 만들어짐
# ------끝-------



# 파일 쓰기 + 읽기
# ------시작-------
f = open('./day03/test.txt', mode='w', encoding='UTF-8')
f.write('파일 쓰기 시작하기~!\n')
f.write('두번째 줄 작성하기~!\n')

f.close()
print('******파일쓰기 완료했습니다******') 


r = open('./day03/test.txt', mode='r', encoding='UTF-8')

while True :
    line = r.readline() # 한줄씩 읽음
    
    if not line : # 한 줄 읽은 값이 None이면 
        break # while문을 빠져나옴
    
    #(1)방법. 줄 공백 없애는 방법 
    #print(line, end='') 
    
    # 출력값 
    # => 파일 쓰기 시작하기~!
    # => 두번째 줄 작성하기~!
    
    #(2)방법. 줄 공백 없애는 방법 
    print(line.replace('\n',''))
    
r.close()    
        
# ------끝-------