#Ahmed Rahman PSID 1820239

Roster = {}
i = 0
while i != 5:
    playerJersey = int(input("Enter player {}'s jersey number:".format(str(i+1))))
    playerRating = int(input("Enter player {}'s rating:".format(str(i+1))))
    Roster[playerJersey]=playerRating
    i += 1
sortedRoster = sorted(Roster.items())

print('ROSTER')
for jersey,rating in sortedRoster:
    print('Jersey number: {}, Rating: {}'.format(jersey,rating))

userinput = ''
while userinput != 'q':
    print("a - Add player"
          "d - Remove player"
          "u - Update player rating"
          "r - Output players above a rating"
          "o - Output roster"
          "q - Quit")
    userinput = input('Choose an option\n')
    while (
            userinput != 'a' and userinput != 'd' and userinput != 'u' and userinput != 'r' and userinput != 'o' and userinput != 'q'):
        userinput = input('Choose an option:\n')



