# py02_pygame.py
#PyGame 그래픽 표현(선, 사각형,...)

import pygame 
from pygame.locals import QUIT 
from pygame.draw import * # pygame.draw 생략
import pygame.image as image
import sys 

# 기본 변수 
pygame.init()
Surface = pygame.display.set_mode((400,400))
FPSCLOCK = pygame.time.Clock() 
pygame.display.set_caption('Pygame Basic') 

def main():
    # 이미지
    snake = image.load('./image/snake.png')
    
    # 텍스트 변수
    myfont = pygame.font.SysFont('NamuGothic', 50)
    message1 = myfont.render('This is my message', True, (255, 150, 255))
    message2 = myfont.render('This is my Pygame', False, (255, 150, 255))
    
    
    while True:
        Surface.fill(color='black') #  Surface.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()   
                sys.exit()  
        
        #(시작값, 끝 값, 간격)
        for x in range(10, 400, 10):
            line(Surface, 'white', (x,0), (x,400))
        
        for y in range(10, 400, 10):
            line(Surface, 'white', (0,y), (400,y)) 

        # 선
        # (화면표현, start_pos, end_pos)두께
        pygame.draw.line(Surface, color='#ED503D', start_pos=(30,30), end_pos=(150,30), width=3)
        line(Surface, (0,255,0), (30,70), (150,70), 5) # 좌표측이 같으면 직석
        line(Surface, ('#0E3FC6'), (30,90), (150,150), 7) #좌표측이 동일하지 않으면 대각선
        
        
        # 사각형 
        pygame.draw.rect(Surface,color='white', rect=(200,30,50,50))
        rect(Surface, (255,0,0), (260,30,100,50), 3) #(Surface,(색깔),(x축, y축, width, height) 두께)  
        
        # 원, 타원 (중심을 시작점으로)
        pygame.draw.circle(Surface, (255,255,0), (40,180), 10) # 화면표현, 색상, (x,y), 반지름
        circle(Surface,(255,255,255), (80, 180), 20) 
        circle(Surface, (255, 122, 20), (280,160), 30, 10) # 화면표현, 색상, (x,y), 반지름, 두께
        
        # 타원
        # (화면표현, 색상, (x,y,넓이,높이) 두께
        pygame.draw.ellipse(Surface, color=(255,255,255), rect=(280, 180, 100, 50)) 
        ellipse(Surface, (255,255,0), (280,300,100,50), 10) # 노란색타원
        
        # polygon 다각형(별 등,...)
        
        #이미지 flaticon.com
        Surface.blit(snake, (336,336)) # 400이 끝이라 - 64사이즈 사진
        Surface.blit(snake, (0,336), (0,0,64,32))
        
        # 텍스트
        Surface.blit(message1, (30, 230))
        Surface.blit(message2, (30, 280))
        
        
        
        pygame.display.update()  
        FPSCLOCK.tick(30)
        
if __name__ == '__main__':
    main()      