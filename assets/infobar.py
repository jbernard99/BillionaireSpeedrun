import pygame
from assets.presets import *
from assets.button import Button

class InfoBar:
	def __init__(self, height, color, txt, display):
		self.bar = pygame.Surface((1280, height))
		self.color = color
		self.txt = txt
		self.display = display
		self.exit_button = Button(1255, 2.5, 20, 20, RED, "X", self.bar)

	def update(self, txt, mp, mc):
		self.bar.fill(self.color)
		surftxt = MEDIUM_D_FONT.render(
			txt, True, WHITE)
		self.bar.blit(surftxt, (10, 2))
		self.exit_button.draw(mp, mc)
		self.display.blit(self.bar, (0, 0))
		
		
		


