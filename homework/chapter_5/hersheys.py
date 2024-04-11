def hersheys_sugar(grams):
    servings = grams / 31
    sugar_per_serving = 17
    return servings * sugar_per_serving

def hersheys_sodium(grams):
    servings = grams / 31
    sodium_per_serving = 25 * 0.001
    return servings * sodium_per_serving