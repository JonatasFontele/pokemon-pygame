import pygame
import model.pokemon
from model.sprite_sheet import SpriteSheet


class Haunter(model.pokemon.Pokemon):
    def __init__(self):
        super().__init__()

        self.image = SpriteSheet("data/Haunter_sprite_sheet.png")
        self.rect = pygame.Rect(50, 50, 100, 100)

        # Animation list
        self.animation_list = []
        self.animation_steps = 4
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 190
        self.frame = 0

        light_blue = (199, 225, 209, 255)

        # First row right — Idle
        self.animation_list.append(self.image.parse_sprite("haunter_idle1"))
        self.animation_list.append(self.image.parse_sprite("haunter_idle2"))
        self.animation_list.append(self.image.parse_sprite("haunter_idle3"))

        # Second row right — Forward
        self.animation_list.append(self.image.parse_sprite("haunter_forward1"))
        self.animation_list.append(self.image.parse_sprite("haunter_forward2"))
        self.animation_list.append(self.image.parse_sprite("haunter_forward3"))

        # # Third row right — Damage
        # self.animation_list.append(self.image.get_image(480, 100, 55, 50, 2, light_blue))
        #
        # # Fourth row right — Down
        # self.animation_list.append(self.image.get_image(485, 142, 50, 57, 2, light_blue))
        # self.animation_list.append(self.image.get_image(425, 142, 60, 57, 2, light_blue))
        # self.animation_list.append(self.image.get_image(364, 142, 60, 57, 2, light_blue))
        # self.animation_list.append(self.image.get_image(295, 142, 65, 57, 2, light_blue))
        #
        # # Fifth row right — Punch
        # self.animation_list.append(self.image.get_image(470, 203, 65, 42, 2, light_blue))
        # self.animation_list.append(self.image.get_image(417, 203, 55, 42, 2, light_blue))
        # self.animation_list.append(self.image.get_image(368, 203, 50, 42, 2, light_blue))
        # self.animation_list.append(self.image.get_image(308, 203, 60, 42, 2, light_blue))
        # self.animation_list.append(self.image.get_image(238, 203, 70, 42, 2, light_blue))
        # self.animation_list.append(self.image.get_image(153, 203, 85, 42, 2, light_blue))
        #
        # # Sixth row right — Lick
        # self.animation_list.append(self.image.get_image(488, 248, 45, 62, 2, light_blue))
        # self.animation_list.append(self.image.get_image(425, 248, 60, 62, 2, light_blue))
        # self.animation_list.append(self.image.get_image(345, 248, 80, 62, 2, light_blue))
        # self.animation_list.append(self.image.get_image(265, 248, 80, 62, 2, light_blue))
        # self.animation_list.append(self.image.get_image(192, 248, 70, 62, 2, light_blue))
        # self.animation_list.append(self.image.get_image(125, 248, 65, 62, 2, light_blue))
        # self.animation_list.append(self.image.get_image(60, 248, 65, 62, 2, light_blue))

        # First row right — Shiny
        # animation_list.append(sprite_sheet.get_image(0, 0, 65, 45, 2, light_blue))

        self.animation = False

    def animate(self):
        self.animation = True

    def update(self):
        # Update animation
        if self.animation:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update >= self.animation_cooldown:
                self.frame += 1
                self.last_update = current_time
                if self.frame >= len(self.animation_list):
                    self.frame = 0
                    self.animation = False
