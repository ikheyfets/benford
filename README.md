# Benford's Law
Benford's Law, or the law of first digits is an observation, that the first digits found in a naturally occuring set of numbers will follow a specific distribution.
The formula for the distribution is:

P{d} = ln(1 + 1/d) / ln(10), where d is each individual digit


This very simple and straightforward repository provides code to plot data against theoretical Benford's distribution.
Becasue this project originated during coronavirus, it is only fair to include a scraping tool for Covid-19 data.
Right now, you can scrape new cases, total cases, new deaths and total deaths and compare the data agaisnt the theoretical Benford's curve.
Alternatively, you can pass your own data to count_digits function and see how that compares to theoretical values via plot_distribution function.
