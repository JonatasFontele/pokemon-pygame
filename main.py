import random

import pygame
from model.pokemon import Pokemon
from model.haunter import Haunter
from model.pokeball import Pokeball
from model.move_attack import MoveAttack

# Initializing pygame and creating the window
pygame.init()
WIDTH, HEIGHT = 840, 480
display = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Pokéball Invaders")
game_icon = pygame.image.load('data/Haunter.png')
pygame.display.set_icon(game_icon)
game_loop = True
game_over = False
timer = 0

# Objects
object_group = pygame.sprite.Group()
pokeball_group = pygame.sprite.Group()
attack_group = pygame.sprite.Group()

# Background
background = pygame.sprite.Sprite(object_group)
background.image = pygame.image.load("data/haunted_house.jpg")
background.image = pygame.transform.scale(background.image, [840, 480])
background.rect = background.image.get_rect()

#pokemon = Pokemon(object_group)
haunter = Haunter(object_group)
# haunter.rect.center = [200, 400]

pokeball = Pokeball(object_group)

# Music
pygame.mixer.music.load("data/lavender-town.mp3")
pygame.mixer.music.set_volume(0.01)
pygame.mixer.music.play(-1)

# Sounds
cry = pygame.mixer.Sound("data/haunter.mp3")
cry.set_volume(0.1)

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
                    haunter.animate()

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
        object_group.draw(display)

        # Frame image
        haunter.update()
        display.blit(haunter.animation_list[haunter.frame], (50, 50))

        pygame.display.update()
