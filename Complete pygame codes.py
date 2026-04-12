"""import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lesson - Delta Time")

clock = pygame.time.Clock()

player = pygame.Rect(100, 100, 50, 50)

speed = 300  # pixels per second

running = True
while running:

    dt = clock.tick(60) / 1000  # seconds since last frame

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    velocity_x = 0
    velocity_y = 0

    if keys[pygame.K_LEFT]:
        velocity_x = -speed
    if keys[pygame.K_RIGHT]:
        velocity_x = speed
    if keys[pygame.K_UP]:
        velocity_y = -speed
    if keys[pygame.K_DOWN]:
        velocity_y = speed

    player.x += velocity_x * dt
    player.y += velocity_y * dt

    # Keep inside window
    player.x = max(0, min(player.x, WIDTH - player.width))
    player.y = max(0, min(player.y, HEIGHT - player.height))

    screen.fill((15, 15, 20))
    pygame.draw.rect(screen, (100, 200, 255), player)

    pygame.display.flip()

pygame.quit()
sys.exit()"""
# Drawing shapes
# Coordinates system
# Rect objects
# Moving objects
# Delta time (frame-independent movement)
# Basic physics logic
# Velocity
# Smooth motion
'''Frame-dependent movement (incorrect)

Time-dependent movement (correct)

Velocity abstraction

Separation of simulation state from rendering'''
import pygame
import sys

pygame.init()

WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lesson 4 - Gravity & Jump")

clock = pygame.time.Clock()

# Player setup
player = pygame.Rect(100, 300, 50, 50)
pos_y = 300.0
velocity_y = 0.0

# Physics constants
gravity = 1200      # px/s^2
jump_force = -500   # px/s
floor_y = 500

on_ground = False

running = True
while running:

    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on_ground:
                velocity_y = jump_force
                on_ground = False

    # Apply gravity
    velocity_y += gravity * dt

    # Update position
    pos_y += velocity_y * dt
    player.y = int(pos_y)

    # Floor collision
    if player.bottom >= floor_y:
        player.bottom = floor_y
        pos_y = player.y
        velocity_y = 0
        on_ground = True

    # Drawing
    screen.fill((25, 25, 30))

    pygame.draw.line(screen, (200, 200, 200), (0, floor_y), (WIDTH, floor_y))
    pygame.draw.rect(screen, (100, 200, 255), player)

    pygame.display.flip()

pygame.quit()
sys.exit()