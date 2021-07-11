# Example code 

import benford_plot, scraping

data = benford_plot.count_digits(scraping.scrape_worldometer('NewCases'))
benford_plot.plot_distribution(data)