spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    list = []
    for x in spicy_foods:
        list.append(x.get("name"))
    return(list)


def get_spiciest_foods(spicy_foods):
    list = []
    for dish in spicy_foods:
        if dish.get("heat_level") > 5:
            list.append(dish)
        return(list)


def print_spicy_foods(spicy_foods):
    for dish in spicy_foods:
        name = dish["name"]
        cuisine = dish["cuisine"]
        heat_level = dish["heat_level"] * "🌶"
        print(f"{name} ({cuisine}) | Heat Level: {heat_level}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for dish in spicy_foods:
        if dish["cuisine"] == cuisine:
            return dish


def print_spiciest_foods(spicy_foods):
    for dish in spicy_foods:
        if dish["heat_level"] > 5:
            name = dish["name"]
            cuisine = dish["cuisine"]
            heat_level = dish["heat_level"] * "🌶"
            print(f"{name} ({cuisine}) | Heat Level: {heat_level}")


def get_average_heat_level(spicy_foods):
    list = []
    for dish in spicy_foods:
        list.append(dish["heat_level"])
    average = sum(list)/len(list)
    return average

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
