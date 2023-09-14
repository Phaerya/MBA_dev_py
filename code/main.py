import pygame, sys
from settings import * 
from level import Level
from overworld import Overworld
from ui import UI
import csv

class Game:
    def __init__(self):

        # game attributes
        self.max_level = 0		# Niveau de démarrage, 0 = lvl 1
        self.max_health = 100
        self.cur_health = 100
        self.coins = 0
        
        # audio 
        self.level_bg_music = pygame.mixer.Sound('../audio/stage.mp3')
        self.overworld_bg_music = pygame.mixer.Sound('../audio/overworld2.mp3')

        # overworld creation
        self.overworld = Overworld(0,self.max_level,screen,self.create_level)
        self.status = 'overworld'
        self.overworld_bg_music.play(loops = -1)

        # user interface 
        self.ui = UI(screen)

    def create_level(self,current_level):
        self.level = Level(current_level,screen,self.create_overworld,self.change_coins,self.change_health)
        self.status = 'level'
        self.overworld_bg_music.stop()
        self.level_bg_music.play(loops = -1)

    def create_overworld(self,current_level,new_max_level):
        if new_max_level > self.max_level:
            self.max_level = new_max_level
        self.overworld = Overworld(current_level,self.max_level,screen,self.create_level)
        self.status = 'overworld'
        self.overworld_bg_music.play(loops = -1)
        self.level_bg_music.stop()

    def change_coins(self,amount):
        self.coins += amount

    def change_health(self,amount):
        self.cur_health += amount

    def check_game_over(self):
        if self.cur_health <= 0:
            self.cur_health = 100
            self.coins = 0
            self.max_level = 0
            self.overworld = Overworld(0,self.max_level,screen,self.create_level)
            self.status = 'overworld'
            self.level_bg_music.stop()
            self.overworld_bg_music.play(loops = -1)

    def run(self):
        if self.status == 'overworld':
            self.overworld.run()
        else:
            self.level.run()
            self.ui.show_health(self.cur_health,self.max_health)
            self.ui.show_coins(self.coins)
            self.check_game_over()

# Appel de la fonction pour modifier les valeurs dans le fichier CSV
chemin_fichier = '../levels/0/level_0_terrain.csv'  # Chemin correct vers votre fichier CSV
ancienne_valeur = -1
nouvelle_valeur = 13

def modifier_valeurs_csv(chemin_fichier, ancienne_valeur, nouvelle_valeur):
    with open(chemin_fichier, 'r') as fichier_csv:
        lecteur_csv = csv.reader(fichier_csv)
        lignes = list(lecteur_csv)
    x=0
    for ligne in lignes:
        for i in range(len(ligne)):
            x+=1
            if int(ligne[i]) == ancienne_valeur  and (x==291 or x==292 or x==293): #and x< 289 and x>292
                ligne[i] = nouvelle_valeur

    with open(chemin_fichier, 'w', newline='') as fichier_modifie:
        ecrivain_csv = csv.writer(fichier_modifie)
        ecrivain_csv.writerows(lignes)
        
# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
game = Game()

while True:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                modifier_valeurs_csv(chemin_fichier, ancienne_valeur, nouvelle_valeur)
                game.create_level(0)

    screen.fill('grey')
    game.run()

    pygame.display.update()
    clock.tick(60)