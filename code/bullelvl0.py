import pygame

class Bullelvl0:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.image = pygame.image.load('../graphics/bulle/test45.png')
        self.image = pygame.transform.scale(self.image, (800, 400))
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2 , screen_height - 530  )

    def draw(self):
        self.screen.blit(self.image, self.rect)
    

