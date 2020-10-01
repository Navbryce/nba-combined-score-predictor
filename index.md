# Project Proposal - NBA Combined Score Prediction
Through supervised learning we will utilize years of data from past NBA games to reach our goal.

We plan on aggregating this data in primarily two ways: by scraping relevant statistics sites and querying existing APIs. In the context of our project, websites such as basketball-reference.com provide an abundance of statistics relevant to what we’re analyzing, so we figured it’d be beneficial to include this information in our dataset. Similarly, we’ve also discovered a few existing APIs that already encapsulate some of this data. This is great for us because, ideally, we don’t want to reinvent the wheel by manually scraping information that’s already available, though this may be necessary for data not contained within an API.

We will attempt to use data analysis--visualizations, correlation metrics, PCA--to identify key features and eliminate insignificant dimensions. We’ll also use unsupervised learning to learn more about the data space.

Since all of our data is labeled (we have previous games' combined scores), we will use supervised learning to create our model. In the end, we will most likely settle for some flavor of neural network, but we’re not too sure yet. We’re going to try several different models to determine the best one--and then we’ll do hyperparameter tuning. Our end goal is to achieve an average of percent difference of at most 60%. We will also look into outputting a percent confidence of our prediction.

## Summary Figure
## Introduction
In 2018, the Supreme Court overturned the Professional and Amateur Sports Protection Act - a ruling of which inhibited states to authorize legal sports gambling. In the two years since, the USA has seen an extraordinary growth in sports betting. Nearly 11 billion dollars were wagered at licensed USA sportsbooks in 2019 alone.

Much of this growth has surrounded speculative bets on NBA games. Roughly 10 millions dollars were wagered legally on each of the 6 2019 NBA finals games. Gamblers would bet on a wide array of props such as the money line and the game’s leading scorer.

As is common across most sports, one of the most common bets placed on a basketball game is the over/under - a bet on whether the combined scores at the end of a game will be above or below a value set by the books.

This semester, our group will leverage various  machine learning methods to estimate the total final score of an NBA game.
 
## Methods
## Features we want to account for in our data
We plan to account for metrics such as a team’s field goal attempts and percentage, 3 points shots and percentage, defense efficiency metrics and more.

We plan to account for metrics such as a team’s field goal attempts and percentage, 3 points shots and percentage, defense efficiency metrics and more.

### Obtaining Data:
We plan on aggregating this data in primarily two ways: by scraping relevant statistics sites and querying existing APIs. In the context of our project, websites such as basketball-reference.com provide an abundance of statistics relevant to what we’re analyzing, so we figured it’d be beneficial to include this information in our dataset. Similarly, we’ve also discovered a few existing APIs that already encapsulate some of this data. This is great for us because, ideally, we don’t want to reinvent the wheel by manually scraping information that’s already available, though this may be necessary for data not contained within an API.

## Results
## Discussion
## References


