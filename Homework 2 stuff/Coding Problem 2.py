# Ahmed Rahman PSID:1820239
from datetime import date
today = date.today()
today_list = [today.month,today.day,today.year]
yikes = open('inputDates.txt','r')
notsoyikes = open('parsedDates.txt','w')
month_dictionary = {"January":"1",
                    "February":"2",
                    "March":"3",
                    "April":"4",
                    "May":"5",
                    "June":"6",
                    "July":"7",
                    "August":"8",
                    "September":"9",
                    "October":"10",
                    "November":"11",
                    "December":"12"}
for anything in yikes:
    if anything != "-1":
        yikers = anything.split()
        if len(yikers) == 3:
            month = yikers[0]
            day = yikers[1]
            year = yikers [2]
            day = day[:len(day)-1]
            if month in month_dictionary:
                monthint = int(month_dictionary[month])
                if monthint <= today_list[0]:
                    if int(day) <= today_list[1]:
                        if int(year) <= today_list[2]:
                            x = (month_dictionary[month] + '/' + day + '/' + year)
                            print(x)
                            notsoyikes.write(x)
                            notsoyikes.write("\n")


yikes.close()
notsoyikes.close()