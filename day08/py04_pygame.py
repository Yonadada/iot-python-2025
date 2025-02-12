#py04_pygame.py
#마우스 이벤트

import pygame 
from pygame.locals import QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION 
import sys 

pygame.init()
Surface = pygame.display.set_mode((640,400))
FPSCLOCK = pygame.time.Clock() 
pygame.display.set_caption('Pygame Mouse') 

def main():
    pos = []
    check = mousebutton = False
    
    while True:
        Surface.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()   
                sys.exit()  
            elif event.type == MOUSEBUTTONDOWN: 
                # pos.append(event.pos)
                check = True
                mousebutton = True
            elif event.type == MOUSEMOTION:
                if mousebutton : pos.append(event.pos)
            elif event.type == MOUSEBUTTONUP:
                mousebutton = False
                check = False
                pos.clear()
                    
        # for mpos in pos:
        #     pygame.draw.circle(Surface,'white',mpos, 5)   
        
        # check는 마우스 버튼이 눌려있는지(True) / 떼어졌는지(False)
        if check: # check 마우스버튼이 눌려져 있는 동안만 True
            if len(pos) > 1:
                pygame.draw.lines(Surface, 'white', False, pos)  # MOUSEBUTTONUP의 check = false랑 다름   
            
        pygame.display.update()  
        FPSCLOCK.tick(30)
        
if __name__ == '__main__':
    main()      