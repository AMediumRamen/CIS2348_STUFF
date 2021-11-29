#Ahmed Rahman PSID:1820239
def fat_burning_heart_rate(age):
    HR = (220- age)*0.7
    return HR

def get_age():
    age = int(input())
    if age >= 18 and age<= 75:
        return age
    else:
        raise ValueError('Invalid age.')

if __name__ == "__main__":
    try:
        age = get_age()
        HR = fat_burning_heart_rate(age)
        print('Fat burning heart rate for a {} year-old: {} bpm'.format(age,HR))
    except ValueError as yikes:
        print(yikes)
        print('Could not calculate heart rate info.\n')


