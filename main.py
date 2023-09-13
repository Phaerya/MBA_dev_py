import pygame
from game import Game

pygame.init()

# Dimensions de la fenêtre
largeur, hauteur = 1080, 700

# générer la fenêtre de notre jeu
screen = pygame.display.set_caption("Code Heroine")
screen = pygame.display.set_mode((largeur, hauteur))

#importer l'arrière plan de notre jeu
background = pygame.image.load('assets/Background.png')

# Redimensionnez l'image d'arrière-plan pour correspondre à la taille de la fenêtre
background = pygame.transform.scale(background, (largeur, hauteur))

#charger notre jeu
game = Game()

running = True

#boucle tant que cette condition est vrai
while running:

    #appliquer l'arrière plan
    screen.blit(background, (0,0))

    #appliquer l'image de notre joueur sur la fenetre du jeu
    screen.blit(game.player.image, game.player.rect)

    #verifier si le joueur souhaite aller a gauche ou a droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width< largeur:
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    #mettre à jour l'écran
    pygame.display.flip()

    #si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        #que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        #detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
