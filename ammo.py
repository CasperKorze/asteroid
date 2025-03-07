import pygame
from constants import *

class Ammo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(self.containers)
        self.image = pygame.Surface((10, 20), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, (0, 255, 0), [(5, 0), (10, 20), (0, 20)])
        self.rect = self.image.get_rect(center=(x, y))
        self.position = pygame.Vector2(x, y)  # Dodajemy atrybut position
        self.radius = 10  # Dodajemy atrybut radius

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)