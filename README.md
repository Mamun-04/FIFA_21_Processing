Project Title: FIFA 21 Player Analysis & Modeling
This repository contains three core Jupyter Notebooks:

fifa_21_analysis — Data cleaning and exploratory analysis on FIFA 21 player statistics.

fifa_21_position — A classification model trained to predict a player's primary position.

fifa_21_value - a model that predicts a player's value

1. fifa_21_analysis— Data Organisation and Exploration
This notebook focuses on:

Loading and cleaning the FIFA 21 dataset.

Removing unnecessary or sparse columns.

Handling missing values and standardizing data types.

Engineering features (e.g., extracting primary positions).

Visualizing relationships using plots such as:

Overall vs. Value (scatter)

Pace vs. Age (trendline)

Position-wise rating distribution

Club comparisons (e.g., Liverpool vs Man City)

Highlights:
Created primary_position feature from player position list.

Cleaned numeric skill attributes (pace, shooting, etc.).

Boxplots and bar charts for performance analysis by club.

Value transformed using log10 for clearer distribution.

 2. fifa_21_positions — Predicting Player Position
This notebook builds a classification model to predict a player’s primary_position based on skill attributes.

 Features Used:
pace, shooting, passing, dribbling, defending, physic, and overall

Steps:
Filtered rare classes (fewer than 2 players).

Stratified train_test_split to preserve class balance.

Trained models (e.g., Random Forest, Logistic Regression).

Evaluated with:

Accuracy

Confusion matrix

Highlights:
Feature importance plot reveals key predictors of position.

Visualized model performance for interpretability.



3. fifa_21_value - the model predicts a players value based on age, overall and thier attributes.

We found that the R^2 score was 0.987 which was very high and we were then able to see that the model was over-fitted to the training data and would be poor in generalising unseen data. 

Conclusions to this were that there were several outliers, a very high MSE was obtained. The best players likely had very high transfer values which were much higher than most.

A positive is that the model used features we were expecting such as age overall and potential which do most of the heavy lifting for a player's value.

This model could perhaps be amended by XGBoost or GradientBoostingRegressor which might give improved scores and make the model better in unseen data.

Dataset
Source: Sofifa.com

File: players_21.csv

Includes stats for 18,944 players from FIFA 21 with 100+ attributes.

Future Work
Combine FIFA 15–21 data to analyze player evolution.

Train regression models (e.g., predict market value or overall rating).

Try clustering (e.g., player archetypes) or NLP on player names.

