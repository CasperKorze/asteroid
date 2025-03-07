import pygame
from constants import *
from player import * 
from asteroid import Asteroid 
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init() #initialize all imported pygame modules
    clock = pygame.time.Clock()
    dt = 0
    score = 0  # Dodaj zmienną do przechowywania punktów

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #Bierze dane z constants.py
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) #gracz
    asteroid_field = AsteroidField()  #asteroidy

    font = pygame.font.Font(None, 36)  # Dodaj czcionkę do wyświetlania punktów

    while True:
        screen.fill((0, 0, 0))  # Wypełniamy ekran czarnym kolorem
        
        updatable.update(dt)

        for entity in drawable: #odświeża gracza each frame
            entity.draw(screen)

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))  # Renderuj tekst punktów
        screen.blit(score_text, (10, 10))  # Wyświetl punkty na ekranie

        pygame.display.flip()    # Odświeżamy ekran

        import sys  # ✅ Importujemy na początku pliku

        for asteroid in asteroids.sprites():  # ✅ Sprawdzamy kolizję dla wszystkich asteroid w grupie
            if player.collides_with(asteroid):  # ✅ Używamy gotowej funkcji Pygame
                print("Game over!") , sys.exit()  # ✅ Poprawne wyjście z gry

        for asteroid in asteroids.sprites():  
            for shot in shots.sprites():  
                if shot.collides_with(asteroid):
                    asteroid.split()
                    shot.kill()
                    score += 10  # Zwiększ punktację, gdy gracz zestrzeli asteroidę

        for event in pygame.event.get():
            if event.type == pygame.QUIT: return

        delta_time = clock.tick(60) / 1000 # - Ustawiam fpsy na 60
        dt = delta_time

if __name__ == "__main__":
    main()