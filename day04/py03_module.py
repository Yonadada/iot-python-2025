# 모듈 (ex.레고)

# 모듈 사용법 
# import 모둘명
# from 모둘명 import 상세...

import py02_car
hisCar = py02_car.Car('기아차','스팅거','몰라')
print(hisCar)

# import는 py02_car 파일 전체를 들고온다
import py02_car as c
herCar = c.Car('제네시스','G90','76너7285')
print(herCar)

# from은 py02_car의  특정(Car) 클래스나 함수만 가져오기
from py02_car import Car
thatCar = Car('람보르기니','이름몰라','11로9009')
print(thatCar)