from game import *
from assets.presets import *
import pygame

game = Game()
game.load_assets()

while True:
	mouse_pos = pygame.mouse.get_pos()
	mouse_pressed = pygame.mouse.get_pressed()[0]

	#Update
	game.draw(mouse_pos, mouse_pressed)

	#Limit FPS
	game.CLOCK.tick(60)