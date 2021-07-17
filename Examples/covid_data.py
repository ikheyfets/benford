# This example takes data from the following dataset:
# https://www.kaggle.com/imdevskp/corona-virus-report
# I am using dailyActivity_merged.csv file

# Variables checked in this example are:
    # Confirmed cases
    # Active cases
    # Deaths


from benford_plot import *
import pandas


covid_df = pandas.read_csv('Datasets/full_grouped.csv')

countries = ['US']
v = ['Confirmed', 'Active', 'Deaths']
for country in countries:
    country_df = covid_df[covid_df['Country/Region'] == country]
    for variable in v:
        data = country_df[variable]
        digits = count_digits(extract_digits(data))
        plot_distribution(digits, variable, png=True, dir='COVID_graphs/US')
