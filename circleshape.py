import pygame
from constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision_check(self, circle_shape):
        total_radius = self.radius + circle_shape.radius
        if self.position.distance_to(circle_shape.position) < total_radius:
            return True
        return False
    
    def wrap_position(self):
    # If we go off the right side, appear on left
        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0
    # If we go off the left side, appear on right
        elif self.position.x < 0:
            self.position.x = SCREEN_WIDTH
    # If we go off the bottom, appear on top
        if self.position.y > SCREEN_HEIGHT:
            self.position.y = 0
    # If we go off the top, appear on bottom
        elif self.position.y < 0:
            self.position.y = SCREEN_HEIGHT