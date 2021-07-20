import pytest

import sys, os
home_directory = '/home/matthew'
sys.path.append(home_directory+'/conway-game-of-life/code/OO/lib')
import conway_game_of_life as cgol

def test_live_cell_with_two_or_three_live_neighbours_stays_alive():
    game = cgol.ConwayGameOfLife(1, 1., 1)

    num_live_neighbours = [2,3]
    for num in num_live_neighbours:
        assert game._get_new_cell_state_using_conways_rules(num, 1) == 1

def test_live_cell_with_not_two_or_three_live_neighbours_dies():
    game = cgol.ConwayGameOfLife(1, 1., 1)

    num_live_neighbours = [0,1,4,5,6,7,8]
    for num in num_live_neighbours:
        assert game._get_new_cell_state_using_conways_rules(num, 1) == 0

def test_dead_cell_with_three_live_neighbours_comes_alive():
    game = cgol.ConwayGameOfLife(1, 1., 1)

    assert game._get_new_cell_state_using_conways_rules(3, 0) == 1

def test_dead_cell_with_not_three_live_neighbours_stays_dead():
    game = cgol.ConwayGameOfLife(1, 1., 1)

    num_live_neighbours = [0,1,2,4,5,6,7,8]
    for num in num_live_neighbours:
        assert game._get_new_cell_state_using_conways_rules(num, 0) == 0