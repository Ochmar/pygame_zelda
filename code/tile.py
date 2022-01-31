import pygame
from settings import *
from typing import Tuple, List


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos: Tuple[int, int], groups: List):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/test/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)
