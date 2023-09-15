import pygame, sys
from settings import * 
from level import Level
from overworld import Overworld
from ui import UI
import csv

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

class Game:
    def __init__(self):

        # game attributes
        self.max_level = 0		# Niveau de démarrage, 0 = lvl 1
        self.max_health = 100
        self.cur_health = 100
        self.coins = 0

        # audio
        self.level_bg_music = pygame.mixer.Sound('../audio/stage.mp3')
        self.menu_bg_music = pygame.mixer.Sound('../audio/intro2.mp3')
        self.menu_bg_music.play(loops = -1)
        self.overworld_bg_music = pygame.mixer.Sound('../audio/overworld2.mp3')
        self.overworld_bg_music.set_volume(0.4)

        # overworld creation
        self.overworld = Overworld(0,self.max_level,screen,self.create_level)
        self.status = 'overworld'
        # self.overworld_bg_music.play(loops = -1)

        # user interface
        self.ui = UI(screen)

        self.image_list = [
            pygame.image.load('../graphics/main_menu/start_button.png'),
            pygame.image.load('../graphics/main_menu/start_button_2.png'),
        ]
        self.image_index = 0
        self.image_change_time = pygame.time.get_ticks()

        self.title_list = [
            pygame.image.load('../graphics/main_menu/title_1.png'),
            pygame.image.load('../graphics/main_menu/title_2.png'),
            pygame.image.load('../graphics/main_menu/title_3.png'),
            pygame.image.load('../graphics/main_menu/title_4.png'),
            pygame.image.load('../graphics/main_menu/title_5.png'),
            pygame.image.load('../graphics/main_menu/title_6.png'),
            pygame.image.load('../graphics/main_menu/title_7.png'),
            pygame.image.load('../graphics/main_menu/title_8.png'),
            pygame.image.load('../graphics/main_menu/title_9.png'),
            pygame.image.load('../graphics/main_menu/title_10.png'),
            pygame.image.load('../graphics/main_menu/title_11.png'),
            pygame.image.load('../graphics/main_menu/title_12.png'),
            pygame.image.load('../graphics/main_menu/title_13.png'),
        ]
        self.title_index = 0
        self.title_change_time = pygame.time.get_ticks()

        screen.blit(background_image, (0, 0))

        self.title = pygame.image.load('../graphics/main_menu/title_1.png')
        self.title_rect = self.title.get_rect(center=(screen_width // 2, screen_height // 2))

        self.start_button = pygame.image.load('../graphics/main_menu/start_button.png')
        self.start_button_rect = self.start_button.get_rect(center=(screen_width // 2, screen_height // 1.8))

        self.in_menu = True  # Add a menu state

    def create_level(self,current_level):
        self.reset_coins()
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

    def reset_coins(self):
        self.coins = 0

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
        if self.in_menu:
            self.show_menu()
        elif self.status == 'overworld':
            self.overworld.run()
        else:
            self.level.run()
            self.ui.show_health(self.cur_health, self.max_health)
            self.ui.show_coins(self.coins)
            self.check_game_over()

    def show_menu(self):
        current_time = pygame.time.get_ticks()

        # Check if 500ms have passed since the last image change for the start_button
        time_elapsed_start_button = current_time - self.image_change_time
        if time_elapsed_start_button >= 500:
            self.image_index = (self.image_index + 1) % len(self.image_list)
            self.image_change_time = current_time

        # Check if 200ms have passed since the last title change
        time_elapsed_title = current_time - self.title_change_time
        if time_elapsed_title >= 200:
            self.title_index = (self.title_index + 1) % len(self.title_list)
            self.title_change_time = current_time

        current_image = self.image_list[self.image_index]
        screen.blit(current_image, self.start_button_rect)

        # Display the current title image
        current_title = self.title_list[self.title_index]
        screen.blit(current_title, self.title_rect)

    def handle_menu_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.in_menu = False
                self.overworld_bg_music.play(loops=-1)
                self.menu_bg_music.stop()

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
background_image = pygame.image.load('../graphics/main_menu/start_screen.png')
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

clock = pygame.time.Clock()
game = Game()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                modifier_valeurs_csv(chemin_fichier, ancienne_valeur, nouvelle_valeur)
                game.create_level(0)

        if game.in_menu:
            game.handle_menu_events(event)

    game.run()
    pygame.display.update()
    clock.tick(60)