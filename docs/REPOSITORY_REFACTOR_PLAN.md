# Notebook Refactor Plan

The original executed notebook remains the authoritative source for reported results. A clean public repository should split it into:

1. `01_data_scope_and_quality.ipynb`
2. `02_nlp_eda_and_sentiment.ipynb`
3. `03_text_classification.ipynb`
4. `04_restaurant_clustering.ipynb`
5. `05_activity_forecasting.ipynb`
6. `06_restaurant_activity_prediction.ipynb`

Reusable functions should move into `src/`:
- text preprocessing
- feature aggregation
- metric reporting
- plotting
- check-in timestamp expansion
- forecasting feature creation

Before publishing, the final integration output must use `final_cluster`, not the obsolete earlier `cluster` variable.
