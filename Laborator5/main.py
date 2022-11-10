import numbers
import module1.utils
import module1.app

def exercitiul2_function(*args, **kwargs):
    sum1 = 0
    for arg in args:
        nr = int(arg)
        sum1 += nr

    for arg in kwargs:
        nr = int(kwargs[arg])
        sum1 += nr

    return sum1


exercitiul2_lambda = lambda *args, **kwargs: sum(args) + sum(kwargs.values())


def exercitul3_method1(text):
    newlist = []
    for c in text:
        if c.lower() in ('a', 'e', 'i', 'o', 'u'):
            newlist.append(c)
    return newlist


def exercitiul3_method2(text):
    newlist = [c for c in text if c in ('a', 'e', 'i', 'o', 'u')]
    return newlist


def exercitiul3_method3(text):
    vocals = ['a', 'e', 'i', 'o', 'u']
    return list(filter(lambda c: c.lower() in vocals, text))


def exercitiul4(*args, **kwargs):
    newlist = []

    for arg in args:
        string_key_min3 = False
        if type(arg) == dict:
            is_dictionary = True
            nr_keys = len(arg.keys())
            for key in arg.keys():
                if type(key) == str and len(key) >= 3:
                    string_key_min3 = True
            if is_dictionary and nr_keys >= 2 and string_key_min3:
                newlist.append(arg)

    for arg in kwargs.values():
        string_key_min3 = False
        if type(arg) == dict:
            is_dictionary = True
            nr_keys = len(arg.keys())
            for key in arg.keys():
                if type(key) == str and len(key) >= 3:
                    string_key_min3 = True
            if is_dictionary and nr_keys >= 2 and string_key_min3:
                newlist.append(arg)

    return newlist


def exercitiul5(list1):
    newlist = []
    for element in list1:
        if isinstance(element, numbers.Number):
            newlist.append(element)
    return newlist


def exercitiul6(numbers):
    odds = list(filter(lambda x: (x % 2 == 0), numbers))
    evens = list(filter(lambda x: (x % 2 == 1), numbers))
    return list(map(lambda odd, even: (odd, even), odds, evens))


def exercitiul7(**kwargs):
    limit = 1000

    fib_list1 = [0, 1]
    [fib_list1.append(fib_list1[k - 1] + fib_list1[k - 2]) for k in range(2, 1000)]

    fib_list = []
    if "filters" in kwargs.keys():
        [fib_list.append(fib_list1[k]) for k in range(0, len(fib_list1)) if eval(kwargs["filters"])]
    else:
        [fib_list.append(fib_list1[k]) for k in range(0, len(fib_list1))]

    if "offset" in kwargs.keys():
        fib_list = fib_list[kwargs["offset"]:]
    if "limit" in kwargs.keys():
        fib_list = fib_list[:kwargs["limit"]]
    return fib_list


def multiply_by_two(x):
    return x * 2


def add_numbers(a, b):
    return a + b


def print_arguments(function):
    def function1(*args, **kwargs):
        print(args, kwargs)
        return function(*args, **kwargs)

    return function1


def multiply_by_three(x):
    return x * 3


def exercitiul8a():
    augmented_multiply_by_two = print_arguments(multiply_by_two)
    x = augmented_multiply_by_two(10)
    print(x)
    augmented_add_numbers = print_arguments(add_numbers)
    x = augmented_add_numbers(3, 4)
    print(x)


def multiply_output(function):
    def function2(x):
        return 2 * function(x)

    return function2


def exercitiul8b():
    augmented_multiply_by_three = multiply_output(multiply_by_three)
    x = augmented_multiply_by_three(10)
    print(x)


def augment_function(function, list_of_functions):
    def function3(a, b):
        aux = function
        for function_parameter in list_of_functions:
            aux=function_parameter(aux)
        return aux

    return function3


def exercitiul8c():
    decorated_function = augment_function(add_numbers, [print_arguments, multiply_output])
    x = decorated_function(3, 4)
    print(x)


def exercitiul9(**kwargs):
    pairs = kwargs.values()
    for value in kwargs.values():
        pairs = value

    newlist = []
    [newlist.append({"sum": k[0] + k[1], "prod": k[0] * k[1], "pow": k[0] ** k[1]}) for k in pairs]
    return newlist


if __name__ == '__main__':
    module1.utils.exercitiul1a()
    module1.app.input_loop()
    print(exercitiul2_function(1, 2, c=3, d=4))
    print(exercitiul2_lambda(1, 2, c=3, d=4))
    print(exercitul3_method1("Programming in Python is fun"))
    print(exercitiul3_method2("Programming in Python is fun"))
    print(exercitiul3_method3("Programming in Python is fun"))
    print(exercitiul4({1: 2, 3: 4, 5: 6}, {'a': 5, 'b': 7, 'c': 'e'}, {2: 3}, [1, 2, 3], {'abc': 4, 'def': 5}, 3764,
                      dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'}, test={1: 1, 'test': True}))
    print(exercitiul5([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))
    print(exercitiul6([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))
    print(exercitiul7(filters="lambda item: item % 2 == 0", offset=10, limit=2))
    exercitiul8a()
    exercitiul8b()
    #exercitiul8c()
    print(exercitiul9(pairs=[(5, 2), (19, 1), (30, 6), (2, 2)]))
