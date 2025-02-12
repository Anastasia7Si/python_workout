def strsort():
    string = input('Введите строку для сортировки:')
    return ''.join(sorted(string))


# print(strsort())


def magic_string():
    string = input('Введите фразу для сортировки:').split()
    result_string = ', '.join(sorted(string))
    lengh_words = [len(word) for word in result_string.split()]
    return result_string, result_string.split()[-1], max(lengh_words)


print(magic_string())
