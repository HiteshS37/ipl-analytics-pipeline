import pandas as pd
import pytest
from src.ipl_analytics.validation import validate_deliveries


def example():
    return pd.DataFrame([{
        "match_id": 101, "innings": 1, "over": 0, "ball": 1,
        "striker": "A", "bowler": "B", "batter_runs": 4,
        "total_runs": 4, "is_wide": 0, "is_no_ball": 0,
    }])


def test_accepts_valid_example():
    assert len(validate_deliveries(example())) == 1


def test_missing_field_rejected():
    with pytest.raises(ValueError, match="Missing"):
        validate_deliveries(example().drop(columns=["bowler"]))


def test_inconsistent_runs_rejected():
    df = example()
    df.loc[0, "batter_runs"] = 6
    with pytest.raises(ValueError, match="exceed"):
        validate_deliveries(df)


def test_wide_flag_rejected():
    df = example()
    df.loc[0, "is_wide"] = 2
    with pytest.raises(ValueError, match="0 or 1"):
        validate_deliveries(df)
