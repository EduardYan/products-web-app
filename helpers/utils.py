"""
Some utils functions to use.
"""

from flask import request
from models.settings import Settings


# utils functions
def get_values_to_add() -> tuple:
    """
    Return a tuple with three
    values, from the inputs form
    to save in the database.
    """

    name = request.form['productName']
    price = int(request.form['productPrice'])
    date = request.form['productDate']

    return name, price, date


def get_values_to_update() -> tuple:
    """
    Return a tuple with three
    values, from the inputs form
    to update in the database.
    """

    new_name = request.form['newProductName']
    new_price = int(request.form['newProductPrice'])
    new_date = request.form['newProductDate']

    return new_name, new_price, new_date


def change_settings(settings: Settings, to_change: str) -> None:
    """
    Change the class Settings
    for the parameter to_change passed for parameter.
    """

    settings.view_style = to_change  # changing


def validate_view_style(products_list: list, view_style: str) -> list:
    """
    Validate the view style for the products.
    Recive the products list of the database, and the view_style
    return a list with the new_products.
    """
    new_products = []  # new products here
    for product in products_list:
        if view_style == 'Mayor or equal to 100.' and product.price >= 100:
            new_products.append(product)
        elif view_style == 'Mayor or equal to 200.' and product.price >= 200:
            new_products.append(product)
        elif view_style == 'Mayor or equal to 300.' and product.price >= 300:
            new_products.append(product)
        elif view_style == 'Mayor or equal to 500.' and product.price >= 500:
            new_products.append(product)
        elif view_style == 'Mayor equal to 1000.' and product.price >= 1000:
            new_products.append(product)
        elif view_style == 'All.':
            new_products.append(product)

    return new_products
