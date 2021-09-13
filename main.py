#Ahmed Rahman PSID:1820239
#Lab 2.19

lemon_juice= input("Enter amount of lemon juice (in cups):\n")
water = input("Enter amount of water (in cups):\n")
agave_nectar = input("Enter amount of agave nectar (in cups):\n")
servings_made = input("How many servings does this make?")
lemon_juicefloat = float(lemon_juice)
water_float = float(water)
agave_nectarfloat = float(agave_nectar)
servings_madefloat = float(servings_made)
print('\n')
print(f'Lemonade ingredients - yields {servings_madefloat:.2f} servings')
print(f'{lemon_juicefloat:.2f} cup(s) lemon juice')
print(f'{water_float:.2f} cup(s) water')
print(f'{agave_nectarfloat:.2f} cup(s) agave nectar')


servings_required = input("How many servings would you like to make?\n")
servings_requiredfloat = float(servings_required)
random = servings_requiredfloat/servings_madefloat
print(f'Lemonade ingredients - yields {servings_requiredfloat:.2f} servings')
print(f'{lemon_juicefloat*random:.2f} cup(s) lemon juice')
print(f'{water_float*random:.2f} cup(s) water')
print(f'{agave_nectarfloat*random:.2f} cup(s) agave nectar')
print('\n')
print(f'Lemonade ingredients - yields {servings_requiredfloat:.2f} servings')
print(f'{lemon_juicefloat*random/16:.2f} gallon(s) lemon juice')
print(f'{water_float*random/16:.2f} gallon(s) water')
print(f'{agave_nectarfloat*random/16:.2f} gallon(s) agave nectar')
