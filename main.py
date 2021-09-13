#Ahmed Rahman PSID:1820239
#LAB 3.19

wall_height = int(input("Enter wall height (feet):\n"))
wall_width = int(input("Enter wall width (feet):\n"))
wall_area = wall_width*wall_height
print("Wall area:",wall_area,"square feet")

square_feet_per_gallon = 350
gallons_needed = wall_area/square_feet_per_gallon
print(f"Paint needed: {gallons_needed:.2f} gallons")
cans_needed = round(gallons_needed)
print("Cans needed:",cans_needed, "can(s)")
print("")
colors_of_paint = {'red':35,'blue':25,'green':23}
colorneeded = input("Choose a color to paint the wall:\n")
print("Cost of purchasing red paint: $",colors_of_paint[colorneeded]*cans_needed,sep='')
