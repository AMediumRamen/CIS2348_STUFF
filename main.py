import csv
csv_input = input()
with open(csv_input, 'r') as yikes:
    yikers = csv.reader(yikes)
    for word in yikers:
        wordlist = word

number_of_iteration = len(wordlist)
for i in range(number_of_iteration):
    a = wordlist[i], wordlist.count(wordlist[i])
    finallist = set(a)
yikes.close()