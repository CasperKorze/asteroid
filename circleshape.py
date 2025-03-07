import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    def collides_with(self, other_shape):
    # Oblicz odległość między środkami dwóch kształtów
        distance = self.position.distance_to(other_shape.position)
    
    # Sprawdź, czy odległość jest mniejsza niż suma promieni
        return distance <= (self.radius + other_shape.radius)

    PLAYER_RADIUS = 20
