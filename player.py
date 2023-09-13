import pygame

#creer une premiere classe qui va representer notre joueur
class Player(pygame.sprite.Sprite):

    def __init__(self):
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 2
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 400

    def move_right (self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity