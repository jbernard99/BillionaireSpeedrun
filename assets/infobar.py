import pygame
from presets import *

class InfoBar:
	def __init__(self):
		self.bar = pygame.Surface((1280, 25))
	
	def draw(self, display):
		self.display = display

	def update(self, usd, btc):
		self.bar.fill(GREY)
		txt = MEDIUM_D_FONT.render(
			f"Wallet : {usd:.2f}$ | {btc:.4f} BTC",
			True, WHITE)
		self.bar.blit(txt, (10, 2))
		self.display.blit(self.bar, (0, 0))
		
		
		


