def random_phrase():
    result = []
    with open('test.txt', 'r', encoding='utf-8') as file:
        for index, line in enumerate(file):
            words = line.split()
            if index < len(words):
                result.append(words[index])
    return ' '.join(result)


# print(random_phrase())


def transport(string):
    words = [line.split() for line in string]
    transposed = []
    for i in range(len(words[0])):
        transposed.append(' '.join(words[j][i] for j in range(len(words))))
    return transposed


print(transport(['abc def ghi', 'jkl mno pqr', 'stu vwx yz']))
