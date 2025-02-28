# this allows us to use code froms
# the open-source pygame library
# throughout this file
import pygame
from constants import *


def main():
	pygame.init() #initialize all imported pygame modules
	clock = pygame.time.Clock()
	dt = 0


	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #Bierze dane z constants.py
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
#Początek pętli, tzn kodu któru tworzy ekran dla gry ---------------------------------------------
	while True:
		screen.fill((0, 0, 0))  # Wypełniamy ekran czarnym kolorem
		pygame.display.flip()    # Odświeżamy ekran
		delta_time = clock.tick(60) / 1000
		dt = delta_time
#-------------------------------------------------------------------------------------------------
		for event in pygame.event.get():
			if event.type == pygame.QUIT: return
#This will check if the user has closed the window and exit the game loop if they do. It will make the window's close button work.




if __name__ == "__main__":
	main()

