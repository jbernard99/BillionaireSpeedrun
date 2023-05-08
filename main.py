from save import *
import pygame
import sys

pygame.init()
from presets import *
from assets.infobar import *
from assets.button import *

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Billionaire Speedrun v0.2")
clock = pygame.time.Clock()
print(pygame.font.get_fonts())

usd, btc = load_data()
info_bar = InfoBar(25, GREY, f"Wallet : {usd:.2f}$ | {btc:.4f} BTC", screen)
usd_button = Button(5, 30, 130, 50, GREY, "Click me!", screen)

while True:
	#Events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			save(usd, btc)
			pygame.quit()
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				usd += 1

	#Generate
	screen.fill(WHITE)

	#Update
	info_bar.update(f"Wallet : {usd:.2f}$ | {btc:.4f} BTC")
	if (usd_button.draw(event)):
		usd += 1
	pygame.display.update()

	#Limit FPS
	clock.tick(60)