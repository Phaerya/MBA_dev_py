from pygame.mixer_music import load as music_load
from pygame.mixer_music import play as music_play

class MusicPlayer():
    
    def intro(self):
        music_load.load('./music/intro.mp3')
        music_play(loops=1)