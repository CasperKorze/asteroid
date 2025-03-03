from constants import *
from circleshape import CircleShape
import pygame


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(self.velocity)
        self.radius = radius
        self.x = x
        self.y = y
        
        

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)  # ✅ Poprawione

    def update(self, dt):
        self.position += self.velocity * dt 