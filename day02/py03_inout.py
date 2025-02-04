# 화면 입출력
## ex01
print('출력입니다~')

number = input('만 나이를 입력해주세요 >') # 입력방법 
print(type(number)) # 결과 => <class 'str'> 
                    # 입력&출력 되는 값이 모두 문자열
                    # 에러발생 => TypeError: can only concatenate str (not "int") to str

number = int(number) # String --> int (형변환)
                    # 즉, 입력받은 String을  int 형으로 형변환을 통해 결과값(number + 1) 출력되도록 한다
                    
print("현재나이는", number + 1 ) # 여러 값을 같이 출력하려면 ,(쉼표)로 구분

#--------------------------------
# 다중입력 
##ex02 

x, y = input('합산할 두 수를 입력해주세요 > ').split() # 공백으로 잘라주는 함수 
# 에러발생 => ValueError: too many values to unpack (expected 2)

x = int(x)
y = int(y)

print(x + y)