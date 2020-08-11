
class GameOfLife():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        #self.grid = [[0 for i in range(width)] for j in range(height)]
        self.grid = self.create_blank_grid()

    def create_blank_grid(self):
        return [[0 for i in range(self.width)] for j in range(self.height)]

    def get_grid(self):
        return self.grid

    def neighbors(self, row, col):
        enums = [ 
            (0, 1),  (0, -1),
            (1, 0),  (-1, 0),
            (1, 1),  (-1, -1),
            (1, -1), (-1, 1)
        ]
        out = []
        for offset in enums:
            xo, yo = row + offset[0], col + offset[1]
            xbounded = xo >= 0 and xo < self.width
            ybounded = yo >= 0 and yo < self.height
            if xbounded and ybounded: 
                out.append((xo, yo))
        return out

    def update_grid(self):
        new_grid = self.create_blank_grid()

        for row in range(self.width):
            for col in range(self.height):
                is_alive = lambda tup: self.grid[tup[0]][tup[1]]
                neighbors = map(is_alive, self.neighbors(row, col))

                # count of adjacent live cells
                pop = sum(neighbors)

                currently_alive = is_alive((row, col))
                if currently_alive and pop == 2 or pop == 3:
                    new_grid[row][col] = 1
                elif not currently_alive and pop == 3:
                    new_grid[row][col] = 1
                else:
                    new_grid[row][col] = 0

        self.grid = new_grid


