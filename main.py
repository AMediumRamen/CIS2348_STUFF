import csv
inputfile = input()
with open(inputfile, 'r') as yikes:
    yikers = csv.reader(yikes)
    for anything in yikers:
        word_list = list(set(anything))
        for word in word_list:
            word_count = anything.count(word)
            print(word, word_count)
