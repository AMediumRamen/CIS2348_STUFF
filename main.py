import csv
csv_input = input()
with open(csv_input, 'r') as yikes:
    yikers = csv.reader(yikes)
    for word in yikers:
        wordlist = word
finallist = list(dict.fromkeys(wordlist))
number_of_iteration = len(finallist)
for i in range(number_of_iteration):
    print(finallist[i], finallist.count(finallist[i]))