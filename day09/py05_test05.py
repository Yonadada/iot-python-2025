# 5. SmartPhone 이라는 클래스를 만들고, 객체를 생성해서 phoneOwner, phoneNumber, company 등의 멤버변수(속성)을 가지도록 만드세요.
# (본인이 다른 기능을 좀 더 추가하여도 무방합니다)


class SmartPhone:
    
    def __init__(self, phoneOwner, phoneNumber, company):
        self.__phoneOwner = phoneOwner
        self.__phoneNumber = phoneNumber
        self.__company = company
        
        
    def __str__(self):
        str_res = (f'핸드폰 주인: {self.__phoneOwner}\n'
                f'핸드폰 번호: {self.__phoneNumber}\n'
                f'브랜드: {self.__company}')
        return str_res
    
    def set_phoneOwner(self, phoneOwner):
        self.__phoneOwner = phoneOwner
    

    def set_phoneNumber(self, phoneNumber = '010-0000-0000'):
        self.__phoneNumber = phoneNumber
        
    def set_company(self, company):
        self.__company = company
        
        
myPhone = SmartPhone('홍여원','010-4644-5683','엘지')
phoneNumber = input('정보를 입력하세요 ')

myPhone.set_phoneNumber(phoneNumber)
myPhone.set_phoneOwner('먀먀')
myPhone.set_company('삼숭')


print(myPhone)    
        



    




# if __name__ == '__main__' :
#     run()
    
# print('----프로그램끝----')
    