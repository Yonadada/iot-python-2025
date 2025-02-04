# 복합 자료형 
# 자료구조 및 알고리즘 

# 리스트 (배열 사용 이전)
a = 1
b = 2
c = 3
d = 4 
e = 5

sum = a + b + c + d 
print(sum)

# 리스트 (배열 사용) => []  ** 다른 언어에서는 리스트와 배열은 다르다! **
f = [1, 2, 3, 4, 5]

print(f)
print(type(f))

# ex01
f = ['Life', 'is', True, 0, None, [1, 2, 3]]
print(f)    # ['Life', 'is', True, 0, None, [1, 2, 3]]
print(f[0]) # Life

#ex02
# 리스트의 한 요소에도 값을 집어 넣을 수 있음 
f[3] = 100
print(f) # 출력값 => ['Life', 'is', True, 100, None, [1, 2, 3]]



# ---------------------------------
## 튜플 => ()
# 리스트와 거의 흡사하며 값을 변경 할 수 없음
t = (1,2,3,4)
print(t)    # 출력값 => (1, 2, 3, 4)
print(t[3]) # 출력값 =>  4

# t[0] = 5 # 에러발생!! => TypeError: 'tuple' object does not support item assignment

print(type(t)) # <class 'tuple'>

# ---------------------------------
## 딕셔너리(복합형) => {key : value} 의 집합

spiderman = { 'name ' : 'Petter Parker', 'age' : 20, 'weapon' : 'Web Shooter'}
print(spiderman)    # 출력값 => {'name ': 'Petter Parker', 'age': 20, 'weapon': 'Web Shooter'}
print(type(spiderman)) # 결과 => <class 'dict'>

print(spiderman['name ']) # 결과 => Petter Parker

spiderman['age'] = 21 
print(spiderman) # 출력값 => {'name ': 'Petter Parker', 'age': 21, 'weapon': 'Web Shooter'}


# ---------------------------------
## 집합 => (), {}, [] 다 사용가능 
# ex01
s = set([1, 3, 5, 7, 9, 5])  # 출력값 => {1, 3, 5, 7, 9} ** 집합만 중복값 제거해서 출력 ** 
print(s)
print(type(s)) # 결과 => <class 'set'>

# ex02
s = set('Hello Wold') # 출력값 => {'W', 'o', ' ', 'l', 'd', 'H', 'e'} 
                      # ** 공백도 값으로 취급 ,인덱스 없음(순서가 없다) **
print(s)

# --------------------------------
## 변수명 지정방식 

# 1) 의미있는 단어들의 조합으로 만들것 
phoneNumber = '010-1111-1111'
salaryBankAccount = '3333-111111-111111'
samsung = ''
samsung1 = ''

# 2) 변수명 첫글자는 숫자로 시작할 수 없다
samsung = '' # (가능)
samsung1 = '' # (가능)


#) _ 이외의 특수문자는 사용불가
_samsung1 = '' # => (가능)

# 1samsung = '' # (불가능)
# samsung1! = ''  =>  (불가능)
# samsung1-apple = '' =>  (불가능)  
# samsung1* = ''  =>  (불가능)
# samsung - apple = ''  => (불가능) Why? 파이썬 연산자라서 ~

