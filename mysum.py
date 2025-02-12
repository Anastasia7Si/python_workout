from string import ascii_letters
from random import choice, randint


def mysum(*numbers, start=0):
    sum = 0
    for number in numbers:
        sum += number
    mean = sum / len(numbers)
    return sum, mean


def mysum_2(*elements):
    result = elements[0]
    for element in elements[1:]:
        result += element
    return result


test_data = [x for x in range(0, 50, 3)]
# print(mysum(*test_data))
# print(mysum(*test_data, 7))
# print(mysum_2(test_data, test_data))


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


# print(words_analiz(*random_words()))
# print(mysum_2(*random_words(), *random_words()))


def mysum_bigger_than(border, *elements):
    result = border
    for element in elements:
        if element > border:
            result += element
    return result


# print(mysum_bigger_than('j', *random_words()))
# print(mysum_bigger_than(10, 5, 20, 30, 6))


def sum_numeric(*elements):
    sum = 0
    for element in elements:
        try:
            sum += int(element)
        except ValueError:
            continue
    return sum


print(sum_numeric(*random_words(), *test_data))
