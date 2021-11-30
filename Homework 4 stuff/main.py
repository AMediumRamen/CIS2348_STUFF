#Ahmed Rahman PSID: 1820239

parts = input().split()
name = parts[0]
while name != '-1':
    try:
        age = int(parts[1]) + 1
        print('{} {}'.format(name, age))
    except ValueError as yikes:
        print(name, 0)

    parts = input().split()
    name = parts[0]