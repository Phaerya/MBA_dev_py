from pygame.sprite import Sprite
from pygame.image import load as load_image
from pygame.transform import scale as image_scale
import pygame

class Robot(Sprite):
    def __init__(self):
        super().__init__() 
        self.image = image_scale(load_image("./assets/robot/Armature_Idle_00.png"), (200,200))
        self.rect = self.image.get_rect(topleft=(1200,0))