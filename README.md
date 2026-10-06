# Philadelphia Restaurant Customer Experience Intelligence

An end-to-end unstructured-data analytics portfolio project using Yelp restaurant reviews and linked restaurant activity to understand dissatisfaction, classify customer experience, segment restaurants, forecast platform activity, and predict restaurant-level engagement.

## Portfolio headline
**12,498 reviews • 484 restaurants • 122,247 check-in events • 93.1% classification accuracy • 0.975 ROC-AUC • 88.8% negative recall**

## Key results
- TF-IDF Logistic Regression: **93.10% accuracy, ROC-AUC 0.975, negative recall 88.78%**
- Neural Network: **93.42% accuracy, ROC-AUC 0.975, negative recall 73.99%**
- Corrected K-Means: **K=2, silhouette 0.3275**
- Rolling Linear Regression forecast reduced **MAE 74.67%** and **RMSE 70.99%** versus seasonal naive.
- Restaurant-level Random Forest: **R² 0.707** on log check-in activity.

## Model-selection story
The neural network was marginally more accurate, but Logistic Regression detected substantially more negative reviews. Because the business objective prioritized identifying dissatisfaction, negative-class recall mattered more than the small gain in aggregate accuracy.

## Skills
Python • Pandas • NLP • spaCy • VADER • TF-IDF • Logistic Regression • Neural Networks • K-Means • Forecasting • Random Forest • Model Evaluation • Feature Engineering • Data Quality
