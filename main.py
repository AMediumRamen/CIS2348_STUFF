import csv
with open('input1.csv','r') as yikes:
    words = csv.reader(yikes)
    for word in words:
        yikes_list = list(words)
        for a in yikes_list:
            b = word.count(a)
            print(a,b)