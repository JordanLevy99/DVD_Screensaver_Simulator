import pygame
import random
import sys

width = 640
height = 480

screen = pygame.display.set_mode((width, height))
player = pygame.image.load('Pygame_tests/dvd.png')
background = pygame.image.load('Pygame_tests/background.jpg')
position = player.get_rect()


def mvmt_gen():
    sign_x = random.choice([-1,1])
    sign_y = random.choice([-1,1])
    mag = random.randint(5,10)
    return (sign_x * mag * random.random(), sign_y * mag *random.random())

mvmts = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]

mvmt = mvmt_gen()
print(mvmt)





while 1:
    for event in pygame.event.get():
        if event.type in (pygame.QUIT, pygame.KEYDOWN):
            sys.exit()
    screen.blit(background, position, position) #erase

    x, y, size_x, size_y = position[0], position[1], position[2], position[3]
    while x > (width - size_x) or x < 0 or y<0 or y > (height - size_y):
        mvmt = mvmt_gen()
        print(mvmt)
        new_position = position.move(mvmt)
        x, y, size_x, size_y = new_position[0], new_position[1], new_position[2], new_position[3]


    position = position.move(mvmt)
    screen.blit(player, position)
    pygame.display.update()
