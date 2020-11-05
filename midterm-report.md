---
layout: default
title: Midterm Report
nav_order: 1
---
# Midterm Report
By Bryce Plunkett, Nicholas Boshart, Sami Rahman, Paul Dittamo

<img style="box-shadow: 2px 2px 10px #00000050" width="100%" src="https://i.imgur.com/nPqxhzs.jpg">

## Data Collection 
Initially, we calculated a team’s running averages of stats leading up to a given game. We first attempted to fetch the information through a 3rd party API. Unfortunately, we only found paid services that satisfied our requirements--obviously, we did not want to spend money. Thus, we resorted to basketballreference.com, a site that hosts a myriad of stats pertinent to the NBA. In true computer science fashion we automated scraping the data instead of manually downloading CSVs of teams' season long game logs: we extended an existing python package, basketball_reference_scraper. Then, we built out a new feature within the package to scrape a team’s game logs throughout the season. After this, we ran a script to get the running average of a team’s stats for each regular season game in the last 20 years. This process involved pairing that data to the given game. 

## Merging Data
### Combining Individual Years
Overall, the data were scraped goes back 20 years, and each year has about 1,200 games (and is contained within its own CSV). Instead of using all 20 seasons of data, we opted to take a subset of games within the past 3 seasons to accelerate data processing and model training. We’ll likely expand this subset in the future once we decide upon a model and a more concrete data cleaning process.

<h3 style="text-align: center">Merging Home and Away Statistics</h3>
<p style="text-align: center"><img width="75%" src="https://i.imgur.com/ZTMYFud.png"></p>

### Combing Home and Away Statistics
There are 51 features for each team. Since each game consists of two teams, there are a total of 102 features per game, excluding the label. For feature selection purposes, if we select the home-team version of a feature, we would naturally want to include the away-team version as well. Thus, for each home-away feature pair, we merged them into a singular feature by taking the difference. We chose difference instead of multiplication because it keeps the directionality of the data. If we used multiplication, for instance, a team with a stacked defense against a team with a stack offense would appear the same as a team with a stacked defense and offense against a normal team.

## Dividing and Standardizing
We divided the dataset into a training and testing set with a 70-30 split, respectively. Then, we standardized the data (excluding the label), so no one feature dominates in the model. Each standardized feature has a mean of 0 and a variance of 1.

## Problem Type and Outliers
<h3 style="text-align: center">Total Points Distribution Before Removing Outliers</h3>
<img width="53%" src="https://i.imgur.com/Nt5uRqt.png"><img width="47%" src="https://i.imgur.com/92QRxIM.png">
<h3 style="text-align: center">Total Points Distribution After Removing Outliers</h3>
<img width="53%" src="https://i.imgur.com/uitFaSt.png"><img width="47%" src="https://i.imgur.com/qHsOmsN.png">


Before diving into how we selected features and performed dimensionality reduction, we should preface this with the type of problem we are trying to solve: regression. As you can see from the visualization, the target labels range from 155 to 301 with a standard deviation of 20.4888. There is a significant amount of variance and a wide range of numeric values we need to predict, suggesting the problem is regression-oriented. Moreover, the target labels are clearly normally distributed. We proceeded to remove outliers using IQR because these outliers represents games with extremely unusual scoring, falling well outside the realm of "probable". They would negatively affect our model's predictive capability with noise.

## Correlation and Feature Selection
<div style="width: 100%; text-align: center"><h3>Correlation Matrix Before Feature Selection</h3>
<p>
Labels removed due to number of features
</p></div>
<p style="text-align: center"><img width="50%" src="https://i.imgur.com/Wonh3Qx.png"></p>


After standardizing the data, we calculated a pearson correlation matrix for all features and created an accompanying visualization to illustrate the relationship between each feature pair in our dataset. The diagonal of the matrix, as expected, was perfectly correlated; however, there appeared to be very few areas in which the correlation between features was high enough to warrant large-scale feature selection. Moreover, the visualization generated was too low-resolution due to the number of features to actually be usable (102 x 102).

<div style="float: left; width: 50%; text-align: center"><h3>F-Regression </h3></div>
<div style="float: left; width: 50%; text-align: center"><h3>Mutual Information Regression</h3></div>
<p style="text-align: center"><img width="100%" src="https://i.imgur.com/I6PZ3TY.png"></p>


In order to narrow down our data to the 20 most relevant features, we decided to score the relationship between each feature and the target label using F-regression and mutual-information regression. Then, we took the top 20 for each score. After viewing the results of these two processes (pearson correlation matrices shown above), we ultimately decided to stick with only F-regression because it most clearly encapsulates the relevant information.

The higher reasolution correlation matrix visualization (20x20) for the feature-selected dataset yields more fruitful results. It’s evident that information such as free throws, free throw attempts, and free throw rate are highly correlated (obviously), so it’s only necessary to include one and minimize the number of features in the data. Similarly trends, were noticed for several other feature groups and well; we kept only one feature for each cluster of highly correlated features.

<h3 style="text-align: center">Final Selected Features</h3>
<p style="text-align: center"><img width="60%" src="https://i.imgur.com/FXv25jd.png"></p>


You can see the final features we selected on in the visualization above. These features will probably change as we evaluate the performance of our models.

<h3 style="text-align: center">Plotting Relationship Between Top 6 Features and Label</h3>
<p style="text-align: center"><img width="75%" src="https://i.imgur.com/bk7n0n4.png"></p>

We proceeded to plot the top 6 features (by F-regression score) against total points for each game. As you can see, we have no features linearly correlated with the target label, which can also be seen in the correlation matrix.

## Unsupervised Learning
### Principal Component Analysis
<p style="text-align: center"><img width="50%" src="https://i.imgur.com/WgrOKeD.png"></p>

Then, we used PCA in order to identify an orthonormal basis for the data. We took a subset of the orthonormal basis generated by PCA and projected the dataset into 10 directions that capture a target amount of variance (.99), thereby reducing the dimensionality .

### K-Means
<div style="float: left; text-align: center; width: 50%"><img width="85%" src="https://i.imgur.com/Gc1s8WG.png"></div>
<div style="float: right; text-align: center; width: 50%"><img width="85%" src="https://i.imgur.com/IqV0GWJ.png"></div>

<div>&nbsp;</div>

We performed K-Means on each dataset for numbers of clusters from 2 to 80. To evaluate K-means, we calculated a silhouette coefficient and loss metric (based on euclidean distance from the center for each point) for each clustering. The silhouette coefficient is calculated using the mean intra-cluster distance and the mean nearest-cluster distance for each clustering. Silhouette coefficients have a range from -1 to 1, where a silhouette coefficient of 1 is best. In short, all clusterings had silhouette scores well below 1, telling us clustering was poor. This was not a surprising result, considering our task is regression-oriented.

## Future Steps
Ultimately, we have to decide on a dataset--some important questions we need to answer: how many seasons of data should we include in the dataset--currently we are using three. Should we keep the feature-selection stage of our data cleaning? Should we use the dimensionality reduction from PCA? Once we decide on which dataset to use, we will try various supervised learning methods: neural networks, random forest regression, and ridge regression. Most likely, we’ll try several datasets in the supervised learning stage and identify the one to use based on the performance of the models. 
