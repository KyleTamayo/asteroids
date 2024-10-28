import pygame
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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

	updatable 		= pygame.sprite.Group()
	drawable  		= pygame.sprite.Group()
	asteroids 		= pygame.sprite.Group()
	shots     = pygame.sprite.Group()

	Player.containers 		 = (updatable, drawable)
	Asteroid.containers 	 = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers          = (shots, updatable, drawable)


	player 	= Player(x, y)
	field 	= AsteroidField()
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		for obj in updatable:
			obj.update(dt)

		screen.fill("black")

		for obj in drawable:
			obj.draw(screen)

		for ast in asteroids:
			if(ast.collision(player)):
				print("Game Over!")
				return
			for shot in shots:
				if ast.collision(shot):
					shot.kill()
					ast.kill()

		pygame.display.flip()
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()