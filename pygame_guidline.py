# Guideline Pygame in Python
# =================================

import pygame

# # Size of the window
# WIDTH = 800
# HEIGHT = 700

# screen = pygame.display.set_mode((WIDTH, HEIGHT))

# # In order to keep the window running, ween need to create the second element of those major elements, which is the game loop

# run = True
# while run:
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			run = False


# pygame.quit()


# ==================================================

# Example
# ---------------------



# Size of the window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((300,250,50,50)) #(x_coord, y_coord, width, height)

# In order to keep the window running, ween need to create the second element of those major elements, which is the game loop

# run = True
# while run:
#     screen.fill((0,0,0))
#     pygame.draw.rect(screen, (255,0,0), player)
#     key = pygame.key.get_pressed()
#     if key[pygame.K_a] == True: # If the player pressed 'a'
#         player.move_ip(-1,0)
#     if key[pygame.K_d] == True: # If the player pressed 'd'
#         player.move_ip(1,0)
#     if key[pygame.K_w] == True: # If the player pressed 'a'
#         player.move_ip(0,-1)
#     if key[pygame.K_s] == True: # If the player pressed 'd'
#         player.move_ip(0,1)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
    
#     pygame.display.update()

pygame.init()

# Create screen
screen = pygame.display.set_mode((500, 500))  # Example window size

# Define font
text_font = pygame.font.SysFont("Arial", 30)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

run = True
while run:
    # Handle events first
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Fill background to prevent ghosting
    screen.fill((255, 255, 255))  # White background

    # Draw text
    draw_text("Hello World", text_font, (0, 0, 0), 120, 150)

    # Update the display
    pygame.display.update()

pygame.quit()
