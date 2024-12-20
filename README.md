# Abstract

The film industry has been with us for well over a century and spans all corners of the globe. With the advent of American political and economic power, which has grown through the past century, its soft power has as well. Thanks in large part to the world renowned Hollywood, the highest worldwide grossing movies are made in America. Therefore, we are interested in researching the impact that their rise to worldwide cinema dominance has had on its domestic performance. We hypothesize that throughout the years as English became the 'lingua franca' of the world and Hollywood gained in international popularity, the percentage of revenue coming from foreign countries increased. Furthermore, we would like to determine what movies genres are more successful domestically and with foreign countries. Poring through this data will help determine the key factors needed to realize a worldwide box office hit for major Hollywood studios.

The link to our data story can be found here: [https://epfl-ada.github.io/ada-2024-project-thelordsofdata/](https://epfl-ada.github.io/ada-2024-project-thelordsofdata/).

# Research Questions
1. What is the evolution of domestic vs. foreign proportion of revenue on American movies over time? Should major Hollywood studios focus on attracting foreign audiences?
2. What are American preferences in genre and character tropes, and which ones would incentive foreign audiences to watch American movies?
3. How does a movie's production budget impact the domestic/foreign revenue split? Does a larger production budget allow movies to reach a larger foreign audience?
4. How has the market of the international movie industry evolved over time, and how has that impacted the American market share?
5. Can we predict which factors will generate a larger foreign audience?


# Dataset

## Budget, Domestic Gross and Worldwide Gross
The CMU dataset only contains information on the total revenue generated by the movie, as well as the genre and the tropes of the characters featured within each movie. In order to look at trends in domestic versus foreign revenues, we needed to supplement this data. In addition to the CMU dataset, we used both the 'Movies Box Office Collection Data' dataset from Kaggle and a custom dataset (which includes data from Box Office Mojo, IMDB, Rotten Tomatoes, TheMovieDB, and The Numbers) from the following github link 'https://github.com/ntdoris/movie-revenue-analysis.git' to add the columns for production budget, domestic gross and worldwide gross. 

We will supplement this data further using web scrapping methods. We will look for American and foreign movie market shares over the years, population sizes, and movies from specific countries for additional case studies.

# Methods
## Data preprocessing
### 1. Cleaning the CMU dataset
Within the CMU dataset, the columns that were no longer needed were removed (e.g. Movie Runtime). Any typos that involved special characters were removed and modifications were made to columns where any unnecessary supplementary information was contained. However, we chose to keep the rows which had NaN values in the columns we need. This missing information was provided by supplemental datasets. We removed the rows that contains NaNs on a case-by-case basis for each of the analysis steps that we did, depending on what data was needed for each step.

### 2. Supplementing dataset
Using the additional datasets mentioned in the section above, we augmented the CMU dataset by adding the following four additional columns: budget, domestic gross, foreign gross, and worldwide gross. Any movies that coincided with the CMU dataset were merged together while any new movies were concatenated at the end. Some of the additional movies added were produced from abroad and therefore help to strengthen the size of our foreign movies.

Finally, we calculated the percentage of the worldwide gross that comes from domestic and foreign revenues and added them in two additional columns. This gives us the final dataset from which many of our plots have been and will be based on.

## Initial Analysis
In our initial analysis, we have a density plot of both the domestic percentage and the foreign percentage share of movie revenue, demonstrating an almost normal distribution but with slight peaks at either end. Other initial plots include looking at the evolution of the average percentage and gross value of foreign and domestic revenues on American movies over the years. 

### 1. Binning data and subsequent Time Series
Data binning was used in this project to group movies of the same year together, and then will also be used for the next milestone by decade in order to reduce noise, handle missing data, and evaluate trends that have changed over the decades.

### 2. Correlation
Within this initial analysis, we have two scatterplots which look at how budget influences the percentage of revenue coming from domestic markets and those coming from foreign markets. The Pearson coefficient was then determined in order to evaluate the correlation. The p-value was found to be very low (< 0.05) showing it to be statistically significant.

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
