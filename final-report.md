# Final Report
## Dataset
### Initial Datasets
Initially, we scraped 20 seasons of basketball data from basketballreference.com using a custom scraper. Each row contained the home and away teams' running averages for the season and the total points for the game, with 103 features for each row.  

### Dataset Transformation Pipeline
![](https://i.imgur.com/hxlyUY7.png)
<h6 class="test" style="text-align:center; margin-top:0px; margin-bottom: 20px; color: darkGray"><i>Model of pipeline used to transform each dataset into 3 variants.</i></h6>

After merging home and away scores with delta, data standardization, feature selection, and dimensionality reduction, we were left with three final datasets --- all of which were derived from the same set of seasons (i.e. 2017, 2018, 2019). One dataset had its features cleaned (51 total features), another had been both cleaned and feature-selected (19 total features), and the last had been cleaned, feature-selected, and dimensionality reduced (10 total features).

## Unsupervised Learning
### Principal Component Analysis
<p style="text-align:center; margin-top: 25px"><img width="50%" src="https://i.imgur.com/WgrOKeD.png"></p>

By using principal component analysis during our unsupervised learning stage, we were able to not only identify an orthonormal basis for the data, but also project the dataset into 10 directions spanning 99% of the original variance (as illustrated in the graph above). In doing so, we successfully reduced the dimensionality of the data and made it more interpretable --- all while minimizing information loss

### K-Means
<div style="float:left; width:50%"><img width="85%" src="https://i.imgur.com/Gc1s8WG.png"></div>
<div style="float:right; width:50%"><img width="85%" src="https://i.imgur.com/IqV0GWJ.png"></div>

<div>&nbsp;</div>

Additionally, we performed K-Means on each dataset with number of clusters ranging from 2 to 80. To evaluate the results, we computed a silhouette coefficient and loss metric for each clustering. The silhouette coefficient was calculated using the mean intra-cluster distance and the mean nearest-cluster distance for each clustering, whereas the loss metric involved the euclidean distance from each cluster's center. In the end, we found that all clusters had a silhouette coefficient well below 1.0 and incredibly high losses, thus indicating the futility of using clustering-based methods. This unsatisfactory result, however, was not at all surprising, as we were already aware of the problem's regression-oriented nature. Thus, little was yielded from K-Means.
## Supervised Learning
### Exploratory Stage
#### Initial Methods
<!-- Insert dataset variant figure -->
Having spent a significant amount of time cleaning our data and receiving lackluster results in the unsupervised learning stage, we were ready to tackle supervised learning head on. We ended up creating three exploratory models for each dataset. We chose random forest regression (initial params: the defaults of sci-kit learn) because it takes a unique approach to regression while minimizing overfitting. Furthermore, we chose ridge regression (initials params: regularization term of 1.0) because it takes a simpler approach to regression while also including bias to prevent overfitting. Finally, we opted to include a neural network because it's incredibly flexible (initial params: five hidden layers containing 50, 50, 50, 50, and 10 nodes). 

The goal of using arbitrarily-selected parameters was to identify the model that has the most potential. In other words, we hoped untuned performance would reflect potential performance, which we could then use to decide on a final model to tune. In order to do so, however, we needed some metrics to assess the relative performance of each model. We decided to use R<sup>2</sup> = Residual Sum of Squares ÷ Total Sum of Squares, where R<sup>2</sup> ∈ [-1, 1]. Put simply, this metric can be viewed as the variance in total points that can be explained by the independent variables in the model.

Additionally, we used root mean square error to evaluate performance. Since we know the context of our problem, there was no need to perform any sort of normalization on this value because we knew the test labels had a standard deviation of 21.2 and a mean of 215.5. As a result, we concluded an RMSE less than 10 would be considered great, anything between 10 and 20 would be mediocre, and greater than 20 would be bad. 

#### Initial Results
We then proceeded to train each of the three models --- the random forest regression, ridge regression, and neural network --- using the three dataset variants described previously. Overall, the results we received were rather underwhelming. The highest R<sup>2</sup> value was less than 0.1 and all the RMSE's were greater than 20. Obviously, this suggested a critical issue with our data, as the performance of our models was comparable to constantly predicting the mean value.


#### A New Plan
<img src="https://i.imgur.com/jlhSifl.png"><br>
<img src="https://i.imgur.com/kMxm0dw.png">
<h6 style="text-align:center; margin-top:10px; margin-bottom: 30px; color: darkGray"><i>Effect of delta-merging on the 2017, 2018, 2019 dataset. Delta-merging's negative impact on the "_scaled" variant was observed on the other datasets as well. The neural network should be taken with a grain of salt due to its arbitrary architecture.</i></h6>

Ultimately, we realized our approach might be inherently flawed --- perhaps you can’t predict the combined score of an NBA game by looking solely at a team’s running seasonal averages. As a result, we decided to take a less fine-tuned approach to the problem. 

<!-- Merge pipeline -->
Rethinking the plan, we knew we had a data cleaning and feature selection pipeline readily available as well as 20 seasons of game data; there were still a few techniques we could utilize to improve performance. First, we tested a dataset --- again, with 3 variants --- where we did not merge home and away features. The results from these trials were more promising, as we were seeing R<sup>2</sup> values around 0.3 and an RMSE between 17 and 18. Although this performance can be best described as adequate, the results were still noticably better than that of our previous trial. Consequently, we realized that merging the home and away features was at least one component of our problem.


#### More Data
Naturally, we wanted to see if throwing more data at the models would give us better performance. As such, we created 2 additional datasets to generate variants from --- one containing data from only the last 10 seasons, and the other with data from the past 20 (all the seasons we scraped). With these two datasets, as well as their 3 respective variants, we saw even greater improvement. Our R<sup>2</sup> values were now consistently hovering around .3 to .4, whereas the RMSE teetered near 17. Despite this advancement, the two datasets each traded blows between different models and variants, so it was not readily apparent which was dataset size was better to use. Additionally, it seemed that no particular variant performed better or worse than the others, thus providing no means of distinction between the three.

#### Different Merging Strategy
Naturally, we wanted to attempt other home/away merging strategies. Since taking the delta did not seem to work in our favor, we decided to pivot to another intuitive operation: multiplication. Using the multiply-merge technique, we observed comparable performance to what we had found before merging --- some variants worked well with particular models and worse with others (none performed noticably better or worse). The takeaway, however, was that it achieved similar results to its unmerged counterpart.

We also attempted an additive-merge strategy on the dataset containing only 10 seasons, but we found its performance was not markedly better (or worse) than our multiplicative approach, so we did not continue pursuing that route.

#### Final Exploratory Methods

![](https://i.imgur.com/fekI1o7.png)

In the end, we had three final datasets utilizing the past 3, 10, and 20 seasons of our data. Each dataset consisted of three additional variant sets: an unmerged variant, a difference-merged variant, and a multiplication-merged variant. Going one level deeper, each of these variants also had three separate subvariants: one with feature scaling and cleaning, one feature scaling, cleaning, and selection, as well as one feature scaling, cleaning, selection, and dimensionality reduction through PCA.

Finally, we trained all three models, random forest regression, ridge regression, and a neural network, for each of these 27 subvariants --- the results of which can be seen below.

#### Final Exploratory Results
<img src="https://i.imgur.com/2kFhdlz.png"><br>
<img src="https://i.imgur.com/n1dgRBN.png"><br>
<img src="https://i.imgur.com/4xW4hQ3.png">
<h6 style="text-align:center; margin-top:10px; margin-bottom: 30px; color: darkGray"><i>Ridge Regression results for all datasets; similar pattern seen for other models.</i></h6>

Given the performance of each model, we were looking to select a final dataset upon which we could perform hyperparameter tuning. While sifting through our results, we concluded that merging with multiplication --- as opposed to not merging at all --- had no significant impact on the results. We also found that 3 seasons was not enough data, as it led to overfitting. As a result, we decided to stick with the ‘all 20 seasons’ dataset, `all_seasons`, with its features merged through multiplication because: (a) it has fewer features (and hence faster training time) than its unmerged counterpart, and (b) it has significantly more training data than the 10 season dataset, even though it doesn't yield remarkably better performance.

<img src="https://i.imgur.com/bJVg0X3.png">
<h6 style="text-align:center; margin-top:10px; margin-bottom: 20px; color: darkGray"><i>Comparison of subvariants on the finalized, 'general' dataset.</i></h6>

Furthermore, we decided to use the feature-selected variant because, overall, it led to faster training and didn't significantly affect model performance (i.e. comparable R<sup>2</sup> values and +-0.5 RMSE difference when compared to its scaled counterpart). Ultimately, we opted not to use PCA because it did not eliminate a significant number of features, 

### Hyperparmeter Tuning on Final Dataset
<!-- Insert hyperparameter tuning graph -->
With our final dataset in hand, we were then able to move onto hyperparameter tuning. First, we partioned the dataset as follows: 70% train; 10% validation; 20% test. Ultimately, because all the models had similar results (with exception to Neural Network due to its arbitrary architecture), we decided to hyperparameter tune _all_ the models. We ended up using Randomized Search Cross Validation (built into SciKitLearn) to search for the best parameters for each model. The train dataset was used to train each model, and the model was scored using R<sup>2</sup> on the validation dataset. The visualizations below represent the a selection of the results for parameter search, including the best among the set. In the end, we chose the parameters that yielded the highest R<sup>2</sup> value for each model. We then ran the models against the test dataset and observed peak values of R<sup>2</sup> = 0.41334 with Random Forest and RMSE = 16.92274 with Ridge Regression.

#### Random Forest
<span style="float:left; width:50%"><img src="https://i.imgur.com/rdBSugm.png"></span>
<br>
```python
Iteration 0  →  R^2 = 0.388828488 for ('n_estimators': 1000, 'min_samples_split': 15, 'max_features': 'sqrt', 'min_samples_leaf': 2)
Iteration 1  →  R^2 = 0.388104509 for ('n_estimators': 1500, 'min_samples_split': 8, 'max_features': 'sqrt', 'min_samples_leaf': 4)
Iteration 2  →  R^2 = 0.388770221 for ('n_estimators': 950, 'min_samples_split': 12, 'max_features': 'sqrt', 'min_samples_leaf': 3)
Iteration 3  →  R^2 = 0.386528596 for ('n_estimators': 500, 'min_samples_split': 15, 'max_features': 0.9, 'min_samples_leaf': 2)
Iteration 4  →  R^2 = 0.389122797 for ('n_estimators': 500, 'min_samples_split': 10, 'max_features': 0.9, 'min_samples_leaf': 3)
```
<br>

#### Ridge Regression
<span style="float:left; width:50%"><img src="https://i.imgur.com/ZC8Bma2.png"></span>
<br>
```python
Iteration 0  →  R^2 = 0.389732731 for (alpha=1)
Iteration 1  →  R^2 = 0.389732731 for (alpha=5)
Iteration 2  →  R^2 = 0.389732731 for (alpha=10)
Iteration 3  →  R^2 = 0.389732731 for (alpha=20)
Iteration 4  →  R^2 = 0.389732731 for (alpha=50)
```
<br>

#### Neural Network
<span style="float:left; width:50%"><img src="https://i.imgur.com/Yx74rtK.png"></span>
<br>
```python
Iteration 0  →  R^2 = 0.385284018 for (max_iter=2500, hidden_layer_sizes=(50, 50, 50, 50, 10))
Iteration 1  →  R^2 = 0.376507212 for (max_iter=2500, hidden_layer_sizes=(100, 100, 100, 100, 20))
Iteration 2  →  R^2 = 0.385024759 for (max_iter=500, hidden_layer_sizes=(200, 200, 200, 200, 40))
Iteration 3  →  R^2 = 0.388527833 for (max_iter=3000, hidden_layer_sizes=(100, 100, 100, 100, 20))
Iteration 4  →  R^2 = 0.375974623 for (max_iter=1500, hidden_layer_sizes=(100, 100, 100, 100, 20))
```
<br>

### Converting to a Classification Problem
#### Idea and Methods
Finally, we attempted to convert the regression problem into one of classification. What if we predicted _ranges_ of total points instead of specific values? For this problem, there are two variants: binary-classification and multi-classification. We settled for ranges of size 10 in both problems. For binary classifcation, we trained our model to predict only a singular range --- in other words, if the game is expected to fall between `[x, x+10]` for some fixed `x`, return `true`.

If this model were to yield few false positives, it could lead to significant profit in betting. For instance, say there exists a binary classifier that predicts whether a game will end with a combined score in the range of `[219, 229]`. If this classifier were to have a high precision, then it's implied that placing a bet when prompted is relatively safe, thus guaranteeing positive returns over a sufficiently large span of time.

For the multi-classification problem, we set ranges of scores as labels in hopes of gaining better prediction results (when compared to predicting the exact score). 

To evaluate our model, we settled on 3 metrics: accuracy, precision, and F1-score. We utilized accuracy to get an idea of the predictions' quality, precision to account (unsafe bets) for the impact of false negatives, F1-score to account for the impact of false positives (missed betting opportunities) and false negatives.

<div style="float:right; width:50%"><img src="https://i.imgur.com/jkefsUK.jpg"></div><div style="float:left; width:50%"><img src="https://i.imgur.com/AiZbb7K.jpg"></div>
<h6 style="text-align:center; margin-top:10px; margin-bottom: 20px; color: darkGray"><i>Results of the two classification problems. Each group represents the various metrics for the model. Gr</i></h6>
#### Results
We did not see good results. Although some models had decent accuracy (.8 - .9) they saw poor F1-scores and precision. Due to this we opted to not continue with hyperparameter tuning.

## Discussion of Results
In the end, we saw mixed unsupervised learning results with poor K-Means performance and decent PCA performance (dimensionality reduction with PCA did not significantly affect the performance of models). With supervised learning as a regression problem, we saw, at best, mediocre results even with hyperparameter tuning. Furthermore, with supervised learning as a classification problem, we saw extremely underwhelming performance with poor precision and F1-score scores.

All things considered, we believe significantly better performance may be unobtainable given our existing datasets, as they are rooted in the running averages of the entire team. Consequently, there exist many confounding variables that exert influence over any given game --- when in the season does the game occur, what are the game's stakes, are there injuries on either team, and do the players' styles combat or complement one another? Today's NBA frequently has star players sitting out games for load management. It is also no longer the norm for players to fully exert themselves on a game to game basis during the regular season. In short, there’s a lot of variability in basketball which overarching team statistics cannot encode, thus making the over-under problem a very difficult one to solve.
