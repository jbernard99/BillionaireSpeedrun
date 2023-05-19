import pygame
from assets.presets import *

class Button:
	def __init__(self, x, y, width, height, color, text, display):
		self.rect = pygame.Rect(x, y, width, height)
		self.color = color
		self.text = text
		self.display = display

		self.is_hovered = False
		self.is_clicked = False
		self.last = pygame.time.get_ticks()
		self.cooldown = 75
		
	def draw(self, mouse_pos, mouse_click):
		self.update(mouse_pos, mouse_click)
		color = self.color
		if (self.is_hovered):
			color = (100, 100, 100)
		pygame.draw.rect(self.display, color, self.rect)

		text = SMALL_D_FONT.render(self.text, True, BLACK)
		text_rect = text.get_rect(center=self.rect.center)
		self.display.blit(text, text_rect)

	def is_cooldowned(self, now):
		if self.is_hovered and self.is_clicked:
			if (now - self.last >= self.cooldown):
				self.last = now
				return (0)
			return (1)

	def update(self, mouse_pos, mouse_click):
		if (self.rect.collidepoint(mouse_pos)):
			self.is_hovered = True
			if (mouse_click):
				self.is_clicked = True
		else:
			self.is_hovered = False
			self.is_clicked = False

	def get_text(self, text):
		self.text_surf = []
		for txt in text:
			self.text_surf.append(SMALL_D_FONT.render(txt, True, BLACK))

class Worker(Button):
	def __init__(self, x, y, size, text, display, id, name):
		y = y + (id * (size[1] + 10))
		Button.__init__(self, x, y, size[0], size[1], GREY, text, display)
		self.name = name
		self.initial_text = text

	def draw(self, mouse_pos, mouse_click, data):
		self.update(mouse_pos, mouse_click)
		color = self.color
		if (self.is_hovered):
			color = (100, 100, 100)
		self.set_new_text(data)
		pygame.draw.rect(self.display, color, self.rect)
		text = SMALL_D_FONT.render(self.text, True, BLACK)
		text_rect = text.get_rect(center=self.rect.center)
		self.display.blit(text, text_rect)

	def set_new_text(self, data):
		self.text = f"{data[0]} - " + self.initial_text + f" - {data[1]:.2f}"
