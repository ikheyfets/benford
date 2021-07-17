# Benford's Law
Benford's Law, or the law of first digits is an observation, that the first digits found in a naturally occuring set of numbers will follow a specific distribution.
The formula for the distribution is:

P{d} = ln(1 + 1/d) / ln(10), where d is each individual digit


This very simple and straightforward repository provides code to plot data against theoretical Benford's distribution.

I also included examples by checking different data against Benford's distribution. 
  - FitBit data (Steps, Distance, Calories), source: https://www.kaggle.com/arashnic/fitbit
  - Covid-19 data (US confirmed cases, Active cases, Deaths), source: https://www.kaggle.com/imdevskp/corona-virus-report
