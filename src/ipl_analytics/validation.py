"""Minimal delivery-data schema validation; not a full cricket scoring engine."""
from __future__ import annotations

import pandas as pd

REQUIRED_COLUMNS = {
    "match_id", "innings", "over", "ball", "striker", "bowler",
    "batter_runs", "total_runs", "is_wide", "is_no_ball",
}


def validate_deliveries(df: pd.DataFrame) -> pd.DataFrame:
    """Validate a normalised ball-level input table.

    The input contract assumes over and ball are integer-like labels, each
    delivered event occupies one row, and is_wide/is_no_ball are 0/1 flags.
    Delivery sequence and cricket-law edge cases need source-specific rules.
    """
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required fields: {sorted(missing)}")
    if df.empty:
        raise ValueError("No delivery records supplied")
    if df[list(REQUIRED_COLUMNS)].isna().any().any():
        raise ValueError("Required fields contain missing values")
    for col in ("innings", "over", "ball", "batter_runs", "total_runs", "is_wide", "is_no_ball"):
        if not pd.api.types.is_numeric_dtype(df[col]):
            raise ValueError(f"{col} must be numeric")
    if (df[["innings", "over", "ball", "batter_runs", "total_runs"]] < 0).any().any():
        raise ValueError("Negative innings/delivery index/runs detected")
    if not df["is_wide"].isin([0, 1]).all() or not df["is_no_ball"].isin([0, 1]).all():
        raise ValueError("Wide and no-ball flags must be 0 or 1")
    if (df["batter_runs"] > df["total_runs"]).any():
        raise ValueError("Batter runs cannot exceed total runs")
    return df.copy()
