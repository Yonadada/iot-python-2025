# 2. 영문이름을 입력하면 웹사이트 주소가 리턴되는 함수, get_url() 를  구현하세요.
# 예) url = get_url('google') 
# print(url) # www.google.com


def get_url(url):
    url = ['www.google.com','www.naver.com','www.daum.net']
    if name == 'google':
        return print(f'{url[0]} 이동중')

    elif name == 'naver':
        return print(f'{url[1]} 이동중')
    elif name == 'daum':
        return print(f'{url[2]} 이동중')
    else :
        print('해당 페이지 추후 업데이트 예정')



name = input(f'방문하고자하는 사이트 이름을 영문으로 입력해주세요 > ').lower()
get_url(name)
