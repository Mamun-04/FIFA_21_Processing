Project Title: FIFA 21 Player Analysis & Modeling
This repository contains two core Jupyter Notebooks:

fifa_21_analysis — Data cleaning and exploratory analysis on FIFA 21 player statistics.

fifa_21_position — A classification model trained to predict a player's primary position.

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

ighlights:
Feature importance plot reveals key predictors of position.

Visualized model performance for interpretability.

📦 Dataset
Source: Sofifa.com

File: players_21.csv

Includes stats for 18,944 players from FIFA 21 with 100+ attributes.

💡 Future Work
Combine FIFA 15–21 data to analyze player evolution.

Train regression models (e.g., predict market value or overall rating).

Try clustering (e.g., player archetypes) or NLP on player names.
