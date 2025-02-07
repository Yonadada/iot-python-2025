# 리스트 연산
# 리스트가 for, while 반복문에서 가장 많이 활용되는 구조
# iterable -> (뜻)반복할 수 있는 / 반복할 수 있는 요소가 for, while 문에 사용

listSample = [1,2,3,4,5,6,7,8,9,10]

# EX01
# -- 반복문 시작 --
# for i in 10:
#     print(i)
# -- 반복문 끝 --
# 에러발생~!! 
# TypeError: 'int' object is not iterable 
# 반복할 수 없는 값은 올 수 없다

#EX02
# -- 반복문 시작 --
sum = 0
for i in listSample:
    sum = sum + i # sum += i
    
print(f'합산결과 = {sum}')
# -- 반복문 끝 --


##----리스트 연산----
arr = [1,2,3,4,5]
arr2 = [2,4,6,8,10]

print(arr[4]) # 출력값 =>[1, 2, 3, 4, 5]
print(arr) # 출력값 => 5
print(arr[0] + arr[3]) # 출력값 => 5
print(arr[-2]) # 출력값 => 4
print(arr[2:3]) # 출력값 => [3]

print(arr + arr2) # 출력값 => [1, 2, 3, 4, 5, 2, 4, 6, 8, 10] ** 중복값 제거 **
print(arr * 2)  # 출력값 => [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

##----리스트 길이----
print(len(arr)) # 출력값 => 5
arr[2] = 9    # 데이터 할당
print(arr) # 출력값 => [1, 2, 9, 4, 5]  ** 배열[2]자리에 9를 할당해서 이와같은 출력값 도출

##----리스트 요소 삭제----
arr[2] = None
print(arr) # 출력값 => [1, 2, None, 4, 5]

del(arr[2])
print(len(arr),arr)  
# 출력값 => 4 [1, 2, 4, 5]
# 4는 len(arr)

##----리스트 요소 추가----
arr.append(7) 
print(arr) # 출력값 => [1, 2, 4, 5, 7]  
# 제일 뒤에 데이터가 추가된다


arr.insert(2, 100)
print(arr) # 출력값 => [1, 2, 100, 4, 5, 7]
# n번째 자리에 기존 데이터를 밀어내고 추가 된다
# Q. arr.replace() 안되는가?
# A. insert()는 리스트에서만 사용가능하고, replace()는 문자열에서만 가능


##----리스트 합칠때----
print(arr.extend(arr2))

##----리스트 정렬(ex. 쇼핑몰 낮은 가격순, 높은 가격순, 최신일자부터,...)----
arr = [1,3,5,6,7,9,0,2,8] 

print(arr) # 출력값 => [1, 3, 5, 7, 9, 0, 2, 8]
#arr.sort() # sort()는 오름차순 정렬 
print(arr) # 출력값 => [0, 1, 2, 3, 5, 7, 8, 9]

arr.sort(reverse=True) # reverse=True 는 내림차순 정렬
print(arr) # 출력값 => [9, 8, 7, 5, 3, 2, 1, 0]

##----요소의 위치파악----
print(arr.index(6)) # 없는 데이터를 인덱스 하면 오류발생
# 출력값 => 3

print()

##----요소꺼내기----
print(arr.pop()) # 출력값 => 0 
print(arr) # 출력값 =>[9, 8, 7, 6, 5, 3, 2, 1]

##----리스트 컴프리핸션---- 
# 대량의 리스트를 쉽게 생성할 수 있는 방법
# 리스트 컴프리헨션은 한 줄로 결과 리스트를 만든다

# ****구조****
# [표현식 for 변수(=루프변수) in 반복가능한 객체]
# 

arr =[i for i in range(1, 100+1)] # 리스트 데이터 개수를 반복문을 통해 100까지 만들어줌  
print(arr)
# Q. for 반복문의 좌측 i는 무엇이며 이름은 무엇인가요? 우측 i는?
# A. 좌측 i는 => 표현식으로, 변수와 관련된 연산이나 값을 리스트에 넣는 작업을 함. 즉, 결과를 만들어준다
#                즉, arr 리스트는 i 값들을 모은 결과물  
#    우측 i는 => range() 생성된 값들을 받는 변수
# 만약에 표현식이 없다면 반복문을 통해 나온 각 값을 어떻게 사용할지 알 수 없기때문에 꼭 필요함!!

sum = 0 
for i in arr:
    sum += i

print(f'{len(arr)}까지의 합산은, {sum}입니다.')

#1~100 홀수만 
#2~100 짝수만  

# append()
x = ['W','Y', 'Z']
y = ['A','C','E']

x.append(y)
print(x)
# 출력값 => ['W', 'Y', 'Z', ['A', 'C', 'E']]
print(len(x)) # 리스트 길이 4개

# extend
x = ['W', 'Y', 'Z']
y = ['A', 'C', 'E']

x.extend(y)
print(x)
# 출력값 => ['W', 'Y', 'Z', 'A', 'C', 'E']
print(len(x)) # 리스트 길이 6개