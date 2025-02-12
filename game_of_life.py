import pygame
import time
import sys
from pygame.locals import *

# Constants
WINDOW_SIZE = 800
CONTROL_PANEL_HEIGHT = 120
CELL_SIZE = 20
BG_COLOR = (245, 245, 245)
GRID_COLOR = (220, 220, 220)
LIVE_COLOR = (65, 105, 225)
DEAD_COLOR = (211, 211, 211)
BUTTON_BG_COLOR = (100, 149, 237)
BUTTON_HOVER_COLOR = (72, 61, 139)
TEXT_COLOR = (255, 255, 255)
ITERATION_COLOR = (30, 144, 255)

# Initialize Pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + CONTROL_PANEL_HEIGHT))
pygame.display.set_caption('Game of Life')
font = pygame.font.SysFont('Arial', 28)  # Reduced font size for buttons

# Calculate grid size
grid_size = WINDOW_SIZE // CELL_SIZE

# Create the grid and simulation state
grid = [[False for _ in range(grid_size)] for _ in range(grid_size)]
running = False
current_step = 0

# Button class definition
class Button:
    def __init__(self, text, x, y, width, height, action):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.action = action

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            color = BUTTON_HOVER_COLOR
        else:
            color = BUTTON_BG_COLOR
        pygame.draw.rect(surface, color, self.rect, border_radius=12)
        text_surf = font.render(self.text, True, TEXT_COLOR)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def is_hovered(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)

# Initialize buttons
buttons = [
    Button('Start/Pause', 20, WINDOW_SIZE + 20, 180, 50, lambda: toggle_running()),
    Button('Step Forward', 220, WINDOW_SIZE + 20, 200, 50, lambda: step_forward()),
    Button('Reset', 450, WINDOW_SIZE + 20, 150, 50, lambda: reset()),
]

# Draw the grid on the display
def draw_grid():
    for x in range(grid_size):
        for y in range(grid_size):
            color = LIVE_COLOR if grid[x][y] else DEAD_COLOR
            pygame.draw.rect(window, color, (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE-1, CELL_SIZE-1), border_radius=5)
    
    for x in range(0, WINDOW_SIZE, CELL_SIZE):
        pygame.draw.line(window, GRID_COLOR, (x, 0), (x, WINDOW_SIZE))
    for y in range(0, WINDOW_SIZE, CELL_SIZE):
        pygame.draw.line(window, GRID_COLOR, (0, y), (WINDOW_SIZE, y))

# Draw control panel, including iteration counter and buttons
def draw_control_panel():
    pygame.draw.rect(window, BG_COLOR, (0, WINDOW_SIZE, WINDOW_SIZE, CONTROL_PANEL_HEIGHT))

    # Draw iteration counter on the right side of the buttons
    iteration_font = pygame.font.SysFont('Arial', 36)  # Larger font for iteration
    iteration_text = iteration_font.render(f'Iteration: {current_step}', True, ITERATION_COLOR)
    window.blit(iteration_text, (WINDOW_SIZE - 250, WINDOW_SIZE + 70))

    for button in buttons:
        button.draw(window)

# Update grid based on Conway's rules
def update_grid():
    global grid
    new_grid = [[grid[x][y] for y in range(grid_size)] for x in range(grid_size)]
    
    for x in range(grid_size):
        for y in range(grid_size):
            alive_neighbors = 0
            
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if not (dx == 0 and dy == 0):
                        neighbor_x, neighbor_y = x + dx, y + dy
                        if 0 <= neighbor_x < grid_size and 0 <= neighbor_y < grid_size:
                            alive_neighbors += grid[neighbor_x][neighbor_y]
            
            if grid[x][y]:  # Cell is alive
                if alive_neighbors < 2 or alive_neighbors > 3:
                    new_grid[x][y] = False
            else:  # Cell is dead
                if alive_neighbors == 3:
                    new_grid[x][y] = True
    
    grid = new_grid

# Button functions
def toggle_running():
    global running
    running = not running

def step_forward():
    global current_step
    update_grid()
    current_step += 1

def reset():
    global grid, running, current_step
    grid = [[False for _ in range(grid_size)] for _ in range(grid_size)]
    running = False
    current_step = 0

# Main game loop
def main():
    global running, current_step
    clock = pygame.time.Clock()

    while True:
        window.fill(BG_COLOR)
        draw_grid()
        draw_control_panel()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    if event.pos[1] > WINDOW_SIZE:  # Click is in the control panel
                        for button in buttons:
                            if button.is_hovered():
                                button.action()
                    else:
                        if not running:
                            x, y = event.pos
                            grid_x, grid_y = x // CELL_SIZE, y // CELL_SIZE
                            grid[grid_x][grid_y] = not grid[grid_x][grid_y]

        if running:
            update_grid()
            current_step += 1
            time.sleep(1)  # Delay to make simulation followable

        clock.tick(60)

if __name__ == '__main__':
    main()
