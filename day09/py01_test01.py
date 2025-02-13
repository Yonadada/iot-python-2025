# 반지름 값을 입력받아 원의 넓이를 구하여 출력하는 프로그램

import math

num = input(f'원의 반지름 값을 입력해주세요 >')

num = int(num)

circle= math.sqrt(num) * math.pi

print(f'원의 넓이는 : {circle:>.2f}')