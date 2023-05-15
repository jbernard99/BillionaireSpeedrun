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
		self.load_workers()
		data = load_data(len(self.workers) + 2)
		self.usd = data[0] 
		self.btc = data[1]
		i = 2
		for worker in self.workers:
			worker.qtty = data[i]
			worker.set_cost()
			worker.set_new_text()
			i += 1

	def load_assets(self):
		self.info_bar = InfoBar(25, GREY, f"Wallet : {self.usd:.2f}$ | {self.btc:.4f} BTC", self.SCREEN)
		self.usd_button = Button(900, 600, 350, 75, GREY, GEEKSQUAD, self.SCREEN)

	def load_workers(self):
		self.workers = []
		self.workers.append(Worker(5, 30, W_SIZES, EBOOK, self.SCREEN, [10, 0.01, "USD", 1]))
		self.workers.append(Worker(5, 30, W_SIZES, INSTA, self.SCREEN, [25, 0.10, "USD", 2]))

	def draw(self, mouse_pos, mouse_click):
		self.SCREEN.fill(WHITE)
		self.info_bar.update(f"Wallet : {self.usd:.2f}$ | {self.btc:.4f} BTC", mouse_pos, mouse_click)
		self.usd_button.draw(mouse_pos, mouse_click)
		for worker in self.workers:
			worker.draw(mouse_pos, mouse_click)
		pygame.display.update()

		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.quit_game()
				elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					if self.usd_button.is_hovered and not self.usd_button.is_cooldowned():
						self.usd += 1
					if self.info_bar.exit_button.is_hovered:
						self.quit_game()
					for worker in self.workers:
						if worker.is_hovered and not worker.is_cooldowned():
							if worker.can_be_bought(self.usd):
								self.usd -= worker.cost
								worker.buy()

		for worker in self.workers:
			if worker.type == "USD":
				self.usd += worker.get_gift()

	def save_game(self):
		data = [self.usd, self.btc]
		for worker in self.workers:
			data.append(worker.qtty)
		save(data)

	def quit_game(self):
		self.save_game()
		pygame.quit()
		sys.exit()
