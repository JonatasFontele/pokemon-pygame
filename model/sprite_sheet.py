import pygame
import json


class SpriteSheet:
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert()
        self.meta_data = self.filename.replace('png', 'json')
        # Implementar tratamento de exceção
        with open(self.meta_data) as file:
            self.data = json.load(file)
        file.close()

    def get_sprite(self, x, y, width, height, scale, colour):
        sprite = pygame.Surface((width, height)).convert_alpha()
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        sprite = pygame.transform.scale(sprite, (width * scale, height * scale))
        sprite.set_colorkey(colour)
        return sprite

    def parse_sprite(self, name):
        sprite = self.data['frames'][name]['frame']
        x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        image = self.get_sprite(x, y, w, h)
        return image
