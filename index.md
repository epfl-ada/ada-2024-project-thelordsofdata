---
layout: page
title: Make Hollywood Great Again
subtitle: Selma Benhassine, Giada Ehrlich, Ameer Elkhayat, Loïc Finette, Liam Gibbons 
---

# The Call to Action

"Folks, **we’ve got a crisis.** Hollywood’s been around for over a century. We’re talking the biggest, highest-grossing movies in the world. But now, foreign movies—they’re coming in hot. They’re coming for our audiences, our **box office,** and, frankly, our jobs. It’s like the Oscars all over again—rigged!

Now, here’s the thing: Hollywood’s top people, the big shots, they’re calling me. They’re saying, ‘Mr. Trump, you’re the only one who can fix this.’ And I say, ‘You’re absolutely right.’ 

So here’s what we’re gonna do, folks. We’re smart, okay? Smarter than those guys. We’re going take a look at the data and have our experts analyse it. All the past American movies, who's buying them, Americans or foreigners, the influencing factors, everything. And we're going to use all that information to attract those foreign audiences. Huge audiences, all over the world, will watch our movies. **Made in America, baby.**

You better believe it folks! We’re going to outshine, outclass, and outplay every single foreign competitor, and **Make Hollywood Great Again!** "

Words from the former and future convicted President himself. So let's get started.

# Dataset

## Building the Data Wall

To understand the dynamics between domestic and international revenues, we began by collecting a variety of datasets:

The CMU dataset provided data on worldwide revenue, genre, and character tropes.
We supplemented this data with additional datasets from Kaggle, Box Office Mojo, IMDb, Rotten Tomatoes, and TheMovieDB, to include important variables like budget, domestic gross, and worldwide gross.

For more detailed insights, we web-scraped data from The Numbers (domestic and foreign gross), Rotten Tomatoes (reviews), Wikipedia (country and language), and Box Office Mojo (ratings and reviews).

After cleaning and merging the data, we focused on movies released between 2000-2019, with a total of 2689 movies that met our criteria of having at least 90 entries per year. This dataset is our starting point for uncovering trends that drive foreign revenue.

## Fact-checking Mr Trump

We decided to compare movies that generate most of their revenue domestically and internationally. We assign movies that make more than 50 % of their revenue internationally to the red class and the other movies to the blue class. Performing this split, we obtain 1145 movies with a higher foreign percentage and 1544 with a higher domestic percentage. We then compute the profitability of a movie by dividing the revenue by the budget


{% include log_profitability_count.html %}

The outliers were removed from the box plots. From the box plots we can observe that the class with more than 50 % of their revenue coming from foreign countries has a higher median than the domestic class. However the red class shows a bit more variance. This confirms that movies that generate more of their revenue internationally are more profitable. Therefore Hollywood should focus on catering to an international audience.

{% include year_plot.html %}

The outliers were removed. Oh no! The foreign percentage steadily goes up until 2015. Then it starts going down. We need it to keep going up to maximize profits. The main goal of our analysis is to determine the factors influencing the foreign percentage.

## Influencing Factors

We've decided to look at the following factors:

- Date of Release (Year, Month)
- Genre
- Reviews (Audience, Critics)
- Ratings
- Budget
- Total Revenue
- Runtime

The result we want to look at is:
- Foreign revenue (gross, percentage)

# Data Exploration

A quick interjection from Mr. Trump: "Alright, folks, before the liberal left starts accusing me of **faking the numbers** again, let me set the record straight. We did something **smart**—we **adjusted the data**. Here’s the deal: **Inflation** and **outliters**-if you ignore them, you're just asking for fake news. It’s a total disaster. So, we did the right thing: we **adjusted** all USD amounts for inflation and took the logarithm of variables including budget and profitability to include outliers without letting them influence our analysis."

## Budget

{% include log_budget.html %}

Looking at the data, we can observe a clear relationship between budget and foreign percentage. The Pearson correlation coefficient is 0.33, indicating a moderate positive correlation between these two variables. Furthermore, the p-value is less than 0.05, which is statistically significant—this suggests that the relationship we’re seeing is not due to chance.

In simpler terms, as the budget increases, there's a tendency for movies to earn a higher percentage of their revenue from international markets. This makes sense: larger budgets often mean more resources for marketing and wider global distribution, which can lead to increased box office sales abroad.

## Genre

{% include genre_proportional.html %}

