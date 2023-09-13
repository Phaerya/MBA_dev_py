from pygame.sprite import Sprite
from pygame import Surface
from pygame.key import get_pressed
import pygame

class Player(Sprite):
    def __init__(self):
        super().__init__() 
        self.character = Surface((24, 24))
        self.image = self.image = image_scale(load_image("./assets/robot/Armature_Idle_00.png"), (200,200))
        self.rect = self.image.get_rect(bottomleft=(0,0))

    def update(self, surf):
        keys = get_pressed()
        self.rect.x += (keys[pygame.K_d]-keys[pygame.K_a]) * 5
        self.rect.y += (keys[pygame.K_s]-keys[pygame.K_w]) * 5
        self.rect.clamp_ip(surf.get_rect())