# py01_pygame.py
import pygame # pygame 기본모듈 추가
from pygame.locals import QUIT # 종료처리 변수
import sys # 운영체제 시스템 명령 => ex) sys.executable 실행시 파이썬 설치 경로 알 수 약있음

# 기본 변수 
pygame.init()
Surface = pygame.display.set_mode((640,400)) ## 예시) tkinter == root.geometry('640x400')
FPSCLOCK = pygame.time.Clock() # 초당 화면 프레임을 몇번 보여줄 것인가
pygame.display.set_caption('Pygame Basic') # 예시) tkinter == root.title('Pygame Basic')

def main():
    while True:
        Surface.fill((255,180,255)) # 색깔로 채우겠다.  ex) FFFFFF == white, #0000000 / #00FFFFFF
        for event in pygame.event.get(): # 키보드, 마우스 이벤트 체크
            if event.type == QUIT: # WM_DELETE_WINDOW
                pygame.quit()   #Pygame을 종료
                sys.exit()  # 윈도우앱 탈출
        
        pygame.display.update() # 지금까지 작성한 코드를 윈도우창에 표시 
        FPSCLOCK.tick(30) # 30FPS로 지정(1초에 30번 화면에 노출) 
        
if __name__ == '__main__':
    main()            