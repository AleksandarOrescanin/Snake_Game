import pygame
import screen
from pygame.math import Vector2

# ****************************************************************************************************

class Snake:
    pygame.init()

    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        self.new_block = False
        self.screen = screen.Screen()

        self.head_up = pygame.image.load('assets/head_up.png').convert_alpha()
        self.head_right = pygame.image.load('assets/head_right.png').convert_alpha()
        self.head_down = pygame.image.load('assets/head_down.png').convert_alpha()
        self.head_left = pygame.image.load('assets/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('assets/tail_up.png').convert_alpha()
        self.tail_right = pygame.image.load('assets/tail_right.png').convert_alpha()
        self.tail_down = pygame.image.load('assets/tail_down.png').convert_alpha()
        self.tail_left = pygame.image.load('assets/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('assets/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('assets/body_horizontal.png').convert_alpha()
        self.body_top_left = pygame.image.load('assets/body_topleft.png').convert_alpha()
        self.body_top_right = pygame.image.load('assets/body_topright.png').convert_alpha()
        self.body_bottom_left = pygame.image.load('assets/body_bottomleft.png').convert_alpha()
        self.body_bottom_right = pygame.image.load('assets/body_bottomright.png').convert_alpha()

        self.eat_sound = pygame.mixer.Sound('assets/crunch.wav')

# ****************************************************************************************************

    def draw_snake(self):
        self.update_head()
        self.update_tail()

        for index, block in enumerate(self.body):
            x_position = int(block.x * self.screen.CELL_SIZE)
            y_position = int(block.y * self.screen.CELL_SIZE)
            snake_rect = pygame.Rect(x_position, y_position, self.screen.CELL_SIZE, self.screen.CELL_SIZE)

            if index == 0:
                self.screen.display.blit(self.head, snake_rect)
            elif index == (len(self.body) - 1):
                self.screen.display.blit(self.tail, snake_rect)
            else:
                previous_block = (self.body[index + 1] - block)
                next_block = (self.body[index - 1] - block)

                if previous_block.x == next_block.x:
                    self.screen.display.blit(self.body_vertical, snake_rect)
                elif previous_block.y == next_block.y:
                    self.screen.display.blit(self.body_horizontal, snake_rect)
                else:
                    if ((previous_block.x == -1) and (next_block.y == -1)) or \
                            ((previous_block.y == -1) and (next_block.x == -1)):
                        self.screen.display.blit(self.body_top_left, snake_rect)
                    elif ((previous_block.x == -1) and (next_block.y == 1)) or \
                            ((previous_block.y == 1) and (next_block.x == -1)):
                        self.screen.display.blit(self.body_bottom_left, snake_rect)
                    elif ((previous_block.x == 1) and (next_block.y == -1)) or \
                            ((previous_block.y == -1) and (next_block.x == 1)):
                        self.screen.display.blit(self.body_top_right, snake_rect)
                    elif ((previous_block.x == 1) and (next_block.y == 1)) or \
                            ((previous_block.y == 1) and (next_block.x == 1)):
                        self.screen.display.blit(self.body_bottom_right, snake_rect)

# ****************************************************************************************************

    def update_head(self):
        head_relation = (self.body[1] - self.body[0])

        if head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down
        elif head_relation == Vector2(1, 0):
            self.head = self.head_left

# ****************************************************************************************************

    def update_tail(self):
        tail_relation = self.body[-2] - self.body[-1]

        if tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down
        elif tail_relation == Vector2(1, 0):
            self.tail = self.tail_left

# ****************************************************************************************************

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, (body_copy[0] + self.direction))
            self.body = body_copy[:]
            self.new_block = False

        body_copy = self.body[:-1]
        body_copy.insert(0, (body_copy[0] + self.direction))
        self.body = body_copy[:]

# ****************************************************************************************************

    def add_block(self):
        self.new_block = True

# ****************************************************************************************************

    def play_eat_sound(self):
        self.eat_sound.play()

# ****************************************************************************************************

    def reset_game(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
