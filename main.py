import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
largeur, hauteur = 1400, 800

# Couleurs
blanc = (255, 255, 255)

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu Mario 2D du développeur")

# Chargement de l'image d'arrière-plan
background_image = pygame.image.load("assets/img.png")  # Remplacez par le chemin de votre image

# Redimensionnez l'image d'arrière-plan pour correspondre à la taille de la fenêtre
background_image = pygame.transform.scale(background_image, (largeur, hauteur))

# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Appui sur la touche "Échap"
                running = False

                
    # Dessine l'arrière-plan
    fenetre.blit(background_image, (0, 0))

    # Dessinez ici les éléments du jeu
    # ...

    # Met à jour l'affichage
    pygame.display.flip()

# Quitte Pygame
pygame.quit()
sys.exit()
