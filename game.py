import pygame
import snake
import fruit
import screen

# ADD BACKGROUND MUSIC, ADD A MUSHROOM(MAKES MAP RAINBOW & FLIPS CONTROLS & CHANGE SOUNDS ETC.),
# ADD SOUND EFFECTS(DEATH SOUND, TURNING SOUND, MENU(ADD WALL GAMEMODE AND NO SIDE WALLS GAMEMODE),
# ADD ANIMATIONS

# ****************************************************************************************************

class Game:
    pygame.init()

    def __init__(self):
        self.response_time = 150
        self.SCREEN_UPDATE = pygame.USEREVENT
        self.score = 0
        self.INITIAL_BODY_LENGTH = 3
        self.score_tracker = 3
        self.game_font = pygame.font.Font(None, 24)

        self.snake = snake.Snake()
        self.fruit = fruit.Fruit()
        self.screen = screen.Screen()

# ****************************************************************************************************

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

# ****************************************************************************************************

    def set_response_time(self):
        pygame.time.set_timer(self.SCREEN_UPDATE, self.response_time)

# ****************************************************************************************************

    def draw_elements(self):
        self.draw_grass()
        self.snake.draw_snake()
        if int(len(self.snake.body) - self.INITIAL_BODY_LENGTH) % 10 == 9:
            self.fruit.draw_x2_fruit()

        else:
            self.fruit.draw_fruit()

        self.draw_score()

# ****************************************************************************************************

    def draw_grass(self):
        grass_color1 = (171, 216, 72)
        grass_color2 = (162, 206, 63)
        self.screen.display.fill(grass_color1)

        for row in range(self.screen.CELL_NUMBER):
            if (row % 2) == 0:
                for col in range(self.screen.CELL_NUMBER):
                    if (col % 2) == 0:
                        grass_rect = pygame.Rect((col * self.screen.CELL_SIZE), (row * self.screen.CELL_SIZE),
                                                 self.screen.CELL_SIZE, self.screen.CELL_SIZE)
                        pygame.draw.rect(self.screen.display, grass_color2, grass_rect)
            else:
                for col in range(self.screen.CELL_NUMBER):
                    if (col % 2) == 1:
                        grass_rect = pygame.Rect((col * self.screen.CELL_SIZE), (row * self.screen.CELL_SIZE),
                                                 self.screen.CELL_SIZE, self.screen.CELL_SIZE)
                        pygame.draw.rect(self.screen.display, grass_color2, grass_rect)

# ****************************************************************************************************

    def draw_score(self):
        self.score = str(len(self.snake.body) - self.score_tracker)
        font_color = (33, 33, 33)
        score_surface = self.game_font.render(self.score, True, font_color)
        score_x = int(self.screen.CELL_SIZE - 33)
        score_y = int(self.screen.CELL_SIZE - 27)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        self.screen.display.blit(score_surface, score_rect)

# ****************************************************************************************************

    def check_collision(self):
        if self.fruit.position == self.snake.body[0]:
            if int(len(self.snake.body) - 3) % 10 == 9:
                self.fruit.randomize()
                self.snake.add_block()
                self.score_tracker -= 1
                if self.response_time > 10:
                    self.response_time -= 10
                self.set_response_time()
                #self.snake.play_lvl_up_sound()
            else:
                self.fruit.randomize()
                self.snake.add_block()
                self.snake.play_eat_sound()

        for block in self.snake.body[1:]:
            if block == self.fruit.position:
                self.fruit.randomize()

# ****************************************************************************************************

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < self.screen.CELL_NUMBER \
                or not 0 <= self.snake.body[0].y < self.screen.CELL_NUMBER:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

# ****************************************************************************************************

    def game_over(self):
        self.score_tracker = self.INITIAL_BODY_LENGTH
        self.response_time = 180
        self.snake.reset_game()
