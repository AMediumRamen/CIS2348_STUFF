#Ahmed Rahman PSID:1820239
#SKELETON CODE WAS PROVIDED IN LAB 14.10
def selection_sort_descend_trace(numbers):
    totalN = len(numbers)
    for a in range(totalN-1):#total number of iterations
        num_big = a#assigns first as the biggest temporarily and finds the index of the biggest element
        for b in range(a+1, totalN):#a+1 to totalN is the unsorted area the the program searches
            if numbers[b] > numbers[num_big]:
                num_big = b#update biggest number in the unsorted area to swap later
        #index a and the biggest number in the unsorted area is swapped below and printed
        numbers[a],numbers[num_big]=numbers[num_big],numbers[a]
        print(' '.join([str(x)for x in numbers]),end=' \n')#formatted to fit with zybooks formatting

    return numbers
if __name__ == "__main__":
    num = input().split()#treats each number as a seperate value as opposed to one string
    numbers = []#initiation of empty list
    for x in num:
        numbers.append(int(x))#appending to the empty list
    selection_sort_descend_trace(numbers)#finally calling the function
