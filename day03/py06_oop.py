# 객체지향 - Object-Oriented Programming(oop)

# *****사용방법******
# class 클래스명:
#   속성변수(멤버변수) = 값      
#                                
#   def 함수(self, 매개변수):   
#       수행할 로직
#       return...
# ******************
# => 클래스는 명사(변수) + 동사(함수)의 집합체

class Person: # 클래스 Person 생성
    pass

man = Person()
print(f'객체 man의 타입 {type(man)}') 
print(f'객체 man의 id {id(man)}')

woman = Person()
print(f'객체 woman의 타입 {type(woman)}') # 출력값 => 객체 woman의 타입 <class '__main__.Person'>
print(f'객체 woman의 id {id(woman)}') # 출력값 => 객체 woman의 id 2251488785424, 메모리의 주소를 의미함  
