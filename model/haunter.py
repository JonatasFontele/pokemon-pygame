import pygame
import model.pokemon
from model.sprite_sheet import SpriteSheet


class Haunter(model.pokemon.Pokemon):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.my_sprite_sheet = SpriteSheet("data/Haunter_sprite_sheet.png")
        self.animation_list = []

        # First row right — Idle
        self.animation_list.append(self.my_sprite_sheet.parse_sprite("haunter_idle1", 2))
        self.animation_list.append(self.my_sprite_sheet.parse_sprite("haunter_idle2", 2))
        self.animation_list.append(self.my_sprite_sheet.parse_sprite("haunter_idle3", 2))

        # # Second row right — Forward
        # self.animation_list.append(self.my_sprite_sheet.parse_sprite("haunter_forward1", 2))
        # self.animation_list.append(self.my_sprite_sheet.parse_sprite("haunter_forward2", 2))
        # self.animation_list.append(self.my_sprite_sheet.parse_sprite("haunter_forward3", 2))

        # # Third row right — Damage
        # self.animation_list.append(self.image.get_image(480, 100, 55, 50, 2))
        #
        # # Fourth row right — Down
        # self.animation_list.append(self.image.get_image(485, 142, 50, 57, 2))
        # self.animation_list.append(self.image.get_image(425, 142, 60, 57, 2))
        # self.animation_list.append(self.image.get_image(364, 142, 60, 57, 2))
        # self.animation_list.append(self.image.get_image(295, 142, 65, 57, 2))
        #
        # # Fifth row right — Punch
        # self.animation_list.append(self.image.get_image(470, 203, 65, 42, 2))
        # self.animation_list.append(self.image.get_image(417, 203, 55, 42, 2)
        # self.animation_list.append(self.image.get_image(368, 203, 50, 42, 2))
        # self.animation_list.append(self.image.get_image(308, 203, 60, 42, 2))
        # self.animation_list.append(self.image.get_image(238, 203, 70, 42, 2))
        # self.animation_list.append(self.image.get_image(153, 203, 85, 42, 2)
        #
        # # Sixth row right — Lick
        # self.animation_list.append(self.image.get_image(488, 248, 45, 62, 2))
        # self.animation_list.append(self.image.get_image(425, 248, 60, 62, 2))
        # self.animation_list.append(self.image.get_image(345, 248, 80, 62, 2))
        # self.animation_list.append(self.image.get_image(265, 248, 80, 62, 2))
        # self.animation_list.append(self.image.get_image(192, 248, 70, 62, 2))
        # self.animation_list.append(self.image.get_image(125, 248, 65, 62, 2))
        # self.animation_list.append(self.image.get_image(60, 248, 65, 62, 2)

        # First row right — Shiny
        # animation_list.append(sprite_sheet.get_image(0, 0, 65, 45, 2))

        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 400
        self.frame = 0
        self.animation = False

        self.image = self.animation_list[self.frame]
        self.rect = self.image.get_rect()

    def animate(self):
        self.animation = True

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.frame += 1
            self.last_update = current_time
            if self.frame >= len(self.animation_list):
                self.frame = 0
                self.animation = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)
        if keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        if keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)

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

        # Update animation
        # if self.animation:
        #     current_time = pygame.time.get_ticks()
        #     if current_time - self.last_update >= self.animation_cooldown:
        #         self.frame += 1
        #         self.last_update = current_time
        #         if self.frame >= len(self.animation_list):
        #             self.frame = 0
        #             self.animation = False
