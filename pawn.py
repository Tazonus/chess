import pygame
from pygame.sprite import Group

class Pawn(pygame.sprite.Sprite):
    def __init__(self, img_path, position, tile_size):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(img_path).convert_alpha(), (tile_size,tile_size))
        self.rect = self.image.get_rect(center = position)