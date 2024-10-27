import pygame as py

# Initialize Pygame
py.init()

# Set up the window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
py.display.set_caption("Rectangle Move and Jump")

# Define colors
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)
BLUE = (65, 105, 225)  # Royal Blue
SILVER = (192, 192, 192)  # Silver
BLUE = (102, 204, 255)        # Light blue
PASTEL_PINK = (255, 204, 204) # Pastel pink



# Define player properties
player_width = 50
player_height = 50
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT // 2 - player_height // 2
player = py.Rect(player_x, player_y, player_width, player_height)
player_speed = 5
is_jumping = False
jump_count = 10

# Main game loop
run = True
while run:
    # Handle events
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

    # Handle key presses
    keys = py.key.get_pressed()
    if keys[py.K_a]:
        player.x -= player_speed
    if keys[py.K_d]:
        player.x += player_speed

    # Jumping mechanism
    if not is_jumping:
        if keys[py.K_SPACE]:
            is_jumping = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            player.y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jumping = False
            jump_count = 10

    # Boundary checking
    if player.x <= 0:
        player.x = 0
    if player.x >= SCREEN_WIDTH - player_width:
        player.x = SCREEN_WIDTH - player_width
    if player.y <= 0:
        player.y = 0
    if player.y >= SCREEN_HEIGHT - player_height:
        player.y = SCREEN_HEIGHT - player_height

    # Draw everything
    screen.fill(BLACK)
    py.draw.rect(screen, GOLD, player)
    py.display.update()

    # Cap the frame rate
    py.time.Clock().tick(60)

# Quit Pygame
py.quit()
