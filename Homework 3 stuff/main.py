class FoodItem:
    def __init__(self,name,fat,carbs,protein,servings):
        self.name = "None"
        self.fat = 0.0
        self.carbs = 0.0
        self.protein = 0.0
        self.servings = 0.0
    def get_calories(self,servings):
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * servings
        return calories
    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))



