import pygame
import platform

WHITE 	= (255, 255, 255)
BLACK 	= (0, 0, 0)
RED		= (255, 0, 0)
GREEN	= (0, 255, 0)
BLUE	= (0, 0, 255)
GREY	= (128, 128, 128)

if platform.system() == "Darwin":
	SMALL_D_FONT = pygame.font.SysFont("assets/Roboto-Regular.ttf", 25)
	MEDIUM_D_FONT = pygame.font.SysFont("assets/Roboto-Regular.ttf", 30)
	BIG_D_FONT = pygame.font.SysFont("assets/Roboto-Regular.ttf", 35)
elif platform.system() == "Linux":
	SMALL_D_FONT = pygame.font.SysFont("urwbookman", 20)
	MEDIUM_D_FONT = pygame.font.SysFont("urwbookman", 24)
	BIG_D_FONT = pygame.font.SysFont("urwbookman", 32)

GEEKSQUAD 	= "Work at GeekSquad(Get $$$)"
EBOOK 		= "Write and ebook using ChatGPT"
INSTA		= "Make a AI Art Instagram account"
BTCMINER	= "Buy a Bitcoin ASIC miner"
PRODPLACE	= "Use an AI to market a product"
COKERUN		= "Buy a coke run from a friend"

W_SIZES = (550, 75)