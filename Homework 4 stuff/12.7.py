#Ahmed Rahman PSID:1820239
#variables are named according to instructions
#Skeleton code provided in lab 12.6
def fat_burning_heart_rate(age):
    HR = (220- age)*0.7 # calculate heart rate and return it
    return HR

def get_age():
    age = int(input())
    if age >= 18 and age<= 75: # adult's age 18-75 inclusive, as per instructions
        return age #return the age if no value error was raised  and meets criteria
    else:
        raise ValueError('Invalid age.')#raising value error as per instructions with message

if __name__ == "__main__":
    #try and catch statements
    try:
        age = get_age()#prompt user to enter age and check if age is valid
        HR = fat_burning_heart_rate(age)#if no exception, proceed to call the fat_burning_heart_rate function
        print('Fat burning heart rate for a {} year-old: {} bpm'.format(age,HR))
    except ValueError as yikes:#exception handling if value error was raised
        print(yikes)#print value error message
        print('Could not calculate heart rate info.\n')#print additional message with a newline due to ZyBooks formatting


