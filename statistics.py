from math import sqrt


def calc_mean(values):
    mean = sum(values)/len(values)
    return mean


def variance(values):
        n = len(values)
        mean = calc_mean(values)
        return sum((x - mean) ** 2 for x in values) / n


def stdv(values):
        var = variance(values)
        std_dev = sqrt(var)
        return std_dev


def calc_covariance(values1, values2):
    mean1 = calc_mean(values1)
    mean2 = calc_mean(values1)
    n=min(len(values1), len(values2))

    return sum((x - mean1) * (y-mean2) for x,y in zip(values1, values2)) / n


def population_statistics(feature_description, data, treatment, target, threshold, is_above,
                          statistic_functions):

