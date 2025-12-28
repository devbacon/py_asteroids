import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH

class Asteroid(CircleShape):
    # asteroid_count = 0

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # self.id = Asteroid.asteroid_count
        # Asteroid.asteroid_count += 1

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        # print(f"Drawing asteroid {self.id} at {self.position}")
        # print(f"Asteroid velocity {self.velocity}")
        # print(f"Adding {self.velocity * dt} to position")
        self.position += (self.velocity * dt)