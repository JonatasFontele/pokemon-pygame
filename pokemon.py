import pygame


class Pokemon(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/Haunter.png")
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(50, 50, 100, 100)

        self.speed = 0
        self.acceleration = 0.1

    def update(self, *args):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        elif keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)
        elif keys[pygame.K_UP]:
            self.speed -= self.acceleration
        elif keys[pygame.K_DOWN]:
            self.speed += self.acceleration
        else:
            self.speed *= 0.9

        self.rect.y += self.speed

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 480:
            self.rect.bottom = 480
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 840:
            self.rect.right = 840
