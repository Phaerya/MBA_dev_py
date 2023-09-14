import pygame

class Arrow:
    def __init__(self):
        self.image = pygame.image.load('assets/arrow.png')
        self.image = pygame.transform.scale(self.image, (40, 40))  # Redimensionner l'image à 40x40 pixels
        self.rect = self.image.get_rect()
        self.margin = 20  # Marge autour du texte

    def draw(self, fenetre, x, y):
        self.rect.topleft = (x, y)
        fenetre.blit(self.image, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                print("Clic détecté sur la flèche")
                return True
        return False

