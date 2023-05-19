from assets.presets import *
import pygame

class Bank():
	def __init__(self):
		self.usd = 0
		self.btc = 0
		self.workers = {
			"ebook": {"cost": 10, "value": 0.05, "type": "USD", "quantity": 0, "text": EBOOK},
			"instagram": {"cost": 25, "value": 0.25, "type": "USD", "quantity": 0, "text": INSTA},
			"asicminer": {"cost": 200, "value": 0.00005, "type": "BTC", "quantity": 0, "text": BTCMINER},
			"prodplace": {"cost": 150, "value": 1.5, "type": "USD", "quantity": 0, "text": PRODPLACE},
			"cokerun": {"cost": 3000, "value": 100, "type": "USD", "quantity": 0, "text": COKERUN}
		}
		self.last_payout = 0

	def update_workers(self):
		now = pygame.time.get_ticks()
		if (now - self.last_payout >= 1000):
			self.payout_workers()
			self.last_payout = now

	def payout_workers(self):
		for worker in self.workers.values():
			if (worker["type"] == "USD"):
				self.usd += worker["value"] * worker["quantity"]
			elif (worker["type"] == "BTC"):
				self.btc += worker["value"] * worker["quantity"]

	def buy_worker(self, worker):
		w = self.workers[worker]
		cost = (w["quantity"] + 1) * w["cost"]
		if cost <= self.usd:
			w["quantity"] += 1
			self.usd -= cost

	
	

