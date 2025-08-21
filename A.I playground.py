import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Super Mario Prototype")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# FPS
FPS = 60
clock = pygame.time.Clock()

# Tile size
TILE_SIZE = 32

# Define Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.vel = None
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed = 5
        self.gravity = 1
        self.jump_power = -15
        self.on_ground = False

    def update(self, platforms):
        # Horizontal movement
        self.velocity_x = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.velocity_x = -self.speed
        if keys[pygame.K_RIGHT]:
            var = self.vel



