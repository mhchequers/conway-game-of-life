import pytest

import numpy as np

import sys, os
home_directory = '/home/matthew'
sys.path.append(home_directory+'/conway-game-of-life/code/OO/lib')
import conway_game_of_life as cgol

def test_all_dead_cells_remain_dead():
    game = cgol.ConwayGameOfLife(3, 1., 1)
    input_grid = np.array([
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ])

    result = game._update_grid(input_grid)

    expected_grid = np.array([
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ])

    np.testing.assert_array_equal(result, expected_grid)

def test_all_live_cells_die():
    game = cgol.ConwayGameOfLife(3, 1., 1)
    input_grid = np.array([
        [1,1,1],
        [1,1,1],
        [1,1,1]
    ])

    result = game._update_grid(input_grid)

    expected_grid = np.array([
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ])

    np.testing.assert_array_equal(result, expected_grid)

# test some interesting game of life patterns
