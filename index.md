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

Alright, folks, before the liberal left starts accusing me of **faking the numbers** again, let me set the record straight. We did something **smart**—we **adjusted the data**. Here’s the deal: **Inflation**—it’s a **huge factor**, believe me. If you compare the box office earnings of a **1990 movie** to a **2019 movie**, you're just asking for fake news. It’s a total disaster. So, we did the right thing: we **adjusted** for inflation! 

Now, we’ve got the real facts, folks. It’s not just about making a ton of money—it’s about making **smart money**. And guess what? We’ve done the work to make sure we’re getting the **truth**. We also have taken the log of some of our continuous variables including budget and profitability to make sure no pesky outliers get in the way of a readable clean graph. We’re not letting **inflation** or **outliers** fool us!

## Budget

{% include log_budget.html %}

Look at the data, folks—it's clear as day: **budget** is closely linked to **foreign percentage**. We've got a **Pearson coefficient** of **0.33**, and the **p-value** is **less than 0.05**—that’s statistically significant! This isn’t some fake news, it’s real data, proving that bigger budgets bring in more international success. Simple, folks!

Now, you might’ve already guessed it—more budget means more marketing, more attention, more box office sales. It’s intuitive, right? But here’s the kicker: **foreigners aren’t just watching American movies by default**—we’ve got to **grab their attention**. If we take this information at face value, it’s time to stop playing small and start focusing on the biggest blockbusters that will pull in those huge international numbers. That’s where the money is!

## Genre

{% include genre_proportional.html %}

"Folks, look at the charts, we’ve got some amazing insights here. Comedy, believe me, it’s doing much better in the United States, but look, terrible, terrible results abroad. Why? It’s all about culture, it’s all about language—stuff that’s hard to translate overseas. The jokes just don’t work the same. But you know what does work abroad? Action, drama, and adventure. These are the big ones. You’ve got explosions, you’ve got emotion, you’ve got everything people love—boom, pow, all that good stuff. And that, my friends, crosses borders easily."

{% include genre_percentage.html %}

"Now, let’s get this straight: While drama does well overseas, there are fewer drama movies that are smashing it abroad compared to those that are killing it here in the U.S. So, while people love a good drama, it’s still the action, adventure, and sci-fi movies that are raking in the big bucks on the international stage.

And let's be honest—some genres are just All-American, okay? If we want to make sure we’re attracting foreign audiences, we might want to stay away from teen, indie, and comedy films. Stick to what works, folks. Stick to the winners."

## Month

{% include month_percentage.html%}

As we can see, the movies that do best internationally tend to be released during the holiday season - November and December. We believe that the biggest blockbuster movies tend to be released around that season due to big holiday movie themes - Christmas, Hannukah, etc. These themes are pretty spread internationally, which makes these movies internationally appealing. On the other hand, we see here a missed opportunity to attract foreign audiences during the summer months, specifically August, where the percentage of foreign revenue is smallest. If we market our big summer blockbusters to international audiences, we have the opportunity to make big profits while everyone is on summer vacation.

## Runtime

{% include runtime_plot.html %}

From the runtime box plots we can observe that there is not much difference in the runtime of movies between the classes. The class where the domestic percentage dominates has a median of 103 and the other class, a median of 108. They both contain a similar amount of outliers. It is to note that for the blue class, there is one big outlier: a movie that has a runtime of 222 minutes.

## Ratings

{% include profit_rating_count.html %}

“Alright, here’s the deal. We had to drop the ‘G’ rating, okay? The count was just too low. You can’t make decisions based on bad data—everyone knows that. So we said, let’s focus on what matters, and that’s the ratings with enough data to work with.

We did the Shapiro-Wilk test on the data—believe me, we got the numbers—and guess what? The p-value came back so small it’s practically zero. It’s clear, even when taking the logarithm of the profitability, the data isn’t normal, okay? But we’re smart. We move on to the **Kruskal-Wallis test**, very powerful. It compares the medians to disregard skewed distributions.

Now, for the domestic movies—you know, the ones with more revenue from the good old US of A—we ran the test, and the p-value was **0.68**. That’s huge. It’s not significant at all. What does that mean? The ratings don’t really matter for domestic movies when it comes to profitability. They’re all doing about the same.

But here's the kicker - for the movies that get the overseas money, we got something very, very different. The p-value was **9.6e-09**. That’s incredibly small, folks, and I’m talking **really significant**. This tells us—big time—that the movie rating does matter when it comes to profitability for movies with more international revenue. Big difference, big results, no question about it. The R rating isn't doing as well as PG-13 or PG overseas, folks."

## Reviews 

We took a look at audience and critics reviews of the movies. Perhaps better rated movies fare better internationally?

<img src="plot_img/audience_score_distribution.png" alt="Audience Scores Distribution" />

<img src="plot_img/critics_score_distribution.png" alt="Critics Scores Distribution" />


---

# Analysis

---

# Conclusion

Alright, Hollywood, listen up. Let me tell you, I know success better than anyone, and I'm about to give you some advice-free of charge, because I care, okey?

Hollywood has the tools, talent, and tenacity to bounce back stronger than ever. By focusing on data-driven strategies, embracing innovation, and delivering content that resonates globally, we can ensure that **Made in America** movies once again dominate the box office.

Believe, me Hollywood, nobody knows how to win over an audience like I do. You'll be number one globally in no time. Let’s make it happen—because nobody does it better than Hollywood!

---