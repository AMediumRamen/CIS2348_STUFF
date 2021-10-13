import csv
yikes = open('input1.csv')
type(yikes)
words = csv.reader(yikes)
for word in words:
    yikes_list = list(words)
    for a in yikes_list:
        b = word.count(a)
        print(a,b)