# 수학모듈 : 수학 함수들이 모여있는 파이썬 모듈
import math     # import나 모듈들은 제일 상단에 함께 묶어놔야함

print(math.pi)

PI = 3.141592

# 2 ** 10 -> int
print(math.pow(2,10)) #float
print(math.sqrt(4))
print(math.log2(2))

#-----------------------
import random

numbers = [i for i in range(1, 45 + 1)] # 1 ~ 45까지의 숫자가 리스트로
result =[]

for i in range(6):
    result.append(random.choice(numbers))
    
print(result) 

# 간단한 로또 
# weight : 가중치
numbers = weight = list(range(1, 45+1))
random.shuffle(weight)

# 한꺼번에 랜덤 여섯개를 추출
result = random.choices(numbers, weights=weight, k=6)
print(result)

# 중복없이 무작위로 6개를 추출 
# sample()은 리스트나 시퀀스에서 지정된 개수만큼 중복 없이 무작위로 뽑는 함수
numbers = list(range(1, 1+45))
result = random.sample(numbers, 6)
print(result.sort())
