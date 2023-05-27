import pygame
import numpy as np
import math
import random
from PerlinNoiseGenerator import generate_noise


class Simulation:
    # green(0): represents the cells with vegetation that can be burned
    # red(1): represents the cells with vegetation that is currently burning
    # black(2): represents the cells that doesn't contain any vegetation
    # gray(3): represents the cells that have already burnt
    colors = {"black": (0, 0, 0), "green": (11, 193, 17), "red": (194, 13, 13),
              "grey": (128, 128, 128)
              }

    def __init__(self, width: int, height: int, block_size: int, settings):
        # instantiating variables width and height of the screen
        self.height = height
        self.width = width

        # block_size is the length and width that each cell takes up
        self.block_size = block_size
        self.settings = settings

        # with the height, width and block_size,
        # we can calculate the number of blocks that go in every column and row
        self.num_cols = math.ceil(self.width / self.block_size)
        self.num_rows = math.ceil(self.height / self.block_size)

        # this is initializing the wind and the landscape
        self.wind = self.get_wind()
        self.landscape = generate_noise(self.num_cols, self.num_rows)

        # initializing the pygame stuff
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill(self.colors["black"])

        # generating the grid cell with the weighted values.
        self.grid_cell = np.array([
            random.choices([0, 2],
                           cum_weights=(settings["density"], 1), k=self.num_cols) for i in range(self.num_rows)
        ])

        # begin the fire
        self.running = True
        self.grid_cell[math.floor(len(self.grid_cell) / 2)][math.floor(len(self.grid_cell[0]) / 2)] = 1

    def iterate(self):
        new_grid_cell = np.copy(self.grid_cell)
        for i in range(0, self.num_rows):
            for j in range(0, self.num_cols):
                if self.grid_cell[i][j] == 1:
                    self.cell_iteration(i, j, new_grid_cell)

        self.grid_cell = new_grid_cell
        
    # i represents each row number; j represents each column number
    def cell_iteration(self, i, j, new_grid_cell):
        new_grid_cell[i][j] = random.choices([3, 1], cum_weights=[self.settings["burnout"], 1], k=1)[0]

        for ii in range(-1, 2):
            if not (i == 0 and ii == -1) and not (i == len(self.grid_cell) - 1 and ii == 1):
                for jj in range(-1, 2):
                    if not (j == 0 and jj == -1) and not (j == len(self.grid_cell[0]) - 1 and jj == 1):
                        if new_grid_cell[i + ii][j + jj] == 0:
                            new_grid_cell[i + ii][j + jj] = \
                            random.choices([1, 0], cum_weights=[(self.landscape[i][j] - self.landscape[i + ii][j + jj])
                            + self.settings["ignition"] * (self.wind[3 * ii + jj + 4] + 1), 1], k=1)[0]

    def get_wind(self):
        power = []
        angle = self.settings["wind-angle"]

        for i in range(8):
            power.append(
                math.cos(math.radians(
                        abs(angle - 45 * i))
                    ) * self.settings["wind-power"] / 100
                )
        
        power = [power[3], power[2], power[1], power[4], 0, power[0], power[5], power[6], power[7]]
        return power

    # Returns RGB value between 100-255 based on slope of cell
    def visual_cell_noise(self, row, col):
        return min(abs(math.floor(self.landscape[row][col] * 255)) + 100, 255)

    def draw_grid(self):
        # This iterates through every single cell to determine what color it should be based on
        # the values in the grid_cell.
        for i in range(self.num_cols):
            for j in range(self.num_rows):

                if self.grid_cell[j][i] == 0:
                    self.color = (11, self.visual_cell_noise(j, i), 17)

                elif self.grid_cell[j][i] == 1:
                    self.color = self.colors["red"]

                elif self.grid_cell[j][i] == 2:
                    self.color = self.colors["black"]

                elif self.grid_cell[j][i] == 3:
                    constant_visual = self.visual_cell_noise(j, i)
                    self.color = (constant_visual, constant_visual, constant_visual)

                pygame.draw.rect(self.screen, self.color,
                                 pygame.Rect((i * self.block_size, j * self.block_size),
                                             (self.block_size, self.block_size))
                                 )
    

    def run(self):
        while self.running:
            self.draw_grid()
            pygame.display.flip()
            self.iterate()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False