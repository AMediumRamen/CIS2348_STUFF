#Ahmed Rahman PSID:1820239

def selection_sort_descend_trace(numbers):
    totalN = len(numbers)
    for a in range(totalN-1):
        num_big = a
        for b in range(a+1, totalN):
            if numbers[b] > numbers[num_big]:
                num_big = b
        numbers[a],numbers[num_big]=numbers[num_big],numbers[a]
        print(' '.join([str(x)for x in numbers]),end=' \n')

    return numbers
if __name__ == "__main__":
    num = input().split()
    numbers = []
    for x in num:
        numbers.append(int(x))
    selection_sort_descend_trace(numbers)