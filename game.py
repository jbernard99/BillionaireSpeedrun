from save import *
import pygame
import sys

pygame.init()
from assets.presets import *
from assets.infobar import *
from assets.button import *

class Game:

	WIDTH, HEIGHT = 1280, 720
	CLOCK = clock = pygame.time.Clock()
	SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

	def __init__(self):
		pygame.display.set_caption("Billionaire Speedrun v0.4")
		self.usd, self.btc, self.saved_eb = load_data()

	def load_assets(self):
		self.info_bar = InfoBar(25, GREY, f"Wallet : {self.usd:.2f}$ | {self.btc:.4f} BTC", self.SCREEN)
		self.usd_button = Button(900, 600, 300, 75, GREY, GEEKSQUAD, self.SCREEN)
		self.w_ebook = Worker(5, 30, 550, 75, EBOOK, self.SCREEN, [10, 0.01, "USD", self.saved_eb])

	def draw(self, mouse_pos, mouse_click):
		self.SCREEN.fill(WHITE)
		self.info_bar.update(f"Wallet : {self.usd:.2f}$ | {self.btc:.4f} BTC")
		self.usd_button.draw(mouse_pos, mouse_click)
		self.w_ebook.draw(mouse_pos, mouse_click)
		pygame.display.update()

		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.quit_game()
				elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					if self.usd_button.is_hovered and not self.usd_button.is_cooldowned():
						self.usd += 1
					elif self.w_ebook.is_hovered and not self.w_ebook.is_cooldowned():
						if self.w_ebook.can_be_bought(self.usd):
							self.usd -= self.w_ebook.cost
							self.w_ebook.buy()

		self.usd += self.w_ebook.get_gift()

	def quit_game(self):
		save(self.usd, self.btc, self.w_ebook.qtty)
		pygame.quit()
		sys.exit()
