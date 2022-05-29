import pygame

pygame.init()
#clock settings
clock = pygame.time.Clock()
fps = 60
#set screen
screen_width = 1200
screen_height = 710

IsJump = False
JumpCount = 10

x = 50
y = 50
x2 = 912
y2 = 50
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
player2_stay = pygame.image.load("assets/enemy/en1_stay.png")

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

class Player2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = 0


    def flip(self):
      self.image = pygame.transform.flip(player2_stay, True, False)

    def update(self):
        self.image.update()

class Player1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('assets/character/stay.png')
        self.image = pygame.transform.scale(img, (60, 80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        screen.blit(self.image, self)


player = Player1(x, y)

run = True
while run:

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and x > 1:
        x -= speed
    if keys[pygame.K_d] and x < 962:
        x += speed
    if keys[pygame.K_w] and y > 1:
        y -= speed
    if keys[pygame.K_s] and y < 470:
        y += speed

    #fps
    clock.tick(fps)

    screen.blit(background,(0,0))
    # screen.blit(player, (50, 50))
    # screen.blit(Player2, (x2, y2))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit()


