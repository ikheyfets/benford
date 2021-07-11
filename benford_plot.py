import matplotlib.pyplot as plt
import numpy as np
import re

# Workflow
# ---------
# Extract digits from list, string or any datatype (v)
# Count digits (v)
# Plot distribution (v)

# Examples
# ---------
# Covid Folder
# Meteorite dataset folder
# US average weight/salary/whatever


def extract_digits(data):
    """
    Parameters
    ----------
    data: can be a list, a string or any dataa type

    Returns
    -------
    digits: a list of integers contained in data input
    """
    digits = []
    for element in data:
        if not isinstance(element, str):
            element = str(element)
        element = re.sub("\D", "", element)
        for i in range(len(element)):
            if element[i] != '0':
                digits.append(int(element[i]))
    return digits


def count_digits(numbers):
    """
    Parameters
    ----------
    numbers: list of integers

    Returns
    -------
    a dictionary with key being a digit and value representing how many times that digit occurs
    """
    digit_count = {}
    for i in range(1, 10):
        digit_count.update({i: 0})
    while len(numbers) > 0:
        for key, value in digit_count.items():
            if numbers[0] == key:
                value += 1
                numbers.pop(0)
                digit_count.update({key: value})
                break
    return digit_count


def plot_distribution(digits, name: str):
    # Reworking
    theory = [np.log(1+1/x)/np.log(10)*sum(digits.values()) for x in range(1, 10)]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.bar(range(len(digits)), list(digits.values()), align='center', label=name)
    ax.plot(range(len(digits)), theory, color='magenta', label='Theoretical Benford Distribution')
    ax.set_ylabel(f'Frequency of digits in {name}')
    plt.xticks(range(len(digits)), list(digits.keys()))
    ax.set_xlabel('Digits')
    ax.legend(loc=0)
    plt.show()
