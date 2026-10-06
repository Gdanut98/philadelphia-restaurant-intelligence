"""Reusable text-feature helpers for the public portfolio refactor."""
import pandas as pd

def expand_checkin_events(checkins: pd.DataFrame, timestamp_col: str = "date") -> pd.DataFrame:
    """Explode Yelp's comma-separated timestamp field to one row per check-in event."""
    out = checkins.copy()
    out[timestamp_col] = out[timestamp_col].fillna("").str.split(", ")
    out = out.explode(timestamp_col)
    out = out[out[timestamp_col].ne("")]
    out[timestamp_col] = pd.to_datetime(out[timestamp_col], errors="coerce")
    return out.dropna(subset=[timestamp_col])

def restaurant_experience_features(reviews: pd.DataFrame) -> pd.DataFrame:
    """Aggregate review-level outputs to restaurant-level experience features."""
    return (
        reviews.groupby("business_id")
        .agg(
            average_sentiment=("sentiment_score", "mean"),
            negative_review_proportion=("is_negative", "mean"),
            average_review_length=("review_length", "mean"),
            observed_reviews=("review_id", "count"),
        )
        .reset_index()
    )
