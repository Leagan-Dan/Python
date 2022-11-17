import os
import re


def exercitiul1(text):
    return re.findall("\w+", text)


def exercitiul2(regex, text, x):
    found_substrings = []
    found = re.search(regex, text)
    if found:
        for i in range(0, found.lastindex + 1):
            if len(found.group(i)) == x:
                found_substrings.append(found.group(i))
    return found_substrings

def exercitiul3(regexes, texts):
    found_substrings=[]
    for text in texts:
        for regex in regexes:
            r=re.compile(regex)
            if r.match(text):
                found_substrings.append(text)
                break

    return found_substrings

def exercitiul6(text):
    result=re.findall("[aeiou][\w]+[aeiou]",text)
    print(result)


def exercitiul7(text):
    regex="[12345678]\d\d(0\d|1[0-2])(0[1-9]|[12]\d|3[01])\d{6}$"
    result=re.compile(regex)
    if re.match(result,text):
        return True
    return False

def exercitiul8(directory, regex):
    list_of_files=[]
    for dir, dirs, files in os.walk(directory):
        path = dir.split('/')
        for f in files:
            if(re.match(regex,f)):
                list_of_files.append(f)
            else:
                open_file=open(dir+"\\"+f,mode='r')
                text=open_file.read()
                if re.match(regex, text):
                    list_of_files.append(f)
                open_file.close()
    return list_of_files


if __name__ == '__main__':
    print(exercitiul1("abcd13&**ancd!"))
    print(exercitiul2("(\d+)[^\d]*(\d+)", "Price is 123 USD aprox 110 EUR", 3))
    print(exercitiul3(["07[0-5]{3}","07[0-4]{1}"],["07123","077"]))
    print(exercitiul6("ana are mere"))
    print(exercitiul7("5050515222222"))
    print(exercitiul8("D:\git\Python\Laborator6\directory_ex8","^\w.*\d"))