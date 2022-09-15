import random

import pygame


class MoveAttack(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/shadow_ball.png")
        self.image = pygame.transform.scale(self.image, [30, 30])
        self.rect = self.image.get_rect()

        self.speed = 4

    def update(self, *args):
        self.rect.x += self.speed

        if self.rect.left > 840:
            self.kill()
