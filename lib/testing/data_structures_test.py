# lib/testing/data_structures_test.py
import pytest
from data_structures import get_names, get_spiciest_food_names  # Adjust the import statement based on your directory structure

class TestDataStructures:
    SPICY_FOODS = [
        {'cuisine': 'Thai', 'heat_level': 9, 'name': 'Green Curry'},
        {'cuisine': 'American', 'heat_level': 3, 'name': 'Buffalo Wings'},
        {'cuisine': 'Sichuan', 'heat_level': 6, 'name': 'Mapo Tofu'}
    ]

    def test_get_names(self):
        '''contains function get_names() that retrieves names from list of foods.'''
        assert get_names(TestDataStructures.SPICY_FOODS) == ['Green Curry', 'Buffalo Wings', 'Mapo Tofu']

    def test_get_spiciest_food_names(self):
        '''contains function get_spiciest_food_names() that retrieves names of the spiciest foods.'''
        assert get_spiciest_food_names(TestDataStructures.SPICY_FOODS) == ['Green Curry']
