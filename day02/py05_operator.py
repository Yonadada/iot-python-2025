# 연산자

# 사칙연산 ( + , -, *, % )
# ex01

a,b = 15,14
print()
print(a + b) # 29
print( a * b) # 210
print( a - b, '\n') # 1

#---------------------------
# 나누기 연산자 / , //, % (3가지)
# ex02

a = 14
b = 4

print(a / b) #나눈 결과는 float(실수) 
print(a // b) # 나눈 몫, int 형으로 출력 
print(a % b, '\n') # 나머지, int 형으로 출력 

#---------------------------
# 거듭제곱(Power) **
# ex03

print(2 ** 10, '\n')

#---------------------------
# 연산자 우선순위
# ex04
## 계산식이 복잡해서 연산자 우선순위를 잘 모르겠으면 () 사용

print( (3 + 4) * 7)
print(3 + (4 * 7))

print('\n')

#---------------------------
# 리스트 연산
# ex04
## index = len(list) - 1 

listSample = [1,3,5,7,9]
print(listSample[0]) # 출력값 => 1

print(len(listSample)) # len() => length(줌말로 리스트의 길이를 구하는 함수)
# 출력값 => 5

print('\n')

print(listSample[1])
print(listSample[2])
print(listSample[3])
print(listSample[4])
#print(listSample[5]) 
# # 오류발생! => IndexError: list index out of range / 인덱스의 범위에서 벗어남

print(listSample[len(listSample) - 1]) # 출력값 => 9
# listSample 의 길이 - 1 의 값을 담은 listSample 을 출력하라~ 
print('\n')

listSample[4] = 11 
print(listSample[len(listSample) - 1]) # 출력값 => 11
# listSample 의 길이 - 1 의 값을 담은 listSample 을 출력하라~ 

print('\n')


#---------------------------
# 문자열 연산 : (+, *) 만 존재
# ex05

greeting = 'Hello'
target = 'World'
print(greeting, target) # 순차적으로 출력   => **문자열 연산이 X **
# 출력값 => Hello World 출력되지만 연산이용 xx


print(greeting + target) # 문자열을 합쳐라(공백이 없다) => String concatenate
# 출력값 => HelloWorld

print(greeting + ' ' + target)
# 출력값 => Hello World

print('{0} {1}'.format(greeting, target))
# 출력값 => Hello World

print(f'{greeting} {target}') # ** f-string 사용할때 f다음 공백이 있으면 안된다
# 출력값 => Hello World

#------
# ex06
print(greeting * 5) # 해당문자열을 * 수로 반복 
# 출력값 => HelloHelloHelloHelloHello


#---------------------------
#ex07
## 문자열(Charater Array) == List 
print(greeting[1]) # 리스트 연산 
#greeting[0] = 'C'

print(greeting)
# 오류발생~! => TypeError: 'str' object does not support item assignment 
# List 와 유사하지만 값 수정 불가능 !!! 


#---------------------------
## 리스트연산, 슬라이싱
# ex08

listSample = ['2','0','2','5','-','0','2','-','0','4']
current = '2025-02-04'

#for문
for i in listSample:
    print(i, end='')
print()    
    
print(current)
# 준비 끝


# 인덱싱, 인덱스에 있는 값을 가져오기
print(listSample[-1]) # 출력값 => 4 
# 해설>> listSample을 오른쪽부터 왼쪽으로 거꾸로 -1, -2, -3,...즉, 4가 나옴
print(current[-1])


##ex09
# 슬라이싱, 리스트를 자르기 
# [start:end] => end - 1 까지만 추출 
print(listSample[0:3])
# 결과값 => ['2', '0', '2']

print(current[0:3])
# 결과값 => 202


print(listSample[0:3 + 1 ])
# 결과값 => ['2', '0', '2', '5']

print(current[0:3 +1])

# 결과값 => 2025


##Ex10
# 2025-02-04
year = current[0:3 + 1]
month = current[5:6 + 1]
day = current[8:] # 숫자: => 끝까지

print(year,month,day) # 출력값 => 2025 02 04
print(current[-2:]) # 출력값 => 04


#---------------------------
# EX11
## 문자열 연산 중 함수를 사용 
# ----자르기----

full_name = "Hong Yeo. Won" #split() 함수는 조건을 잘라내서 결과를 리스트화 하는것 
print(full_name.split()) #출력값 => ['Hong', 'Yeo', 'Won']
print(full_name.split(' ')) #출력값 => ['Hong', 'Yeo', 'Won']

names = full_name.split(' ')
print(type(names)) # 출력값 => <class 'list'>
print(names) # 출력값 => ['Hong', 'Yeo', 'Won']

names = full_name.split('.')
print(type(names)) # 출력값 => <class 'list'>
print(names) # 출력값 => ['Hong Yeo', ' Won']

print('\n')
print('\n')

## 문제 ## 
# T로 자를 때 
# '' == Empty(비어있다)
# ' ', " " == Space(공백존재)

origin = 'TESTSTRING'
print(origin.split('T'))
# 출력값 => ['', 'ES', 'S', 'RING']


#---------------------------
# EX12
# ----바꾸기----

print(full_name.replace('Hong Yeo.', 'Yonova' )) # 출력값 => Yonova Won


#---------------------------
# EX13
# ----공백제거----
origin = '        Hello        '
print(f'//{origin}//') # 출력값 => //        Hello        //

print(f'//{origin.lstrip()}//') 
# 출력값 => //Hello        // 
# 즉, 왼쪽 공백 없애기 

print(f'//{origin.rstrip()}//')
# 출력값 => //        Hello//
# 즉, 오른쪽 공백 없애기 

print(f'//{origin.strip()}//')
# 출력값 => //Hello//
# 즉, 모든 공백 없애기


#---------------------------
# EX14
# ----단어찾기----
full_name = "Hong Na. Da"
print(full_name.find('H'))
print(full_name.find('g'))
print(full_name.find('i'))
# 출력값 = > 0
#            3
#           -1  => i를 찾을 수 없음을 나타냄 

print(full_name.count('g')) # 'g'가 문장에 몇개 있는가
# print(full_name.index('i')) # 오류발생 !!!
# i가 

print(full_name.upper()) # upper() 모든 글자를 대문자로 출력
# 출력값 => HONG NA. DA

print(full_name.lower()) # lower() 모든 글자를 소문자로 출력 
# 출력값 => hong na. da 

