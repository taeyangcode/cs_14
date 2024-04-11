def mandm_sugar(grams):
    servings = grams / 100
    sugar_per_serving = 64
    return servings * sugar_per_serving

def mandm_sodium(grams):
    servings = grams / 100
    sodium_per_serving = 71 * 0.001
    return servings * sodium_per_serving
