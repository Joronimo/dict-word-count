#open file


def word_count(file):
    file = open(file)

    dict_word_count = {}

    for line in file:
        lines = line.lower()
        row = lines.split(',')

        for word in row:
            dict_word_count[word] = dict_word_count.get(word, 0) + 1

    return dict_word_count
print(word_count('test.txt'))
