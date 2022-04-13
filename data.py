import pandas


def load_data(path, features):
    df = pandas.read_csv(path)
    data = df.to_dict(orient="list")
    return {feature: data[feature] for feature in features}


def filter_by_feature(data, feature, values):
    data1 = {}
    data2 = {}
    for index, val in enumerate(data[feature]):
        if val in values:
            add_row_to_dict(data, data1, index)
        else:
            add_row_to_dict(data, data2, index)
    return data1, data2


def add_row_to_dict(data_from, data_to, index):
    for key in data_from:
        if key not in data_to:
            data_to[key] = list()
        data_to[key].append(data_from[key][index])


def print_details(data, features, statistic_functions):
    for feature in features:
        for i, func in enumerate(statistic_functions):
            if i == 0:
                print(f"{feature}: {func(data[feature]):.2f},", end="")
            else:
                print(f" {func(data[feature]):.2f}", end="")
        print('')


def print_joint_details(data, features, statistic_functions, statistic_functions_names):
    for i, func in enumerate(statistic_functions):
        print(f"{statistic_functions_names[i]}({features[0]}, {features[1]}): "
              f"{func(data[features[0]], data[features[1]]):.2f}")
