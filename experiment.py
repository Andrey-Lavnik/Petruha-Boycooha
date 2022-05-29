class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/blob.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1


def reset_level(level):
    player.reset(100, screen_height - 130)
    blob_group.empty()
    platform_group.empty()
    coin_group.empty()
    lava_group.empty()
    exit_group.empty()



class Player():
    def __init__(self, x, y):
        self.reset(x, y)

    def update(self, game_over):
        # check for collision with enemies
        if pygame.sprite.spritecollide(self, blob_group, False):
            game_over = -1
            game_over_fx.play()


row_count = 0
for row in data:
     col_count = 0
     for tile in row:
         if tile == 3:
             blob = Enemy(col_count * tile_size, row_count * tile_size + 15)
             blob_group.add(blob)

blob_group = pygame.sprite.Group()

run = True

while run:

    if game_over == 0:
        blob_group.update()

    blob_group.draw(screen)


    #warrior

    # function for drawing fighter health bars
    def draw_health_bar(health, x, y):
        ratio = health / 100
        pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
        pygame.draw.rect(screen, RED, (x, y, 400, 30))
        pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))


#ensure players face each other
    if target.rect.centerx > self.rect.centerx:
      self.flip = False
    else:
      self.flip = True