import sys
import pygame
import random
import time
from collections import deque
from queue import PriorityQueue

# ------------------------
# ------ SETTING UP ------
# ------------------------

pygame.init()

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Finding Path Algorithms")

# Colors for background
BACKGROUND_COLOR = (245, 245, 245)
GRID_LINE_COLOR = (200, 200, 200) # is used to draw the boundaries between cells in the grid.
BUTTON_BG_COLOR = (40, 40, 40)
BUTTON_HOVER_COLOR =  (60, 60, 60)
BUTTON_TEXT_COLOR = (245, 245, 245)

# Node Colors
WALL_NODE_COLOR = (40, 40, 40)
FREE_NODE_COLOR = (255, 255, 255)
START_NODE_COLOR = (50, 205, 50)
END_NODE_COLOR = (220, 20, 60)
VISITED_NODE_COLOR = (173, 216, 230)
FRONTIER_NODE_COLOR = (100, 149, 237)
PATH_COLOR = (65, 105, 225)
TEXT_COLOR = (40, 40, 40)

# Setting size of the screen
SCREENWIDTH, SCREENHEIGHT = 1280, 720

# Fonts
FONT_TITLE = pygame.font.Font(None, 80)
FONT_MEDIUM = pygame.font.Font(None, 40)
FONT_SMALL = pygame.font.Font(None, 28)

# Nuumber of ROWS and COLUMNS
ROWS_GRID, COLUMNS_GRID = 25, 25

# ---------------------------------
# ------ Building Class Node ------
# ---------------------------------

class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.width = width
        self.total_rows = total_rows
        self.color = FREE_NODE_COLOR
        self.neighbors = []

    def get_pos(self):
        return self.row, self.col

    def is_visited(self):
        return self.color == VISITED_NODE_COLOR

    def is_frontier(self):
        return self.color == FRONTIER_NODE_COLOR

    def is_barrier(self):
        return self.color == WALL_NODE_COLOR

    def is_start(self):
        return self.color == START_NODE_COLOR

    def is_end(self):
        return self.color == END_NODE_COLOR

    def reset(self):
        self.color = BACKGROUND_COLOR

    def make_start(self):
        self.color = START_NODE_COLOR

    def make_visited(self):
        self.color = VISITED_NODE_COLOR

    def make_frontier(self):
        self.color = FRONTIER_NODE_COLOR

    def make_barrier(self):
        self.color = WALL_NODE_COLOR

    def make_end(self):
        self.color = END_NODE_COLOR

    def update_neighbors(self, grid):
         
        return True

    def __lt__(self, other):
        # If you need to compare nodes (e.g., for a priority queue),
        # implement the less-than operator here.
        return False

    def make_path(self):
        self.color = PATH_COLOR
  
  
      
# ----------------------------------
# ------ Building a Functions ------
# ----------------------------------

# Heuristic Function
def manhattan_h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)


def maze_generator(rows, columns):
    pass

def bfs_search(grid, start, end):
    pass

def dfs_search(grid, start, end):
    pass

def ufc_search(grid, start, end):
    pass

def greedy_search(grid, start, end):
    pass

def a_star_search(grid, start, end):
    pass

# -----------------------------
# ------ Building A GAME ------
# -----------------------------

## Building Buttons
class Button:
    def __init__(self, rect, text, callback, font=FONT_MEDIUM, bg=BUTTON_BG_COLOR, hover_bg=BUTTON_HOVER_COLOR, text_color=BUTTON_TEXT_COLOR):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.callback = callback
        self.font = font
        self.bg = bg
        self.hover_bg = hover_bg
        self.text_color = text_color
        self.hovered = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.hovered:
                self.callback()

    def draw(self, surface):
        color = self.hover_bg if self.hovered else self.bg
        pygame.draw.rect(surface, color, self.rect, border_radius=8)
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)
        
# The Base Scene
class BaseScene:
    def __init__(self):
        self.next = self

    def handle_events(self, event):
        pass

    def update(self):
        pass

    def draw(self, screen):
        pass

