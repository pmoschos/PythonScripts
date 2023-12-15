import pygame
from pygame.locals import *
import random
from constants import *
from my_classes import Button, Pipe, Bird

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Game Variables
ground_scroll = 0
flying = False
game_over = False
last_pipe = pygame.time.get_ticks() - PIPE_FREQUENCY
score = 0
pass_pipe = False

# Load images
def load_image(path):
    try:
        return pygame.image.load(path)
    except pygame.error as e:
        print(f"Error loading image {path}: {e}")
        exit(1)

bg = load_image('images/bg.png')
ground_img = load_image('images/ground.png')
button_img = load_image('images/restart.png')

# Font and Colors
font = pygame.font.SysFont('Bauhaus 93', 60)

# Utility Functions
def draw_text(text, x, y):
    img = font.render(text, True, WHITE)
    screen.blit(img, (x, y))

# Game Initialization
bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()
flappy = Bird(100, SCREEN_HEIGHT // 2, flying, game_over)
bird_group.add(flappy)
button = Button(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 100, button_img, screen)

# Main Game Loop
def main():
    global flying, game_over, score, pass_pipe, ground_scroll

    run = True
    while run:
        clock.tick(FPS)
        screen.blit(bg, (0, 0))

        bird_group.draw(screen)
        bird_group.update(flying, game_over)
        pipe_group.draw(screen)

        # Update ground scroll only when the game is not over
        if not game_over:
            ground_scroll -= SCROLL_SPEED
            if abs(ground_scroll) > 35:
                ground_scroll = 0
        
        # Draw the ground
        screen.blit(ground_img, (ground_scroll, GROUND_HEIGHT))

        check_score()
        check_collisions()
        update_pipes()
        handle_game_over()

        handle_events()

        pygame.display.update()

    pygame.quit()


def check_score():
    global score, pass_pipe
    if len(pipe_group) > 0:
        pipe = pipe_group.sprites()[0]
        if pipe.rect.left < flappy.rect.left < pipe.rect.right and not pass_pipe:
            pass_pipe = True
        if pass_pipe and flappy.rect.left > pipe.rect.right:
            score += 1
            pass_pipe = False
    draw_text(str(score), SCREEN_WIDTH // 2, 20)

def check_collisions():
    global game_over
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
        game_over = True
    if flappy.rect.bottom >= GROUND_HEIGHT:
        game_over = True
        flying = False

def update_pipes():
    global last_pipe
    if not game_over and flying:
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > PIPE_FREQUENCY:
            pipe_height = random.randint(-100, 100)
            btm_pipe = Pipe(SCREEN_WIDTH, SCREEN_HEIGHT // 2 + pipe_height, -1)
            top_pipe = Pipe(SCREEN_WIDTH, SCREEN_HEIGHT // 2 + pipe_height, 1)
            pipe_group.add(btm_pipe)
            pipe_group.add(top_pipe)
            last_pipe = time_now
        pipe_group.update()

def handle_game_over():
    if game_over and button.draw(screen):
        reset_game()

def reset_game():
    global game_over, score, flying
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = SCREEN_HEIGHT // 2
    score = 0
    game_over = False
    flying = False

def handle_events():
    global flying
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN and not flying and not game_over:
            flying = True

if __name__ == "__main__":
    main()
