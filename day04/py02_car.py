## 객체지향(복습)

class Car:
    #__new__ # 사용빈도 낮음, __init__ 많이 사용
    # Car() 호출하면 아래의 메서드가 실행
    
    # myCar 
    def __init__(self, company=None, name=None, plateNumber=None):
        # company, name, plateNumber 모를때는 값 부분에 None 입력
        self.__company = company # 멤버변수 이름 앞에__쓰면 외부접근이(private) 불가능!!
        self.__name = name
        self.__plateNumber = plateNumber
        print('-----Car 클래스를 새로 생성-----')
    
    # 클래스 자체가 출력되는데, __str__ 문자열로 출력되도록 도와줌 
    def __str__(self):
        return f'제 차는 {self.__name}이고, 차번호는 {self.__plateNumber}'
    
    # 외부에서 잘못된 차 번호를 넣으면 안들어간다
    def setPlateNumber(self, newPlateNumber):
        if type(newPlateNumber) is str:
            self.__plateNumber = newPlateNumber
            
            
    def setName(self, newName='뭐더라'): # 이름을 모를때 뭐더라로 대체
        self.__name = newName
    
    # 왜 필요한거?
    # __name은 private 변수라서 클래스 외부에서 직접 접근이 불가능합니다. 
    # 그래서 이 값을 읽어오려면 getName()같은 메서드가 꼭 필요한 거죠!
    def getName(self): 
        return self.__name

# ****모듈화 하려면 예제소스는 없어야함*****
            
#myCar = Car('현대차', '아이오닉','17너7285') #  회사-> 이름 -> 차번호 순서에 영향을 받음 
# myCar = Car(name='아이오닉', plateNumber='17너7285', company='현대')  
# => 파라미터 명=값으로 매개변수 순서를 지정할 수 있다 

#(1) 차의 번호를 출력
# print(myCar) 

#(1-1)
# 차의 번호를 바꾸고 싶음  # 좋은 방법이 아니다! 
# myCar.plateNumber = '11너7777' 
# print(myCar)

#(2)
# myCar.__plateNumber = '11너7777'
# print(myCar)
# 클래스 외부에서 잘못된 데이터를 넣어도 문제가 발생 x 
# Why? => 잘못된 데이터 할당을 막기 위해

#(3)
# myCar.setPlateNumber('11너7777')
# print(myCar)

# 출력값 (1,2,3)
# -----Car 클래스를 새로 생성-----
# 제 차는 현대이고, 차번호는 17너7285
# 제 차는 현대이고, 차번호는 17너7285
# 제 차는 현대이고, 차번호는 11너7777

#======================================
# yourCar = Car()
# print(yourCar)
# 에러발생~!
# TypeError: Car.__init__() missing 3 required positional arguments: 'company', 'name', and 'plateNumber'
# 전달될 필수 인자값이 빠졌기 때문

# yourCar.setPlateNumber('88조4532')
# print(yourCar) 

# yourCar.setName('제네시스')
# print(yourCar)

#출력값 
# -----Car 클래스를 새로 생성-----
# 제 차는 None이고, 차번호는 None
# 제 차는 None이고, 차번호는 88조4532
# 제 차는 제네시스이고, 차번호는 88조4532


