# myMovieApp.py

import os # 운영체제 모듈 

from Movie import Movie # Movie 파일에 있는 Movie클래스를 들고오겟다

# 변수를 상수로 표현
VERSION = 0.1


# os에 특화된 팁 
def clearScreen():
    command = 'clear'
    if os.name in('nt', 'dos'):
        command = 'cls'

    os.system(command)



# 메인에서 제일 처음 실행되는 함수
def run() :
    #movie = Movie(' 해리 포터와 마법사의 돌', 2001, '박스오피스', 9.2 )
    #print(movie)
    #set_movie()/
    
    clearScreen() # 최초화면클리어
    
    lst_movie = [] # 영화리스트를 담는 변수이고 자료형은 list 타입 
    load_movie(lst_movie)
        
    while True:

        sel_menu = set_menu()
        if sel_menu == 1:
            #print('영화입력')
            
            try:
                movie = set_movie()
                lst_movie.append(movie)
                print('-----영화입력 성공-----')
            except Exception as e:
                print(f'-----영화입력 실패-----{e}')
                
                
        elif sel_menu == 2:
            print('영화출력')
            get_movie(lst_movie)
            
            
        elif sel_menu == 3:
            print('영화검색')
            
            title = input('검색할 영화 이름 입력 > ')
            search_movie(lst_movie, title)
            
            
        elif sel_menu == 4:
            print('영화삭제')  
            title = input('삭제할 영화 이름 입력 > ')
            if del_movie(lst_movie, title) :
                
                print('-----영화삭제 성공-----')
            else :
                print('-----영화삭제 성공-----')

                
        
        elif sel_menu == 5:
            #print('어플종료')
            
            # ------종료 직전 DB 생성하고 완료------
            save_movie(lst_movie)
            break # 반복문 탈출
        
        else:
            pass # 아무것도 출력되지 않고 종료
        
        input() # 입력대기
        clearScreen() # 메뉴 기능이 완료되면 화면 클리어
        
        
#영화검색 함수 
def search_movie(items: list, title: str):
    count = 0
    
    for item in items:   # item이 Movie 클래스인지 알 수 없음
        if item.isNameContain(title): # 오타발생 위험이 큼!
            count += 1 # 검색된 결과가 있음
            print(item)
            print('----------')
            
    print(f'검색 데이터 수 : {count}개')
        
    
#영화삭제 함수   #enumerate 클래스는 인덱스에 위치한 번호와 값이 나오게 해준다
def del_movie(items: list, title: str):
    for i, item in enumerate(items):
        if item.isNameExist(title):
            del items[i] # i에 있는 인덱스로 리스트에 요소 하나를 삭제 


    
    
    # title, year, company, rate -> 튜플인데 () 생략가능
def set_movie(): 
    title, year, company, rate = input('영화입력 [제목|개봉년도|제작사|평점 순] > ').split('|') # 입력 중 발생하는 예외 발생  
    year = int(year) # 년도는 정수로
    rate= float(rate) # 평점은 실수로
    #print(title,year,company,rate)
    
    #movie = Movie(title, year, company, rate)
    movie = Movie(title=title, year=year, company=company, rate=rate) # 데이터형 예외 발생
    return movie

#lst 변수는 list 타입이라고 지정
def get_movie(items :list):
    for item in items:
        print(item) # Movie 객체
        print('----------') # 각 영화 아이템별 구분 실선
        
    print(f'총 데이터 수 : {len(items)}개') # 총 영화 데이터 개수 

#폴더에 파일로 영화리스트 저장
def save_movie(items: list) :
    f = open('movie_db.txt', encoding='utf-8', mode='w') #파일 쓰기 모드

    for item in items:
        f.write(f'{item.getTitle()}|')
        f.write(f'{item.getYear()}|')
        f.write(f'{item.getCompany()}|')
        f.write(f'{item.getRate()}\n')
        
    f.close()
    
def load_movie(items : list):
    f = open('movie_db.txt', encoding='utf-8', mode='r') # 파일 읽기
    
    while True:
        line = f.readline().replace('\n','')  # 한줄 읽기 => 어벤져스 : 인피니티 워 |2000 |디즈니 |1.0
        if not line : break # 라인 없으면 무한루프 break로 인해 빠져나감 

        lines = line.split('|') # 구분자로 잘라서 네개의 요소 리스트 생성
        title = lines[0] 
        year = int(lines[1])
        company = lines[2]
        rate = float(lines[3]) #'8.6\n'
        
        movie = Movie(title, year, company, rate)
        items.append(movie)
                
    f.close()

def set_menu():
    str_menu = (f'영화 어플 v{VERSION}\n'
                '1. 영화 입력\n'
                '2. 영화 출력\n'
                '3. 영화 검색\n'
                '4. 영화 삭제\n'
                '5. 어플 종료\n')
    
    print(str_menu)
    
    # 1 ~ 5 외의 문자, 숫자,...예외처리
    try :
        sel_menu = int(input('메뉴 번호입력: ')) #예외있음
    except Exception as e :
        sel_menu = 0
        
    return sel_menu


if __name__ == '__main__':
    # print('------- 내 영화앱 시작 -------')
    run()
print('------- 프로그램 종료 -------')    






