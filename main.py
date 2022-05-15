import pygame

pygame.init()
#clock settings
clock = pygame.time.Clock()
fps = 60
#set screen
screen_width = 1200
screen_height = 710

x = 50
y= 50
speed = 5

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Petruxa Boycooha')

#load images
background = pygame.image.load('assets/bg/bg.jpg')
player_stay = pygame.image.load('assets/character/stay.png')
obrez = pygame.image.load('assets/platforms/obrez.png')
obrez2 = pygame.image.load('assets/platforms/obrez2.png')
block = pygame.image.load('assets/platforms/block1.png')
block = pygame.image.load('assets/platforms/block2.png')

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

class Player(pygame.sprite.Sprite):
    right = True


run = True
while run:

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 1:
        x -= speed
    elif keys[pygame.K_RIGHT] and x < 962:
        x += speed
    elif keys[pygame.K_UP] and y > 1:
        y -= speed
    elif keys[pygame.K_DOWN] and y < 470:
        y += speed

    #fps
    clock.tick(fps)

    screen.blit(background,(0,0))
    screen.blit(player_stay, (x, y))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()


