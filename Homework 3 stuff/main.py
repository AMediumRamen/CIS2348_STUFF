class FoodItem:
    def __init__(self,Foodname = "None",Foodfat=0.0,Foodcarbs=0.0,Foodprotein=0.0,Foodservings=0.0):
        self.name = Foodname
        self.fat = Foodfat
        self.carbs= Foodcarbs
        self.protein = Foodprotein
        self.servings = Foodservings

    def get_calories(self,Foodservings):
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * Foodservings
        return calories
    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))

if __name__ == "__main__":
    first = FoodItem()
    Foodname = input()
    Foodfat = float(input())
    Foodcarbs = float(input())
    Foodprotein = float(input())
    Foodservings = float(input())

    second = FoodItem(Foodname,Foodfat,Foodcarbs,Foodprotein)

    first.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(Foodservings,first.get_calories(Foodservings)))
    print()
    second.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(Foodservings, second.get_calories(Foodservings)))