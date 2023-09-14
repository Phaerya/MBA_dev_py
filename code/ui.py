import pygame


class UI:
    def __init__(self, surface):
        # setup
        self.display_surface = surface

        # health
        self.health_bar = pygame.image.load('../graphics/ui/health_bar.png').convert_alpha()
        self.health_bar_topleft = (54, 39)
        self.bar_max_width = 152
        self.bar_height = 4

        # keys
        self.key = pygame.image.load('../graphics/ui/key.png').convert_alpha()
        self.key_rect = self.key.get_rect(topleft=(50, 61))
        self.font = pygame.font.Font('../graphics/ui/ARCADEPI.ttf', 30)

    def show_health(self, current, full):
        self.display_surface.blit(self.health_bar, (20, 10))
        current_health_ratio = current / full
        current_bar_width = self.bar_max_width * current_health_ratio
        health_bar_rect = pygame.Rect(self.health_bar_topleft, (current_bar_width, self.bar_height))
        pygame.draw.rect(self.display_surface, '#dc4949', health_bar_rect)

    def show_keys(self, amount):
        self.display_surface.blit(self.key, self.key_rect)
        key_amount_surf = self.font.render(str(amount), False, '#ffffff')
        key_amount_rect = key_amount_surf.get_rect(midleft=(self.key_rect.right + 4, self.key_rect.centery))
        self.display_surface.blit(key_amount_surf, key_amount_rect)
