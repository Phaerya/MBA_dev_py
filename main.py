import pygame
pygame.init()

#creer une premiere classe qui va representer notre joueru
class Player:

    def __init__(self):
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5

# générer la fenêtre de notre jeu
pygame.display.set_caption("Code Heroine")
pygame.display;set_mode((1080,720))

#importer l'arrière plan de notre jeu
background = pygame.image.load('assets/Background.png')

running = True

#boucle tant que cette condition est vrai
while running:

    #appliquer l'arrière plan
    screen.blit(background, (0,0))

    #mettre à jour l'écran
    pygame.display.flip()

    #si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
