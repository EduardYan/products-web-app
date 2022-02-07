"""
This file have the routes
to use in the server.
"""


from crypt import methods
from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    redirect,
    flash
)
from helpers.db import db
from models.product import Products
from models.settings import Settings
from helpers.utils import get_values_to_add, get_values_to_update, change_settings, validate_view_style

# routes
products = Blueprint('products', __name__)

# settings of the view
settings = Settings(
    view_style='All.'
)


@products.route('/')
def home():
    """
    Initial route,
    consult alls the products for show.
    """

    # getting the product for pass into page
    products = Products.query.all()
    # validating the style for the view of product
    view_style = settings.view_style
    new_products = validate_view_style(products, view_style)

    return render_template('index.html', products=new_products)


@products.route('/add', methods=['POST'])
def add_product():
    """
    Route for add a new product.
    """

    # getting the creating a product
    name, price, date = get_values_to_add()
    product = Products(name, price, date)

    db.session.add(product)  # adding
    db.session.commit()

    flash('Product Saved Successfully.')

    return redirect(url_for('products.home'))


@products.route('/update/<id>', methods=['GET', 'POST'])
def update_product(id):
    """
    Route for update a product.
    Id is required for update.

    If the method is GET, return the page, with
    the formulary. If the method is POST, update
    the product in the database.
    """

    id = int(id)

    # changeing values and adding
    product = Products.query.filter_by(id=id).first()

    if request.method == 'GET':
        return render_template('update-product.html', product=product)
    elif request.method == 'POST':
        # getting new values
        new_name, new_price, new_date = get_values_to_update()
        product.name = new_name
        product.price = new_price
        product.date = new_date
        db.session.add(product)
        db.session.commit()

        flash('Product Updated Successfully.')

        return redirect(url_for('products.home'))

    else:
        return 'Method not is available.'


@products.route('/delete/<id>')
def delete_product(id):
    """
    Route for delete a product,
    recived the id for the product.

    """
    # converting
    id = int(id)

    productFound = Products.query.filter_by(id=id).first()
    db.session.delete(productFound)  # removing
    db.session.commit()

    flash('Product Deleted Successfully.')

    # redirect
    return redirect(url_for('products.home'))


@products.route('/change-settings', methods=['GET', 'POST'])
def change_settings_route():
    """
    Return the page
    with the settings.
    Running with GET and POST
    method for change the setting.
    """

    global settings
    # in case is get
    if request.method == 'GET':
        return render_template('settings.html', settings=settings)

    elif request.method == 'POST':
        new_view_style = request.form['view-style']
        change_settings(settings, new_view_style)
        return redirect(url_for('products.home'))


@products.route('/about')
def about():
    """
    Route for render
    the about page
    """

    return render_template('about.html')
