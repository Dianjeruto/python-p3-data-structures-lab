# lib/data_structures.py

def get_names(spicy_foods):
    """
    Returns a list of names of all spicy foods.
    """
    return [food["name"] for food in spicy_foods]

def get_spiciest_food_names(spicy_foods):
    """
    Returns a list of names of the spiciest foods.
    """
    max_heat_level = max(food["heat_level"] for food in spicy_foods)
    return [food["name"] for food in spicy_foods if food["heat_level"] == max_heat_level]
