number_list = [1, 3, 5, 7, 2.6, 9.1, 3.5]
string = 'asdfghhj'


def square_number(number):
    return number ** 2

# for i in number_list:
#    print(square_number(i), end=' ')


def max_element(sequence):
    return max(sequence)


# print(max_element(number_list))
# print(max_element(string))

def max_word(file):
    longet_word = ''
    for line in file:
        words = line.split()
        for word in words:
            if len(word) > len(longet_word):
                longet_word = word
    return longet_word


# print(max_word(open('test.txt', 'r', encoding='utf-8')))


def even_odd_sums(number_sequence):
    even_sum = sum(
        number_sequence[i] for i in range(len(number_sequence)) if i % 2 == 0
        )
    odd_sum = sum(
        number_sequence[i] for i in range(len(number_sequence)) if i % 2 != 0
        )
    return [even_sum, odd_sum]


# print(even_odd_sums(number_list))


def plus_minus(number_sequence):
    result = number_sequence[0]
    for index in range(1, len(number_sequence)):
        if index % 2 == 0:
            result -= number_sequence[index]
        elif index % 2 != 0:
            result += number_sequence[index]
    return result


# print(plus_minus(number_list))


def zip_emulation(*objs):
    min_length = min(len(obj) for obj in objs)
    result = []
    for i in range(min_length):
        result.append(tuple(obj[i] for obj in objs))
    return result


# print(zip_emulation(string, number_list))


def sum_dict(*dict_list):
    result_dict = {}
    for dict in dict_list:
        for key, value in dict.items():
            if key in result_dict:
                if isinstance(result_dict[key], list):
                    result_dict[key].append(value)
                else:
                    result_dict[key] = [result_dict[key], value]
            else:
                result_dict[key] = value
    return result_dict


keys = [x for x in range(0, 10)]
values = [x ** 2 for x in range(0, 10)]
test_dict_1 = {k: v for (k, v) in zip_emulation(keys, values)}
test_dict_2 = {k: v for (k, v) in zip_emulation(keys, values) if k % 2 == 0}
test_dict_3 = {k: v for (k, v) in zip_emulation(keys, string)}
test_dict_4 = {k: v for (k, v) in zip_emulation(keys, string) if k % 2 == 0}

print(sum_dict(test_dict_1, test_dict_2, test_dict_3))
print(sum_dict(test_dict_3, test_dict_4))