import pygame

class Bullelvl0:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.image = pygame.image.load('../graphics/bulle/ert.png')
        self.image = pygame.transform.scale(self.image, (600, 350))
        self.rect = self.image.get_rect()
        self.rect.center = (350, screen_height - 420  )

    def draw(self):
        self.screen.blit(self.image, self.rect)
    

