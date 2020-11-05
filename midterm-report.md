# Midterm Report
By Bryce Plunkett, Nicholas Boshart, Sami Rahman, Paul Dittamo

<img style="box-shadow: 2px 2px 10px #00000050" width="100%" src="https://i.imgur.com/nPqxhzs.jpg">

## Data Collection 
Initially, we calculated a team’s running averages of stats leading up to a given game. We first attempted to fetch the information through a 3rd party API. Unfortunately, we only found paid services that satisfied our requirements--obviously, we did not want to spend money. Thus, we resorted to basketballreference.com, a site that hosts a myriad of stats pertinent to the NBA. In true computer science fashion we automated scraping the data instead of manually downloading CSVs of teams' season long game logs: we extended an existing python package, basketball_reference_scraper. Then, we built out a new feature within the package to scrape a team’s game logs throughout the season. After this, we ran a script to get the running average of a team’s stats for each regular season game in the last 20 years. This process involved pairing that data to the given game. 

## Merging Data
### Combining Individual Years
Overall, our data goes back 20 years, and each year has about 1,200 games (and is contained within its own CSV). Instead of using all 20 seasons of data, we opted to take a subset of games within the past 3 seasons to accelerate data processing and model training. We’ll likely expand this subset in the future once we decide upon a model and a more concrete data cleaning process.

<h3 style="text-align: center">Merging Home and Away Statistics</h3>
<p style="text-align: center"><img width="75%" src="https://i.imgur.com/ZTMYFud.png"></p>


There are 51 features for each team. Since each game consists of two teams, there are a total of 102 features per game. For feature selection purposes, if we select the home-team version of a feature, we would naturally want to include the away-team version as well. Thus, for each home-away feature pair, we merged them into a singular feature by taking the difference. We chose difference instead of multiplication because it keeps the directionality of the data. If we used multiplication, for instance, a team with a stacked defense vs a team with a stack offense would appear the same as a team with a stacked defense and offense vs a normal team.

## Dividing and Standardizing
We divided the dataset into a training and testing site with a 70-30 split, respectively. Then, we standardized the data (excluding the label), so no one feature dominates in the model. Each feature has a mean of 0 and a variance of 1.

## Problem Type
<h3 style="text-align: center">Before Removing Outliers</h3>
<img width="53%" src="https://i.imgur.com/Nt5uRqt.png"><img width="47%" src="https://i.imgur.com/92QRxIM.png">
<h3 style="text-align: center">After Removing Outliers</h3>
<img width="53%" src="https://i.imgur.com/uitFaSt.png"><img width="47%" src="https://i.imgur.com/qHsOmsN.png">


Before diving into how we selected features and performed dimensionality reduction, we should preface this with the type of problem we are trying to solve: regression. As you can see from the visualization, the target labels range from 155 to 301 with a standard deviation of 20.4888. There is a significant amount of variance and a wide range of numeric values we need to predict--suggeting the problem is regression-oriented. Moreover, the target labels are clearly normally distributed. We proceeded to remove outliers using IQR beause these outliers represents games with extremely unusual scoring, falling well outside the realm of "probable".

## Correlation and Feature Selection
After standardizing the data, we calculated a pearson correlation matrix and created an accompanying visualization to illustrate the relationship between each feature pair in our dataset. As you can see, the results weren’t great. The diagonal, as expected, was perfectly correlated; however, there appears to be very few areas in which the correlation between features is high enough to warrant large-scale feature selection, and the visualization is too low-resolution due to the number of features to actually be usable.

<div style="float: left; width: 50%; text-align: center"><h3>F-Regression</h3></div>
<div style="float: left; width: 50%; text-align: center"><h3>Mutual Information Regression</h3></div>
<p style="text-align: center"><img width="100%" src="https://i.imgur.com/I6PZ3TY.png"></p>


In order to narrow down our data to the 20 most relevant features, we decided to score the relationship between each feature and the target label using F-regression and mutual-information regression, and take the top 20 for each score. After viewing the results of these two processes, we ultimately decided to stick with only F-regression because it most clearly encapsulates the relevant information.

After looking at the higher-resolution correlation matrix visualization for the feature-selected dataset, it’s evident that information such as free throws, free throw attempts, and free throw rate are highly correlated (obviously), so it’s only necessary to include one and minimize the number of features in the data.

<h3 style="text-align: center">Final Selected Features</h3>
<p style="text-align: center"><img width="60%" src="https://i.imgur.com/FXv25jd.png"></p>


You can see the final features we settled on in the visualization above. These features will probably change--we are going to train the models on several datasets.

<h3 style="text-align: center">Plotting Relationship Between Top 6 Features and Label</h3>
<p style="text-align: center"><img width="75%" src="https://i.imgur.com/bk7n0n4.png"></p>
We proceeded to plot the top 6 features by f-regression score against total points for the game. As you can see, we have no features linearly correlated with the target label, which can also be seen in the correlation matrix.

## Unsupervised Learning
### Principal Component Analysis
<p style="text-align: center"><img width="50%" src="https://i.imgur.com/WgrOKeD.png"></p>

Then, we used PCA in order to identify an orthonormal basis for the data  and project the data into the directions that capture the most variance. We took a subset of the orthonormal basis generated by PCA and projected the dataset into 13 directions that capture a target amount of variance (.95), thereby reducing the dimensionality .

### K-Means
<div style="float: left; text-align: center; width: 50%"><img width="85%" src="https://i.imgur.com/Gc1s8WG.png"></div>
<div style="float: right; text-align: center; width: 50%"><img width="85%" src="https://i.imgur.com/IqV0GWJ.png"></div>

<div>&nbsp;</div>

We performed K-Means on each dataset for numbers of clusters from 2 to 80. To evaluate K-means, we calculated the mean euclidean distance for each point from its assigned center and the silhouette coefficient. The Silhouette Coefficient is calculated using the mean intra-cluster distance and the mean nearest-cluster distance for each clustering with a range of -1 to 1, where a silhouette score of 1 is best. In short, all clusterings had silhouette scores well below 1, telling us clustering was poor. This was not a surprising result, considering our task is regression-oriented.

## Future Steps
Ultimately, we have to decide on a dataset--some important questions we need to answer: how many seasons of data should we include in the dataset--currently we are using three. Should we keep the feature-selection stage of our data cleaning? Should we use the dimensionality reduction from PCA? Once we decide on which dataset to use, we will try various supervised learning methods: neural networks, random forest regression, and ridge regression. Most likely, we’ll try several datasets in the supervised learning stage and identify the one to use based on the performance of the models. 
