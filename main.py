# ****************************************************************************************************
#
#       Name:       Alex Orescanin
#       File:       store.py
#       Description:
#               This program holds the main function and display the dictionary
#
#       Other files included: person.py, customer.py, sales_associate.py
#
# ****************************************************************************************************

import pygame
import sys
import game
from pygame.math import Vector2

# ****************************************************************************************************

def main():
    pygame.init()

    frame_rate = 60
    clock = pygame.time.Clock()

    main_game = game.Game()
    main_game.set_response_time()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == main_game.SCREEN_UPDATE:
                main_game.update()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if main_game.snake.direction.y != 1:
                        main_game.snake.direction = Vector2(0, -1)

                if event.key == pygame.K_RIGHT:
                    if main_game.snake.direction.x != -1:
                        main_game.snake.direction = Vector2(1, 0)

                if event.key == pygame.K_DOWN:
                    if main_game.snake.direction.y != -1:
                        main_game.snake.direction = Vector2(0, 1)

                if event.key == pygame.K_LEFT:
                    if main_game.snake.direction.x != 1:
                        main_game.snake.direction = Vector2(-1, 0)

        main_game.draw_elements()
        pygame.display.update()
        clock.tick(frame_rate)

# ****************************************************************************************************

if __name__ == '__main__':
    main()
