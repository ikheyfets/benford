# Example code 

import main, scraping 

data = main.count_digits(scraping.scrape_worldometer('NewCases'))
main.plot_distribution(data)