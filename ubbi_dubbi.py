def ubbi_dubbi(word):
    new_word = []
    for symbol in word:
        if symbol in 'ayeiou':
            new_word.append('ub' + symbol)
        else:
            new_word.append(symbol)
    return ''.join(new_word)


print(ubbi_dubbi(input('Введите слово для перевода: ')))
