#Ahmed Rahman PSID: 1820239
#SKELETON CODE WAS PROVIDED IN LAB 12.8

parts = input().split()
name = parts[0]
while name != '-1':
    try:#implementation of try block as per FIX-ME instructions
        age = int(parts[1]) + 1
        print('{} {}'.format(name, age))
    except ValueError as yikes:#Implementation of except block as per FIX-ME instructions
        print('{} {}'.format(name, 0))

    parts = input().split()
    name = parts[0]