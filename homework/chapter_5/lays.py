def lays_sugar(grams):
    servings = grams / 28
    sugar_per_serving = 1
    return servings * sugar_per_serving

def lays_sodium(grams):
    servings = grams / 28
    sodium_per_serving = 170 * 0.001
    return servings * sodium_per_serving
