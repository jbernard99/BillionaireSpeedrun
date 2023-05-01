from save import *
import pygame
import sys

pygame.init()
from presets import *
from assets.infobar import *

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Billionaire Speedrun v0.2")
clock = pygame.time.Clock()

usd, btc = load_data()

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
	info_bar = InfoBar()
	screen.fill(WHITE)

	#Draw
	info_bar.draw(screen)

	#Update
	info_bar.update(usd, btc)
	pygame.display.update()

	#Limit FPS
	clock.tick(30)