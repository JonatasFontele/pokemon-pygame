import pygame


class Pokemon(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/Ghost.png")
        self.image = pygame.transform.scale(self.image, [120, 120])
        self.rect = pygame.Rect(50, 50, 100, 100)
        # self.rect = self.image.get_rect()

        # For inertia movement
        self.speed = 0
        self.acceleration = 0.3

    def update(self, *args):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.move_ip(-5, 0)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.move_ip(5, 0)
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            # self.rect.move_ip(0, -5)
            self.speed -= self.acceleration
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            # self.rect.move_ip(0, 5)
            self.speed += self.acceleration
        else:
            self.speed *= 0.99

        self.rect.y += self.speed

        # Boundaries
        if self.rect.top < 0:
            self.rect.top = 0
            self.speed = 0
        if self.rect.bottom > 480:
            self.rect.bottom = 480
            self.speed = 0
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 840:
            self.rect.right = 840
