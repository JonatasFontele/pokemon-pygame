import random

import pygame
import math


class Pokeball(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/Pokeballs/Pokeball.png")
        self.image = pygame.transform.scale(self.image, [30, 30])
        self.rect = pygame.Rect(50, 50, 100, 100)

        self.rect.x = 840 + random.randint(1, 400)
        self.rect.y = random.randint(0, 449)
        #self.timer = 0
        self.speed = 1 + random.random() * 2

    def update(self, *args):
        self.rect.x -= self.speed
        #self.timer += 0.01
        #self.rect.x = math.sin(self.timer) * 100

        if self.rect.right < 0:
            self.kill()
