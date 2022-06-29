from random import random
from secrets import choice
import pygame
import time
pygame.init()

#screen
X = 700
Y = 700
screen = pygame.display.set_mode((X,Y))
#BACKGROUND
background = pygame.Color(20,20,20)
pygame.display.set_caption("CAR GAME")

#LINING
# line_x = 0
line_y = 0
line = pygame.image.load("line2.png").convert_alpha()


#CAR
car = pygame.image.load("1.PNG").convert_alpha()
cropped_car = pygame.transform.scale(car,(120,200))
car_x = 350
car_y = 510

#fence
fence = pygame.image.load("fence.png").convert_alpha()
random_fence_x = choice((0,1,2,3)) #0,180,360,540
fence_x = random_fence_x * 175
fence_y = 120
def fence_pos():
    global fence_y
    fence_y += 120

# text
myfont = pygame.font.Font("freesansbold.ttf",100)
render_text = myfont.render("Car Crashed" , False,(0,0,0))


running = True 
while running: 
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car_x -= 175 
                fence_pos()
                line_y +=100
                if car_x < 0:
                    car_x+=175
            if event.key == pygame.K_RIGHT:
                car_x += 175 
                line_y +=100
                fence_pos()
                if car_x > 525:
                    car_x-=175
    
    if fence_y > 700:
        fence_y=120
        random_fence_x = choice((0,1,2,3))
        fence_x = random_fence_x * 180

        fence_reappear()

    if line_y>400:
        line_y = 0

    if car_x-fence_x <50 and car_x - fence_x > -180:
        if car_y - fence_y < 120 and car_y -fence_y > -110:
            screen.blit(render_text,(80,200))
            pygame.display.update()
    # BG color
    screen.fill(background)


    #LINES
    screen.blit(line, ( 700/4 , line_y + 35) )
    screen.blit(line, ( 700/4 , line_y + 375) )
    screen.blit(line, ( 700/2 , line_y + 35) )
    screen.blit(line, ( 700/2 , line_y + 375) )
    screen.blit(line, ( 700/4*3 ,line_y + 35) )
    screen.blit(line, ( 700/4*3 ,line_y + 375) )

    #CAR
    screen.blit(cropped_car,(car_x,car_y))

    #fence
    def fence_reappear():
        screen.blit(fence,(fence_x,fence_y))
        
    # timer = threading.Timer(9,fence_pos)
    # timer.start()
    fence_reappear()
    pygame.display.update()