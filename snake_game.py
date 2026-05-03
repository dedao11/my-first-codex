import pygame
import random

# 初始化 Pygame
pygame.init()

# 屏幕与网格设置
CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("贪吃蛇")
clock = pygame.time.Clock()
font = pygame.font.SysFont("SimHei", 28)

# 颜色
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (220, 30, 30)
WHITE = (255, 255, 255)


def random_food(snake):
    """生成不与蛇身重叠的食物位置。"""
    while True:
        pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if pos not in snake:
            return pos


def draw_cell(pos, color):
    x, y = pos
    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, BLACK, rect, 1)


def game_loop():
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    direction = (1, 0)  # 初始向右
    food = random_food(snake)
    score = 0

    running = True
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if game_over and event.key == pygame.K_r:
                    return game_loop()  # 按 R 重新开始
                if event.key == pygame.K_UP and direction != (0, 1):
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)

        if not game_over:
            head_x, head_y = snake[0]
            dx, dy = direction
            new_head = (head_x + dx, head_y + dy)

            # 撞墙或撞自己
            if (
                new_head[0] < 0
                or new_head[0] >= GRID_WIDTH
                or new_head[1] < 0
                or new_head[1] >= GRID_HEIGHT
                or new_head in snake
            ):
                game_over = True
            else:
                snake.insert(0, new_head)
                if new_head == food:
                    score += 1
                    food = random_food(snake)
                else:
                    snake.pop()

        # 绘制
        screen.fill(BLACK)
        draw_cell(food, RED)
        for segment in snake:
            draw_cell(segment, GREEN)

        score_text = font.render(f"分数: {score}", True, WHITE)
        screen.blit(score_text, (10, 8))

        if game_over:
            over_text = font.render("游戏结束! 按 R 重开", True, WHITE)
            text_rect = over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(over_text, text_rect)

        pygame.display.flip()
        clock.tick(10)  # 控制速度

    pygame.quit()


if __name__ == "__main__":
    game_loop()
