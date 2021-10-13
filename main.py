import csv
inputfile = input()
with open(inputfile, 'r') as yikes:
    yikers = csv.reader(yikes)
    for anything in yikers:
        word_list = set(anything)
no_duplicates_in_list = list(dict.fromkeys(word_list))
listlength = len(no_duplicates_in_list)

for i in range(listlength):
    print(no_duplicates_in_list[i], word_list.count(no_duplicates_in_list[i]))

