from pprint import pprint

with open("21_input.txt") as fin:
    data = fin.read().split("\n")

# Let's always define functions at the top now
def find_ingredient(allergen):
    possible_ingredients = []
    for i, ingredients in enumerate(all_ingredients):
        if allergen in all_allergens[i]:
            possible_ingredients.append(ingredients)

    return set.intersection(*possible_ingredients)
    

def count_ingredient(ingredient):
    count = 0
    for i in all_ingredients:
        count += ingredient in i

    return count


all_ingredients = []
all_allergens = []

ingredients_unique = set(all_ingredients)
allergens_unique = set(all_allergens)

for line in data:
    new_ingredients = set(line[:line.index("(") - 1].split(" "))
    all_ingredients.append(new_ingredients)
    new_allergens = set(line[line.index("contains") + len("contains") + 1:-1].split(", "))
    all_allergens.append(new_allergens)

    ingredients_unique.update(new_ingredients)
    allergens_unique.update(new_allergens)


final_ingredient = {}
taken_ingredients = set()
while len(final_ingredient) != len(allergens_unique):
    for allergen in allergens_unique:
        possible = find_ingredient(allergen).difference(taken_ingredients)
        if len(possible) == 1:
            ingredient = possible.pop()
            final_ingredient[allergen] = ingredient
            taken_ingredients.add(ingredient)


allergen_given_ingredient = {}
for allergen in final_ingredient:
    allergen_given_ingredient[final_ingredient[allergen]] = allergen

pprint(allergen_given_ingredient)

dangerous = sorted(allergen_given_ingredient, key=allergen_given_ingredient.get)

print(",".join(dangerous))