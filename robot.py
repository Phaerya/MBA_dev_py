import pygame
import random
from bubble import Bubble
pygame.init()

class Robot(pygame.sprite.Sprite):
    def __init__(self, largeur_fenetre, hauteur_fenetre ):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = largeur_fenetre - self.rect.width
        self.rect.y = hauteur_fenetre - self.rect.height
        self.original_x = self.rect.x

    def vibrate(self):
        self.rect.x = self.original_x + random.randint(-5, 5)
        
# Lorsque vous créez votre robot, passez les dimensions de la fenêtre comme arguments
largeur_fenetre = 1400
hauteur_fenetre = 800
robot = Robot(largeur_fenetre, hauteur_fenetre)