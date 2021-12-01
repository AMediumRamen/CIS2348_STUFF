num = input().split()
numbers = [int(x) for x in num]
iter1 = 0
iter2 = iter1 + 1
while iter1 != (len(numbers)-1):
    num_big = numbers[iter1]
    if numbers[iter2] > num_big:
        num_big = numbers[iter2]
        iter1 += 1
    numbers[iter1], numbers[num_big] = numbers[num_big], numbers[iter1]
print(numbers)