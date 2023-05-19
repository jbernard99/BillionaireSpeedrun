import pygame
import pickle
import sys

pygame.init()
import bank
from assets.presets import *
from assets.infobar import *
from assets.button import *

class Game:

	WIDTH, HEIGHT = 1280, 720
	CLOCK = clock = pygame.time.Clock()
	SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

	def __init__(self):
		pygame.display.set_caption("Billionaire Speedrun v0.4")
		self.bk = self.load_game()
		self.bk.last_payout = pygame.time.get_ticks()
		print(self.bk.workers)
		self.load_workers()

	def load_assets(self):
		self.info_bar = InfoBar(25, GREY, f"Wallet : {self.bk.usd:.2f}$ | {self.bk.btc:.4f} BTC", self.SCREEN)
		self.usd_button = Button(900, 600, 350, 75, GREY, GEEKSQUAD, self.SCREEN)

	def load_workers(self):
		self.workers = []
		i = 1
		for worker in self.bk.workers.items():
			self.workers.append(Worker(5, 30, W_SIZES, worker[1]["text"], self.SCREEN, i, worker[0]))
			i += 1

	def draw(self, mouse_pos, mouse_click):
		now = pygame.time.get_ticks()
		self.SCREEN.fill(WHITE)
		self.info_bar.update(f"Wallet : {self.bk.usd:.2f}$ | {self.bk.btc:.4f} BTC", mouse_pos, mouse_click)
		self.usd_button.draw(mouse_pos, mouse_click)
		for w in self.workers:
			cost = self.bk.workers[w.name]["cost"] * (self.bk.workers[w.name]["quantity"] + 1)
			w.draw(mouse_pos, mouse_click, [self.bk.workers[w.name]["quantity"], cost])
		pygame.display.update()

		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.quit_game()
				elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					if self.usd_button.is_hovered and not self.usd_button.is_cooldowned(now):
						self.bk.usd += 1
					if self.info_bar.exit_button.is_hovered:
						self.quit_game()
					for worker in self.workers:
						if worker.is_hovered and not worker.is_cooldowned(now):
							self.bk.buy_worker(worker.name)

		self.bk.update_workers()

	def save_game(self):
		with open("save.pickle", "wb") as file:
			pickle.dump(self.bk, file)
		

	def load_game(self):
		with open("save.pickle", "rb") as file:
			try:
				return (pickle.load(file))
			except:
				return (bank.Bank())

	def quit_game(self):
		self.save_game()
		pygame.quit()
		sys.exit()
