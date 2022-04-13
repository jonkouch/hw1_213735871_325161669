from math import sqrt
from data import add_row_to_dict


def calc_mean(values):
    return sum(values)/len(values)


def variance(values):
        n = len(values)
        mean = calc_mean(values)
        return sum((x - mean) ** 2 for x in values) / (n-1)


def calc_stdv(values):
        var = variance(values)
        std_dev = sqrt(var)
        return std_dev


def calc_covariance(values1, values2):
    mean1 = calc_mean(values1)
    mean2 = calc_mean(values1)
    n = min(len(values1), len(values2))-1
    return sum((x - mean1) * (y-mean2) for x, y in zip(values1, values2)) / n


def population_statistics(feature_description, data, treatment, target,
                          threshold, is_above, statistic_functions):
    print(f"{feature_description}:")
    data1 = {}
    for index, val in enumerate(data[treatment]):
        if val > threshold and is_above:
            add_row_to_dict(data, data1, index)
        if val <= threshold and not is_above:
            add_row_to_dict(data, data1, index)
    print(f"{target}: ", end='')
    for i, func in enumerate(statistic_functions):
        if i < len(statistic_functions)-1:
            print(f"{func(data[target]):.2f}, ", end='')
        else:
            print(f"{func(data[target]):.2f}")


