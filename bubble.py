import pygame

from textwrap import wrap

class Bubble:
    def __init__(self):
        self.bubble_image_original = pygame.image.load('assets/bulles/bulles1.png')
        self.margin = 20  # Marge autour du texte

    def draw(self, window, message, x, y):
        font = pygame.font.Font(None, 36)

        # Wrapper le texte si une ligne dépasse 200 pixels de largeur
        wrapped_message = wrap(message, 30)  # Ajustez le deuxième argument pour obtenir une largeur approximative de 200px
        wrapped_message = '\n'.join(wrapped_message)

        text_surface = font.render(wrapped_message, True, (0, 0, 0))
        
        text_width, text_height = text_surface.get_size()
        
        bubble_width = max(text_width * 2, text_width + self.margin * 2)
        bubble_height = max(text_height * 2, text_height + self.margin * 2)
        
        bubble_image = pygame.transform.scale(self.bubble_image_original, (bubble_width, bubble_height))
        
        bubble_x = x - bubble_width - 20
        bubble_y = y - bubble_height - 60
        
        window.blit(bubble_image, (bubble_x, bubble_y))
        window.blit(text_surface, (bubble_x + bubble_width / 2 - text_width / 2, bubble_y + bubble_height / 2 - text_height / 2))
