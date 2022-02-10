import numpy as np


class GameOfLife:
    cells = None  # Acá voy a almacenar la generacion actual
    previous = None  # Acá voy a almacenar la generación anterior
    xs = 0
    ys = 0

    def __init__(self, xs, ys):
        self.xs = xs
        self.ys = ys
        self.set_random()

    def switch(self, x, y):
        self.cells[y][x] = (self.cells[y][x] + 1) % 2

    def set_random(self):
        self.cells = np.random \
            .randint(2, size=self.xs * self.ys) \
            .reshape((self.ys, self.xs))

    def set_ceros(self):
        self.cells = np.zeros_like(self.cells)

    def compute_next(self, life_rule):
        self.previous = self.cells
        self.cells = np.zeros_like(self.previous)

        for y in range(self.cells.shape[0]):
            for x in range(self.cells.shape[1]):

                neighbors = 0  # Cuento los vecinos!

                for i in [-1, 0, 1]:
                    if y + i < 0 or y + i > self.cells.shape[0] - 1:  # Extremos superior e inferior
                        continue

                    for j in [-1, 0, 1]:
                        if x + j < 0 or x + j > self.cells.shape[1] - 1:  # Extremos izquierdo y derecho
                            continue

                        if i == 0 and j == 0:  # La celula en cuestion
                            continue

                        if self.previous[y + i][x + j] != 0:
                            neighbors += 1

                if neighbors in life_rule:
                    self.cells[y][x] += 1
