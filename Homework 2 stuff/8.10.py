# Ahmed Rahman PSID:1820239

yikes = input()
yikes2 = yikes.replace(' ','')
if yikes2 == yikes2[::-1]:
    print(yikes,'is a palindrome')
else:
    print(yikes,'is not a palindrome')
