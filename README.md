# Abstract

The film industry has been with us for well over a century and spans all corners of the globe. With the advent of American political and economic power, which has grown through the past century, its soft power has as well. Thanks in large part to the world renowned Hollywood, the highest worldwide grossing movies are made in America. Therefore, we are interested in researching the impact that their rise to worldwide cinema dominance has had on its domestic performance. We hypothesize that throughout the years as English became the 'lingua franca' of the world and Hollywood gained in international popularity, the percentage of revenue coming from foreign countries increased. Furthermore, we would like to determine what movies genres are more successful domestically and with foreign countries. Poring through this data will help determine the key factors needed to realize a worldwide box office hit for major Hollywood studios.

The link to our data story can be found here: [https://epfl-ada.github.io/ada-2024-project-thelordsofdata/](https://epfl-ada.github.io/ada-2024-project-thelordsofdata/).

# Research Questions
1. Is there an incentive for American studios to produce movies that attract foreign audiences?
2. How can American studios produce movies that attract foreign audiences in order to maximize profit?
3. How does a movie's production budget impact the domestic/foreign revenue split? Does a larger production budget allow movies to reach a larger foreign audience?
4. What are American preferences in genre, runtime, and ratings, and what are international preferences in those same categories? 
5. What is the impact of the season of release of the movie as well as audience and critic scores on the likelihood of foreign interest?
6. Can we predict which factors will generate a larger foreign audience?


# Dataset

## Budget, Domestic Gross and Worldwide Gross
We started with the CMU movie.metadata dataset. It contains 81740 movies with the following useful  information: Name, Release_Date, Revenue, Runtime and Genres. In order to be able to analyze the Foreign Revenue and Domestic Revenue, we were able to supplement our dataset using a concatenation of information from Kaggle, Box Office Mojo, IMDb, Rotten Tomatoes, and TheMovieDB available at [https://github.com/ntdoris/movie-revenue-analysis](here). We then further augmented our dataset by scrapping information from The Numbers (domestic and foreign gross and genres), Rotten Tomatoes (reviews, ratings, runtime and plot summary), Wikipedia (country), and Box Office Mojo (domestic and foreign gross). Emotional classification of the plot summaries into the seven following categories : suprise, fear, disgust, joy, anger, sadness and neutral was done using Hartman's DistilRoberta model available at [https://huggingface.co/j-hartmann/emotion-english-distilroberta-base](here). All of our USD values were adjusted for inflation to 2024. 

# Methods
## Data preprocessing
### 1. Cleaning the CMU dataset
Within the CMU dataset, the columns that were no longer needed were removed (e.g. the Wikipedia and Free base IDs). Any typos that involved special characters were removed and modifications were made to columns where any unnecessary supplementary information was contained. However, any rows that had NaNs in columns that we required were removed or replaced by information obtained via the scraping method detailed above.

### 2. Supplementing dataset
In order to augment the CMU dataset, we used the scraping method mentioned above which resulted in the addition of additional columns,  of which the most important include budget, domestic gross, foreign gross, and worldwide gross. Any movies that coincided with the CMU dataset were merged together while any new movies were concatenated at the end. The addition of new movies at the end help to bring up the number of movies in our dataset to nearly 2,700.

### 3. Data Exploration
From the augmented dataset, we were then able to explore how some of the different factors (e.g genre, budget, etc...) impacted the domestic and foreign revenue of these movies. We then plotted different variations of how those respective factors impacted revenue.


## Analysis
For our analysis, we used OLS in order to evaluate the correlation between the different factors and revenue. 

### OLS Coefficient 
Now that we have explored at the distribution and relationships between the budget, genre, release date, runtime, rating, reviews, and finally the percentage of foreign revenue of a movie, we can now begin to properly analyse these relationships. We want to know which features predict a higher percentage of foreign revenue by comparing the OLS Coefficient of each feature.

The OLS coefficient represents the expected change in the foreign percentage of revenue for a one-unit increase in the predictor variable, holding all other variables constant. It's important to look at the p-value associated with the coefficient to determine whether the relationship is statistically significant.

Below, we compare the OLS coefficients over 2000-2019, but then separate between 2000-2010 and 2010-2019 in order to take a closer look at more recent impact of the features.

# Proposed Timeline
The steps that will need to be completed for the third and final milestone:

### Step 1 - Complete Analysis
Complete analysis on current data. Now we have looked at foreign vs. domestic revenues with respect to genre, time, and budget. Our next steps will be to look at population, tropes, and time with larger bins.

### Step 2 - Market share globally
Look at how the global market share of the film industry has evolved over time and see whether the American film industry is shrinking in the face of emerging markets

### Step 3 - Case studies
Look at a few countries (e.g. India, France, etc...) outside of the United States and look at how the respective factors mentioned in the research questions impact the countries in question. We have already started on India under the test folder.

### Step 4 - Unsupervised learning
Use unsupervised learning on genre and tropes in order to figure out whether a certain movie that has those characteristics would earn more domestically or internationally



- 15.11.2024    -   Initial Analysis and Data Handling Framework (Milestone 2)
- 22.11.2024    -   Step 1, Step 2
- 29.11.2024    -   Homework 2
- 06.12.2024    -   Step 3
- 13.12.2024    -   Step 4
- 20.12.2024    -   Project Milestone 3 Submission

# Organization

- Liam: Step 1 + 3
- Selma: Step 2 + 3
- Giada: Step 3 + 4
- Ameer: Steps 3 + 4
- Loïc:  Step 4

# Data Structure
```text
├── data                        <- Project data files
│
├── src                         <- Source code
│   ├── data                            <- Data directory
│   ├── models                          <- Model directory
│   ├── utils                           <- Utility directory
│   ├── scripts                         <- Shell scripts
│
├── tests                       <- Tests for all the different plots that were attempted
│
├── results.ipynb               <- Notebook that displays all the results obtained, with all plots shown in the data story present
│
├── .gitignore                  <- List of files ignored by git
├── pip_requirements.txt        <- File for installing python dependencies
└── README.md
```
