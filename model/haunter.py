import pygame
import model.pokemon
from model.sprite_sheet import SpriteSheet


class Haunter(model.pokemon.Pokemon):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.my_sprite_sheet = SpriteSheet("data/Ghost/Haunter_sprite_sheet.png")
        self.animation_list = []

        # Animation
        self.animation_steps = [4, 3, 1, 4, 6, 7]  # [idle, forward, damage, down, punch, lick]
        self.step_counter = 0
        self.action = 0
        self.frame = 0
        self.animation = False

        # Speed animation
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 200  # milliseconds

        for animation in self.animation_steps:
            temp_animation_list = []
            for _ in range(animation):
                temp_animation_list.append(self.my_sprite_sheet.parse_sprite(str(self.step_counter), 2))
                self.step_counter += 1
            self.animation_list.append(temp_animation_list)

        self.image = self.animation_list[self.action][self.frame - 1]
        self.rect = pygame.Rect(50, 50, 100, 100)

    def animate(self):
        self.animation = True

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.image = self.animation_list[self.action][self.frame]
            self.frame += 1
            self.last_update = current_time
            if self.frame >= len(self.animation_list[self.action]):
                self.frame = 0
                self.animation = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.move_ip(-5, 0)
            self.action = 2
            self.frame = 0
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.move_ip(5, 0)
            self.action = 1
            self.frame = 0
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.move_ip(0, -5)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.move_ip(0, 5)
            self.action = 3
            self.frame = 0
        else:
            self.action = 0

        # Boundaries
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 480:
            self.rect.bottom = 480
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 840:
            self.rect.right = 840
