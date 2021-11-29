def fat_burning_heart_rate(age):
    HR = (220*0.7)- age
    return HR

def get_age():
    age = int(input())
    if age >= 18 and age<= 75:
        return age
    else:
        raise ValueError('Invalid age.')

if __name__ == "__main__":
