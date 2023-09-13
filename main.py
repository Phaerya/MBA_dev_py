import pygame
import sys
from classes.robot_npc import Robot
from classes.music import GameMusic
from personnage import Personnage
# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
largeur, hauteur = 1400, 800

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu Mario 2D du développeur")

# Chargement de l'image d'arrière-plan
background_image = pygame.image.load("assets/img.png")  # Remplacez par le chemin de votre image

# Redimensionnez l'image d'arrière-plan pour correspondre à la taille de la fenêtre
background_image = pygame.transform.scale(background_image, (largeur, hauteur))

# Création du personnage
personnage = Personnage(largeur // 2, hauteur // 2)

# Création du groupe de sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(personnage)

# Boucle principale du jeu

robot = Robot()
music = GameMusic()
all_sprites.add(robot)

running = True
music.play("./assets/music/intro.mp3")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dessine l'arrière-plan
    fenetre.blit(background_image, (0, 0))

    # Mettez à jour le groupe de sprites
    all_sprites.update()

    # Dessinez le groupe de sprites
    all_sprites.draw(fenetre)

    # Met à jour l'affichage
    pygame.display.flip()

# Quitte Pygame
pygame.quit()
sys.exit()
