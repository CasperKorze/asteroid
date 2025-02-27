# this allows us to use code froms
# the open-source pygame library
# throughout this file
import pygame
from constants import *


def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	while True:
        	screen.fill((0, 0, 0))  # Wypełniamy ekran czarnym kolorem
        	pygame.display.flip()    # Odświeżamy ekran



if __name__ == "__main__":
	main()

