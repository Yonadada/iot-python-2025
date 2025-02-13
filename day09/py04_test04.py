#4. 입력한 수를 거꾸로 출력하는 프로그램을 구현하세요.
# 예) 1 3 5 7 9 --> 9 7 5 3 1




# list 함수
def list(n):
    # print(f'결과는 : {n[-4:]}',end='')
    n.reverse()
    print(n)

number = input('입력하고 싶은 수를 기입하세요 > ').split(' ')

list(number)

