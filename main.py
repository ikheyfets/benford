import scraping
import matplotlib.pyplot as plt
import numpy as np
    
def count_digits(numbers):
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

def plot_distribution(digits):
    theory = [np.log(1+1/x)/np.log(10) for x in range(1, 10)]
    plt.figure()
    plt.bar(range(len(digits)), list(digits.values()), align='center')
    axes = plt.twinx()
    axes.plot(range(len(digits)), theory, color = 'magenta')
    plt.xticks(range(len(digits)), list(digits.keys()))
    plt.show()
