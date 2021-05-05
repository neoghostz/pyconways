import pygame
import logging
import os
import copy
import sys
import numpy as np
from gameboards import Toad, Block, Pulsar, Penta, BeeHive
from random import random

class Conway():
    def __init__(self):
        pygame.init()
        logging.basicConfig(format="%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
        self.logger = logging.getLogger("ConwaysGame")
        self.logger.setLevel(int(os.environ.get("Logging", logging.DEBUG)))
        self.caption = "Conways Game of Life"
        self.game = Penta()
        self.fps = 1
        self.clock = pygame.time.Clock()
        self.run_state = True
        self.game_screen()
        #self.game_board = np.array([[x for x in range(400)] for y in range(400)])
        

    def game_screen(self):
        self.array_width = self.game.array_width
        self.array_height = self.game.array_height
        self.width = self.game.array_width*10
        self.height = self.game.array_height*10
        self.block_size = self.game.block_size
        self.game_board = np.array(self.game.board)
        self.background_colour = (70,200,5)
        self.active_block_colour = (0,0,0)
        self.dead_block_colour = (255,255,255)

    def run(self):
        counter = 0
        self.window = pygame.display.set_mode((self.width, self.height))
        self.window.fill(self.background_colour)
        pygame.display.set_caption(self.caption)
        self.logger.debug(self.game_board)
        while self.run_state and counter < 300:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run_state = False
            self.draw()
            self.game_board = self.iterate()
            self.logger.debug(self.game_board)
            counter = counter + 1
        pygame.quit()
        sys.exit()

    def draw(self):
        self.window.fill(self.background_colour)
        pygame.display.update()
        for x in range(0, self.array_height, 1):
            for y in range(0, self.array_width, 1):
                rect = pygame.Rect(y*self.block_size, x*self.block_size, 10, 10)
                if self.game_board[x][y]:
                    pygame.draw.rect(self.window, self.active_block_colour, rect, 0)
                else:
                    pygame.draw.rect(self.window, self.dead_block_colour, rect, 0)
        pygame.display.update()

    def iterate(self):
        temp_board = copy.deepcopy(self.game_board)
        for x in range(0, self.array_height, 1):
            for y in range(0, self.array_width, 1):
                temp_board[x][y] = 1 if self.eval(self.calc_cords(x, y)) else 0

        return temp_board


    def eval(self, game_array):
        team_board = copy.deepcopy(game_array)
        self.logger.debug(f"{team_board} size: {len(team_board)}")
        if len(team_board):
            if 1 < len(team_board) > 3:
                raise ArithmeticError("Game Array is miss configured")
            else:
                if team_board[1][1]:
                    return True if sum([sum(x) for x in team_board]) in [3, 4] else False
                else:
                    return True if sum([sum(x) for x in team_board]) in [3] else False
        else:
            return False

    def calc_cords(self, x, y):
        if x < 1 and y < 1:
            return self.game_board[0:x+2, 0:y+2].tolist()
        elif x < 1 and y >= 1:
            return self.game_board[0:x+2, y-1:y+2].tolist()
        elif x >= 1 and y < 1:
            return self.game_board[x-1:x+2, 0:y+2].tolist()
        else:
            return self.game_board[x-1:x+2, y-1:y+2].tolist()


def array_splice():
    data = np.array(
        [
            [0,1,2,3,4,5],
            [6,7,8,9,10,11],
            [12,13,14,15,16,17],
            [18,19,20,21,22,23],
            [24,25,26,27,28,29],
            [30,31,32,33,34,35]
        ]
    )

    return data

def calc_coords(x, y, game_board, width=6, height=6):
    if x < 1 and y < 1:
        return game_board[0:x+2, 0:y+2].tolist()
    elif x < 1 and y >= 1:
        return game_board[0:x+2, y-1:y+2].tolist()
    elif x >= 1 and y < 1:
        return game_board[x-1:x+2, 0:y+2].tolist()
    else:
        return game_board[x-1:x+2, y-1:y+2].tolist()

if __name__ == "__main__":
    Conway().run()
