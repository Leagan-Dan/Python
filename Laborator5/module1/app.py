import module1.utils

def input_loop():
    while True:
        input1 = input()
        if input1 == "q":
            break
        else:
            number = int(input1)
            print(module1.utils.process_item(number))
