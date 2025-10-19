import random
import pygame.draw
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(self.position.x, self.position.y, radius)
        asteroid_one.velocity = a * 1.2
        asteroid_two = Asteroid(self.position.x, self.position.y, radius)
        asteroid_two.velocity = b * 1.2
