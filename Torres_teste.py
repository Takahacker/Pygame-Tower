# Inicialização
import pygame
import random
import sys

# Tower Types
TOWER_RED = "red"
TOWER_BLUE = "blue"
TOWER_GREEN = "green"

# Tower Images
red_tower_image = pygame.image.load("assets/img/red_tower.png")
blue_tower_image = pygame.image.load("assets/img/blue_tower.png")
green_tower_image = pygame.image.load("assets/img/green_tower.png")

# Tower Positions
red_tower_position = (WIDTH - TAMANHO_QUADRADO // 2 - 10, TAMANHO_QUADRADO // 2 + 10)
blue_tower_position = (WIDTH - TAMANHO_QUADRADO // 2 - 10, TAMANHO_QUADRADO // 2 + 2 * TAMANHO_QUADRADO + 10)
green_tower_position = (WIDTH - TAMANHO_QUADRADO // 2 - 10, TAMANHO_QUADRADO // 2 + 4 * TAMANHO_QUADRADO + 10)

# Selected Tower
selected_tower = None

# Game Loop
running = True
while running:
    clock.tick(FPS)

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_started = True
        elif event.type == pygame.MOUSEBUTTONDOWN and game_started:
            if event.button == 1:  # Left Mouse Button
                mouse_pos = pygame.mouse.get_pos()
                if selected_tower is not None:
                    # Check if the player clicked on a valid grid position
                    clicked_grid_x = mouse_pos[0] // TAMANHO_QUADRADO
                    clicked_grid_y = mouse_pos[1] // TAMANHO_QUADRADO
                    if (clicked_grid_x, clicked_grid_y) not in path_points:
                        if selected_tower == TOWER_RED:
                            projectiles.append(
                                red_tower.shoot_projectile((clicked_grid_x * TAMANHO_QUADRADO + TAMANHO_QUADRADO // 2,
                                                           clicked_grid_y * TAMANHO_QUADRADO + TAMANHO_QUADRADO // 2))
                            )
                        elif selected_tower == TOWER_BLUE:
                            projectiles.append(
                                blue_tower.shoot_projectile((clicked_grid_x * TAMANHO_QUADRADO + TAMANHO_QUADRADO // 2,
                                                            clicked_grid_y * TAMANHO_QUADRADO + TAMANHO_QUADRADO // 2))
                            )
                        elif selected_tower == TOWER_GREEN:
                            projectiles.append(
                                green_tower.shoot_projectile((clicked_grid_x * TAMANHO_QUADRADO + TAMANHO_QUADRADO // 2,
                                                             clicked_grid_y * TAMANHO_QUADRADO + TAMANHO_QUADRADO // 2))
                            )
                else:
                    # Check if the player clicked on a tower
                    if distance(mouse_pos, red_tower_position) <= TAMANHO_QUADRADO // 2:
                        selected_tower = TOWER_RED
                    elif distance(mouse_pos, blue_tower_position) <= TAMANHO_QUADRADO // 2:
                        selected_tower = TOWER_BLUE
                    elif distance(mouse_pos, green_tower_position) <= TAMANHO_QUADRADO // 2:
                        selected_tower = TOWER_GREEN

    # Game Logic
    if game_started:
        # Update ball and projectiles

    # Render
    screen.blit(game_background_image, (0, 0))

    # Draw Grid

    # Draw Path

    # Draw Towers
    screen.blit(red_tower_image, (red_tower_position[0] - TAMANHO_QUADRADO // 2, red_tower_position[1] - TAMANHO_QUADRADO // 2))
    screen.blit(blue_tower_image, (blue_tower_position[0] - TAMANHO_QUADRADO // 2, blue_tower_position[1] - TAMANHO_QUADRADO // 2))
    screen.blit(green_tower_image, (green_tower_position[0] - TAMANHO_QUADRADO // 2, green_tower_position[1] - TAMANHO_QUADRADO // 2))

    # Draw Selected Tower Indicator
    if selected_tower is not None:
        if selected_tower == TOWER_RED:
            pygame.draw.circle(screen, (255, 0, 0), red_tower_position, TAMANHO_QUADRADO // 2, 3)
        elif selected_tower == TOWER_BLUE:
            pygame.draw.circle(screen, (0, 0, 255), blue_tower_position, TAMANHO_QUADRADO // 2, 3)
        elif selected_tower == TOWER_GREEN:
            pygame.draw.circle(screen, (0, 255, 0), green_tower_position, TAMANHO_QUADRADO // 2, 3)

    # Draw Ball

    # Draw Projectiles

    pygame.display.flip()

pygame.quit()
sys.exit()
