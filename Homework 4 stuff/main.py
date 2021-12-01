#Ahmed Rahman PSID:1820239

list_to_sort = list[int(input())]
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
    list_to_sort = list[int(input())]
    selection_sort_descend_trace(list_to_sort)
