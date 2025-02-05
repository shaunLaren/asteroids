import pygame
from constants import *
from player import Player
from asteroid import Asteroid

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteriods = pygame.sprite.Group()
    Asteroid.containers = (updateable, drawable, asteriods)
    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    
    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Update player (movement)
        updateable.update(dt)

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