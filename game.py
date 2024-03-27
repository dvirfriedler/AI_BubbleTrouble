import pygame
from bubble import Bubble
from player import Player
from shoot import Shoot

import math


class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Bubble Trouble Clone")

        self.clock = pygame.time.Clock()
        self.running = True

        # Game colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)

        # Player properties
        self.player = Player(self.screen_width // 2, self.screen_height - 50, 50, 50, 5, self.screen_width, self.screen_height)


        # Bubble
        self.bubbles = [Bubble(self.screen_width // 2, 50, 20, 3, 3, self.red)]



        # Harpoon properties
        self.shooting_system = Shoot()


    def run(self):
        while self.running:
            self.screen.fill(self.black)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.handle_input()
            self.update_game()
            self.draw()

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move_left()
        if keys[pygame.K_RIGHT]:
            self.player.move_right()
        if keys[pygame.K_SPACE]:
                self.shooting_system.shoot(self.player.x + self.player.width // 2, self.player.y, 10, shot_type="basic")


    def update_game(self):
        self.shooting_system.update_projectiles()
        for bubble in self.bubbles:
            bubble.move(self.screen_width, self.screen_height)
            if self.player.shooting and bubble.check_collision(self.player.harpoon_x, self.player.harpoon_y):
                self.handle_shoot_hit(bubble)
                # Reset or split the bubble here
                
        self.player.update()

        # Check collision between the bubble and the harpoon
        for bubble in self.bubbles:
            if self.player.shooting and bubble.check_collision(self.player.harpoon_x, self.player.harpoon_y):
                self.player.shooting = False
                self.handle_shoot_hit(bubble)
            
            
    
    def handle_shoot_hit(self,bubble):
            self.player.shooting = False
            self.bubbles.remove(bubble)
            self.bubbles.append(Bubble(bubble.x, bubble.y, bubble.radius // 2, -bubble.speed_x, -abs(bubble.speed_y), self.red))
            self.bubbles.append(Bubble(bubble.x, bubble.y, bubble.radius // 2, bubble.speed_x,  -abs(bubble.speed_y), self.red))
            
            for bubble in self.bubbles:
                if bubble.radius < 5:
                    self.bubbles.remove(bubble)
            # Reset or split the bubble here


    def draw(self):
        self.screen.fill(self.black)  # It's good practice to clear the screen at the start of draw
        self.player.draw(self.screen)
        self.shooting_system.draw_projectiles(self.screen)
        for bubble in self.bubbles:
            bubble.draw(self.screen)


if __name__ == "__main__":
    game = Game()
    game.run()
