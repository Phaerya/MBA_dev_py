import pygame

class Bullelvl01:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.image = pygame.image.load('../graphics/bulle/oppo.png')
        self.image = pygame.transform.scale(self.image, (350, 400))
        self.rect = self.image.get_rect()
        self.rect.center = (1600, screen_height - 250  )

    def draw(self):
        self.screen.blit(self.image, self.rect)
    

