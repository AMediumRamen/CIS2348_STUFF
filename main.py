import csv
with open('input1.csv', 'r') as yikes:
    yikers = csv.reader(yikes)
    for anything in yikers:
        word_list = set(anything)
        for word in word_list:
            word_count = anything.count(word)
            print(word, word_count)
