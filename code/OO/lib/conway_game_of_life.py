import numpy as np
import time

class ConwayGameOfLife():
    def __init__(self, grid_size, interval_s, num_steps):
        self._validate_input_parameters_types(grid_size, interval_s, num_steps)
        self.grid_size = int(grid_size)
        self.interval_s = float(interval_s)
        self.num_steps = int(num_steps)

    def _validate_input_parameters_types(self, grid_size, interval_s, num_steps):
        try:
            int(grid_size)
        except:
            raise TypeError('Grid size must be an integer')

        try:
            float(interval_s)
        except:
            raise TypeError('Interval must be a float')

        try:
            int(num_steps)
        except:
            raise TypeError('Number of steps must be an integer')

    def _update_grid(self, grid):
        new_grid = grid.copy()

        for row in range(self.grid_size):
            for col in range(self.grid_size):
                num_live_neighbours = self._get_number_of_live_neighbours(row, col, grid)
                new_grid[row][col] = self._get_new_cell_state_using_conways_rules(num_live_neighbours, grid[row][col])

        return new_grid

    def _get_number_of_live_neighbours(self, row, col, grid):
        # determine number of live neighbours
        # Note, grid is an infinite (toiroidal) plane!
        N = self.grid_size
        return (
            grid[(row-1)%N][(col-1)%N] + grid[(row-1)%N][col] + grid[(row-1)%N][(col+1)%N] +
            grid[row][(col-1)%N] + grid[row][(col+1)%N] +
            grid[(row+1)%N][(col-1)%N] + grid[(row+1)%N][col] + grid[(row+1)%N][(col+1)%N]
        )

    def _get_new_cell_state_using_conways_rules(self, num_live_neighbours, old_element):
        # Conway's rules to determine if the new cell is alive or dead
        # Taken from https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
        if old_element == 1 and num_live_neighbours in [2, 3]:
            return 1
        elif old_element == 0 and num_live_neighbours == 3:
            return 1
        else:
            return 0

    def _visualize_grid(self, step, grid):
        print('')
        print('Step = {}'.format(step))
        # print(grid)

        output = ''
        for row in grid:
            for elem in row:
                if elem == 0:
                    output += ' '
                else:
                    output += 'O'
            output += '\n'
        print(output)

    def run(self):
        '''
        This function runs Conway's game of life.
        Here, we access the class's input parameters directly.

        The run function consists of the following components:
        1. initialize a random grid
        2. Update the grid
        3. visualize the grid
        4. repeat 2 and 3 num_steps times at intervals of interval_s
        '''

        # initialize grid
        # grid_size * grid_size array containing 0s or 1s.
        # 0 = dead cell, 1 = live cell
        grid = np.random.choice([0, 1], (self.grid_size, self.grid_size), p=[0.7, 0.3])
        self._visualize_grid(0, grid)
        
        # update grid num_steps times at interval_s intervals
        for step in range(1, self.num_steps+1):
            grid = self._update_grid(grid)
            self._visualize_grid(step, grid)
            time.sleep(self.interval_s)