def exercitiul1(a, b):
    intersection = set(a).intersection(b)
    union = set(a).union(b)
    a_minus_b = set(a) - set(b)
    b_minus_a = set(b) - set(a)
    aux = [intersection, union, a_minus_b, b_minus_a]
    return aux


def exercitiul2(text):
    letters = {}
    for character in text:
            if character in letters:
                letters[character] += 1
            else:
                letters[character] = 1
    return letters


def exercitiul3(dict1, dict2):
    if len(dict1) != len(dict2):
        return False

    for key in dict1:
        if type(dict1[key]) is dict and type(dict2[key]) is dict:
            if not exercitiul3(dict1[key],dict2[key]):
                return False
        if dict1[key] != dict2[key]:
            return False
    return True


def exercitiul4(tag, content, **pairs):
    link = "<" + tag + " "
    for key, value in pairs.items():
        link = link + key + "=\\\"" + value + "\\\""
    link = link + ">" + content + "<" + tag + ">\""
    return link


def exercitiul5(rules, dictionary):
    for key in dictionary:
        text = dictionary[key]
        rule_key = None
        for rule in rules:
            if key == rule[0]:
                rule_key = rule[0]
                break

        if rule_key is None:
            return False
        found_prefix = False
        found_middle = False
        found_suffix = False

        if rule[1] == "":
            found_prefix = True
        else:
            if rule[1] in text:
                x = text.find(rule[1])
                text = text[x + len(rule[1]):]
                found_prefix = True

        if rule[2] == "":
            found_middle = True
        else:
            if rule[2] in text:
                x = text.find(rule[2])
                text = text[x + len(rule[2]):]
                found_middle = True

        if rule[3] == "":
            found_suffix = True
        else:
            if rule[3] in text:
                x = text.find(rule[3])
                text = text[x + len(rule[3]):]
                found_suffix = True

        if not found_prefix or not found_middle or not found_suffix:
            return False
    return True


def exercitiul6(elements):
    unique = set(elements)

    seen = set()
    dupes = []

    for x in elements:
        if x in seen:
            dupes.append(x)
        else:
            seen.add(x)

    return len(unique), len(dupes)


def exercitiul7(*pairs):
    operations = {}
    for a in pairs:
        for b in pairs:
            if a != b:
                list_of_strings = [str(s) for s in a]
                string_a = " ".join(list_of_strings)
                string_a = "{" + string_a + "}"
                list_of_strings = [str(s) for s in b]
                string_b = " ".join(list_of_strings)
                string_b = "{" + string_b + "}"

                if string_b + " | " + string_a not in operations:
                    operations[string_a + " | " + string_b] = set(a).union(b)
                if string_b + " & " + string_a not in operations:
                    operations[string_a + " & " + string_b] = set(a).intersection(b)
                if string_a + " - " + string_b not in operations:
                    operations[string_a + " - " + string_b] = set(a) - set(b)
                if string_b + " - " + string_a not in operations:
                    operations[string_b + " - " + string_a] = set(b) - set(a)

    return operations


def exercitiul8(mapping):
    current = "start"
    visited = []
    iterations = []
    visited.append(current)
    while mapping[current] not in visited:
        iterations.append(mapping[current])
        visited.append(mapping[current])
        current = mapping[current]
    return iterations


def exercitiul9(*positions, **keywords):
    count = 0
    for position in positions:
        for key, value in keywords.items():
            if position == value:
                count += 1
                break
    return count


if __name__ == '__main__':
    print("exercitiul:1 ", exercitiul1([3, 4, 5], [2, 3, 4]))
    print("exercitiul:2 ", exercitiul2("Ana has apples."))
    print("exercitiul:3 ", exercitiul3({'number': 1, 'list': [2, 3]}, {'number': 1, 'list': [2, 4]}))
    print("exercitiul:4 ", exercitiul4("a", "Hello there", href="http://python.org", _class="my-link", id="someid"))
    print("exercitiul:5 ", exercitiul5({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
                                       {"key1": "come inside, it's too cold out", "key3": "this is not valid"}))
    print("exercitiul:6 ", exercitiul6([2, 2, 3, 4, 5, 6, 6, 8]))
    print("exercitiul:7 ", exercitiul7({1, 2}, {2, 3}))
    print("exercitiul:8 ",
          exercitiul8({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
    print("exercitiul:9 ", exercitiul9(1, 2, 3, 4, x=1, y=2, z=3, w=5))
