import pytest

import sys, os
home_directory = '/home/matthew'
sys.path.append(home_directory+'/conway-game-of-life/code/OO/lib')
import conway_game_of_life as cgol

def test_exception_for_incorrect_grid_size_type():
    with pytest.raises(TypeError) as e:
        cgol.ConwayGameOfLife('not an integer', 1., 10) 

    assert str(e.value) == 'Grid size must be an integer'

def test_exception_for_incorrect_interval_type():
    with pytest.raises(TypeError) as e:
        cgol.ConwayGameOfLife(10, 'not a float', 10) 

    assert str(e.value) == 'Interval must be a float'

def test_exception_for_incorrect_num_steps_type():
    with pytest.raises(TypeError) as e:
        cgol.ConwayGameOfLife(10, 1., 'not an integer') 

    assert str(e.value) == 'Number of steps must be an integer'

def test_correct_input_parameter_types():
    game = cgol.ConwayGameOfLife(10, 1., 10)

    assert type(game.grid_size) is int
    assert type(game.interval_s) is float
    assert type(game.num_steps) is int

def test_correct_input_parameter_values():
    game = cgol.ConwayGameOfLife(10, 1., 5)

    assert game.grid_size == 10
    assert game.interval_s == 1.0
    assert game.num_steps == 5