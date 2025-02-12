def firstlast(sequence):
    return sequence[:1] + sequence[-1:]


number_list = [1, 3, 5, 7]
string = 'asdfghhj'
number_tuple = (1, 3, 5, 7, 1)
TEST_DATA = [number_list, string, number_tuple]

for i in TEST_DATA:
    print(firstlast(i))
