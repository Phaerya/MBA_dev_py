import pygame, sys
from settings import *
from level import Level
from overworld import Overworld
from ui import UI


class Game:
    def __init__(self):

        # game attributes
        self.max_level = 0  # Niveau de démarrage, 0 = lvl 1
        self.max_health = 100
        self.cur_health = 100
        self.coins = 0

        # audio
        self.level_bg_music = pygame.mixer.Sound('../audio/stage.mp3')
        self.menu_bg_music = pygame.mixer.Sound('../audio/intro2.mp3')
        self.menu_bg_music.play(loops=-1)
        self.overworld_bg_music = pygame.mixer.Sound('../audio/overworld2.mp3')
        self.overworld_bg_music.set_volume(0.4)

        # overworld creation
        self.overworld = Overworld(0, self.max_level, screen, self.create_level)
        self.status = 'overworld'
        # self.overworld_bg_music.play(loops = -1)

        # user interface
        self.ui = UI(screen)

        self.start_button = pygame.image.load('../graphics/main_menu/start_button.png')
        self.start_button_rect = self.start_button.get_rect(center=(screen_width // 2, screen_height // 2))
        self.in_menu = True  # Add a menu state

    def create_level(self, current_level):
        self.reset_coins()
        self.level = Level(current_level, screen, self.create_overworld, self.change_coins, self.change_health)
        self.status = 'level'
        self.overworld_bg_music.stop()
        self.level_bg_music.play(loops=-1)

    def create_overworld(self, current_level, new_max_level):
        if new_max_level > self.max_level:
            self.max_level = new_max_level
        self.overworld = Overworld(current_level, self.max_level, screen, self.create_level)
        self.status = 'overworld'
        self.overworld_bg_music.play(loops=-1)
        self.level_bg_music.stop()

    def change_coins(self, amount):
        self.coins += amount

    def reset_coins(self):
        self.coins = 0

    def change_health(self, amount):
        self.cur_health += amount

    def check_game_over(self):
        if self.cur_health <= 0:
            self.cur_health = 100
            self.coins = 0
            self.max_level = 0
            self.overworld = Overworld(0, self.max_level, screen, self.create_level)
            self.status = 'overworld'
            self.level_bg_music.stop()
            self.overworld_bg_music.play(loops=-1)

    def run(self):
        if self.in_menu:
            self.show_menu()
        elif self.status == 'overworld':
            self.overworld.run()
        else:
            self.level.run()
            self.ui.show_health(self.cur_health, self.max_health)
            self.ui.show_keys(self.coins)
            self.check_game_over()

    def show_menu(self):
        # Draw the Start button
        screen.blit(self.start_button, self.start_button_rect)

    def handle_menu_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.in_menu = False
                self.overworld_bg_music.play(loops=-1)
                self.menu_bg_music.stop()


# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game.in_menu:
            game.handle_menu_events(event)

    screen.fill('grey')
    game.run()

    pygame.display.update()
    clock.tick(60)
