"""Elementary cricket rates. No context/role adjustments are implied."""
from __future__ import annotations


def strike_rate(runs: int, balls_faced: int) -> float:
    """Batting runs per 100 balls faced."""
    if balls_faced <= 0:
        raise ValueError("balls_faced must be positive")
    if runs < 0:
        raise ValueError("runs must be nonnegative")
    return 100.0 * runs / balls_faced


def economy_rate(runs_conceded: int, legal_deliveries: int) -> float:
    """Bowling runs conceded per six legal deliveries."""
    if legal_deliveries <= 0:
        raise ValueError("legal_deliveries must be positive")
    if runs_conceded < 0:
        raise ValueError("runs_conceded must be nonnegative")
    return 6.0 * runs_conceded / legal_deliveries


def dot_ball_percentage(dot_balls: int, legal_deliveries: int) -> float:
    """Percentage of legal deliveries that are dots."""
    if legal_deliveries <= 0:
        raise ValueError("legal_deliveries must be positive")
    if dot_balls < 0 or dot_balls > legal_deliveries:
        raise ValueError("dot_balls must lie between zero and legal_deliveries")
    return 100.0 * dot_balls / legal_deliveries
