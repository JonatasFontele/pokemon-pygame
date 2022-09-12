import random

import pygame
from sprite_sheet import SpriteSheet
from pokemon import Pokemon
from pokeball import Pokeball
from move_attack import MoveAttack

# Initializing pygame and creating the window
pygame.init()
display = pygame.display.set_mode([840, 480])
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
# haunter = pygame.sprite.Sprite(draw_group)

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
pygame.mixer.music.set_volume(0.05)
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

# First row right
animation_list.append(sprite_sheet.get_image(5.15, 0, 65, 45, 2, (199, 225, 209, 255)))
animation_list.append(sprite_sheet.get_image(5.72, 0, 70, 50, 2, (199, 225, 209, 255)))
animation_list.append(sprite_sheet.get_image(7.23, 0, 65, 45, 2, (199, 225, 209, 255)))

# Second row right
animation_list.append(sprite_sheet.get_image(5.23, 1, 65, 50, 2, (199, 225, 209, 255)))
animation_list.append(sprite_sheet.get_image(6.23, 1, 65, 50, 2, (199, 225, 209, 255)))
animation_list.append(sprite_sheet.get_image(7.23, 1, 65, 50, 2, (199, 225, 209, 255)))

# Third row right
animation_list.append(sprite_sheet.get_image(8.72, 2, 55, 50, 2, (199, 225, 209, 255)))

# Fourth row right
animation_list.append(sprite_sheet.get_image(4.53, 3, 65, 50, 2, (199, 225, 209, 255)))
animation_list.append(sprite_sheet.get_image(6.08, 3, 60, 50, 2, (199, 225, 209, 255)))
animation_list.append(sprite_sheet.get_image(7.08, 3, 60, 50, 2, (199, 225, 209, 255)))
animation_list.append(sprite_sheet.get_image(8.72, 3, 55, 50, 2, (199, 225, 209, 255)))

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
        display.blit(animation_list[frame], (100, 100))

        pygame.display.update()
