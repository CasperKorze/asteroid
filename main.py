import pygame
import random  # Importujemy moduł random
from constants import *
from player import * 
from asteroid import Asteroid 
from asteroidfield import AsteroidField
from shot import Shot
from ammo import Ammo

def draw_game_over(screen, score):
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over", True, (255, 0, 0))
    text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50))
    screen.blit(text, text_rect)

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    score_text_rect = score_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    screen.blit(score_text, score_text_rect)

    new_game_text = font.render("Press N for New Game", True, (255, 255, 255))
    new_game_text_rect = new_game_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50))
    screen.blit(new_game_text, new_game_text_rect)

    pygame.display.flip()

def main():
    pygame.init() #initialize all imported pygame modules
    clock = pygame.time.Clock()
    dt = 0
    score = 0  # Dodaj zmienną do przechowywania punktów
    game_over = False

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #Bierze dane z constants.py
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    ammos = pygame.sprite.Group()  # Dodaj grupę dla amunicji
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    Ammo.containers = (ammos, updatable, drawable)  # Dodaj kontenery dla amunicji

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) #gracz
    asteroid_field = AsteroidField()  #asteroidy

    font = pygame.font.Font(None, 36)  # Dodaj czcionkę do wyświetlania punktów

    while True:
        if game_over:
            draw_game_over(screen, score)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        main()  # Restart the game
            continue

        screen.fill((0, 0, 0))  # Wypełniamy ekran czarnym kolorem
        
        updatable.update(dt)

        for entity in drawable: #odświeża gracza each frame
            entity.draw(screen)

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))  # Renderuj tekst punktów
        screen.blit(score_text, (10, 10))  # Wyświetl punkty na ekranie

        ammo_text = font.render(f"Ammo: {player.ammo}", True, (255, 255, 255))  # Renderuj tekst amunicji
        screen.blit(ammo_text, (10, 50))  # Wyświetl amunicję na ekranie

        pygame.display.flip()    # Odświeżamy ekran

        import sys  # ✅ Importujemy na początku pliku

        for asteroid in asteroids.sprites():  # ✅ Sprawdzamy kolizję dla wszystkich asteroid w grupie
            if player.colliderect(asteroid):  # ✅ Używamy metody colliderect
                game_over = True  # Ustawiamy stan gry na game over

        for asteroid in asteroids.sprites():  
            for shot in shots.sprites():  
                if shot.colliderect(asteroid):
                    asteroid.split()
                    shot.kill()
                    score += 10  # Zwiększ punktację, gdy gracz zestrzeli asteroidę
                    if random.random() < 0.5:  # 50% szans na wypadnięcie amunicji
                        Ammo(asteroid.position.x, asteroid.position.y)

        for ammo in ammos.sprites():
            if player.colliderect(ammo):
                player.collect_ammo()
                ammo.kill()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: return

        delta_time = clock.tick(60) / 1000 # - Ustawiam fpsy na 60
        dt = delta_time

if __name__ == "__main__":
    main()