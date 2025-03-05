# this allows us to use code froms
# the open-source pygame library
# throughout this file
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
#Instacja klasy player  - Tworzy i wyświetla statek gracza (trójkąt). 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #Bierze dane z constants.py
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
#Grupy (https://www.boot.dev/lessons/6a09887c-ad3f-4fb3-8726-c7bd9fa4161c)
    
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
    
 

#Początek pętli, tzn kodu któru tworzy ekran dla gry ---------------------------------------------	
    while True:
        screen.fill((0, 0, 0))  # Wypełniamy ekran czarnym kolorem
        
        updatable.update(dt)

        for entity in drawable: #odświeża gracza each frame
            entity.draw(screen)

        pygame.display.flip()    # Odświeżamy ekran

        import sys  # ✅ Importujemy na początku pliku

        for asteroid in asteroids.sprites():  # ✅ Sprawdzamy kolizję dla wszystkich asteroid w grupie
                if player.collides_with(asteroid):  # ✅ Używamy gotowej funkcji Pygame
                    print("Game over!") , sys.exit()  # ✅ Poprawne wyjście z gry


#-------------------------------------------------------------------------------------------------
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return
#This will check if the user has closed the window and exit the game loop if they do. It will make the window's close button work.
        delta_time = clock.tick(60) / 1000 # - Ustawiam fpsy na 60
        dt = delta_time
        
#============================================================





if __name__ == "__main__":
    main()

