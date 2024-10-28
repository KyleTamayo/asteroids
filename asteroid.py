import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, 2)

	def update(self, dt):
		self.position += (self.velocity * dt)

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		else:
			angle = random.uniform(20, 50)
			v1 = pygame.Vector2.rotate(self.velocity, angle)
			v2 = pygame.Vector2.rotate(self.velocity, -angle)
			newSize = self.radius - ASTEROID_MIN_RADIUS
			a1 = Asteroid(self.position.x, self.position.y, newSize)
			a2 = Asteroid(self.position.x, self.position.y, newSize)
			a1.velocity = v1 * 1.2
			a2.velocity = v2 * 1.2