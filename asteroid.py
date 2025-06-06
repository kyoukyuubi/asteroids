from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.can_wrap = False
        self.spawn_timer = 0  # Time since spawn

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.spawn_timer += dt
        
        # Only start wrapping after asteroid has moved a bit
        if self.spawn_timer > 2: 
            self.can_wrap = True
            
        if self.can_wrap:
            self.wrap_position()

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_vector1 = self.velocity.rotate(random_angle)
            new_vector2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            astroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            astroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            astroid1.velocity = new_vector1 * 1.2
            astroid2.velocity = new_vector2 * 1.2
        self.kill()
