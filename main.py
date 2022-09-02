import pygame
from pokemon import Pokemon

# Initializing pygame and creating the window
pygame.init()
display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("Gather da Lampp-it")

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
pygame.mixer.music.play(-1)

# Sounds
cry = pygame.mixer.Sound("data/haunter.mp3")

game_loop = True

if __name__ == "__main__":
    while game_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_loop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    cry.play()

        # draw()
        display.fill([105, 61, 28])

        object_group.update()
        object_group.draw(display)

        pygame.display.update()
