import pygame
from save import *
import sys

pygame.init()

# set up the display
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Billionaire Speedrun v0.2")

# set up the clock
clock = pygame.time.Clock()

# set up the font
print(pygame.font.get_fonts())
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
                usdollars += 1.01

    # update the screen
    screen.fill((255, 255, 255))  # white background
    score_text = font.render(f"Wallet : {usdollars:.2f}$", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    pygame.display.update()

    # limit the frame rate
    clock.tick(30)