# The Home Scene
class HomeScene(BaseScene):
    def __init__(self):
        super().__init__()
        self.title_text = FONT_TITLE.render('Pathfinding Visualizer', True, TEXT_COLOR)
        self.buttons = []
        self.buttons.append(Button((WIDTH//2 - 125, WIDTH * 0.6, 250, 60),
            "Start", lambda: self.change_scene(InputScene())))
        self.buttons.append(Button((WIDTH//2 - 125, WIDTH * 0.7, 250, 60),
            "Exit", self.exit_game))
    def change_scene(self, scene):
        self.next = scene
    def exit_game(self):
        self.next = None
    def handle_events(self, event):
        for button in self.buttons:
            button.handle_event(event)
    def update(self):
        pass
    def draw(self, screen):
        screen.fill(BACKGROUND_COLOR)
        title_rect = self.title_text.get_rect(center=(WIDTH//2, WIDTH * 0.3))
        screen.blit(self.title_text, title_rect)
        for button in self.buttons:
            button.draw(screen)

# The Input Scene
class InputScene(BaseScene):
    def __init__(self):
        super().__init__()
        self.rows = ROWS_GRID
        self.cols = COLUMNS_GRID
        self.grid = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        self.start = None
        self.end = None
        self.bfs_path = None
        self.dfs_path = None
        self.bfs_gen = None
        self.dfs_gen = None
        self.maze_gen = None
        self.design_submode = "toggle"
        self.status_msg = "Design Mode: Toggle Walls by clicking grid."
        margin = 40
        self.panel_width = 250
        self.grid_area_width = WIDTH - self.panel_width - 40
        self.cell_size = min(self.grid_area_width // self.cols, (WIDTH - margin) // self.rows)
        self.offset_x = 20
        self.offset_y = 20
        self.buttons = []
        panel_x = WIDTH - self.panel_width + 10
        y_pos = 20
        spacing = 50
        self.buttons.append(Button((panel_x, y_pos, 230, 45), "BFS Search", self.start_bfs))
        y_pos += spacing
        self.buttons.append(Button((panel_x, y_pos, 230, 45), "DFS Search", self.start_dfs))
        y_pos += spacing
        self.buttons.append(Button((panel_x, y_pos, 230, 45), "Build Maze", self.start_maze))
        y_pos += spacing
        self.buttons.append(Button((panel_x, y_pos, 230, 45), "Random Blocks", self.build_random_blocks))
        y_pos += spacing
        self.buttons.append(Button((panel_x, y_pos, 230, 45), "Toggle Walls", lambda: self.set_mode("toggle")))
        y_pos += spacing
        self.buttons.append(Button((panel_x, y_pos, 230, 45), "Set Start", lambda: self.set_mode("set_start")))
        y_pos += spacing
        self.buttons.append(Button((panel_x, y_pos, 230, 45), "Set End", lambda: self.set_mode("set_end")))
        y_pos += spacing
        self.buttons.append(Button((panel_x, y_pos, 230, 45), "Run Path", self.run_path))
        y_pos += spacing
        self.buttons.append(Button((panel_x, y_pos, 230, 45), "New Grid", self.new_grid))
        y_pos += spacing
        self.buttons.append(Button((panel_x, y_pos, 230, 45), "Clear Grid", self.clear_grid))
        y_pos += spacing
        self.buttons.append(Button((panel_x, y_pos, 230, 45), "Main Menu", lambda: self.change_scene(HomeScene())))

    def start_bfs(self):
        if self.start and self.end:
            self.bfs_gen = bfs_search(self.grid, self.start, self.end)
            self.dfs_gen = None

    def start_dfs(self):
        if self.start and self.end:
            self.dfs_gen = dfs_search(self.grid, self.start, self.end)
            self.bfs_gen = None
    
    def start_maze(self):
        self.maze_gen = maze_generator(self.rows, self.cols)
        self.feedback = ""

    def build_random_blocks(self):
        self.grid = [[True if random.random() < 0.3 else False for _ in range(self.cols)] for _ in range(self.rows)]
        self.start = None
        self.end = None
        self.bfs_path = None
        self.dfs_path = None
        
    def run_path(self):
        if self.start and self.end:
            self.bfs_gen = bfs_search(self.grid, self.start, self.end)
            self.dfs_gen = dfs_search(self.grid, self.start, self.end)

    def new_grid(self):
        self.grid = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        self.start = None
        self.end = None
        self.bfs_path = None
        self.dfs_path = None
        
    def clear_grid(self):
        for r in range(self.rows):
            for c in range(self.cols):
                self.grid[r][c] = False
        self.bfs_path = None
        self.dfs_path = None
        
    def get_clicked_position(position, rows, width):
        gap = width // rows
        y, x = row
        
        row = y // gap
        col = x // gap
        
        return row, col
    
    def change_scene(self, scnene):
        self.next = scnene
    
    def handle_events(self, event):
        for button in self.buttons:
            button.handle_event(event)
            
        if (event.type == pygame.MOUSEBUTTONDOWN):
            x, y = event.pos
            if (x >= self.offset_x and
                x < self.offset_x + self.cell_size * self.cols and
                y >= self.offset_y and
                y < self.offset_y + self.cell_size * self.rows):
                
                col = (x - self.offset_x) // self.cell_size
                row = (y - self.offset_y) // self.cell_size
                if self.design_submode == "set_start":
                    if not self.grid[row][col]:
                        self.start = (row, col)
                        
                elif self.design_submode == "set_end":
                    if not self.grid[row][col]:
                        self.end = (row, col)

                elif self.design_submode == "toggle":
                    if (row, col) != self.start and (row, col) != self.end:
                        self.grid[row][col] = True
            
        elif event.type == pygame.KEYDOWN:
            pass
    
    def update(self):
        if (self.maze_gen):
            try:
                new_grid = next(self.maze_gen)
                self.grid = new_grid
            except StopIteration:
                self.maze_gen = None
        
        if (self.bfs_gen):
            try:
                pass
            except StopIteration:
                pass
                
                
        if (self.dfs_gen):
            try:
                pass
            except StopIteration:
                pass
                
                
    def draw(self, win, grid, rows, width):
        win.fill(BACKGROUND_COLOR)

        for row in grid:
            for node in row:
                x = node * self.cell_size + self.offset_x
                y = row * self.cell_size + self.offset_y
                node.draw(win)
        
        pygame.display.update()
                
        if self.start:
            pass
        
        if self.end:
            pass
        
        if self.bfs_gen:
            pass
        
        if self.dfs_gen:
            pass
        
        if self.bfs_path:
            pass
        
        if self.dfs_path:
            pass
    
    
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        self.clock = pygame.time.Clock()
        

        
        self.states = {
            'start': self.start,
            'level': self.level
        }

    def run(self):
        
        # Title and Icon
        pygame.display.set_caption("maze")
        icon = pygame.image.load('images/appIcon.png')
        pygame.display.set_icon(icon)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT
                    sys.exit()
                        
            self.states[self.gameStateManager.get_state()].run()
            pygame.display.update()
            

if __name__ == '__main__':
    game = Game()
    game.run()