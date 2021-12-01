#Ahmed Rahman PSID:1820239
num_calls = 0

def partition(user_ids, i, k):
    mid = i
    for a in range(i+1,k+1):
        if str(user_ids[i]) <= str(i):
            mid += 1
            user_ids[a], user_ids[mid] = user_ids[mid], user_ids[a]
    user_ids[mid],user_ids[i] = user_ids[i], user_ids[mid]
    return mid



def quicksort(user_ids, i, k):
    global num_calls
    if i < k:
        mid = partition(user_ids,i,k)
        quicksort(user_ids,i,mid-1)
        quicksort(user_ids,mid+1,k)
    num_calls += 1


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
