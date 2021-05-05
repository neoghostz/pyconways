from pytest import fixture
import numpy as np
from conways import calc_coords

@fixture
def gameboard():
    data = np.array(
        [
            [0,0,0,0],
            [0,1,1,0],
            [0,1,1,0],
            [0,0,0,0]
        ]
    )

    return data

def test_calc_coords(gameboard):
    assert isinstance(calc_coords(0, 0, gameboard), list)
    assert calc_coords(0,0, gameboard, width=4, height=4) == [[0, 0], [0, 1]]
    assert calc_coords(1,0, gameboard, width=4, height=4) == [[0, 0], [0, 1], [0, 1]]
    assert calc_coords(0,1, gameboard, width=4, height=4) == [[0, 0, 0], [0, 1, 1]]
    assert calc_coords(1,1, gameboard, width=4, height=4) == [[0, 0, 0], [0, 1, 1], [0, 1, 1]]
    assert calc_coords(2,1, gameboard, width=4, height=4) == [[0, 1, 1], [0, 1, 1], [0, 0, 0]]
    assert calc_coords(2,3, gameboard, width=4, height=4) == [[1, 0], [1, 0], [0, 0]]
    assert calc_coords(3,3, gameboard, width=4, height=4) == [[1, 0], [0, 0]]