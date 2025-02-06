#py06_exception.py

# 예외처리
# -  오류, Error, Fault
# 1. Error(문법적 오류) - 빨간색 밑줄
#    오류표시가 안나는 코딩을 잘못한 오류 포함!! ex. mul(7, 6) --> 42예상. 결과 13 

# 2. Exception(실행중 예외 발생) - 문법오류 수정 후 실행하다가 비정상적인 종료
# ** 파이썬은 Error, Exception 둘다 Error 라고 뜸(구분이 어려움)
# ->Error는 에디터 상에 오류표시
# ->Exception은 실행 중에 발생

numbers = list(range(1,11))

#  Error(문법적 오류 예시(1))
# for i int numbers:
#     print(i)

for i in numbers:
    # print(i)
    pass

def mul(a, b):
    return a * b

def div(a,b):
    return a / b

print('-------계산시작-------')

while True:
    op = input('계산할 연산을 3개중에 1개 입력(*, /, q)')
    if op == 'q': # 종료조건
        break
    
    elif op == '*': # 곱하기
        x, y = input('곱할 두 수 입력> ').split()
        x = int(x)
        y = int(y)
        print(f'{x} x {y} = {mul(x, y)}')  # 47 두수를 붙여서 입력했을시, 에러발생!!! => ValueError: not enough values to unpack (expected 2, got 1) 
        
    elif op == '/': # 나누기
        x, y = input('나누기할 두 수 입력> ').split()   
        x = int(x)
        y = int(y)
        print(f'{x} / {y} = {div(x, y)}')   # 19 0 나누면  에러발생!!! => ZeroDivisionError: division by zero [무한대]
    else :
        print('다시 한번 입력부탁드리겠습니다~')