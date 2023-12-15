import pygame
from pygame.locals import *
import random

# Constants
SCREEN_WIDTH = 864
SCREEN_HEIGHT = 936
FPS = 60
PIPE_GAP = 150
PIPE_FREQUENCY = 1500  # milliseconds
GRAVITY = 0.5
FLAP_STRENGTH = -10
MAX_DROP_SPEED = 8
GROUND_HEIGHT = 768
SCROLL_SPEED = 4
FLAP_COOLDOWN = 5

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

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
WHITE = (255, 255, 255)

# Utility Functions
def draw_text(text, x, y):
    img = font.render(text, True, WHITE)
    screen.blit(img, (x, y))

# Game Classes
class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = [load_image(f'images/bird{num}.png') for num in range(1, 4)]
        self.index = 0
        self.counter = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=[x, y])
        self.vel = 0
        self.clicked = False

    def update(self):
        if flying:
            self.vel = min(self.vel + GRAVITY, MAX_DROP_SPEED)
            if not game_over or (game_over and self.rect.bottom < GROUND_HEIGHT):
                self.rect.y += int(self.vel)
        if not game_over:
            self.handle_flapping()
        self.rotate_bird()

    def handle_flapping(self):
        if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
            self.clicked = True
            self.vel = FLAP_STRENGTH
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        self.counter += 1
        if self.counter > FLAP_COOLDOWN:
            self.counter = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

    def rotate_bird(self):
        self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('images/pipe.png')
        self.rect = self.image.get_rect()
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - PIPE_GAP // 2]
        else:
            self.rect.topleft = [x, y + PIPE_GAP // 2]

    def update(self):
        self.rect.x -= SCROLL_SPEED
        if self.rect.right < 0:
            self.kill()

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

# Game Initialization
bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()
flappy = Bird(100, SCREEN_HEIGHT // 2)
bird_group.add(flappy)
button = Button(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 100, button_img)

# Game Variables
ground_scroll = 0
flying = False
game_over = False
last_pipe = pygame.time.get_ticks() - PIPE_FREQUENCY
score = 0
pass_pipe = False

# Main Game Loop
def main():
    global flying, game_over, score, pass_pipe, ground_scroll

    run = True
    while run:
        clock.tick(FPS)
        screen.blit(bg, (0, 0))

        bird_group.draw(screen)
        bird_group.update()
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
    if game_over and button.draw():
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
