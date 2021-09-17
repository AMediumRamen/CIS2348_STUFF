#Ahmed Rahman PSID:1820239
#LAB 5.22
print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")
print('')

services = {'Oil change':35,'Tire rotation':19,'Car wash':7,'Car wax':12}
first_service = input("Select first service:\n")
second_service = input("Select second service:\n")
print('')
print("Davy's auto shop invoice")
print('')
a=0
b=0
if first_service in services:
    print("Service 1: ", first_service, ", $", services[first_service], sep='')
    a = services[first_service]

elif first_service not in services:
    print("Service 1: No Service")
else:
    print("Error")

if second_service in services:
    print("Service 2: ", second_service, ", $", services[second_service], sep='')
    b =services[second_service]
elif second_service not in services:
    print("Service 2: No service")
else:
    print("Error")

print('')
total = a+b
print('Total: $',total,sep='')

