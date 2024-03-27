import pygame

class Projectile:
    def __init__(self, x, y, speed, width=2, height=20, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.speed = speed
        self.width = width
        self.height = height
        self.color = color
        self.active = True

    def update(self):
        self.y -= self.speed
        if self.y < 0:
            self.active = False

    def draw(self, screen):
        pygame.draw.line(screen, self.color, (self.x, self.y), (self.x, self.y + self.height), self.width)

class Shoot:
    def __init__(self):
        self.projectiles = []

    def shoot(self, x, y, speed, shot_type="basic"):
        if shot_type == "basic":
            self.projectiles.append(Projectile(x, y, speed))
        elif shot_type == "fast":
            self.projectiles.append(Projectile(x, y, speed * 1.5))
        elif shot_type == "wide":
            self.projectiles.append(Projectile(x, y, speed, width=5))
        # Add more shot types as needed

    def update_projectiles(self):
        for projectile in self.projectiles[:]:
            projectile.update()
            if not projectile.active:
                self.projectiles.remove(projectile)

    def draw_projectiles(self, screen):
        for projectile in self.projectiles:
            projectile.draw(screen)
