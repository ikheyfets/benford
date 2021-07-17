# This example takes data from the following dataset:
# https://www.kaggle.com/arashnic/fitbit
# I am using dailyActivity_merged.csv file

# Variables checked in this example are:
    # Total Steps
    # Total Distance
    # Calories

from benford_plot import *
import pandas

fitbit_df = pandas.read_csv('Datasets/dailyActivity_merged.csv')

v = ['TotalSteps', 'TotalDistance', 'Calories']
for variable in v:
    data = fitbit_df[variable]
    digits = count_digits(extract_digits(data))
    plot_distribution(digits, variable, png=True, dir='FitBit_graphs')