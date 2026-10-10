import pytest
from src.ipl_analytics.metrics import strike_rate, economy_rate, dot_ball_percentage


def test_strike_rate():
    assert strike_rate(45, 30) == 150.0


def test_economy():
    assert economy_rate(24, 18) == 8.0


def test_dot_ball_percentage():
    assert dot_ball_percentage(9, 18) == 50.0


@pytest.mark.parametrize("fn,args", [
    (strike_rate, (10, 0)),
    (economy_rate, (10, 0)),
    (dot_ball_percentage, (4, 3)),
])
def test_invalid_inputs(fn, args):
    with pytest.raises(ValueError):
        fn(*args)
