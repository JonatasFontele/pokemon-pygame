import pygame
import json


class SpriteSheet:
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert_alpha()
        self.meta_data = self.filename.replace('png', 'json')
        # Implementar tratamento de exceção
        with open(self.meta_data) as file:
            self.data = json.load(file)
        file.close()

    def get_sprite(self, x, y, width, height, scale, colour):
        sprite = pygame.Surface((width, height))
        sprite.set_colorkey(colour)
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        sprite = pygame.transform.scale(sprite, (width * scale, height * scale))
        return sprite

    def parse_sprite(self, name, scale):
        sprite = self.data["frames"][name]["frame"]
        x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        colour = eval(self.data["meta"]["colour"])
        image = self.get_sprite(x, y, w, h, scale, colour)
        return image
