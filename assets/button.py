import pygame
from presets import *

class Button:
	def __init__(self, x, y, width, height, color, text, display):
		self.last = pygame.time.get_ticks()
		self.cooldown = 2000
		self.rect = pygame.Rect(x, y, width, height)
		self.color = color
		self.text = text
		self.display = display
		
	def draw(self, event=None):
		pygame.draw.rect(self.display, self.color, self.rect)
		text = MEDIUM_D_FONT.render(self.text, True, BLACK)
		text_rect = text.get_rect(center=self.rect.center)
		self.display.blit(text, text_rect)

		now = pygame.time.get_ticks()
		if event:
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					if self.rect.collidepoint(event.pos):
						if now - self.last >= self.cooldown:
							print("click")