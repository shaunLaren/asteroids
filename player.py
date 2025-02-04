import pygame
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, 20)
        self.color = (255, 255, 255)
        self.rotation = 0

    # Draw the player
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "White", self.triangle(), 2)
