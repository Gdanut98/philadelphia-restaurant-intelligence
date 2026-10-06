# Quality Decisions and Limitations

## Quality corrections retained in the portfolio

### Check-in event expansion
Yelp check-in records contain multiple comma-separated timestamps per business. Counting source rows would count businesses with check-ins, not actual events. Timestamps were exploded to event level and validated to **122,247** check-in events.

### Clustering correction
The initial clustering run used a feature that behaved as a 0/1 check-in-availability flag. It produced an artificial 18-restaurant cluster. That feature was removed and K-Means was rerun.

The authoritative segmentation is the validated `final_cluster` solution:
- 379 higher-satisfaction/higher-engagement restaurants
- 105 lower-satisfaction/lower-engagement restaurants

### Redundant clustering variables
Average rating correlated approximately -0.92 with negative-review proportion. Average rating was removed from the final clustering feature set to reduce redundancy and retained for external validation.

### Check-in target transformation
Restaurant check-ins had raw skewness of 3.47. `log1p(total_checkins)` reduced skewness to approximately -0.28 before regression.

### Forecast evaluation window
COVID introduced a major structural break and 2022 was partial. Forecast evaluation therefore used the complete pre-COVID 2019 holdout.

## Limitations
- Yelp users are self-selected.
- Ratings are positively skewed and the classification target is imbalanced.
- Restaurants have uneven review volume; low-volume segment assignments are less stable.
- Yelp check-ins are platform engagement, not direct foot traffic or revenue.
- 2020 is a structural break.
- Random Forest feature importance is predictive, not causal.
