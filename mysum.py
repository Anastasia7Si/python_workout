from string import ascii_letters
from random import choice, randint


def mysum(*numbers, start=0):
    sum = 0
    for number in numbers:
        sum += number
    mean = sum / len(numbers)
    return sum, mean


test_data = [x for x in range(0, 50, 3)]
# print(mysum(*test_data))
# print(mysum(*test_data, 7))


def words_analiz(*words):
    min_word = len(words[0])
    max_word = len(words[0])
    mean_length = 0
    for word in words:
        if len(word) < min_word:
            min_word = len(word)
        elif len(word) > max_word:
            max_word = len(word)
    sum_length = 0
    for word in words:
        sum_length += len(word)
        mean_length = sum_length / len(words)
    return (min_word, max_word, mean_length)


def random_words():
    result = []
    count = 0
    while count < 6:
        word = ''
        for i in range(randint(0, 6)):
            word += choice(ascii_letters)
        result.append(word)
        count += 1
    return result


print(words_analiz(*random_words()))
