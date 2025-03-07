import pygame
import math
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0 
        self.timer = 0 
        self.shots_fired = 0  # Dodaj zmienną do przechowywania liczby strzałów
        self.reloading = False  # Dodaj zmienną do przechowywania stanu przeładowania
        self.reload_time = 2  # Czas przeładowania w sekundach
        self.last_shot_time = 0  # Czas ostatniego strzału

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        self.draw_reload_timer(screen)

    def draw_reload_timer(self, screen):
        if self.reloading:
            elapsed_time = (pygame.time.get_ticks() - self.last_shot_time) / 1000
            reload_progress = min(elapsed_time / self.reload_time, 1)
            timer_radius = 10
            timer_position = self.position + pygame.Vector2(30, 0)
            pygame.draw.circle(screen, "white", timer_position, timer_radius, 1)
            pygame.draw.arc(screen, "white", (timer_position.x - timer_radius, timer_position.y - timer_radius, timer_radius * 2, timer_radius * 2), 0, reload_progress * 2 * math.pi, 2)

    def rotate(self, dt):
        cr = PLAYER_TURN_SPEED * dt
        self.rotation += cr
        
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        if self.timer > 0:
            self.timer -= dt

        if self.reloading:
            if pygame.time.get_ticks() - self.last_shot_time > self.reload_time * 1000:
                self.shots_fired = 0
                self.reloading = False

        if self.timer <= 0 and not self.reloading:  # Tylko jeśli cooldown się skończył i nie przeładowujemy
            if keys[pygame.K_SPACE]:  # Jeśli SPACE jest naciśnięty, strzelamy
                self.shoot()
                self.timer = PLAYER_SHOOT_COOLDOWN  # BLOKUJEMY SPACE na 0.3s

    def shoot(self):
        if self.shots_fired < 5:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
            self.shots_fired += 1
            self.last_shot_time = pygame.time.get_ticks()
        else:
            self.reloading = True
            self.last_shot_time = pygame.time.get_ticks()