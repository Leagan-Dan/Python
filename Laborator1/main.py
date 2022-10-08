import string


# exercitiul1
def cmmdc_many_numbers(numbers):
    cmmdc = numbers[0]
    for number in numbers:
        cmmdc = cmmdc_2_numbers(cmmdc, number)
    return cmmdc


def cmmdc_2_numbers(number1, number2):
    while number2 != 0:
        rest = number1 % number2
        number1 = number2
        number2 = rest
    return number1


# exercitiul2
def vowels(my_string):
    total_vowels = 0
    for vowel in "aeiouAEIOU":
        count = my_string.count(vowel)
        total_vowels = total_vowels + count
    return total_vowels


# exercitiul3
def occurences(string1, string2):
    return string2.count(string1)


# exercitiul4
def camel_to_snake(message):
    message2 = ""
    for letter in message:
        if letter.islower():
            message2 = message2 + letter
        else:
            message2 = message2 + "_" + letter.lower()
    if message2[0] == '_':
        message2 = message2[1:]
    return message2


# exercitiul5
def spiral_matrix():
    matrix = [['f', 'i', 'r', 's'],
              ['n', '_', 'l', 't'],
              ['0', 'b', 'a', '_'],
              ['h', 't', 'y', 'p']]

    answer = ""
    seen = [[0 for i in range(4)] for j in range(4)]
    direction_row = [0, 1, 0, -1]
    direction_collumn = [1, 0, -1, 0]
    x = 0
    y = 0
    direction = 0

    for i in range(4 * 4):
        answer = answer + matrix[x][y]
        seen[x][y] = True
        candidate_row = x + direction_row[direction]
        candidate_collumn = y + direction_collumn[direction]

        if (0 <= candidate_row < 4 and 0 <= candidate_collumn < 4 and not (
                seen[candidate_row][candidate_collumn])):
            x = candidate_row
            y = candidate_collumn
        else:
            direction = (direction + 1) % 4
            x += direction_row[direction]
            y += direction_collumn[direction]

    return answer


# exercitiul6
def is_palindrom(number):
    aux = number
    reverse = 0
    while aux > 0:
        digit = aux % 10
        reverse = reverse * 10 + digit
        aux = aux // 10
    if number == reverse:
        return "palindrom"
    else:
        return "not palindrom"


# exercitiul7
def extract_number(message):
    search_number = False
    number = 0
    for letter in message:
        if search_number == True and letter.isdigit() == 0:
            return number
        if letter.isdigit():
            search_number = True
            number = number * 10 + ord(letter) - 48
    return number


# exercitiul8
def number_of_1_binary(number):
    binary = bin(number)
    count = 0
    for digit in binary:
        if digit == '1':
            count = count + 1
    return count


# exercitiul9
def most_common_letter(message):
    message = message.lower()
    dictionary = {}
    max_letter = ""
    max = 0
    alphabet = string.ascii_letters
    for letter in alphabet:
        dictionary[letter] = 0
    for letter in message:
        if letter.isalpha():
            dictionary[letter] += 1
            if dictionary[letter] > max:
                max = dictionary[letter]
                max_letter = letter
    answer = max_letter + ", " + str(max)
    return answer


# exercitiul10
def how_many_words(text):
    count = 0
    for character in text:
        if character == ' ':
            count += 1
    return count + 1


if __name__ == '__main__':
    print("exercitiul1:", cmmdc_many_numbers([25,15,55]))
    print("exercitiul2:", vowels("cuvant"))
    print("exercitiul3:", occurences("are", "arenareare"))
    print("exercitiul4:", camel_to_snake("CamelCase"))
    print("exercitiul5:", spiral_matrix())
    print("exercitiul6:", is_palindrom(434))
    print("exercitiul7:", extract_number("abc123cd58e"))
    print("exercitiul8:", number_of_1_binary(24))
    print("exercitiul9:", most_common_letter("Buna ziua"))
    print("exercitiul10:", how_many_words("I have Python exam"))
