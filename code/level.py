
from settings import *
from sprites import *
from player import *

class Level: 
    def __init__(self, tmx_map):
        self.display_surface = pygame.display.get_surface()

        # *groups
        self.all_sprites = pygame.sprite.Group()

        self.setup(tmx_map)
    
    def setup(self, tmx_map):
        for x, y, surf, in tmx_map.get_layer_by_name('Terrain').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)

        for obj in tmx_map.get_layer_by_name('Objects'):
            if obj.name == 'player':
                PLayer((obj.x, obj.y), surf, self.all_sprites)

    def run(self):
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)