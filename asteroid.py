from constants import *
from circleshape import CircleShape
import pygame
import random


class Asteroid(CircleShape):

    def __init__(self, x, y, radius, velocity=None):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        if velocity is None:
        # Tutaj ustaw domyślną prędkość, jeśli nie została podana
            self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        else:
            self.velocity = velocity
        self.radius = radius
        self.x = x
        self.y = y
        
        

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)  # ✅ Poprawione

    def update(self, dt):
        self.position += self.velocity * dt 


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
        
            # Tworzymy dwa nowe wektory prędkości
            new_velocity1 = self.velocity.rotate(random_angle)
            new_velocity2 = self.velocity.rotate(-random_angle)
        
            # Zwiększamy prędkość nowych asteroidów
            new_velocity1 *= 1.2
            new_velocity2 *= 1.2
        
            # Obliczamy nowy promień
            new_radius = self.radius - ASTEROID_MIN_RADIUS
        
            # Tworzymy dwa nowe asteroidy w tej samej pozycji co obecny
            Asteroid(self.position.x, self.position.y, new_radius, new_velocity1)
            Asteroid(self.position.x, self.position.y, new_radius, new_velocity2)
