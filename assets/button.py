import pygame
from presets import *

class Button:
	def __init__(self, x, y, width, height, color, text, display):
		self.rect = pygame.Rect(x, y, width, height)
		self.color = color
		self.text = text
		self.display = display

		self.is_hovered = False
		self.is_clicked = False
		self.last = pygame.time.get_ticks()
		self.cooldown = 200
		
	def draw(self):
		color = self.color
		if (self.is_hovered):
			color = (100, 100, 100)
		pygame.draw.rect(self.display, color, self.rect)

		text = MEDIUM_D_FONT.render(self.text, True, BLACK)
		text_rect = text.get_rect(center=self.rect.center)
		self.display.blit(text, text_rect)

		now = pygame.time.get_ticks()
		if self.is_hovered and self.is_clicked:
			if (now - self.last >= self.cooldown):
				self.last = now


	def update(self, mouse_pos):
		if (self.rect.collidepoint(mouse_pos)):
			self.is_hovered = True
			if (0):
				self.is_clicked = True
		else:
			self.is_hovered = False
			self.is_clicked = False