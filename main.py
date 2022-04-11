import sys
import statistics
import data


def main(argv):
    features = {"hum", "t1", "cnt"}
    categories = {"Summer", "Holiday", "All"}
    season = {0, 1, 2, 3}
    is_holiday = {0, 1}
    statistic_functions = {statistics.calc_mean(), statistics.variance(),
                           statistics.stdv(), statistics.calc_covariance()}
    statistic_functions_names = {"Cov"}
    print("Question 1:")
    data_src = data.load_data(path, features)
    for category in categories:
        print(f"{category}:")
        data1, data2 = data.filter_by_feature(data_src, season, {1})
        data.print_details(data1, features, statistic_functions)







if __name__ == '__main__':
    main(sys.argv)
