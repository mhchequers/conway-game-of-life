

class ConwayGameOfLife():
    def __init__(self, grid_size, interval_s, num_steps):
        self._validate_input_parameters(grid_size, interval_s, num_steps)
        self.grid_size = int(grid_size)
        self.interval_s = float(interval_s)
        self.num_steps = int(num_steps)

    def _validate_input_parameters(self, grid_size, interval_s, num_steps):
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