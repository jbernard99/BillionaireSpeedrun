from save import *
import pygame
import sys

pygame.init()
from presets import *
from assets.infobar import *
from assets.button import *

class Game:

	WIDTH, HEIGHT = 1280, 720
	CLOCK = clock = pygame.time.Clock()
	SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

	def __init__(self):
		pygame.display.set_caption("Billionaire Speedrun v0.3")
		self.usd, self.btc = load_data()

	def load_assets(self):
		self.info_bar = InfoBar(25, GREY, f"Wallet : {self.usd:.2f}$ | {self.btc:.4f} BTC", self.SCREEN)
		self.usd_button = Button(5, 30, 130, 50, GREY, "Click me!", self.SCREEN)

	def draw(self, mouse_pos):
		self.SCREEN.fill(WHITE)
		self.info_bar.update(f"Wallet : {self.usd:.2f}$ | {self.btc:.4f} BTC")
		self.usd_button.update(mouse_pos)
		self.usd_button.draw()
		pygame.display.update()

		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.quit_game()
				elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					if self.usd_button.is_hovered:
						self.usd += 1

	def quit_game(self):
		save(self.usd, self.btc)
		pygame.quit()
		sys.exit()
