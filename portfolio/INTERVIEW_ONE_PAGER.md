# Interview One-Pager

## 30-second explanation
I built an end-to-end restaurant customer-intelligence project from Yelp data covering 484 Philadelphia restaurants, 12,498 reviews and 122,247 check-in events. I used NLP and TF-IDF classification to detect dissatisfied customers, compared Logistic Regression with a neural network, clustered restaurants into experience/engagement profiles, forecast monthly check-in activity, and used Random Forest to predict restaurant-level engagement.

## Best model-selection story
The neural network was slightly more accurate overall, but Logistic Regression achieved much stronger negative recall—88.8% versus 74.0%. Since the business objective was detecting dissatisfaction, I selected the simpler model with better minority-class performance.

## Best QA story
My first clustering run produced a suspicious small cluster. I traced it to a check-in feature that represented availability rather than event volume. I removed the flawed feature, reran clustering, and used the corrected K=2 result. That reinforced the importance of validating feature meaning, not just accepting model output.

## Best forecasting story
A seasonal-naive forecast overpredicted 2019 because Yelp engagement was already declining. Adding lag-1, lag-12, trend and monthly indicators reduced MAE by 74.67% and RMSE by 70.99%.

## Important limitation
Yelp check-ins measure platform engagement, not restaurant revenue or total foot traffic. The analysis is predictive and associational rather than causal.
