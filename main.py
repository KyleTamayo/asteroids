import pygame
from player import *
from constants import *

def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	clock = pygame.time.Clock()
	dt = 0

	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	player = Player(x, y)
	
	while(True):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")

		for obj in updatable:
			obj.update(dt)

		for obj in drawable:
			obj.draw(screen)


		pygame.display.flip()
		dt = 1000 / clock.tick(60)

if __name__ == "__main__":
	main()