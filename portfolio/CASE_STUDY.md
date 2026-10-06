# Case Study — Philadelphia Restaurant Customer Experience Intelligence

## Problem
Restaurant star ratings compress complex customer experiences into one number. The project asks whether review text and linked Yelp activity can provide a richer system for detecting dissatisfaction, understanding operational complaints, profiling restaurants, and forecasting engagement.

## Data
The final analytical population includes 484 Philadelphia restaurants, 12,498 reviews from 9,963 reviewers, and 122,247 event-level check-ins.

## NLP
Review text was normalized with spaCy, retaining alphabetic tokens, removing stopwords, and lemmatizing terms. Unigrams, bigrams, part-of-speech patterns, and VADER sentiment were explored.

Negative reviews were longer and emphasized operational language around ordering, waiting, staff interaction, food execution, and value.

## Classification
TF-IDF Logistic Regression achieved 93.1% accuracy, ROC-AUC 0.975, and 88.8% negative recall.

A neural network achieved slightly higher accuracy (93.4%) but only 74.0% negative recall. Logistic Regression was selected because identifying dissatisfied customers was more important than marginal aggregate accuracy.

## Segmentation
Restaurant-level experience features were standardized and clustered. A flawed early check-in feature was identified and removed. The corrected K=2 solution separated:
- 379 higher-satisfaction/higher-engagement restaurants
- 105 lower-satisfaction/lower-engagement restaurants

## Forecasting
A rolling Linear Regression model combining recency, prior-year activity, trend, and monthly indicators was evaluated on 2019. It reduced MAE 74.67% and RMSE 70.99% relative to a seasonal-naive benchmark.

## Restaurant engagement prediction
A Random Forest predicted log restaurant check-in activity with R²=0.707. Review volume dominated feature importance, but removing it still left R²=0.463, indicating additional predictive signal from restaurant and customer-experience features.

## Business recommendations
1. Use the Logistic Regression model as a dissatisfaction-monitoring layer.
2. Route negative-review language into an operational complaint taxonomy.
3. Track sentiment alongside star ratings rather than treating ratings as sufficient.
4. Use restaurant segments as experience/engagement profiles, not causal quality labels.
5. Use trend-aware forecasts rather than simple seasonal extrapolation when platform behavior is shifting.
6. Treat check-ins as digital engagement rather than direct revenue or foot traffic.

## Why this project is portfolio-worthy
It integrates unstructured text, supervised learning, neural-model comparison, unsupervised learning, forecasting, cross-sectional prediction, quality control, and business decision-making in one coherent analytical system.
