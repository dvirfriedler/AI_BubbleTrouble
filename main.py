## import pygame
## import sys
## from bubble import Bubble
## 
## 
## # Initialize Pygame
## pygame.init()
## 
## # Screen dimensions
## screen_width = 800
## screen_height = 600
## 
## 
## # Colors
## black = (0, 0, 0)
## white = (255, 255, 255)
## red = (255, 0, 0)
## 
## # Set up the display
## screen = pygame.display.set_mode((screen_width, screen_height))
## pygame.display.set_caption("Bubble Trouble Clone")
## 
## # Player properties
## player_x = screen_width // 2
## player_width = 50
## player_height = 50
## player_speed = 5
## 
## # Bubble properties
## # Create a bubble instance
## bubble_obj = Bubble(screen_width // 2, 50, 20, 3, 3, red)
## 
## 
## bubble_obj.x = screen_width // 2
## bubble_obj.y = 50
## bubble_obj.radius = 20
## bubble_obj.speed_x = 3
## bubble_obj.speed_y = 3
## 
## # Harpoon properties
## harpoon_y = screen_height
## harpoon_speed = 10
## shooting = False
## 
## clock = pygame.time.Clock()
## 
## # Game loop
## running = True
## while running:
##     screen.fill(black)
## 
##     for event in pygame.event.get():
##         if event.type == pygame.QUIT:
##             running = False
## 
##     # Player movement
##     keys = pygame.key.get_pressed()
##     if keys[pygame.K_LEFT] and player_x > 0:
##         player_x -= player_speed
##     if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
##         player_x += player_speed
## 
##     if keys[pygame.K_SPACE] and not shooting:
##         shooting = True
##         harpoon_x = player_x + player_width // 2
##         harpoon_y = screen_height - player_height
## 
##     # Draw player
##     pygame.draw.rect(screen, white, (player_x, screen_height - player_height, player_width, player_height))
## 
##     # Bubble movement
##     bubble_obj.x += bubble_obj.speed_x
##     bubble_obj.y += bubble_obj.speed_y
## 
##     if bubble_obj.x <= 0 or bubble_obj.x >= screen_width:
##         bubble_obj.speed_x *= -1
##     if bubble_obj.y <= 0 or bubble_obj.y >= screen_height:
##         bubble_obj.speed_y *= -1
## 
##     # Draw bubble
##     pygame.draw.circle(screen, red, (bubble_obj.x, bubble_obj.y), bubble_obj.radius)
## 
##     # Harpoon shooting
##     if shooting:
##         harpoon_y -= harpoon_speed
##         pygame.draw.line(screen, white, (harpoon_x, harpoon_y), (harpoon_x, harpoon_y + 20), 2)
##         if harpoon_y < 0:
##             shooting = False
## 
##     # Collision detection
##     if shooting and bubble_obj.y - bubble_obj.radius <= harpoon_y <= bubble_obj.y + bubble_obj.radius and bubble_obj.x - bubble_obj.radius <= harpoon_x <= bubble_obj.x + bubble_obj.radius:
##         shooting = False
##         # For simplicity, reset bubble position (you could implement splitting here)
##         bubble_obj.x = screen_width // 2
##         bubble_obj.y = 50
## 
##     pygame.display.flip()
##     clock.tick(30)
## 
## pygame.quit()
## 