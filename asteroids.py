import pygame
import random

from typing import override
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_SPLIT_SPEED_MULTIPLIER, LINE_WIDTH
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    @override
    def draw(self, screen: pygame.Surface) -> None:
        _ = pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    @override
    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        asteroid1 = Asteroid(self.position[0], self.position[1], (self.radius - ASTEROID_MIN_RADIUS))
        asteroid1.velocity = self.velocity * ASTEROID_SPLIT_SPEED_MULTIPLIER
        asteroid1.velocity = asteroid1.velocity.rotate(angle)

        asteroid2 = Asteroid(self.position[0], self.position[1], (self.radius - ASTEROID_MIN_RADIUS))
        asteroid2.velocity = self.velocity * ASTEROID_SPLIT_SPEED_MULTIPLIER
        asteroid2.velocity = asteroid2.velocity.rotate(-angle)
