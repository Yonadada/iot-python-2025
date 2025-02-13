# 구구단을 수행할 단번호를 입력하면 그 단의 9까지의 결과를 나열하는 프로그램을 입력하세요.
# 예) 3 --> 3 6 9 12 15 18 21 24 27

for i in range(1,9+1):
    print()
    print(f'{i}단 시작\n')
    for j in range(1,10):
        print(f'{i} x {j} = {i*j}\t',end='')
    print()
    