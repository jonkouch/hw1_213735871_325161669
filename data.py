import pandas


def load_data(path, features):
    df = pandas.read_csv(path)
    data = df.to_dict(orient="list")
    dictionary = {}
    for feature in features:
        dictionary[feature] = data[feature]
    return dictionary


def filter_by_feature(data, feature, values):
    data1 = {}
    data2 = {}
    for index in len(data[feature]):
        if data[feature][index] in values:
            add_values_to_dict(data, data1, index)
        else:
            add_values_to_dict(data, data2, index)
    return data1, data2


def add_values_to_dict(data_from, data_to, index):
    for key in data_from.keys():
        data_to[key][index].append(data_from[key][index])


def print_details(data, features, statistic_functions):
    for feature in features:
        for func in statistic_functions:
            if func == statistic_functions[0]:
                print(f"{feature}: {func(data[feature])},", end="")
            else:
                print(f" {func(data[feature])}", end="")


def print_joint_details(data, features, statistic_functions, statistic_functions_names):
    for func in len(statistic_functions_names):
        for i in len(features):
            for j in len(features):
                if i < j and func == statistic_functions[func]:
                    print(f"{func}({features[i]}, {features[j]}):"
                          f" {statistic_functions[func](data[features[i]],data[features[j]])}")


