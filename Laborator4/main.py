import os.path
from os import listdir


def exercitiul1(director):
    files = [file for file in listdir(director)]
    extensions = []
    for file in files:
        file_path = director + file
        file_name, file_extension = os.path.splitext(file_path)
        extensions.append(file_extension)
    extensions.sort()
    return extensions


def exercitiul2(director, fisier):
    f = open(fisier, "w")
    files = [file for file in listdir(director)]
    for file in files:
        if file[0] == 'A':
            f.write(file + "\n")
    f.close()

    f = open(fisier, "r")
    text = f.readlines()
    f.close()
    return text


def exercitiul3(my_path):
    if os.path.isfile(my_path):
        f = open(my_path, "r")
        text_list = f.readlines()
        f.close()
        text = ""
        for element in text_list:
            text += element
        return text[-20:]
    else:
        files = [file for file in listdir(my_path)]
        extensions_count = {}
        for file in files:
            if os.path.isdir(file):
                print(file)
            else:
                file_path = my_path + file
                file_name, file_extension = os.path.splitext(file_path)
                if file_extension not in extensions_count:
                    extensions_count[file_extension] = 1
                else:
                    extensions_count[file_extension] += 1
        extensions_count = dict(sorted(extensions_count.items(), key=lambda item: item[1], reverse=True))
        touples = []
        for key in extensions_count:
            touples.append((key, extensions_count[key]))
        return touples


def exercitiul4():
    path = input()
    files = [file for file in listdir(path)]
    extensions = []
    for file in files:
        file_path = path + file
        file_name, file_extension = os.path.splitext(file_path)
        if file_extension != "":
            extensions.append(file_extension)
    extensions.sort()
    return extensions


def exercitiul5(target, to_search):
    found_files = []
    if os.path.isfile(target):
        file = open(target, "r")
        text_list = file.readlines()
        text = ""
        for element in text_list:
            text += element
        if to_search in text:
            found_files.append(file.name)
        file.close()
    elif os.path.isdir(target):
        files = [file for file in listdir(target)]
        for file1 in files:
            text_list = exercitiul5(target + "\\" + file1, to_search)
            if text_list:
                found_file = ""
                for element in text_list:
                    found_file += element
                found_files.append(found_file)
    else:
        raise ValueError(target + ' isn\'t a file of a directory')
    return found_files


def callback(error_instance):
    error = None
    if error_instance == IOError:
        error = "Could not open the file"
    elif error_instance == ValueError:
        error = "The input isn't a file or a directory"
    return error


def exercitiul6(target, to_search):
    found_files = []
    opened=False
    if os.path.isfile(target):
        file = open(target, "r")
        if file:
            opened = True
        text_list = file.readlines()
        if not opened:
            raise IOError(callback(IOError))
        text = ""
        for element in text_list:
            text += element
        if to_search in text:
            found_files.append(file.name)
        file.close()
    elif os.path.isdir(target):
        files = [file for file in listdir(target)]
        for file1 in files:
            text_list = exercitiul6(target + "\\" + file1, to_search)
            if text_list:
                found_file = ""
                for element in text_list:
                    found_file += element
                found_files.append(found_file)
    else:
        raise ValueError(callback(ValueError)) from Exception
    return found_files


def exercitiul7(path):
    info = {}
    info["full_path"] = os.path.abspath(path)
    info["file_size"] = os.path.getsize(path)
    file_name, file_extension = os.path.splitext(path)
    if file_extension:
        info["extension"] = file_extension
    else:
        info["extension"] = ""

    file = open(path, "r")
    info["can_read"] = file.readable()
    file.close()

    file = open(path, "w")
    info["can_write"] = file.writable()
    file.close()
    return info


def exercitiul8(dir_path):
    paths = []
    for file_name in os.listdir(dir_path):
        file = os.path.join(dir_path, file_name)
        if os.path.isfile(file):
            paths.append(file)
    return paths


if __name__ == '__main__':
    print(exercitiul1("D:\git\Python\Laborator4\director_exercitiul1"))
    print(exercitiul2("D:\git\Python\Laborator4\director_exercitiul2",
                      "D:\git\Python\Laborator4\director_exercitiul2\\fisier_exercitiul2.txt"))
    print(exercitiul3("D:\git\Python\Laborator4\\fisier_exercitiul3.txt"))
    print(exercitiul3("D:\git\Python\Laborator4\director_exercitiul3"))
    print(exercitiul4())
    print(exercitiul5("D:\git\Python\Laborator4\\fisier_exercitiul5.txt", "search"))
    print(exercitiul5("D:\git\Python\Laborator4\director_exercitiul5", "search"))
    print(exercitiul5("a","search"))
    print(exercitiul6("D:\git\Python\Laborator4\\fisier_exercitiul5.txt", "search"))
    print(exercitiul6("D:\git\Python\Laborator4\director_exercitiul5", "search"))
    print(exercitiul6("a", "search"))
    print(exercitiul7("D:\git\Python\Laborator4\\fisier_exercitiul7.txt"))
    print(exercitiul8("D:\\git\Python\\Laborator4\\director_exercitiul8"))
