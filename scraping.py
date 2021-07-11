import requests
import pandas as pd


def scrape_worldometer(column):
    """
    Parameters
    ----------
    column : string: NewCases, TotalCases, NewDeaths, TotalDeaths
        Please select on of the column names to retrieve data from.

    Returns
    -------
    data : list
    List of datapoints from the column specified.
    """
    data = []
    url = 'https://www.worldometers.info/coronavirus/country/us'
    r = requests.get(url)
    dfs = pd.read_html(r.text)

    for i in range(1, len(dfs[1])-12):
        value = dfs[1].get(column).get(i)
        if 'New' in column:
            if isinstance(value, str):
                value = value.replace('+', '')
                value = value.replace(',', '')
                data.append(value)
        else:
            data.append(str(value))
    return data
