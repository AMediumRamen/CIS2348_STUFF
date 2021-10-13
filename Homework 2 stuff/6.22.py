# Ahmed Rahman PSID:1820239

first = int(input())
second = int(input())
third = int(input())
fourth = int(input())
fifth = int(input())
sixth = int(input())
yikes = 0

for x in range(-10, 11):
    for y in range(-10,11):
        if first * x + second * y == third and  fourth* x + fifth * y == sixth:
            print(x, y)
            yikes = 1
if yikes != 1:
    print('No solution')



