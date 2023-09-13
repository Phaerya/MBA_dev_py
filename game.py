import pygame
from robot import Robot
pygame.init()

class Game:
    def __init__(self, largeur_fenetre, hauteur_fenetre ):
        self.robot = Robot(largeur_fenetre, hauteur_fenetre)