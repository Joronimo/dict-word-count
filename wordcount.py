#open file


def word_count(file):
    file = open(file) # blob of file

    dict_word_count = {}
    exclude = ",.?!:;"
    for line in file:
        lines = line.lower() # removes case sensitivity ( => string) 
        row = lines.split() # list of words in a line ( => list)


        for word in row:
            for char in word:
                if char in exclude:
                    word = word[0:-1]
            dict_word_count[word] = dict_word_count.get(word, 0) + 1

    return dict_word_count
print(word_count('test.txt'))
