import pygame

class Bulle:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.image = pygame.image.load('../graphics/bulle/rrrrr.png')
        self.image = pygame.transform.scale(self.image, (600, 300))
        self.rect = self.image.get_rect()
        self.rect.center = (200, screen_height // 2)

    def draw(self):
        self.screen.blit(self.image, self.rect)
    

