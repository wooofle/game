import sys
import pygame as pg
import sprite as S
import config as C
from os import path


class Game:
    """Class to manage main game."""
    def __init__(self):
        """Initialise pygame and settings."""
        pg.init()
        self.screen = pg.display.set_mode((C.WIDTH, C.HEIGHT))
        pg.display.set_caption(C.TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        """Load map data as list of strings."""
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder, "map.txt"), "rt") as maplayout:
            for line in maplayout:
                self.map_data.append(line)

    def new(self):
        """Add docstring here."""
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
#        self.player = Player(self, 10, 10)
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == "1":
                    S.Wall(self, col, row)
                if tile == "P":
                    self.player = S.Player(self, col, row)

    def run(self):
        """Add docstring here."""
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(C.FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        """Quit program."""
        pg.quit()
        sys.exit()

    def update(self):
        """Add docstring here."""
        self.all_sprites.update()

    def draw_grid(self):
        """Add docstring here."""
        for x in range(0, C.WIDTH, C.TILESIZE):
            pg.draw.line(self.screen, C.LIGHTGRAY, (x, 0), (x, C.HEIGHT))
        for y in range(0, C.HEIGHT, C.TILESIZE):
            pg.draw.line(self.screen, C.LIGHTGRAY, (0, y), (C.WIDTH, y))

    def draw(self):
        """Add docstring here."""
        self.screen.fill(C.BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        """Add docstring here."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=1)
                if event.key == pg.K_UP:
                    self.player.move(dy=-1)
                if event.key == pg.K_DOWN:
                    self.player.move(dy=1)

    def show_start_screen(self):
        """Add docstring here."""
        pass

    def show_go_screen(self):
        """Add docstring here."""
        pass


g = Game()
g.show_start_screen()

# Main game loop
while True:
    g.new()
    g.run()
    g.show_go_screen()
