import sys
import statistics
import data


def q2(dict):
    data1, data2 = data.filter_by_feature(dict, "season", {3})
    data1, data2 = data.filter_by_feature(data1, "is_holiday", {1})
    print("Question 2:")
    print("If t1<=13.0, then:")
    statistics.population_statistics("Winter Holiday records", data1,
                                     "t1", "cnt", 13, False,
                                     [statistics.calc_mean, statistics.calc_stdv])
    statistics.population_statistics("Winter weekday records:", data2, "t1", "cnt", 13, False,
                                     [statistics.calc_mean, statistics.calc_stdv])
    print("If t1>13.0, then:")
    statistics.population_statistics("Winter Holiday records", data1,
                                     "t1", "cnt", 13, True,
                                     [statistics.calc_mean, statistics.calc_stdv])
    statistics.population_statistics("Winter weekday records:", data2, "t1", "cnt", 13, True,
                                     [statistics.calc_mean, statistics.calc_stdv])


def q1(dict):
    print("Question 1:")
    features = ['hum', 't1', 'cnt']
    functions = [statistics.calc_mean, statistics.calc_stdv]
    samples = {"Summer:": ["season", {1}], "Holiday:": ["is_holiday", {1}], "All:": None}
    for sample, flt in samples.items():
        data1 = dict
        print(sample)
        if flt is not None:
            data1, data2 = data.filter_by_feature(dict, flt[0], flt[1])
        data.print_details(data1, features, functions)
        data.print_joint_details(data1, ['t1', 'cnt'], [statistics.calc_covariance], ["Cov"])


def main(argv):
    path = "/Users/eyaltadmor/Documents/intro_to_data_science/hw1/london_sample.csv"
    dict = data.load_data(path, {"hum", "t1", "cnt", "season", "is_holiday"})
    q1(dict)
    print("")
    q2(dict)


if __name__ == '__main__':
    main(sys.argv)
