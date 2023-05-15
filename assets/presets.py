import pygame
import platform

WHITE 	= (255, 255, 255)
BLACK 	= (0, 0, 0)
RED		= (255, 0, 0)
GREEN	= (0, 255, 0)
BLUE	= (0, 0, 255)
GREY	= (128, 128, 128)

if platform.system() == "Darwin":
	SMALL_D_FONT = pygame.font.SysFont("hiraginosansgb", 18)
	MEDIUM_D_FONT = pygame.font.SysFont("hiraginosansgb", 22)
	BIG_D_FONT = pygame.font.SysFont("hiraginosansgb", 32)
elif platform.system() == "Linux":
	SMALL_D_FONT = pygame.font.SysFont("urwbookman", 20)
	MEDIUM_D_FONT = pygame.font.SysFont("urwbookman", 24)
	BIG_D_FONT = pygame.font.SysFont("urwbookman", 32)

GEEKSQUAD 	= "Work at GeekSquad(Get $$$)"
EBOOK 		= "Write and ebook using ChatGPT"
INSTA		= "Make a AI Art Instagram account"

W_SIZES = (550, 75)