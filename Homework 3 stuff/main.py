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
    while (userinput != 'a' and userinput != 'd' and userinput != 'u' and userinput != 'r' and userinput != 'o' and userinput != 'q'):
        userinput = input('Choose an option:\n')

    if userinput == 'a':
        playerJersey = int(input('Enter a new player jersey number:\n'))
        playerRating = int(input("Enter a new player's rating:"))

        Roster[playerJersey]=playerRating


    if userinput == 'd':
        playerJersey = int(input('Enter a jersey number:\n'))
        del Roster[playerJersey]


    if userinput == 'u':
        playerJersey = int(input('Enter a Jersey number:\n'))
        playerRating = int(input('Enter a new rating for the player:\n'))
        for item in Roster:
            if item == playerJersey:
                Roster[item]=playerRating


    if userinput == 'r':
        playerRating = int(input('Enter a rating:\n'))

        for jersey,rating in Roster.items():
            if rating > playerRating:
                print('Jersey number: {}, Rating: {}'.format(jersey,rating))


    if userinput == 'o':
        print('ROSTER')
        for jersey,rating in sorted(Roster.items()):
            print('Jersey number: {}, Rating: {}'.format(jersey, rating))



    if userinput == 'q':
        break






