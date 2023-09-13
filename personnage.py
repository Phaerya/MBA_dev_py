import pygame

class Personnage(pygame.sprite.Sprite):
    def __init__(self, largeur, hauteur):
        super().__init__()
        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (largeur, hauteur)
        self.vitesse = 5

    def update(self):
        # Mettez à jour la logique du personnage ici
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect)
