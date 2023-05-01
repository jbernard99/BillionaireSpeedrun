from save import *
import pygame
import sys

pygame.init()
from presets import *
from assets.bar import *

# set up the display
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Billionaire Speedrun v0.2")

# set up the clock
clock = pygame.time.Clock()

# set up the font
font = pygame.font.SysFont("urwbookman", 22)

# set up the score
usdollars = load_data()

# main game loop
while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save(usdollars)
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # left mouse button
                usdollars += 1

    # update the screen
    screen.fill(WHITE)  # white background
    navbar = Bar(0, 0, 1280, 25, GREY)
    navbar.draw(screen)
    score_text = font.render(f"Wallet : {usdollars:.2f}$", True, WHITE)
    screen.blit(score_text, navbar, area=(-10, -3, 1280, 25))
    pygame.display.update()

    # limit the frame rate
    clock.tick(30)