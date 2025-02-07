import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteriods = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (updateable, drawable, asteriods)
    AsteroidField.containers = (updateable)
    asteroid_field = AsteroidField()

    Shot.containers = (updateable, drawable, shots)

    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Update player (movement)
        updateable.update(dt)

        # Check for collisions
        for asteroid in asteriods:
            if player.collision(asteroid):
                print("GAME OVER!")
                running = False
        
        # Black screen
        screen.fill((0, 0, 0))
        # Draw objects
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        
        # Limit frame rate to 60 fps
        # dt - delta time (time between frames)
        dt = clock.tick(60) / 1000


    
if __name__ == "__main__":
    main()