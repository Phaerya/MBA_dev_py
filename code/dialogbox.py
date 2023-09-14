from pygame import Surface
from pygame.display import get_surface
from pygame.font import Font
from pygame.draw import rect
from pygame import Rect
from pygame.time import delay
from pygame.display import update

class DialogBox:
    def __init__(self, x, y, w, h, text):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.surf = Surface((w, h))
        self.surf.fill("black")
        self.rect = self.surf.get_rect(topleft = (x, y))

        self.text = text
        self.index = 0

        self.font = Font(None, 50)


    def render(self):
        ### Dialog box
        get_surface().blit(self.surf, self.rect)
        rect(self.surf, "white", Rect(0, 0, 1000, 250), 4)
        ###

        ### Text
        y = 25
        lines = self.text.split("\n")
        for line in lines:
            for i in range(len(line)):
                delay(35)
                font_surf = self.font.render(line[0:i+1], False, "white")
                font_rect = font_surf.get_rect(topleft = (25, y))
                self.surf.blit(font_surf, font_rect)
                update()
            y += 50
        ###