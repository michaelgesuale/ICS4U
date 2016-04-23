class Ingredient(object):

    def __init__(self, n='', c=0):
        self.name = n
        self.calorieCount = c


class IngredientList(object):

    def __init__(self):
        self.ingredients = []

    def add(self, ing):
        self.ingredients.append(ing)

    def find(self, ingName):
        for ing in self.ingredients:
            if ingName == ing.name:
                return ing.calorieCount

    def readList(self, ingToAdd):
        ingList = open(ingToAdd).read().splitlines()
        for item in ingList:
            splitItem = item.split()
            self.add(Ingredient(splitItem[0], int(splitItem[1])))

    def count(self, filename):
        recipe = open(filename).read().splitlines()
        calories = 0
        for ingredient in recipe:
            splitIng = ingredient.split()
            ingName = splitIng[0]
            grams = int(splitIng[1])
            name = self.find(ingName)
            per100 = int(name)
            calories += (per100 / 100) * grams
        return calories

if __name__ == '__main__':
    myList = IngredientList();

    myList.readList('table.txt')
    print(myList.count('pasta.txt'))

