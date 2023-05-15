import pygame
from presets import *

class InfoBar:
	def __init__(self, height, color, txt, display):
		self.bar = pygame.Surface((1280, height))
		self.color = color
		self.txt = txt
		self.display = display

	def update(self, txt):
		self.bar.fill(self.color)
		surftxt = MEDIUM_D_FONT.render(
			txt, True, WHITE)
		self.bar.blit(surftxt, (10, 2))
		self.display.blit(self.bar, (0, 0))
		
		
		


