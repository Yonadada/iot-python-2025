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

print(f'{greeting} {target}') # ** f-string 사용할때 f 다음에 공백이 있으면 안된다
# 출력값 => Hello World


# ex06
print(greeting * 5) # 해당문자열을 * 수로 반복 
# 출력값 => HelloHelloHelloHelloHello


