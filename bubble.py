import pygame

from textwrap import wrap

class Bubble:
    def __init__(self):
        self.bubble_image_original = pygame.image.load('assets/bulles/bulles1.png')
        self.margin = 20  # Marge autour du texte

    def draw(self, window, message, x, y):
        window_width, window_height = window.get_size()
        font = pygame.font.Font(None, 20)

        # Wrapper le texte si une ligne dépasse 200 pixels de largeur
        wrapped_message = wrap(message, 30)
        wrapped_message = '\n'.join(wrapped_message)

        text_surface = font.render(wrapped_message, True, (0, 0, 0))
        
        text_width, text_height = text_surface.get_size()
        
        bubble_width = 300
        bubble_height = 200
        
        bubble_image = pygame.transform.scale(self.bubble_image_original, (bubble_width, bubble_height))
        
        # Placer la bulle en bas à droite
        bubble_x = window_width - 300
        bubble_y = window_height - 350
        
        # Centrer le texte dans la bulle
        text_x = bubble_x + (bubble_width - text_width) // 2
        text_y = bubble_y + (bubble_height - text_height) // 2
        
        window.blit(bubble_image, (bubble_x, bubble_y))
        window.blit(text_surface, (text_x, text_y))
