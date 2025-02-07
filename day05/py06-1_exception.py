#py06-1_exception.py

# 예외처리
# -  오류, Error, Fault
# 1. Error(문법적 오류) - 빨간색 밑줄
#    오류표시가 안나는 코딩을 잘못한 오류 포함!! ex. mul(7, 6) --> 42예상. 결과 13 

# --<<사용법>>--
# try :
#   예외가 발생할 수 있는 로직
# except 예외클래스 as e: -> Exception 클래스는 모든 예외 클래스의 조상, Exception만 쓰면 된다
#   예외처리로직
# [finally] -> 옵션
#   예외발생 유무와 상관없이 항상 처리해야 하는 로직
#
# ++ try문을 반복해서 사용하거나 이중 try문을 지양할 것 => 속도가 느려지기때문

# -----------------------------------------------------------------------------------

# 2. Exception(실행중 예외 발생) - 문법오류 수정 후 실행하다가 비정상적인 종료
# ** 파이썬은 Error, Exception 둘다 Error 라고 뜸(구분이 어려움)
# ->Error는 에디터 상에 오류표시
# ->Exception은 실행 중에 발생
#=> 그래서 debugging(디버깅) 해줘야한다

# 디버깅 - 천천히 어디에서 예외(오류)가 발생하는지 확인하기 위해 사용 => !!! 디버깅 너무 중요!!!!
# --<<단축키>>--
# 1) f9 - 중단점(Break Point) 표시/해제 기능
# 2) f5 - 디버깅 시작, 중단점까지 실행
# 3) f10 - 한줄 실행, 함수가 있어도 함수를 실행하고 넘어감
# 4) f11 - 한줄 실행, 함수가 있으면 함수 안으로 진입 
# 5) shift + f5 - 디버깅 종료
# 6) 실행및 디버그 
#    - 변수 탭 -> 현재 변수에 들어있는 값을 표시해준다
#    - 조사식 탭 -> 내가 원하는 식을 실행하고 결과 표시

# -----------------------------------------------------------------------------------

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
        
        try : # try 구문 안에는 예외가 발생할 것 같은 구문들을 넣는다
            x, y = input('곱할 두 수 입력> ').split()
            x = int(x)
            y = int(y)
            print(f'{x} x {y} = {mul(x, y)}')  
            
        except Exception as e:
            # print('======잘못입력하셨습니다======') # 사용자가 보게 되는 에러메세지
            print(f'-입력 실수- {e}')
        
    elif op == '/': # 나누기
        try :
            x, y = input('나누기할 두 수 입력> ').split()   
            x = int(x)
            y = int(y)
            
            print(f'{x} / {y} = {div(x, y)}')   # 19 0 나누면  에러발생!!! => ZeroDivisionError: division by zero [무한대]
            
        except ValueError as e :
            # print('======잘못입력하셨습니다======') # 사용자가 보게 되는 에러메세지
            print(f'-입력실수- {e}')
        except ZeroDivisionError as e :
            print('0으로 나누면 무한대가됩니다')
            print('{e}')        
                    
    else :
        print('다시 한번 입력부탁드리겠습니다~')