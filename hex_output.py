def hex_output():
    decnum = 0
    hexnum = input(
        'Ввведите шестнадцатеричное число для преобразования:'
        )
    for power, digit in enumerate(reversed(hexnum)):
        decnum += int(digit, 16) * (16 ** power)
    print(decnum)


# hex_output()

def hex_output2():
    decnum = 0
    hexnum = input(
        'Ввведите шестнадцатеричное число для преобразования:'
        )
    for power, digit in enumerate(reversed(hexnum)):
        if '0' <= digit <= '9':
            value = ord(digit) - ord('0')
        elif 'A' <= digit <= 'F':
            value = ord(digit) - ord('A') + 10
        elif 'a' <= digit <= 'f':
            value = ord(digit) - ord('a') + 10
        else:
            continue
        decnum += value * (16 ** power)
    print(decnum)


# hex_output2()


def whats_your_name():
    name = input('Введите ваше имя: ')
    for number, sumbol in enumerate(name):
        print(name[:number])
    print(name)


# whats_your_name()
