import pygame
from settings import *
from typing import Tuple, List


class Player(pygame.sprite.Sprite):
    def __init__(self, pos: Tuple[int, int], groups: List):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