Looking at the data, we can see clear trends: Comedy performs significantly better in the United States, but struggles to gain traction in international markets. This is likely due to cultural and linguistic differences that make humor difficult to translate effectively. On the other hand, genres like Action, Drama, and Adventure have broader appeal across borders. These genres, characterized by strong visual elements, excitement, and universal themes of emotion, tend to resonate more easily with global audiences, leading to better international performance.

{% include genre_percentage.html %}

It’s important to note that while Drama performs well internationally, there are fewer drama films that are performing exceptionally abroad compared to those that are succeeding domestically in the U.S. We can see that Drama movies garner more of their revenue domestically than internationally. On the global stage, Action, Adventure, and Sci-Fi movies are the big earners, generating the more significant share of the revenue.

Additionally, some genres have a strong American appeal but don’t translate as well internationally. To capture a larger foreign audience, it may be more effective to focus on genres like Action, Adventure, and Sci-Fi while steering away from Teen, Indie, and Comedy films, which tend to have a more limited international appeal.

## Month

{% include month_percentage.html%}

As we can see, the movies that do best internationally tend to be released during the holiday season - November and December. We believe that the biggest blockbuster movies tend to be released around that season due to big holiday movie themes - Christmas, Hannukah, etc. These themes are pretty spread internationally, which makes these movies internationally appealing. On the other hand, we see here a missed opportunity to attract foreign audiences during the summer months, specifically August, where the percentage of foreign revenue is smallest. If we market our big summer blockbusters to international audiences, we have the opportunity to make big profits while everyone is on summer vacation.

## Runtime

{% include runtime_plot.html %}

From the runtime box plots we can observe that there is not much difference in the runtime of movies between the classes. The class where the domestic percentage dominates has a median of 103 and the other class, a median of 108. They both contain a similar amount of outliers. It is to note that for the blue class, there is one big outlier: a movie that has a runtime of 222 minutes.

## Ratings

{% include profit_rating_count.html %}

We decided to exclude the **'G'** rating due to a low count of data, as decisions based on insufficient data would lead to unreliable conclusions. Our focus shifted to the ratings with more substantial data, ensuring meaningful analysis.

To assess the data distribution, we conducted the **Shapiro-Wilk test**, and the result was a very low p-value, effectively approaching zero. This indicates that, even after applying the logarithm to profitability, the data is not normally distributed. As a result, we proceeded with the **Kruskal-Wallis test**, which is appropriate for comparing medians in skewed distributions, bypassing the assumptions of normality.

For domestic movies, the test returned a p-value of **0.68**, which is not statistically significant. This suggests that movie ratings do not have a notable impact on profitability for movies primarily earning revenue in the U.S. market.

However, the results were strikingly different for foreign movies. Here, the p-value was **9.6e-09**, which is incredibly small and **statistically significant**. This indicates that the movie rating does indeed affect profitability for films with higher international revenue. In particular, R-rated movies appear to underperform compared to PG-13 or PG films in international markets.

## Reviews 

We took a look at audience and critics reviews of the movies. We hypothesized that perhaps the audience and critic scores of movies influence the international impact of the movie.

<img src="plot_img/audience_score_distribution.png" alt="Audience Scores Distribution" />

Here we can see an approximately normal distribution for both movies with a foreign percentage of revenue higher than 50%, and movies with domestic percentage higher than 50%. The distributions seem to be overlapping and very similar, though the movies that do better internationally seem to be slightly bi-modal between 0.5 and 0.8. On average however, the general public tends to score movies pretty favorably, worldwide.

<img src="plot_img/critics_score_distribution.png" alt="Critics Scores Distribution" />

The same cannot be said for critics scores. While we see the same overlap between the distribution of movies that garner more international or domestic revenue, we do not see the same normal distribution as with the audience score. There is a far more even probability of a movie getting any score within the full range. Again, this is across the board, worldwide. 

What we can conclude from these distributions is that the audience or critics scores do not seem to be correlated with the percentage of foreign revenue of a movie. 

---

# Analysis

---

# Conclusion

"Alright, Hollywood, listen up. Let me tell you, I know success better than anyone, and I'm about to give you some advice-free of charge, because I care, okey?

Hollywood has the tools, talent, and tenacity to bounce back stronger than ever. By focusing on data-driven strategies, embracing innovation, and delivering content that resonates globally, we can ensure that **Made in America** movies once again dominate the box office.

Believe, me Hollywood, nobody knows how to win over an audience like I do. You'll be number one globally in no time. Let’s make it happen—because nobody does it better than Hollywood!"

- Donald J. Trump, champion of women's rights

---