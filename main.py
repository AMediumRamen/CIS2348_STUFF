#Ahmed Rahman PSID:1820239
#LAB 5.22
print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")
print('')

services = {'Oil change':35,'Tire rotation':19,'Car wash':7,'Car wax':12,'No service':'No service'}
first_service = input("Select first service:\n")
second_service = input("Select second service:\n")
print('')
print("Davy's auto shop invoice")
print('')
print("Service 1: ",first_service,", $",services[first_service],sep='')
print("Service 2: ",second_service,", $",services[second_service],sep='')
total = services[first_service]+services[second_service]
print('')
print('Total: $',total,sep='')

