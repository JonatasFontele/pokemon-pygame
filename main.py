import pygame
from pokemon import Pokemon

# Initializing pygame and creating the window
pygame.init()
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("Pokéball Invaders")
gameIcon = pygame.image.load('data/Haunter.png')
pygame.display.set_icon(gameIcon)

#def draw():
    #display.fill([105, 61, 28])
    # player = pygame.Rect(50, 50, 100, 100)
    # pygame.draw.rect(display, [255, 255, 255, 255], player)

# Objects
object_group = pygame.sprite.Group()
# haunter = pygame.sprite.Sprite(draw_group)

haunter = Pokemon(object_group)

# Music
pygame.mixer.music.load("data/lavender-town.mp3")
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)

# Sounds
cry = pygame.mixer.Sound("data/haunter.mp3")
cry.set_volume(0.2)

game_loop = True

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
                if event.key == pygame.K_SPACE:
                    cry.play()

        # Update logic
        object_group.update()

        # Draw
        display.fill([105, 61, 28])
        object_group.draw(display)

        pygame.display.update()
