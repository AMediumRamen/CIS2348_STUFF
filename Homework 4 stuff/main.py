#Ahmed Rahman PSID:1820239

list_to_sort = list[int(input())]
def selection_sort_descend_trace(numbers):
    iter1 = 0
    iter2 = iter1+1
    while iter1 != len(numbers):
        num_big = numbers[iter1]
        if numbers[iter2] > num_big:
            num_big = numbers[iter2]
            iter1 +=1
        numbers[iter1],numbers[num_big] = numbers[num_big],numbers[iter1]
    print(numbers)





if __name__ == "__main__":
    numbers = []
