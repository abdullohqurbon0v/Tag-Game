import pygame
import random

pygame.init()

SIZE = 400
GRID_SIZE = 4
TILE_SIZE = SIZE // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 50)
ANIMATION_SPEED = 10 

tiles = list(range(1, GRID_SIZE ** 2)) + [0]
random.shuffle(tiles)

screen = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption("Пятнашки")


def draw_board():
    screen.fill(WHITE)
    for i, tile in enumerate(tiles):
        if tile != 0:
            x, y = (i % GRID_SIZE) * TILE_SIZE, (i // GRID_SIZE) * TILE_SIZE
            pygame.draw.rect(screen, BLACK, (x, y, TILE_SIZE, TILE_SIZE))
            text = FONT.render(str(tile), True, WHITE)
            screen.blit(text, (x + TILE_SIZE // 3, y + TILE_SIZE // 4))


def animate_move(start_index, end_index):
    sx, sy = (start_index % GRID_SIZE) * TILE_SIZE, (start_index // GRID_SIZE) * TILE_SIZE
    ex, ey = (end_index % GRID_SIZE) * TILE_SIZE, (end_index // GRID_SIZE) * TILE_SIZE

    steps = TILE_SIZE // ANIMATION_SPEED
    for step in range(steps + 1):
        draw_board()
        x = sx + (ex - sx) * step / steps
        y = sy + (ey - sy) * step / steps
        pygame.draw.rect(screen, BLACK, (x, y, TILE_SIZE, TILE_SIZE))
        text = FONT.render(str(tiles[start_index]), True, WHITE)
        screen.blit(text, (x + TILE_SIZE // 3, y + TILE_SIZE // 4))
        pygame.display.flip()
        pygame.time.delay(10)


def move_tile(index):
    empty = tiles.index(0)
    if index in [empty - 1, empty + 1, empty - GRID_SIZE, empty + GRID_SIZE]:
        animate_move(index, empty)
        tiles[empty], tiles[index] = tiles[index], tiles[empty]


running = True
while running:
    draw_board()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            index = (y // TILE_SIZE) * GRID_SIZE + (x // TILE_SIZE)
            move_tile(index)

pygame.quit()
