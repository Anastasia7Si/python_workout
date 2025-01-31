def run_timing():
    count = 0
    sum = 0
    while True:
        enter = input('Введите время (в мин) пробега 10 км: ')
        if enter:
            count += 1
            sum += int(enter)
        else:
            result = sum / count
            print(f'Средний показатель {result:.2f}, более {count} пробежек')
            break


# run_timing()


def format_print(fl, before, after):
    integer_part, decimal_part = str(fl).split('.')
    print(f'{integer_part[:before]}.{decimal_part[:after]}')


format_print(1872.743, 2, 1)
