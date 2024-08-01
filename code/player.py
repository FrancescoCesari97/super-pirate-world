
from typing import Any
from settings import *

class PLayer(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.Surface((48, 56))
        self.image.fill('red')

    # * rects
        self.rect = self.image.get_frect(topleft = pos)
        self.old_rect = self.rect.copy

    # *movement
        self.direction = vector()
        self.speed = 150
        self.gravity = 1000
    
    # * collisoin
        self.collision_sprites = collision_sprites



    def input(self):
        keys = pygame.key.get_pressed()
        input_vector = vector(0,0)
        if keys[pygame.K_d]:
            input_vector.x += 1

        if keys[pygame.K_a]:
            input_vector.x -= 1
        
        self.direction.x = input_vector.normalize().x if input_vector else input_vector.x

    def move(self, dt):
        # * horizontal
        self.rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')

        # *vertical
        self.direction.y += self.gravity / 2 * dt
        self.rect.y += self.direction.y * dt
        self.direction.y += self.gravity / 2 * dt
        self.collision('vertical')
    
    def collision(self, axis):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                if axis == 'horizontal':
                    # * left
                    if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                        self.rect.left = sprite.rect.right
                  
                    # * right
                    if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
                        self.rect.right = sprite.rect.left

                else: 
                    pass

    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.input()
        self.move(dt)