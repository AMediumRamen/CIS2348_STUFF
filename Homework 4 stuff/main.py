#Ahmed Rahman PSID:1820239

# CODE SKELETON WAS PROVIDED BY ZYBOOKS IN LAB 14.12
num_calls = 0
def partition(user_ids, i, k):
    piv = user_ids[(i+k)//2] #assigning PIV as the middle index
    while True:
        while user_ids[i]<piv:#increment through the left side while < variable piv
            i += 1
        while user_ids[k] > piv:#decrement through the right side while > varible piv
            k -= 1
        if i >= k: #determines if the swap is necessary based on if number at user_ids[i] is greater than user_ids[k]
            break
        else:#actual swap
            user_ids[i],user_ids[k] = user_ids[k],user_ids[i]
    return k



def quicksort(user_ids,i,k):
    global num_calls #call num_calls global variable
    if i < k: #checking for actual entries to sort
        part = partition(user_ids,i,k)
        quicksort(user_ids,i,part-1)#sort from i=0 to part(the pivot)-1
        quicksort(user_ids,part+1,k)#sort from part(pivot)+1 to k(last index)
    num_calls += 1#increments the global variable after each call of quicksort function


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    quicksort(user_ids, 0, len(user_ids) - 1)

    print(num_calls)

    for user_id in user_ids:
        print(user_id)
