from string import punctuation


def pig_latin():
    word = input('Введите слово для перевода:')

    punctuation_symbol = ''
    if word[-1] in punctuation:
        punctuation_symbol = word[-1]
        word = word[:-1]

    if word[0] in 'aeiouAEIOU':
        return word + 'way' + punctuation_symbol
    else:
        return word[1:] + word[0] + 'ay' + punctuation_symbol


# print(pig_latin())


def pig_latin_alt():
    word = input('Введите слово для перевода:')
    count = []
    for symbol in word:
        if symbol in 'ayeiouAEIOUY':
            count.append(symbol)
    if len(count) >= 2 and len(count) == len(set(count)):
        return word + 'way'
    else:
        return word[1:] + word[0] + 'ay'


# print(pig_latin_alt())


def pl_sentence():
    words = input('Введите предложение для перевода:').split()
    result = []
    for word in words:
        if word[0] in 'aeiouAEIOU':
            result.append(word + 'way')
        else:
            result.append(word[1:] + word[0] + 'ay')
    return ' '.join(result)


print(pl_sentence())
