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

block_size = 32

map_data = []
with open('../levels/1/level_1_terrain.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        map_data.append(list(map(int, row)))

# Define the CSV cell coordinates where you want to add blocks
# For example, here we're using row_index and column_index
row_index = 8
column_index = 8


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
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_e:
                # Specify the row and column indices in the CSV where you want to replace a value
				row_index = 8
				column_index = 8

                # Specify the new value you want to set in the CSV
				new_value = 1  # Replace with the value you want

                # Update the CSV data with the new value
				map_data[row_index][column_index] = new_value

	screen.fill('grey')
	screen.fill((0, 0, 0))

	for row_index, row in enumerate(map_data):
		for column_index, value in enumerate(row):
			if value != -1:  # Skip empty cells
				block_color = (255, 255, 255)  # Change the color as needed
				pygame.draw.rect(screen, block_color, pygame.Rect(column_index * block_size, row_index * block_size, block_size, block_size))
				
	game.run()

	pygame.display.update()
	clock.tick(60)