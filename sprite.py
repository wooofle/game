import pygame as pg
import config as C


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        """Initialise player sprite."""
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((C.TILESIZE, C.TILESIZE))
        self.image.fill(C.RED)
        self.rect = self.image.get_rect()
        self.x = x * C.TILESIZE
        self.y = y * C.TILESIZE

#    def move(self, dx=0, dy=0):
#        """Move player sprite based off of difference in x and y coords."""
#        if self.wall_collision(dx, dy):
#            self.x += dx
#            self.y += dy

    def update(self):
        """Update player sprite."""
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.topleft = (self.x, self.y)
    # Checks wall collusion withing update function
        if pg.sprite.spritecollideany(self, self.game.walls):
            self.x -= self.vx * self.game.dt
            self.y -= self.vy * self.game.dt
            self.rect.x = self.x
            self.wall_collision('x')
            self.rect.y = self.y
            self.wall_collision('y')

# self note if diagonal movement is added the correct number to fix the speed of it "7071"
    def get_keys(self):
        """Detects if the keys are pressed and makes the character move according to keys pressed"""
        self.vx = 0
        self.vy = 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vx = -C.MOVEMENT_SPEED
        elif keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx = C.MOVEMENT_SPEED
        elif keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vy = C.MOVEMENT_SPEED
        elif keys[pg.K_UP] or keys[pg.K_w]:
            self.vy = -C.MOVEMENT_SPEED

    def wall_collision(self, direction):
        """Detect player sprite collision with walls."""
#        if direction == 'x':
#            hit = pg.sprite.spritecollide(self, self.game.walls, False)
#            if self.vx > 0:
#                self.x = hit[0].rect.left - self.rect.width
#            if self.vx < 0:
#                self.x = hit[0].self.rect.height
#            self.vx = 0
#            self.rect.x = self.x
#        if direction == 'y':
#            hit = pg.sprite.spritecollide(self, self.game.walls, False)
#            if self.vy > 0:
#                self.y = hit[0].rect.top - self.rect.height
#            if self.y < 0:
#                self.y = hit[0].self.rect.bottom
#            self.vy = 0
#            self.rect.y =# self.y

class Wall(pg.sprite.Sprite):
    """Creates background grids"""
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((C.TILESIZE, C.TILESIZE))
        self.image.fill(C.WHITE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * C.TILESIZE
        self.rect.y = y * C.TILESIZE