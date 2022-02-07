"""
This file have the model
for add a product in the database.
"""

from enum import unique
from helpers.db import db


class PriceInvalid(TypeError):
    """
    Execption class in case
    the price for save in the database
    not is valid.
    """

    pass


class Products(db.Model):
    """
    Model for the tabel of products
    """

    # values
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer, unique = False)
    date = db.Column(db.String(100))

    def __init__(self, name: str, price: int, date: str) -> None:
        # validating the price
        if type(price) not in [int]:
            raise PriceInvalid('The price passed for parameter not is valid.')

        self.name = name
        self.price = price
        self.date = date
