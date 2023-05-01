import pygame
from bar import Bar
from presets import *

class InfoBar:
    def __init__(self):
        self.bar = Bar(0, 0, 25, 1280, GREY)
