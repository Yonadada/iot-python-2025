# 객체지향 문제

class Person:
    #명사 (속성)인 멤버변수들
    name = '요키'
    age = 5
    weight = 5.65
    gender = 'Female'
    
    #초기화(생성자) 메서드(파이썬은 기본적으로 포함하고 있음)
    def __init__(self, name, age, weight,gender ):  # self가 가지고 있는 변수들을 초기화 하겠다!!
        self.name = name 
        self.age = age 
        self.weight = weight 
        self.gender = gender
        
        
    def __str__(self): # 객체 정보들을 출력하여 문자열을 포맷팅
        retStr = f'{self.name}\n{self.age}\n{self.weight}\n{self.gender}'
        return retStr
    
        
    #동사(기상하다)인 멤버함수=(메서드)라고 말한다.  #class에 속하는 함수를 메서드라고 함 / 멤버함수 안에 무조건 self
    def getup(self): # 주의!!!!! -> self는 클래스 함수 선언할 때만 사용된다!!!<-
        print(f'{self.name}(가) 일어납니다')
        
    
    def setWeight(self, weight): # weight 의 몸무게를 변경 
        print(f'{self.name}의 몸무게가 변경됩니다')
        print(f'현재 {self.weight}Kg')
        self.weight = weight
        
        print(f'변경 후 {weight}kg') 
    
    # 성별을 가져옴    
    def getGender(self):
        return self.getGender
        
woman = Person('나다', 4, 3.22, 'Female') 
# => __init__() 특수함수가 Pers클래스 대신에 초기화하여  실행한다. 
# => 그래서 man.getup() 결과가 '나다',...바뀌어서 나옴

woman.getup()
woman.setWeight(3.52)
print(f'{woman.name}의 성별은 {woman.gender}')

print('-----------------')

print('****객체정보****')
print(woman)