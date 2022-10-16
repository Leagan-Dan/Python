# exercitiul1


def fibonacci(n):
    fibonacci_list = [1]
    if n == 1:
        return fibonacci_list
    fibonacci_list.append(1)
    if n == 2:
        return fibonacci_list
    index = 2
    while index <= n:
        fibonacci_list.append(fibonacci_list[index - 1] + fibonacci_list[index - 2])
        index += 1
    return fibonacci_list


# exercitiul2
def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    index = 2
    while index <= (number / 2):
        if number % index == 0:
            return False
        index += 1
    return True


def prime_numbers(numbers_list):
    prime_list = []
    for number in numbers_list:
        if is_prime(number):
            prime_list.append(number)
    return prime_list


# exercitiul3
def calculate_lists(a, b):
    intersection = set(a).intersection(b)
    union = set(a).union(b)
    a_minus_b = set(a) - set(b)
    b_minus_a = set(b) - set(a)
    return intersection, union, a_minus_b, b_minus_a


# exercitiul4
def compose(notes_list, moves_list, start):
    final_notes = [notes_list[start]]
    current = start
    for move in moves_list:
        current = (current + move) % len(notes_list)
        final_notes.append(notes_list[current])
    return final_notes


# exercitiul5
def replace_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i > j:
                matrix[i][j] = 0
    return matrix


# exercitiul6
def numbers_in_lists(x, *argv):
    appearances = {}
    for arg in argv:
        for element in arg:
            appearances[element] = 0

    for arg in argv:
        for element in arg:
            appearances[element] += 1

    elements_to_return = []
    for element in appearances:
        if appearances[element] == x:
            elements_to_return.append(element)

    return elements_to_return


# exercitiul7
def is_palindrome(number):
    aux_number = number
    reversed_number = 0
    while aux_number != 0:
        last_digit = aux_number % 10
        reversed_number = reversed_number * 10 + last_digit
        aux_number = aux_number // 10
    if number == reversed_number:
        return True
    return False


def palindromes(numbers):
    count = 0
    max_palindrome = 0
    for number in numbers:
        if is_palindrome(number):
            count += 1
            if number > max_palindrome:
                max_palindrome = number
    return count, max_palindrome


# exercitiul 8

def ascii_divisible(x, words, divisible):
    characters_lists = []
    for word in words:
        separate_list = []
        for character in word:
            if divisible:
                if ord(character) % x == 0:
                    separate_list.append(character)
            else:
                if ord(character) % x != 0:
                    separate_list.append(character)
        if separate_list:
            characters_lists.append(separate_list)
    return characters_lists


# exercitiul 9

def find_spectators(seats):
    positions = []
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            if i > 0:
                if seats[i][j] < seats[i - 1][j]:
                    positions.append(tuple((i, j)))
    return positions


# exercitiul 10

def elements_to_tuples(*argv):
    max_len = 0
    index = 0
    tuples = []

    for arg in argv:
        if len(arg) > max_len:
            max_len = len(arg)
        tupple_to_append = ()
        tuples.append(tupple_to_append)

    for arg in argv:
        while len(arg) < max_len:
            arg.append(None)

    while index < max_len:
        for arg in argv:
            tuple_to_add = (arg[index],)
            tuples[index] = tuples[index] + tuple_to_add
        index += 1
    return tuples


# exercitiul 11
def get_3rd(characters_tuple):
    return characters_tuple[1][-1]


def order_tuples(tuples_list):
    tuples_list.sort(key=get_3rd)
    return tuples_list


# exercitiul 12
def group_by_rhyme(words):
    rhymes = []
    for word in words:
        found = False
        if rhymes:
            for placed_words in rhymes:
                for word2 in placed_words:
                    if word[-1] == word2[-1] and word[-2] == word2[-2]:
                        placed_words.append(word)
                        found = True
                        break
            if not found:
                placed_words = [word]
                rhymes.append(placed_words)
        if not rhymes:
            placed_words = [word]
            rhymes.append(placed_words)
    return rhymes


if __name__ == '__main__':
    print("exercitiul1: ", fibonacci(5))
    print("exercitiul2: ", prime_numbers([2, 7, 10, 12, 13]))
    print("exercitiul3: ", calculate_lists([2, 4, 5], [1, 4]))
    print("exercitiul4: ", compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
    print("exercitiul5: ", replace_matrix([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]))
    print("exercitiul6: ", numbers_in_lists(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]))
    print("exercitiul7: ", palindromes([22, 23, 454, 500, 505]))
    print("exercitiul8: ", ascii_divisible(2, ["test", "hello", "lab002"], False))
    print("exercitiul9: ",
          find_spectators([[1, 2, 3, 2, 1, 1], [2, 4, 4, 3, 7, 2], [5, 5, 2, 5, 6, 4], [6, 6, 7, 6, 5]]))
    print("exercitiul10: ", elements_to_tuples([1, 2], [5, 6, 7], ["a", "b", "c"]))
    print("exercitiul11: ", order_tuples([('abc', 'bcd'), ('abc', 'zza')]))
    print("exercitiul12: ", group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))
