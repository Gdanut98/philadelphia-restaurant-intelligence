# Validated Results

## Analytical population
- 484 Philadelphia restaurants
- 12,498 reviews
- 9,963 unique reviewers
- 122,247 event-level check-ins
- 466 restaurants with check-ins
- 3,173 tips across 368 restaurants

## Review corpus
- 1,379,537 tokens
- 24,317 unique vocabulary terms
- Average review length: 110.38 words
- Positive / Neutral / Negative: 69.57% / 13.69% / 16.74%

## Sentiment
VADER sentiment vs Yelp star rating correlation: **0.578**.

## Classification
| Model | Accuracy | ROC-AUC | Positive F1 | Negative Recall |
|---|---:|---:|---:|---:|
| TF-IDF Logistic Regression | 93.10% | 0.975 | 0.9565 | 88.78% |
| Neural Network | 93.42% | 0.975 | 0.9600 | 73.99% |

Logistic Regression correctly identified **372 of 419** negative reviews in the reported confusion matrix.

## Clustering
Validated final feature set:
- average_sentiment
- negative_review_proportion
- average_review_length
- log_observed_reviews
- clustering_price_range

K=2 produced the strongest reported silhouette score: **0.3275**.

| Segment | Restaurants | Avg Rating | Avg Sentiment | Negative Review Share | Avg Reviews |
|---|---:|---:|---:|---:|---:|
| Higher Satisfaction / Higher Engagement | 379 | 3.93 | 0.75 | 0.14 | 31.42 |
| Lower Satisfaction / Lower Engagement | 105 | 2.20 | 0.15 | 0.67 | 5.61 |

## Forecasting
2019 pre-COVID holdout:

| Model | MAE | RMSE |
|---|---:|---:|
| Seasonal Naive | 190.25 | 197.79 |
| Rolling Linear Regression | ~48.19 | ~57.38 |

Improvement:
- MAE: **74.67%**
- RMSE: **70.99%**

## Restaurant-level prediction
| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | 0.832 | 1.100 | 0.673 |
| Random Forest | 0.807 | 1.041 | 0.707 |
| RF without review volume | 1.145 | 1.411 | 0.463 |

Random Forest feature importance:
- log_observed_reviews: 70.92%
- weekly_open_hours: 7.46%
- average_review_length: 6.83%
- average_sentiment: 5.10%
- negative_review_proportion: 3.66%
