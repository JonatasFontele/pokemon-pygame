import pygame


class Pokemon(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/Haunter.gif")
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(50, 50, 100, 100)

    def update(self, *args):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-1, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(1, 0)
        if keys[pygame.K_UP]:
            self.rect.move_ip(0, -1)
        if keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 1)