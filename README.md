# Philadelphia Restaurant Customer Experience Intelligence

An end-to-end unstructured-data analytics portfolio project using Yelp restaurant reviews and linked restaurant activity to understand dissatisfaction, classify customer experience, segment restaurants, forecast platform activity, and predict restaurant-level engagement.

## Portfolio headline
**12,498 reviews • 484 restaurants • 122,247 check-in events • 93.1% classification accuracy • 0.975 ROC-AUC • 88.8% negative recall**

## Business questions
1. What language distinguishes satisfied from dissatisfied restaurant customers?
2. Can review text identify dissatisfied customers reliably?
3. Do restaurants form meaningful experience/engagement segments?
4. Can monthly Yelp activity be forecast?
5. Which restaurant characteristics predict check-in engagement?

## Analytical pipeline
Yelp business/review/user/tip/check-in data
→ scope and quality control
→ NLP preprocessing
→ sentiment and language exploration
→ TF-IDF classification
→ neural-network comparison
→ K-Means restaurant segmentation
→ monthly activity forecasting
→ restaurant-level Random Forest prediction
→ business recommendations

## Key results
- TF-IDF Logistic Regression: **93.10% accuracy, ROC-AUC 0.975, negative recall 88.78%**
- Neural Network: **93.42% accuracy, ROC-AUC 0.975, negative recall 73.99%**
- Operational model choice: Logistic Regression because negative-review detection was the priority.
- Corrected K-Means: **K=2, silhouette 0.3275**
- Segments: **379 higher-satisfaction/higher-engagement** and **105 lower-satisfaction/lower-engagement** restaurants.
- Rolling Linear Regression forecast reduced **MAE 74.67%** and **RMSE 70.99%** versus seasonal naive.
- Restaurant-level Random Forest: **R² 0.707** on log check-in activity.
- Removing review volume reduced Random Forest R² to **0.463**, showing that customer-experience variables retain signal but review volume dominates platform-engagement prediction.

## Model-selection story
The neural network was marginally more accurate, but Logistic Regression detected substantially more negative reviews. Because the business objective prioritized identifying dissatisfaction, negative-class recall mattered more than a 0.32 percentage-point gain in aggregate accuracy.

## Quality-control story
An early clustering feature represented check-in *availability* rather than check-in *volume* and created an artificial cluster. The feature was removed, clustering was rerun, and the validated two-cluster solution is used here. This correction is deliberately retained as evidence of analytical QA rather than hidden.

## Skills demonstrated
Python • Pandas • NLP • spaCy • VADER • TF-IDF • Logistic Regression • Neural Networks • K-Means • Forecasting • Random Forest • Model Evaluation • Feature Engineering • Data Quality • Business Translation

## Evidence boundary
This repository is a portfolio packaging of a graduate unstructured-data analytics project. Results are preserved from the executed final notebook/executive summary. Any later refactoring should preserve the validated metrics unless the model is explicitly rerun and new results are documented.
