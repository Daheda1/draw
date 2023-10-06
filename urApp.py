import pygame
from datetime import datetime
import math

def Main() -> None:
    pygame.display.set_mode()
    pygame.display.set_caption('Ur application')    #Sætter navnet på apilicationen

    pygame.init()
    screen = pygame.display.set_mode((500, 500))    #Sætter størrelsen på vinduet

    background = (255, 255, 255)
    sort = (0, 0, 0)
    red = (255, 0, 0)
    center = (screen.get_width()/2, screen.get_height()/2)
    watch_face(screen, sort, center, background)    #Tegner en cirkel med streger der indikere minutter og timer

    run_flag = True
    while run_flag is True:
        watch_hands(screen, center, background, sort, red)  #Tegner ur hænderne på det rigtige tidspunkt
        pygame.time.wait(20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_flag = False
        pygame.display.flip()


#Tegnerer alle linjer på cirklen
def watch_face(screen, sort: tuple, center: tuple, background: tuple):
    screen.fill(background)

    for x in range(12): #Tegner time streger
        pygame.draw.line(screen, sort, center, calc_pos(center, x, 198, 30), 8) 
        watch_numbers(screen, center,  sort, x)

    for x in range(60): #Tegner minut streger
        pygame.draw.line(screen, sort, center, calc_pos(center, x, 198, 6), 1)

    pygame.draw.circle(screen, sort, center, 200, 6) # Tegner yderste cirkel

#Tegnerer ur hænder
def watch_hands(screen, center: tuple, background: tuple, sort: tuple, red: tuple):
    pygame.draw.circle(screen, background, center, 180) # Tegner over tidligere ur hænder

    currentDateAndTime = datetime.now()
    microsecond = currentDateAndTime.microsecond
    second  = currentDateAndTime.second + (microsecond/1000000)
    minute  = currentDateAndTime.minute + (second/6)*0.1
    hour    = (currentDateAndTime.hour % 12) + (minute/6)*0.1

    pygame.draw.line(screen, sort, center, calc_pos(center, hour,   100, 30), 4) # Hour hand
    pygame.draw.line(screen, sort, center, calc_pos(center, minute, 150, 6), 4) # Minute Hand
    pygame.draw.line(screen, red , center, calc_pos(center, second, 150, 6), 2) # Second hand

#Tegner numre på uret
def watch_numbers(screen, center: tuple,  sort: tuple, num):
    if num == 0:
        num = 12
    font = pygame.font.SysFont(None, 40)
    text = font.render(str(num), True, sort)
    x, y = calc_pos(center, num, 220, 30)
    x = x - (text.get_rect().width/2) #Trækker halv brede fra så den ikke tegner dem for langt til højre
    y = y - (text.get_rect().height/2)
    screen.blit(text, (x, y))


#Beregner den nye vektor slutpostion
def calc_pos(center: tuple, time: int, radius: int, parts: int) -> tuple :
    angle = ((time-15) * parts)
    newx = radius * math.cos(math.radians(angle)) + center[0]
    newy = radius * math.sin(math.radians(angle)) + center[1]

    return (newx, newy)

Main()
