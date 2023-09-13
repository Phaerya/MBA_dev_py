from pygame.mixer import init as music_init
from pygame.mixer_music import load as music_load
from pygame.mixer_music import play as music_play
from pygame.mixer_music import stop as music_stop

class GameMusic():
    
    def play(self, music_file):
        music_load(music_file)
        music_play()
    
    def stop():
        music_stop()