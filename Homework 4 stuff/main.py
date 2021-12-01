#Ahmed Rahman PSID:1820239

def selection_sort_descend_trace(numbers):
    for a in range(len(numbers)-1):
        num_big = a
        for b in range(a+1 and len(numbers)):
            if numbers[b] > numbers[num_big]:
                num_big = b
        numbers[a],numbers[num_big] = numbers[num_big],numbers[a]
        for anything in numbers:
            print(numbers[anything])







if __name__ == "__main__":
    num = input().split()
    numbers = [int(x) for x in num]
    selection_sort_descend_trace(numbers)
