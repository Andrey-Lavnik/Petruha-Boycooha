import pygame

pygame.init()
#clock settings
clock = pygame.time.Clock()
fps = 60
#set screen
screen_width = 1200
screen_height = 710

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Petruxa Boycooha')

#load images
background = pygame.image.load('assets/bg/bg.jpg')

#define variables


class Calculations():
    def __init__(self):
        self.kills = 0
        self.sekundomer = 0
        self.lifes = 3
        self.ticks = 0

    def update(self):
        self.ticks = pygame.time.get_ticks()
        self.sekundomer += self.ticks // 1000


run = True
while run:
    #fps
    clock.tick(fps)

    screen.blit(background,(0,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()


