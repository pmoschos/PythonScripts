import pygame
from constants import *

# Game Classes

# Bird Class
class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y, flying, game_over):
        pygame.sprite.Sprite.__init__(self)
        self.images = [load_image(f'images/bird{num}.png') for num in range(1, 4)]
        self.index = 0
        self.counter = 0

        # old
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=[x, y])

        self.vel = 0
        self.clicked = False
        self.flying = flying
        self.game_over = game_over

    def update(self, flying, game_over):
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

# Button class
class Button():
    def __init__(self, x, y, image, screen):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.screen = screen

    def draw(self, screen):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

# Pipe class
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

# helper function
def load_image(path):
    try:
        return pygame.image.load(path)
    except pygame.error as e:
        print(f"Error loading image {path}: {e}")
        exit(1)