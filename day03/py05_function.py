# 함수, Function, Method, Procedure,...
# 전달인자(Argument), 파라미터(매개변수)

# parameter (매개변수)
# 함수의 정의 부분에 나열되어 있는 변수, 여기서는 plus 함수 정의시에 사용되는 a, b를
# parameter(매개변수) 라고 한다.
# def plus(a, b):
#     return a + b

# argument (전달인자)
# 함수를 호출할때 전달 되는 실제 값, 여기서는 plus 라는 함수에 넣어주는 값 1, 2를 
# argument(전달인자)라고 한다.
# result = plus(1, 2)


# *****사용법*****
# def 함수명(인자1, 파라미터2, 매개변수3) :      ex) 식빵(함수명) 인자=파라미터=매개변수(이스트, 밀가루,등)
#   함수 안으로 진입

#------------------------------------

## EX01
def say_hi(): # 함수정의(1)
    print('안녕~~~')
    return None         # return None => 돌려줄 값이 없을 때 생략가능

# name = '여원'
def say_hello (name) : # 함수정의(2)~
    print(f'{name}야!! 안녕? ㅎㅎ')    
    return None
    
def get_age(bithYear):  # 함수정의(3)
    age = 2025 - bithYear
    return age  

def closing():
    return '바이바이~'  

    
print('인사하기: ', end=' ')
say_hi() # 함수호출!!

name = input('이름입력 > ')
print('이름으로 인사하기 : ', end='')
say_hello(name) # 함수호출!!

year = int(input('생일년도 입력하세요 >'))
real_age = get_age(year)
print(f'나이는:{real_age}세')


print('수고하셨습니다: ', closing())



