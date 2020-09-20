import requests
import pandas as pd
import matplotlib.pyplot as plt

column = "NewCases"

url = 'https://www.worldometers.info/coronavirus/country/us'
cases = []
r = requests.get(url)
dfs = pd.read_html(r.text)
print(dfs)
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
