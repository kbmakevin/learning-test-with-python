def hello_world():
    return 'hello world'


def create_num_list(length):
    return [x for x in range(length)]


def custom_func_x(x, power, const):
    return x**power * const


def custom_non_lin_num_list(length, const, power):
    return [custom_func_x(x, power, const) for x in range(length)]


def multi_return_func(string_a, string_b):
    return len(string_a), string_a == string_b
