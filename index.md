# Project Proposal
## Summary Figure
## Introduction
In 2018, the Supreme Court overturned the Professional and Amateur Sports Protection Act - a ruling of which inhibited states to authorize legal sports gambling. In the two years since, the USA has seen an extraordinary growth in sports betting. Nearly 11 billion dollars were wagered at licensed USA sportsbooks in 2019 alone.

Much of this growth has surrounded speculative bets on NBA games. Roughly 10 millions dollars were wagered legally on each of the 6 2019 NBA finals games. Gamblers would bet on a wide array of props such as the money line and the game’s leading scorer.

As is common across most sports, one of the most common bets placed on a basketball game is the over/under - a bet on whether the combined scores at the end of a game will be above or below a value set by the books.

This semester, our group will leverage various  machine learning methods to estimate the total final score of an NBA game.
 
## Methods
### Features of Our Data
We plan to account for metrics such as a team’s field goal attempts and percentage, 3 points shots and percentage, and defense efficiency metrics.
Obviously, we are not committed to these features and will most likely discover more as we progress into the project.

Conversely, we do not plan to account for player specific stats--we plan to ignore team composition, and we also plan to disregard team name. The primary reason for these exlusions: to keep the model more generalizable and simplify the dataset. 

One issue we might encounter with a team's statistics is uncertainty. Early in a season, a team's statistics are for more fluid due to the lack of data in the season. Thus, we might exclude games early in the season from the training dataset. Alternatively, we might somehow plug an "uncertainty" metric in the model.

### Obtaining Data:
We plan on aggregating the data in three possible ways: downloading CSV's from sport statistics sites with "export" options, querying existing API's, and by scraping relevant statistics sites. In the context of our project, websites such as basketball-reference.com provide an abundance of statistics relevant to what we’re analyzing and  "export" option, so ideally,
most of our dataset will come from sites such as these.

In a perfect world, we won't have to use the API's because we have yet to find any that are free. Similarly, web scraping is a last resort because of the complexity of the task; we don't won't to burn too much time making a web scraper.

Once we have our dataset, we will need to augment it with additional features since most of the statistics will be on a game to game basis. Essentially, we will have to calculate the "average" of each team's statistic's before the game that is being estimated (this will be the input vector). This should be relatively trivial to do with a scripting language.

### Creating Models
We will attempt to use data analysis--visualizations, correlation metrics, PCA--to identify key features and eliminate insignificant dimensions. Most likely, we will only use unsupervised learning to give us insights into the data.

In the end, our "prediction" model will (probably) leverage supervised learning, since all of our training dataset is labeled with the games' combined scores. We will probably settle with some flavor of neural network, but we will also look into decisions trees and various forms of regression.
## Results
Ultimately, our model will output a combined score. To measure the success of its prediction, we will primarily look at the percent different in combined score of expected vs actual. Ideally, we want to see our model output an average percent difference in score of at most 60%. Furthermore, we'll look at metrics like Mean Square Error, however (obviously) we have no expecations for metrics such as these. Moreover, we would like to see the model output a confidence in its prediction to give more actionable information when placing bets. 
## Discussion
The best outcome, as referenced earlier, would be an estimation reasonably close to the combined score (~5%). Ideally, a confidence metric would augment this prediction by telling the user how actionable the information actually is. A more reasonable "best outcome" would be (as mentioned earlier) an average percent difference in score of at most 60%. If this model is actually successful, the benefit would be apparent: making informed, accurate over-under bets on combined scores. 

Our next step is to actually obtain the data and make the necessary augmentations. Then, we will perform data analysis (and unsupervised learning) to get a better understanding of the the information and its patterns.
## References


