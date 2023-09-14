import pygame
from game import Game
from bubble import Bubble
from arrow import Arrow
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

# Variables pour suivre le temps de secousse
start_time = pygame.time.get_ticks()
shake_duration = 500  # 500 ms, soit .5 secondes

# Création des instance de class
game = Game(largeur, hauteur)
bubble = Bubble()
arrow = Arrow()

message = "Bonjour, je suis votre robotd"

# Variable pour suivre si la bulle a été affichée
bubble_displayed = False

# Boucle principale du jeu
running = True
while running:
    fenetre.fill(blanc)

    # Obtenez le temps actuel
    current_time = pygame.time.get_ticks()

    # Vérifiez si nous sommes dans la période de secousse
    if current_time - start_time < shake_duration:
        game.robot.vibrate()
    elif current_time - start_time >= shake_duration and not bubble_displayed:
        print("Trying to display bubble...")
        bubble_displayed = True

    fenetre.blit(background_image, (0, 0))
    fenetre.blit(game.robot.image, game.robot.rect)

    # Dessinez ici les éléments du jeu
    # ...
    
    if bubble_displayed:
        bubble.draw(fenetre, message, game.robot.rect.x + game.robot.rect.width / 2, game.robot.rect.y)
        arrow.draw(fenetre, game.robot.rect.x + game.robot.rect.width / 2 + 20, game.robot.rect.y + 10)

    # Met à jour l'affichage
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif arrow.handle_event(event):
            bubble_displayed = False
            print("bubble_displayed réglé sur False")

# Quitte Pygame
pygame.quit()
sys.exit()