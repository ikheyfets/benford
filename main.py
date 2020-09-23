import requests
import pandas as pd
import matplotlib.pyplot as plt

class Benford:
    def __init__(self):
        self.data = []
        self.digits = {}



    # Scrape data from worldometer
    '''
    Column can take the following values:
        NewCases
        TotalCases
        NewDeaths
        TotalDeaths
    '''
    def scrape_worldometer(self, column):
        
        url = 'https://www.worldometers.info/coronavirus/country/us'
        r = requests.get(url)
        dfs = pd.read_html(r.text)

        for i in range(1,len(dfs[1])-12):
            value = dfs[1].get(column).get(i)
            if 'New' in column:
                if isinstance(value, str) == True:    
                    value = value.replace('+','')
                    value = value.replace(',','')
                    self.data.append(value)
            else:
                self.data.append(str(value))


    
    def count_digits(numbers):
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
    
    def plot_distribution(digits):
        plt.bar(range(len(digits)), list(digits.values()), align='center')
        plt.xticks(range(len(digits)), list(digits.keys()))
        plt.show()
