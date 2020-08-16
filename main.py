# Scrape data from worldometer
import requests
import pandas as pd

def get_worldometer(column):
    url = 'https://www.worldometers.info/coronavirus/country/us'
    cases = []
    r = requests.get(url)
    dfs = pd.read_html(r.text)
    for i in range(1,len(dfs[1])-12):
        # key = dfs[1].get('USAState').get(i)
        value = dfs[1].get(column).get(i)
        #print(value)
        if 'New' in column:
            if isinstance(value, str) == True:    
                value = value.replace('+','')
                value = value.replace(',','')
                cases.append(value)
        else:
            cases.append(str(value))
    return cases

# def get_Benfordness(numbers):
# Too many compairsons
#     digits = {}
#     for i in range(1,10):
#         digits.update({i:0})
    
#     for i in range(len(numbers)):
#         first = numbers[i][0]
#         for k, v in digits.items():
#             if first == str(k):
#                 v = v + 1
#                 digits.update({k:v})
#     return digits

def get_Benfordness(numbers):
    # Algorithmically correct
    digits = {}
    for i in range(1,10):
        digits.update({i:0})
    for k, v in digits.items():
        i = 0
        while i != len(numbers):
            if numbers[i][0] == str(k):
                v += 1
                numbers.pop(i)
            else:
                i += 1
        digits.update({k:v})
    return digits

numbers = get_worldometer('TotalDeaths')
digits = get_Benfordness(numbers)

import matplotlib.pyplot as plt

plt.bar(range(len(digits)), list(digits.values()), align='center')
plt.xticks(range(len(digits)), list(digits.keys()))

plt.show()
