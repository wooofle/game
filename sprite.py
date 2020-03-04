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
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        """Move player sprite based off of difference in x and y coords."""
        if self.wall_collision(dx, dy):
            self.x += dx
            self.y += dy

    def update(self):
        """Update player sprite."""
        self.rect.x = self.x * C.TILESIZE
        self.rect.y = self.y * C.TILESIZE

    def wall_collision(self, dx=0, dy=0):
        """Detect player sprite collision with walls."""
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return False
        return True


class Wall(pg.sprite.Sprite):
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