import numbers

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
    list1 = [(lambda c: c if (c.lower() in vocals) else None)(c) for c in text]
    aux_list1 = list1.copy()
    for element in aux_list1:
        if not element:
            list1.remove(element)
    return list1


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
    newlist=[]
    for element in list1:
        if isinstance(element,numbers.Number):
            newlist.append(element)
    return newlist

if __name__ == '__main__':
    # module1.utils.exercitiul1a()
    # module1.app.input_loop()
    print(exercitiul2_function(1, 2, c=3, d=4))
    print(exercitiul2_lambda(1, 2, c=3, d=4))
    print(exercitul3_method1("Programming in Python is fun"))
    print(exercitiul3_method2("Programming in Python is fun"))
    print(exercitiul3_method3("Programming in Python is fun"))
    print(exercitiul4({1: 2, 3: 4, 5: 6}, {'a': 5, 'b': 7, 'c': 'e'}, {2: 3}, [1, 2, 3], {'abc': 4, 'def': 5}, 3764,
                      dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'}, test={1: 1, 'test': True}))
    print(exercitiul5([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))
