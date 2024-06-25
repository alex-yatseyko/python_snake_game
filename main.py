# Example file showing a basic pygame "game loop"
import pygame
import random

# pygame setup
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

def generate_starting_position():
    position_range = (pixel_width // 2, screen_width - pixel_width // 2, pixel_width)
    return random.randrange(*position_range), random.randrange(*position_range)


# Playground
pixel_width = 50

# snake
snake_pixel = pygame.rect.Rect(0, 0, pixel_width, pixel_width)
snake_pixel.center = generate_starting_position()
snake = snake_pixel.copy()

# target
target_pixel = pygame.rect.Rect(0, 0, pixel_width, pixel_width)
target_pixel.center = generate_starting_position()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    pygame.draw.rect(screen, "purple", snake_pixel)
    pygame.draw.rect(screen, "green", target_pixel)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()