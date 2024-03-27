import pygame

class Player:
    def __init__(self, x, y, width, height, speed, screen_width, screen_height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.color = (255, 255, 255)  # White

        # Harpoon properties
        self.shooting = False
        self.harpoon_x = 0
        self.harpoon_y = 0
        self.harpoon_speed = 10
        self.harpoon_color = (255, 255, 255)  # White

    def move_left(self):
        if self.x - self.speed > 0:
            self.x -= self.speed

    def move_right(self):
        if self.x + self.width + self.speed < self.screen_width:
            self.x += self.speed

    def shoot(self):
        if not self.shooting:
            self.shooting = True
            self.harpoon_x = self.x + self.width // 2
            self.harpoon_y = self.y

    def update(self):
        if self.shooting:
            self.harpoon_y -= self.harpoon_speed
            if self.harpoon_y < 0:
                self.shooting = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        if self.shooting:
            pygame.draw.line(screen, self.harpoon_color, (self.harpoon_x, self.harpoon_y), (self.harpoon_x, self.harpoon_y + 20), 2)
