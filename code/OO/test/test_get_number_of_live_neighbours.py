import pytest

import numpy as np

import sys, os
home_directory = '/home/matthew'
sys.path.append(home_directory+'/conway-game-of-life/code/OO/lib')
import conway_game_of_life as cgol

def test_all_dead_neighbours():
    game = cgol.ConwayGameOfLife(3, 1., 1)
    input_grid = np.array([
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ])

    for i in range(3):
        for j in range(3):
            assert game._get_number_of_live_neighbours(i,j,input_grid) == 0

def test_all_live_neighbours():
    game = cgol.ConwayGameOfLife(3, 1., 1)
    input_grid = np.array([
        [1,1,1],
        [1,1,1],
        [1,1,1]
    ])

    for i in range(3):
        for j in range(3):
            assert game._get_number_of_live_neighbours(i,j,input_grid) == 8

def test_cell_in_middle_grid():
    game = cgol.ConwayGameOfLife(5, 1., 1)
    input_grid = np.array([
        [0,1,1,0,1],
        [1,1,0,1,0],
        [1,1,1,0,1],
        [0,0,1,0,1],
        [1,0,0,1,1]
    ])

    assert game._get_number_of_live_neighbours(2,2,input_grid) == 4

def test_cells_in_corners_of_grid():
    game = cgol.ConwayGameOfLife(5, 1., 1)
    input_grid = np.array([
        [0,1,1,0,1],
        [1,1,0,1,0],
        [1,1,1,0,1],
        [0,0,1,0,1],
        [1,0,0,1,1]
    ])

    assert game._get_number_of_live_neighbours(0,0,input_grid) == 6
    assert game._get_number_of_live_neighbours(4,4,input_grid) == 4
    assert game._get_number_of_live_neighbours(4,0,input_grid) == 4
    assert game._get_number_of_live_neighbours(0,4,input_grid) == 5

def test_cells_at_edge_of_grid():
    game = cgol.ConwayGameOfLife(5, 1., 1)
    input_grid = np.array([
        [0,1,1,0,1],
        [1,1,0,1,0],
        [1,1,1,0,1],
        [0,0,1,0,1],
        [1,0,0,1,1]
    ])

    # top edge of grid
    assert game._get_number_of_live_neighbours(0,1,input_grid) == 4
    assert game._get_number_of_live_neighbours(0,2,input_grid) == 4
    assert game._get_number_of_live_neighbours(0,3,input_grid) == 5
    # left edge of grid
    assert game._get_number_of_live_neighbours(1,0,input_grid) == 6
    assert game._get_number_of_live_neighbours(2,0,input_grid) == 5
    assert game._get_number_of_live_neighbours(3,0,input_grid) == 6
    # right edge of grid
    assert game._get_number_of_live_neighbours(1,4,input_grid) == 5
    assert game._get_number_of_live_neighbours(2,4,input_grid) == 4
    assert game._get_number_of_live_neighbours(3,4,input_grid) == 5
    # bottom edge of grid
    assert game._get_number_of_live_neighbours(4,1,input_grid) == 4
    assert game._get_number_of_live_neighbours(4,2,input_grid) == 4
    assert game._get_number_of_live_neighbours(4,3,input_grid) == 5