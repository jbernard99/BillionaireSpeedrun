from save import *
import pygame
import sys

pygame.init()
from presets import *
from assets.infobar import *

# set up the display
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Billionaire Speedrun v0.2")

# set up the clock
clock = pygame.time.Clock()

# set up the font
font = pygame.font.SysFont("urwbookman", 22)

# set up the score
usd, btc = load_data()

# main game loop
while True:
	# handle events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			save(usd, btc)
			pygame.quit()
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:  # left mouse button
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