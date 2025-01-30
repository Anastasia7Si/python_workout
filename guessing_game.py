from random import randint


def to_base(n, base):
    if n == 0:
        return 0
    digits = []
    while n:
        digits.append(n % base)
        n //= base
    print(''.join(str(x) if x < 10 else chr(x - 10 + ord('A'))
                  for x in reversed(digits)))


def guessing_game():
    random_number = randint(0, 100)
    while True:
        input_number = int(input('Введите число: '))
        if input_number == random_number:
            print('Вы угадали!')
            break

        if input_number > random_number:
            print('Число слишком большое!')
        else:
            print('Число слишком маленькое!')


def guessing_game2():
    dic = {1: 'apple',
           2: 'beer',
           3: 'coca-cola',
           4: 'energy drink',
           5: 'fastfood'}
    random_word = dic[randint(1, 5)]
    while True:
        input_word = input('Введите слово: ')
        if input_word == random_word:
            print('Вы угадали!')
            break
        else:
            print('Выберите другое слово!')


# guessing_game2()
# # guessing_game()

input_number = int(input('Введите число: '))
input_base = int(input('Введите систему счисления: '))
to_base(input_number, input_base)
