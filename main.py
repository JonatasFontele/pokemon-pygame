import random

import pygame
from model.sprite_sheet import SpriteSheet
from model.pokemon import Pokemon
from model.pokeball import Pokeball
from model.move_attack import MoveAttack

# Initializing pygame and creating the window
pygame.init()
WIDTH = 840
HEIGHT = 480
display = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Pokéball Invaders")
game_icon = pygame.image.load('data/Haunter.png')
pygame.display.set_icon(game_icon)

#def draw():
    #display.fill([105, 61, 28])
    # player = pygame.Rect(50, 50, 100, 100)
    # pygame.draw.rect(display, [255, 255, 255, 255], player)

# Objects
object_group = pygame.sprite.Group()
pokeball_group = pygame.sprite.Group()
attack_group = pygame.sprite.Group()

# Background
background = pygame.sprite.Sprite(object_group)
background.image = pygame.image.load("data/haunted_house.jpg")
background.image = pygame.transform.scale(background.image, [840, 480])
background.rect = background.image.get_rect()

haunter = Pokemon(object_group)
sprite_sheet_image = pygame.image.load("data/Haunter_sprite_sheet.png").convert_alpha()
sprite_sheet = SpriteSheet(sprite_sheet_image)

pokeball = Pokeball(object_group)
# pokeball.rect.center = [200, 400]

# Music
pygame.mixer.music.load("data/lavender-town.mp3")
pygame.mixer.music.set_volume(0.01)
pygame.mixer.music.play(-1)

# Sounds
cry = pygame.mixer.Sound("data/haunter.mp3")
cry.set_volume(0.1)

# Animation list
animation_list = []
animation_steps = 4
last_update = pygame.time.get_ticks()
animation_cooldown = 190
frame = 0

LIGHT_BLUE = (199, 225, 209, 255)

# First row right — Idle
animation_list.append(sprite_sheet.get_image(470, 0, 65, 45, 2, LIGHT_BLUE))
animation_list.append(sprite_sheet.get_image(402, 0, 68, 50, 2, LIGHT_BLUE))
animation_list.append(sprite_sheet.get_image(335, 0, 65, 45, 2, LIGHT_BLUE))

# Second row right — Forward
animation_list.append(sprite_sheet.get_image(470, 50, 65, 50, 2, LIGHT_BLUE))
animation_list.append(sprite_sheet.get_image(405, 50, 65, 50, 2, LIGHT_BLUE))
animation_list.append(sprite_sheet.get_image(340, 50, 65, 50, 2, LIGHT_BLUE))

# Third row right — Damage
animation_list.append(sprite_sheet.get_image(480, 100, 55, 50, 2, LIGHT_BLUE))

# Fourth row right — Down
animation_list.append(sprite_sheet.get_image(485, 142, 50, 57, 2, LIGHT_BLUE))
animation_list.append(sprite_sheet.get_image(425, 142, 60, 57, 2, LIGHT_BLUE))
animation_list.append(sprite_sheet.get_image(364, 142, 60, 57, 2, LIGHT_BLUE))
animation_list.append(sprite_sheet.get_image(295, 142, 65, 57, 2, LIGHT_BLUE))

# Fifth row right — Punch
animation_list.append(sprite_sheet.get_image(470, 203, 65, 42, 2, LIGHT_BLUE))
animation_list.append(sprite_sheet.get_image(417, 203, 55, 42, 2, LIGHT_BLUE))
animation_list.append(sprite_sheet.get_image(368, 203, 50, 42, 2, LIGHT_BLUE))
animation_list.append(sprite_sheet.get_image(308, 203, 60, 42, 2, LIGHT_BLUE))
animation_list.append(sprite_sheet.get_image(238, 203, 70, 42, 2, LIGHT_BLUE))
animation_list.append(sprite_sheet.get_image(153, 203, 85, 42, 2, LIGHT_BLUE))

# Sixth row right — Lick
animation_list.append(sprite_sheet.get_image(488, 248, 45, 62, 2, LIGHT_BLUE))
animation_list.append(sprite_sheet.get_image(425, 248, 60, 62, 2, LIGHT_BLUE))
animation_list.append(sprite_sheet.get_image(345, 248, 80, 62, 2, LIGHT_BLUE))
animation_list.append(sprite_sheet.get_image(265, 248, 80, 62, 2, LIGHT_BLUE))
animation_list.append(sprite_sheet.get_image(192, 248, 70, 62, 2, LIGHT_BLUE))
animation_list.append(sprite_sheet.get_image(125, 248, 65, 62, 2, LIGHT_BLUE))
animation_list.append(sprite_sheet.get_image(60, 248, 65, 62, 2, LIGHT_BLUE))

# First row right — Shiny
# animation_list.append(sprite_sheet.get_image(0, 0, 65, 45, 2, LIGHT_BLUE))

game_loop = True
game_over = False
timer = 0

# For FPS
clock = pygame.time.Clock()

if __name__ == "__main__":
    while game_loop:
        # 60 FPS
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    cry.play()
                    newAttack = MoveAttack(object_group, attack_group)
                    newAttack.rect.center = haunter.rect.center

        # Update logic
        if not game_over:
            object_group.update()

            timer += 1
            if timer > 30:
                timer = 0
                if random.random() < 0.3:
                    newPokeball = Pokeball(object_group, pokeball_group)

            collisions = pygame.sprite.spritecollide(haunter, pokeball_group, False, pygame.sprite.collide_mask)

            if collisions:
                print("YOU GOT CAUGHT!")
                game_over = True

            hits = pygame.sprite.groupcollide(attack_group, pokeball_group, True, True, pygame.sprite.collide_mask)

        # Draw
        display.fill([105, 61, 28])
        object_group.draw(display)

        # Update animation
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            frame += 1
            last_update = current_time
            if frame >= len(animation_list):
                frame = 0

        # Frame image
        display.blit(animation_list[frame], (200, 50))

        pygame.display.update()
