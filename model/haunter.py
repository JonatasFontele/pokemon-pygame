import pygame
import model.pokemon
from model.sprite_sheet import SpriteSheet


class Haunter(model.pokemon.Pokemon):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.my_sprite_sheet = SpriteSheet("data/Ghost/Haunter_sprite_sheet.png")
        self.animation_list = []

        # First row right — Idle
        self.animation_list.append(self.my_sprite_sheet.parse_sprite("haunter_idle1", 2))
        self.animation_list.append(self.my_sprite_sheet.parse_sprite("haunter_idle2", 2))
        self.animation_list.append(self.my_sprite_sheet.parse_sprite("haunter_idle3", 2))

        # Second row right — Forward
        self.animation_list.append(self.my_sprite_sheet.parse_sprite("haunter_forward1", 2))
        self.animation_list.append(self.my_sprite_sheet.parse_sprite("haunter_forward2", 2))
        self.animation_list.append(self.my_sprite_sheet.parse_sprite("haunter_forward3", 2))

        # Third row right — Damage
        self.animation_list.append(self.my_sprite_sheet.parse_sprite("haunter_damage", 2))

        # Fourth row right — Down
        self.animation_list.append(self.my_sprite_sheet.parse_sprite("haunter_down1", 2))
        self.animation_list.append(self.my_sprite_sheet.parse_sprite("haunter_down2", 2))
        self.animation_list.append(self.my_sprite_sheet.parse_sprite("haunter_down3", 2))
        self.animation_list.append(self.my_sprite_sheet.parse_sprite("haunter_down4", 2))

        # Fifth row right — Punch
        self.animation_list.append(self.my_sprite_sheet.parse_sprite("haunter_punch1", 2))
        self.animation_list.append(self.my_sprite_sheet.parse_sprite("haunter_punch2", 2))
        self.animation_list.append(self.my_sprite_sheet.parse_sprite("haunter_punch3", 2))
        self.animation_list.append(self.my_sprite_sheet.parse_sprite("haunter_punch4", 2))
        self.animation_list.append(self.my_sprite_sheet.parse_sprite("haunter_punch5", 2))
        self.animation_list.append(self.my_sprite_sheet.parse_sprite("haunter_punch6", 2))

        # Sixth row right — Lick
        self.animation_list.append(self.my_sprite_sheet.parse_sprite("haunter_lick1", 2))
        self.animation_list.append(self.my_sprite_sheet.parse_sprite("haunter_lick2", 2))
        self.animation_list.append(self.my_sprite_sheet.parse_sprite("haunter_lick3", 2))
        self.animation_list.append(self.my_sprite_sheet.parse_sprite("haunter_lick4", 2))
        self.animation_list.append(self.my_sprite_sheet.parse_sprite("haunter_lick5", 2))
        self.animation_list.append(self.my_sprite_sheet.parse_sprite("haunter_lick6", 2))
        self.animation_list.append(self.my_sprite_sheet.parse_sprite("haunter_lick7", 2))

        # First row right — Shiny
        # animation_list.append(sprite_sheet.get_image(0, 0, 65, 45, 2))

        # Animation
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 200
        self.frame = 0
        self.animation = False
        self.image = self.animation_list[self.frame - 1]
        # self.rect = self.image.get_rect()
        self.rect = pygame.Rect(50, 50, 100, 100)

        # For inertia movement
        self.speed = 0
        self.acceleration = 0.3

    def animate(self):
        self.animation = True

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.image = self.animation_list[self.frame]
            self.frame += 1
            self.last_update = current_time
            if self.frame >= len(self.animation_list):
                self.frame = 0
                self.animation = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.move_ip(-5, 0)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.move_ip(5, 0)
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.speed -= self.acceleration
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
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
