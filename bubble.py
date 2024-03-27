import pygame

class Bubble:
    def __init__(self, x, y, radius, speed_x, speed_y, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.color = color

    def move(self, screen_width, screen_height):
        # Update the bubble position
        self.x += self.speed_x
        self.y += self.speed_y

        # Reverse direction if hitting the screen edge
        if self.x <= 0 or self.x >= screen_width:
            self.speed_x *= -1
        if self.y <= 0 or self.y >= screen_height:
            self.speed_y *= -1

    def draw(self, screen):
        # Draw the bubble on the screen
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def check_collision(self, harpoon_x, harpoon_y):
        # Check if the harpoon hits the bubble
        return self.y - self.radius <= harpoon_y <= self.y + self.radius and self.x - self.radius <= harpoon_x <= self.x + self.radius


